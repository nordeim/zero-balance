#!/usr/bin/env bash
# v29: clone trend-icon inset measurement (the VLM mobile flag #2).
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-trendicon-v29.sh
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
  const card = [...document.querySelectorAll('div')].find(d => {
    const cs = getComputedStyle(d);
    return /Total Net Worth/i.test(d.textContent) && (cs.backgroundImage || '').includes('linear-gradient') && cs.borderRadius !== '0px';
  });
  if (!card) return { error: 'no card' };
  const cr = card.getBoundingClientRect();
  const svgs = [...card.querySelectorAll('svg')].map(s => {
    const r = s.getBoundingClientRect();
    return { w: Math.round(r.width), h: Math.round(r.height), insetFromRight: Math.round(cr.right - r.right) };
  });
  return { cardRight: Math.round(cr.right), svgs };
})())" 2>/dev/null
