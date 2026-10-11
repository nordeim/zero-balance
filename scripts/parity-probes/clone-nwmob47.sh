#!/usr/bin/env bash
# v47 measurement — clone side: the net-worth card MOBILE census at 390
# (the post-v46-fix internal rhythm + the fit — the reference's own card
# is 432 wide on its 464-overflow page, the clone's documented superset).
set -u
export AGENT_BROWSER_SESSION="clone47b"
BASE="http://localhost:3200"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already?';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 3
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3

echo "=== clone net-worth card census at 390 ==="
agent-browser eval "(() => {
  const grid = [...document.querySelectorAll('div')].find(d => d.className.toString().includes('grid-cols-1') && d.className.toString().includes('md:grid-cols-2') && d.className.toString().includes('lg:grid-cols-3') && d.querySelector('button'));
  if (!grid) return 'no grid';
  const card = grid.children[0];
  const cs = getComputedStyle(card);
  const r = card.getBoundingClientRect();
  const vp = card.querySelector('p.text-2xl');
  const vcs = vp ? getComputedStyle(vp) : null;
  const facts = vp ? vp.parentElement.nextElementSibling : null;
  return JSON.stringify({
    grid: { w: Math.round(grid.getBoundingClientRect().width), gap: getComputedStyle(grid).gap, cols: getComputedStyle(grid).gridTemplateColumns.split(' ').length },
    card: { w: Math.round(r.width), h: Math.round(r.height), pad: cs.padding, radius: cs.borderRadius, borderW: cs.border, shadow: cs.boxShadow, transition: cs.transition },
    value: vcs ? { mb: vcs.marginBottom, fs: vcs.fontSize, lh: vcs.lineHeight, color: vcs.color } : null,
    facts: facts ? { fs: getComputedStyle(facts).fontSize, color: getComputedStyle(facts).color } : null,
    gapMeasured: (vp && facts) ? Math.round(facts.getBoundingClientRect().y - vp.getBoundingClientRect().bottom) : null,
    docSW: document.documentElement.scrollWidth,
    mainSW: document.querySelector('main') ? document.querySelector('main').scrollWidth : null
  });
})()" 2>/dev/null | tail -1
