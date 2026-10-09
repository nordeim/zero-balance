#!/usr/bin/env bash
# v29: clone-side breakdown nested-row REAL hover measurement.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-bdhover-v29.sh
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
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const rows = [...document.querySelectorAll('button[aria-expanded]')].filter(r => r.offsetParent !== null && /Total Income/i.test(r.textContent));
  rows[0].click();
  return 'expanded';
})()" >/dev/null 2>&1
sleep 1
POS=$(agent-browser eval "(() => {
  const nested = [...document.querySelectorAll('button[aria-expanded]')].filter(r => r.offsetParent !== null && !/Total/i.test(r.textContent));
  const row = nested[0];
  const r = row.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ' ' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tr -d '"')
X=$(echo "$POS" | cut -d' ' -f1)
Y=$(echo "$POS" | cut -d' ' -f2)
echo "hovering at $X $Y"
agent-browser mouse move "$X" "$Y" >/dev/null 2>&1
sleep 0.7
agent-browser eval "JSON.stringify((() => {
  const nested = [...document.querySelectorAll('button[aria-expanded]')].filter(r => r.offsetParent !== null && !/Total/i.test(r.textContent));
  return { bgHover: getComputedStyle(nested[0]).backgroundColor };
})())" 2>/dev/null
