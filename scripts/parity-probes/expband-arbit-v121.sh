#!/usr/bin/env bash
# expband-arbit-v121.sh — the ONE-SHOT both-sides arbitration census for the
# v121 candidate pin family: the EXPENSES variant's filter-card md-band
# state (768 <= w < 1024) at 800x600 on /expenses — the band state NO spec
# pins (the coverage map: the expenses filter pinned only at 390 [v52] and
# 1280 [v70/v91]; the v115 md-band pin holds the INCOME variant's state —
# a DIFFERENT source line; the v42 640 census sits BELOW md). The family:
#   the FILTER CARD's inner grid md state — the expenses line's 2-col
#     template (md:grid-cols-2, overridden at lg by grid-cols-4): at 800
#     the tracks read 208px 208px ((480 - 48 pad - 16 gap)/2) — the
#     never-pinned band state of the v70 filter family;
#   the SEARCH WRAPPER's not-spanning state (the expense-conditional
#     relative wrapper — NO md:col-span-2 on this variant; the income
#     twin spans 2 of the 4 tracks): w 208 at the band;
#   the 3 COMBOBOX TRIGGERS' band-state boxes (w 208 / h 36 / fs 14px —
#     the v91 resting-chrome axes at the never-pinned band);
#   the filter CARD's own box in the band (w 480 / mb 24px — the v115
#     income measurement's expenses twin);
#   the docSW 800 guard.
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors (geometry + text-content
# filters only — the reference's class strings are NOT trusted).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const main = document.querySelector('main') || document.body;
  const out = { url: location.pathname };
  // the FILTER CARD's inner grid (the search input -> the rounded-2xl card
  // -> the grid child) — the v115 census finder.
  const search = [...main.querySelectorAll('input')].find(i =>
    (i.getAttribute('placeholder') || '').indexOf('Search') === 0);
  if (!search) { out.searchFound = false; return JSON.stringify(out); }
  let card = search.parentElement;
  for (let i = 0; i < 4 && card; i++) {
    if (getComputedStyle(card).borderRadius === '16px' &&
        getComputedStyle(card).padding === '24px') break;
    card = card.parentElement;
  }
  if (!card) { out.cardFound = false; return JSON.stringify(out); }
  const inner = [...card.children].find(c => getComputedStyle(c).display === 'grid');
  if (!inner) { out.innerFound = false; return JSON.stringify(out); }
  const ics = getComputedStyle(inner);
  out.filterInner = {
    cols: ics.gridTemplateColumns,
    gap: ics.gap,
    childCount: inner.children.length,
  };
  // the SEARCH WRAPPER (the inner grid's first child — the expense-
  // conditional relative wrapper, the NOT-spanning state).
  const wrap = inner.children[0];
  out.searchWrap = {
    w: Math.round(wrap.getBoundingClientRect().width),
    h: Math.round(wrap.getBoundingClientRect().height),
    position: getComputedStyle(wrap).position,
    colSpan: ics.gridColumn.startsWith('span') ? ics.gridColumn : 'auto',
  };
  // the search input's own box inside the wrapper.
  out.searchInput = {
    w: Math.round(search.getBoundingClientRect().width),
    h: Math.round(search.getBoundingClientRect().height),
    fs: getComputedStyle(search).fontSize,
  };
  // the COMBOBOX TRIGGERS (the inner grid's remaining children): the
  // resting boxes at the band — the v91 axes re-measured at 800.
  out.combos = [...inner.children].slice(1).map(kid => {
    const trig = kid.querySelector('[role=combobox]') || kid;
    const tcs = getComputedStyle(trig);
    return {
      w: Math.round(trig.getBoundingClientRect().width),
      h: Math.round(trig.getBoundingClientRect().height),
      fs: tcs.fontSize,
      radius: tcs.borderRadius,
      text: (trig.textContent || '').trim().slice(0, 24),
    };
  });
  // the filter CARD's own box in the band.
  const ccs = getComputedStyle(card);
  out.filterCard = {
    w: Math.round(card.getBoundingClientRect().width),
    h: Math.round(card.getBoundingClientRect().height),
    mb: ccs.marginBottom,
    pad: ccs.padding,
    radius: ccs.borderRadius,
  };
  out.docSW = document.documentElement.scrollWidth;
  out.vw = window.innerWidth;
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (800, /expenses) ==="
export AGENT_BROWSER_SESSION="refexpband121"
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
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- expenses md-band census:"
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (800, /expenses) ==="
cd "$(dirname "$0")/../.."
CENSUS_JS="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneexpband121"
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
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- expenses md-band census:"
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF

echo "=== expband arbit v121 done ==="
