#!/usr/bin/env bash
# v29: clone-side breakdown-row hover computed + mobile-nav R1-R4 (23rd).
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-sweep2-v29.sh
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
agent-browser set viewport 1280 800 >/dev/null 2>&1

echo "=== breakdown nested-row hover (clone) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const rows = [...document.querySelectorAll('button[aria-expanded]')].filter(r => r.offsetParent !== null && /Total Income/i.test(r.textContent));
  rows[0].click();
  await new Promise(r => setTimeout(r, 700));
  const nested = [...document.querySelectorAll('button[aria-expanded]')].filter(r => r.offsetParent !== null && !/Total (Income|Expenses|Savings)/i.test(r.textContent));
  if (!nested.length) return JSON.stringify({ error: 'no nested rows' });
  const row = nested[0];
  const r = row.getBoundingClientRect();
  return JSON.stringify({ txt: row.textContent.trim().slice(0,25), pos: { x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2) }, bgRest: getComputedStyle(row).backgroundColor });
})()" 2>/dev/null
