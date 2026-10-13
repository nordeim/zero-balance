#!/usr/bin/env bash
# badge-census-clone-v57-debug.sh — DEBUG rerun of the v57 CLONE badge census.
# badge-census-clone-v57.sh (left byte-exact as mandated) feeds
# `agent-browser eval "$BADGE"` through an UNQUOTED heredoc: the outer shell
# expands $BADGE, and the inner `bash -s` re-parses the JS's double quotes as
# shell quoting — the eval argument gets word-split and the census prints
# nothing. This variant keeps the census logic byte-identical but uses a
# QUOTED heredoc (<<'EOF') and exports BADGE so the inner bash expands it
# safely from the environment. Also runs the /url+grids page check.
# READ-ONLY.
set -u
cd "$(dirname "$0")/../.."

BADGE='(async () => {
  const grid = [...document.querySelectorAll("div")].find(
    (d) => typeof d.className === "string" && /grid-cols-3/.test(d.className) && d.children.length > 0
  );
  if (!grid) return JSON.stringify({ grid: "not found" });
  const out = { gridChildren: grid.children.length };
  const card = grid.children[0];
  const row = [...card.children].find((c) => /flex-wrap/.test((c.className || "").toString()));
  if (!row) return JSON.stringify({ badgeRow: "not found" });
  const s = getComputedStyle(row);
  out.badgeRow = {
    display: s.display,
    wrap: s.flexWrap,
    gap: s.gap,
    mb: s.marginBottom,
    h: Math.round(row.getBoundingClientRect().height),
    n: row.children.length,
  };
  out.badges = [...row.children].map((c) => {
    const cs = getComputedStyle(c);
    return {
      text: (c.textContent || "").trim().slice(0, 16),
      display: cs.display,
      alignItems: cs.alignItems,
      radius: cs.borderRadius,
      pad: cs.padding,
      border: cs.borderTopWidth + " " + cs.borderTopStyle + " " + cs.borderTopColor,
      fs: cs.fontSize,
      fw: cs.fontWeight,
      h: Math.round(c.getBoundingClientRect().height),
      gap: cs.gap,
      iconW: c.querySelector("svg") ? Math.round(c.querySelector("svg").getBoundingClientRect().width) : null,
      iconH: c.querySelector("svg") ? Math.round(c.querySelector("svg").getBoundingClientRect().height) : null,
    };
  });
  return JSON.stringify(out);
})()'
export BADGE

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonebadge57"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1

echo "=== CLONE /income badge census ==="
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 3
agent-browser eval "$BADGE" 2>/dev/null | tail -1

echo "=== CLONE /income page check ==="
agent-browser eval "(async () => JSON.stringify({url: location.href, grids: [...document.querySelectorAll('div')].filter(d => typeof d.className === 'string' && /grid-cols-3/.test(d.className)).length}))()" 2>/dev/null | tail -1

echo "=== CLONE /expenses badge census ==="
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "$BADGE" 2>/dev/null | tail -1

echo "=== CLONE /expenses page check ==="
agent-browser eval "(async () => JSON.stringify({url: location.href, grids: [...document.querySelectorAll('div')].filter(d => typeof d.className === 'string' && /grid-cols-3/.test(d.className)).length}))()" 2>/dev/null | tail -1

echo "=== clone badge census (debug) done ==="
EOF
