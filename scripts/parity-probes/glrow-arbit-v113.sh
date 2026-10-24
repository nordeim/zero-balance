#!/usr/bin/env bash
# glrow-arbit-v113.sh — the ONE-SHOT both-sides arbitration census for the
# v113 F4 candidate: the BUDGET GUIDELINES card's TILE LABEL-ROW family +
# the tile stack rhythm at 1280 (the guidelines card renders below the
# fold on the dashboard — passive render, zero clicks, the v46 read-only
# rule holds). The never-pinned family (the coverage map: the v61 F2 pin
# holds the card box + first-tile box + the STRETCH contract; the v77 F4
# pin the header typography + all three tiles' label/pct/desc TEXT chrome
# + the qa icon viewBoxes; the v89 F4 pin the qa transition + plus
# viewBoxes + the body display/pad; the v83 F4 pin the card bottom / grid
# top / rendered gap / grid mt — NEVER the label-row's own flex chrome
# {display/align/justify/mb/h}, NEVER the label/pct edge anchors (the
# justify-between consequence), NEVER the tile-to-tile stack rhythm):
# (1) the row {display flex, align center, justify space-between, mb, h}
# (2) the junction — the label at the row's LEFT edge, the pct at the
#     row's RIGHT edge
# (3) the tile rhythm — the two inter-tile gaps (the space-y-3 stack).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS (the v64 rule — no money regexes needed, the finders are structural);
# no backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const heading = [...document.querySelectorAll('h1,h2,h3,div,span')].find(
    (e) => (e.textContent || '').trim() === 'Budget Guidelines' && e.children.length === 0
  );
  if (!heading) return 'no guidelines heading';
  let card = heading;
  while (card.parentElement) {
    const cs = getComputedStyle(card);
    if (cs.boxShadow !== 'none' && cs.borderRadius !== '0px' && card.querySelector('p')) break;
    card = card.parentElement;
  }
  if (!card || card === heading) return 'no card';
  const tiles = [...card.querySelectorAll('div')].filter((d) => {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return (
      cs.borderRadius === '8px' && r.height > 40 && r.height < 200 &&
      d.querySelector('span, p') && cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && d !== card
    );
  });
  if (tiles.length !== 3) return 'tile count ' + tiles.length;
  // The label row of tile 0 (Needs): label = the FIRST span, pct = the
  // LAST span; the row = the nearest flex ancestor of the label that ALSO
  // contains the pct (the structural walk — the v72 class; never by class
  // alone).
  const t0 = tiles[0];
  const spans = [...t0.querySelectorAll('span')].filter((s) => s.children.length === 0);
  const label = spans[0];
  const pct = spans[spans.length - 1];
  if (!label || !pct || label === pct) return 'no label/pct pair';
  let row = label.parentElement;
  while (row && row !== t0) {
    if (row.contains(pct) && getComputedStyle(row).display === 'flex') break;
    row = row.parentElement;
  }
  if (!row || row === t0) return 'no label row';
  const rcs = getComputedStyle(row);
  const rr = row.getBoundingClientRect();
  const lr = label.getBoundingClientRect();
  const pr = pct.getBoundingClientRect();
  const trs = tiles.map((t) => t.getBoundingClientRect());
  return JSON.stringify({
    docSW: window.innerWidth,
    row: {
      display: rcs.display,
      align: rcs.alignItems,
      justify: rcs.justifyContent,
      mb: rcs.marginBottom,
      h: Math.round(rr.height),
      w: Math.round(rr.width),
      childCount: row.children.length,
    },
    label: {
      text: (label.textContent || '').trim(),
      xInRow: Math.round(lr.left - rr.left),
      fs: getComputedStyle(label).fontSize,
      fw: getComputedStyle(label).fontWeight,
    },
    pct: {
      text: (pct.textContent || '').trim(),
      rightGap: Math.round(rr.right - pr.right),
      fs: getComputedStyle(pct).fontSize,
      fw: getComputedStyle(pct).fontWeight,
    },
    junction: {
      labelAtLeft: Math.abs(lr.left - rr.left) < 0.5,
      pctAtRight: Math.abs(rr.right - pr.right) < 0.5,
      centersAligned: Math.abs((lr.top + lr.height / 2) - (pr.top + pr.height / 2)) < 1.5,
    },
    tileRhythm: {
      gap1: Math.round(trs[1].top - trs[0].bottom),
      gap2: Math.round(trs[2].top - trs[1].bottom),
    },
  });
})()"

echo "=== REFERENCE side (1280, /dashboard guidelines card) ==="
export AGENT_BROWSER_SESSION="refgr113"
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- guidelines label-row census:"
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo ""
echo "=== CLONE side (1280, /dashboard guidelines card) ==="
cd "$(dirname "$0")/../.."
CENSUS_EXPORT="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonegr113"
export CENSUS_JS="$CENSUS_EXPORT"
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
agent-browser open "http://localhost:3200/dashboard" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- guidelines label-row census:"
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== glrow arbit v113 done ==="
