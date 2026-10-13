#!/usr/bin/env bash
# savings-census-clone-v58.sh — the v58 savings-view DOM arbitration census,
# CLONE side (via with-server on :3200). Read-only. Uses the P1.2 lesson:
# a QUOTED heredoc (<<'EOF') + an EXPORTED census variable so the inner
# bash expands it safely from the environment (the unquoted-heredoc
# word-splitting bug the v57 debug variant documented).
set -u
cd "$(dirname "$0")/../.."

CENSUS='(async () => {
  const out = {};
  const grid = [...document.querySelectorAll("div")].find(
    (d) => typeof d.className === "string" && /grid-cols-3/.test(d.className) && d.children.length > 0
  );
  if (!grid) return JSON.stringify({ grid: "not found" });
  const gcs = getComputedStyle(grid);
  out.grid = {
    template: gcs.gridTemplateColumns,
    gap: gcs.gap,
    w: Math.round(grid.getBoundingClientRect().width),
    childCount: grid.children.length,
  };
  const card = grid.children[0];
  const flexRows = [...card.querySelectorAll("div")].filter((d) => {
    const s = getComputedStyle(d);
    return s.display === "flex" && s.justifyContent === "space-between" && d.children.length >= 1 && !d.querySelector("h4") && d.getBoundingClientRect().height < 40;
  });
  const footer = flexRows[flexRows.length - 1];
  if (footer) {
    const fs = getComputedStyle(footer);
    out.footer = {
      display: fs.display,
      justify: fs.justifyContent,
      fs: fs.fontSize,
      color: fs.color,
      h: Math.round(footer.getBoundingClientRect().height),
      childCount: footer.children.length,
      children: [...footer.children].map((c) => {
        const cs = getComputedStyle(c);
        return {
          tag: c.tagName,
          text: (c.textContent || "").trim().slice(0, 24),
          display: cs.display,
          gap: cs.gap,
          fs: cs.fontSize,
          color: cs.color,
          iconW: c.querySelector("svg") ? Math.round(c.querySelector("svg").getBoundingClientRect().width) : null,
          iconH: c.querySelector("svg") ? Math.round(c.querySelector("svg").getBoundingClientRect().height) : null,
          iconColor: c.querySelector("svg") ? getComputedStyle(c.querySelector("svg")).color : null,
        };
      }),
    };
  }
  const row = [...card.children].find((c) => /flex-wrap/.test((c.className || "").toString()));
  if (row) {
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
        bg: cs.backgroundColor,
        fs: cs.fontSize,
        fw: cs.fontWeight,
        h: Math.round(c.getBoundingClientRect().height),
        gap: cs.gap,
        iconW: c.querySelector("svg") ? Math.round(c.querySelector("svg").getBoundingClientRect().width) : null,
        iconH: c.querySelector("svg") ? Math.round(c.querySelector("svg").getBoundingClientRect().height) : null,
      };
    });
  }
  const ccs = getComputedStyle(card);
  out.card = {
    w: Math.round(card.getBoundingClientRect().width),
    pad: ccs.padding,
    radius: ccs.borderRadius,
    border: ccs.borderTopWidth + " " + ccs.borderTopStyle + " " + ccs.borderTopColor,
    bg: ccs.backgroundColor,
  };
  return JSON.stringify(out);
})()'
export CENSUS

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonesv58"
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

echo "=== CLONE /savings census (grid + card + footer + badges) ==="
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 3
agent-browser eval "$CENSUS" 2>/dev/null | tail -1

echo "=== clone savings census v58 done ==="
EOF
