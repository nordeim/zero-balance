#!/usr/bin/env bash
# headgap-arbit-v102.sh — the supplemental one-shot census arbitrating the
# v102 cycle's NEW VLM flag: the networth mobile page's "top header
# spacing" claimed "noticeably larger in the reference" (the vertical gap
# between the top navigation bar and the 'Net Worth' header). Measures the
# top-bar height + the h1 block + BOTH gaps (topbar→h1, h1→summary card)
# on BOTH sides at 390x844 — the geometric form (the v98/v99 lesson).
# READ-ONLY. The v87..v96 one-shot precedent.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

HG_CENSUS="(async () => {
  // the top bar: the fixed/sticky header chrome containing the burger
  const burger = [...document.querySelectorAll('button, [role=button]')].find(b => {
    const t = (b.getAttribute('aria-label') || '').toLowerCase();
    return t.includes('menu') || t.includes('open');
  }) || document.querySelector('header button');
  const topbar = burger ? burger.closest('header, div') : document.querySelector('header');
  // the page h1 ('Net Worth')
  const h1 = [...document.querySelectorAll('h1')].find(h => (h.textContent || '').includes('Net Worth'));
  // the gradient summary card (same finder as NW_CENSUS)
  const cards = [...document.querySelectorAll('main div, div')].filter(d => {
    const s = getComputedStyle(d);
    return d.getBoundingClientRect().height > 100 && d.getBoundingClientRect().width > 200
      && s.backgroundImage && s.backgroundImage.includes('linear-gradient');
  });
  const card = cards.find(c => c.getBoundingClientRect().width < 500) || cards[0];
  if (!topbar || !h1 || !card) return JSON.stringify({found: {topbar: !!topbar, h1: !!h1, card: !!card}});
  const tr = topbar.getBoundingClientRect();
  const hr = h1.getBoundingClientRect();
  const cr = card.getBoundingClientRect();
  const tbStyle = getComputedStyle(topbar);
  return JSON.stringify({
    docSW: document.documentElement.scrollWidth,
    topbar: { h: Math.round(tr.height), bottom: Math.round(tr.bottom), pos: tbStyle.position },
    h1: { h: Math.round(hr.height), top: Math.round(hr.top), fs: getComputedStyle(h1).fontSize, fw: getComputedStyle(h1).fontWeight, lh: getComputedStyle(h1).lineHeight },
    gapTopbarToH1: Math.round(hr.top - tr.bottom),
    gapH1ToCard: Math.round(cr.top - hr.bottom)
  });
})()"

echo "=== REFERENCE side (390): header rhythm ==="
export AGENT_BROWSER_SESSION="headgapref102"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$HG_CENSUS" 2>/dev/null | tail -1

echo "=== CLONE side (390): header rhythm ==="
cd "$(dirname "$0")/../.."
HG_CENSUS="$HG_CENSUS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="headgapclone102"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$HG_CENSUS" 2>/dev/null | tail -1
EOF
echo "=== headgap arbitration v102 done ==="
