#!/usr/bin/env bash
# mdband-arbit-v115.sh — the ONE-SHOT both-sides arbitration census for the
# v115 candidate pin family: the ITEMS view's md-band state (768 <= w < 1024)
# at 800x600 on /income — the band NO spec pins (the coverage map: the items
# views pinned only at 390 [v52] and 1280 [v45/v64/v91/v92/v109]; the v42
# 640 census sits BELOW md — the 1-col state). The family:
#   the ITEM GRID's md state (the 2-col template + gap + the card box at
#     the 2-col width) — the never-pinned state of the v45 grid family;
#   the PAGE HEADER ROW's md state (flex-row/space-between/center/gap 16)
#     — the never-pinned state of the v109 row family;
#   the FILTER CARD's inner grid md state (the 4-track template at 800)
#     — the never-pinned state of the v64 filter family;
#   the docSW 800 guard.
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors (geometry + text-content
# filters only — the reference's class strings are NOT trusted).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const main = document.querySelector('main') || document.body;
  // the ITEM GRID: the grid inside main whose children are CARD-like
  // (radius 12px + pad 20px + bg white) — robust across sites.
  const grids = [...main.querySelectorAll('div')].filter(d => {
    if (getComputedStyle(d).display !== 'grid') return false;
    const kids = [...d.children];
    return kids.length >= 1 && kids.every(k => {
      const cs = getComputedStyle(k);
      return cs.borderRadius === '12px' && cs.padding === '20px';
    });
  });
  const out = { url: location.pathname };
  if (!grids.length) { out.gridFound = false; return JSON.stringify(out); }
  const grid = grids[0];
  const gcs = getComputedStyle(grid);
  const card0 = grid.children[0];
  const ccs = getComputedStyle(card0);
  out.grid = {
    display: gcs.display,
    cols: gcs.gridTemplateColumns,
    gap: gcs.gap,
    childCount: grid.children.length,
  };
  out.card0 = {
    w: Math.round(card0.getBoundingClientRect().width),
    h: Math.round(card0.getBoundingClientRect().height),
    pad: ccs.padding,
    radius: ccs.borderRadius,
    border: ccs.borderTopColor,
    bg: ccs.backgroundColor,
  };
  // the PAGE HEADER ROW (the v109 walk): the Add button -> UP to the
  // container holding the visible h1.
  const addBtn = [...main.querySelectorAll('button')].find(b =>
    (b.textContent || '').trim().startsWith('Add') &&
    b.getBoundingClientRect().top < 200);
  if (addBtn) {
    let row = null;
    let cur = addBtn.parentElement;
    for (let i = 0; i < 6 && cur; i++) {
      if (cur.querySelector('h1') && cur !== addBtn) { row = cur; break; }
      cur = cur.parentElement;
    }
    if (row) {
      const rcs = getComputedStyle(row);
      out.headerRow = {
        display: rcs.display,
        flexDirection: rcs.flexDirection,
        justify: rcs.justifyContent,
        align: rcs.alignItems,
        gap: rcs.columnGap,
        mb: rcs.marginBottom,
        h: Math.round(row.getBoundingClientRect().height),
        childCount: row.children.length,
      };
    }
  }
  // the FILTER CARD's inner grid (the search input -> the rounded-2xl card
  // -> the grid child).
  const search = [...main.querySelectorAll('input')].find(i =>
    (i.getAttribute('placeholder') || '').indexOf('Search') === 0);
  if (search) {
    let card = search.parentElement;
    for (let i = 0; i < 4 && card; i++) {
      if (getComputedStyle(card).borderRadius === '16px' &&
          getComputedStyle(card).padding === '24px') break;
      card = card.parentElement;
    }
    if (card) {
      const inner = [...card.children].find(c =>
        getComputedStyle(c).display === 'grid');
      if (inner) {
        const ics = getComputedStyle(inner);
        out.filterInner = {
          cols: ics.gridTemplateColumns,
          gap: ics.gap,
          childCount: inner.children.length,
        };
        out.filterCard = {
          w: Math.round(card.getBoundingClientRect().width),
          mb: getComputedStyle(card).marginBottom,
        };
      }
    }
  }
  out.docSW = document.documentElement.scrollWidth;
  out.vw = window.innerWidth;
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (800, /income) ==="
export AGENT_BROWSER_SESSION="refmdband115"
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
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 800 600 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- md-band census:"
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (800, /income) ==="
cd "$(dirname "$0")/../.."
CENSUS_JS="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonemdband115"
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
agent-browser set viewport 800 600 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- md-band census:"
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF

echo "=== mdband arbit v115 done ==="
