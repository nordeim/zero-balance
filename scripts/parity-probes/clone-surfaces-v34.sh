#!/usr/bin/env bash
# v34: clone-side surface probes — the forgot-state focus walk + the
# frequency Select listbox keyboard contract. Runs INSIDE with-server.sh.
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes

# login first (desktop viewport)
agent-browser set viewport 1280 800 >/dev/null 2>&1
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
sleep 2
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 2

echo "=== CLONE forgot state: open + census ==="
agent-browser eval "(async () => {
  const b = [...document.querySelectorAll('button')].find(x => /forgot/i.test(x.textContent));
  if (b) b.click();
  await new Promise(r => setTimeout(r, 600));
  return 'clicked: ' + (b ? 'yes' : 'no');
})()" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" default "$PB/probe-forgot-census-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE forgot Tab walk (parked, REAL Tab) ==="
agent-browser eval "document.activeElement.blur && document.activeElement.blur(); 'parked'" >/dev/null 2>&1
sleep 0.3
agent-browser press Tab >/dev/null 2>&1; sleep 0.8
echo "T1:"; bash "$PB/run-probe.sh" default "$PB/probe-focus-read-v34.mjs" 2>/dev/null | tail -1
agent-browser press Tab >/dev/null 2>&1; sleep 0.8
echo "T2:"; bash "$PB/run-probe.sh" default "$PB/probe-focus-read-v34.mjs" 2>/dev/null | tail -1
agent-browser press Tab >/dev/null 2>&1; sleep 0.8
echo "T3:"; bash "$PB/run-probe.sh" default "$PB/probe-focus-read-v34.mjs" 2>/dev/null | tail -1
agent-browser press Tab >/dev/null 2>&1; sleep 0.8
echo "T4:"; bash "$PB/run-probe.sh" default "$PB/probe-focus-read-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE forgot submit (honest no-mail state) ==="
bash "$PB/run-probe.sh" default "$PB/probe-forgot-submit-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE frequency listbox: open + census ==="
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" default "$PB/probe-calc-open-v34.mjs" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" default "$PB/probe-lisub-open-v34.mjs" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" default "$PB/probe-freq-open-v34.mjs" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" default "$PB/probe-freq-census-v34.mjs" 2>/dev/null | tail -1
