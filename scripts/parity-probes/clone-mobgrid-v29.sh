#!/usr/bin/env bash
# v29: clone mobile summary-card grid measurement (the VLM mobile pair's
# 2-col-vs-1-col flag arbitration).
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-mobgrid-v29.sh
set -u
BASE="http://localhost:3200"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
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

agent-browser eval "JSON.stringify((() => {
  const leaf = [...document.querySelectorAll('p, span, div')].filter(e => (e.textContent||'').trim() === 'Total Assets' && e.children.length === 0)[0];
  if (!leaf) return { error: 'no leaf' };
  let g = leaf.parentElement, chain = [];
  while (g && g.tagName !== 'BODY') {
    const disp = getComputedStyle(g).display;
    chain.push({ disp, cols: getComputedStyle(g).gridTemplateColumns, cls: (g.className||'').slice(0,60) });
    if (disp === 'grid') break;
    g = g.parentElement;
  }
  // also the trend icon inset
  const card = [...document.querySelectorAll('div')].filter(d => /Total Net Worth/i.test(d.textContent)).pop();
  const cr = card ? card.getBoundingClientRect() : null;
  const svg = card ? [...card.querySelectorAll('svg')].map(s => { const r = s.getBoundingClientRect(); return { x: Math.round(r.x), w: Math.round(r.width), insetFromRight: cr ? Math.round(cr.right - r.x - r.width) : null }; })[0] : null;
  return { chain: chain.slice(0, 4), svg };
})())" 2>/dev/null
