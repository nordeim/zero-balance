#!/usr/bin/env bash
# v29: live DOM experiment — flip the clone's mobile summary grid to the
# reference's 2-col and measure fit + cell overflow with the seed data.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-gridtest-v29.sh
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
  let g = leaf.parentElement; while (g && getComputedStyle(g).display !== 'grid') g = g.parentElement;
  // patch to the reference's 2-col
  g.className = 'grid grid-cols-2 gap-4';
  const sw = document.documentElement.scrollWidth;
  const cs = getComputedStyle(g);
  // per-cell text overflow check
  const cells = [...g.children].map(c => {
    const cr = c.getBoundingClientRect();
    const ps = [...c.querySelectorAll('p')].map(p => {
      const pr = p.getBoundingClientRect();
      return { txt: p.textContent.trim().slice(0,18), w: Math.round(pr.width), right: Math.round(pr.right), fs: getComputedStyle(p).fontSize };
    });
    return { cellW: Math.round(cr.width), cellRight: Math.round(cr.right), ps };
  });
  return { swAfter: sw, cols: cs.gridTemplateColumns, cells,
    glyphOverflow: [...g.querySelectorAll('p')].map(p => ({ txt: p.textContent.trim().slice(0,14), clientW: p.clientWidth, scrollW: p.scrollWidth, overflows: p.scrollWidth > p.clientWidth })) };
})())" 2>/dev/null
