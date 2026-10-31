#!/usr/bin/env bash
# statfooter-arbit-v136.sh — the ONE-SHOT both-sides arbitration for the
# v136 pass-1 drill-down pair's NEW flag: the VLM claimed "the horizontal
# divider lines above the item counts ('1 item', etc.) in the three white
# stat cards are present in Image 1 (ref) but missing in Image 2 (clone)".
# The clone's StatCard footer (dashboard-view.tsx:604-620) carries
# [count span] [h-px flex-1 divider, backgroundColor rgb(229,231,227)]
# [trend icon] — the divider is BESIDE the count, not above it; the claim
# needs the computed truth on BOTH sides.
# Measured per stat card (the tag-agnostic finder: the element whose text
# is exactly "N item(s)" -> the flex row parent -> every child's computed
# geometry/colors + the row's own borderTop + the trend icon), at 1280x800
# on the dashboard. READ-ONLY (login + passive navigation only — the v46
# rule; the stat cards navigate on click and are NEVER clicked).
# The v73 heredoc lesson: the QUOTED <<'EOF' with the env-injected census
# JS for the clone half; no literal dollar sequences in the census JS (the
# v64 rule); no single quotes inside single-quoted census strings (the v60
# lesson); tr -d '"' on the extraction (the v124 lesson).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS='(async () => {
  const counts = [...document.querySelectorAll("main *")].filter((el) => {
    if (el.children.length > 0) return false;
    const t = (el.textContent || "").trim();
    return /^[0-9]+ items?$/.test(t);
  });
  if (!counts.length) return JSON.stringify({err: "no item-count spans"});
  const cards = counts.map((span) => {
    const row = span.parentElement;
    const rs = row ? getComputedStyle(row) : null;
    const kids = row ? [...row.children].map((k) => {
      const ks = getComputedStyle(k);
      const r = k.getBoundingClientRect();
      return {
        tag: k.tagName,
        text: (k.textContent || "").trim().slice(0, 24),
        display: ks.display,
        w: Math.round(r.width),
        h: Math.round(r.height),
        bg: ks.backgroundColor,
        borderTopW: ks.borderTopWidth,
        borderTopC: ks.borderTopColor,
      };
    }) : [];
    let card = row;
    while (card && card !== document.body) {
      const cs = getComputedStyle(card);
      if (cs.borderRadius !== "0px" && cs.backgroundColor === "rgb(255, 255, 255)") break;
      card = card.parentElement;
    }
    const title = card ? [...card.querySelectorAll("h3, h2, [class*=title]")].map((h) => (h.textContent || "").trim()).filter(Boolean)[0] : null;
    const svg = row ? row.querySelector("svg") : null;
    const ss = svg ? getComputedStyle(svg) : null;
    const sr = svg ? svg.getBoundingClientRect() : null;
    const rowRect = row ? row.getBoundingClientRect() : null;
    return {
      title: title || "(untitled)",
      countText: (span.textContent || "").trim(),
      row: row ? {
        display: rs.display,
        gap: rs.gap,
        align: rs.alignItems,
        borderTopW: rs.borderTopWidth,
        borderTopStyle: rs.borderTopStyle,
        borderTopC: rs.borderTopColor,
        w: Math.round(rowRect.width),
        h: Math.round(rowRect.height),
      } : null,
      children: kids,
      trendIcon: svg ? { w: Math.round(sr.width), h: Math.round(sr.height), color: ss.color } : null,
    };
  });
  return JSON.stringify({view: "statfooter-1280-v136", cardCount: cards.length, cards});
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refstatfooter136"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "ref login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF: the three stat cards' footer rows (the divider arbitration) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1 | tr -d '"'
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
CENSUS_JS="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonestatfooter136"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
LOGIN_JS="(async () => {
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
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "clone login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
  sleep 3
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== CLONE: the three stat cards' footer rows (the divider arbitration) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1 | tr -d '"'
pkill -f "agent-browser" 2>/dev/null
echo "=== statfooter arbit v136 done ==="
EOF
