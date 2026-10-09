#!/usr/bin/env bash
# v28: clone-side real-Tab walk to the card Edit/Calculate buttons on
# /expenses — mirrors the reference walk (parked pointer, 12 stops).
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-tabwalk-v28.sh
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  const set = (el, v) => {
    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
    setter.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser mouse move 5 5 >/dev/null 2>&1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3

for i in $(seq 1 12); do
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.35
  R=$(bash "$PB/run-probe.sh" default "$PB/probe-v28-focus-stop.mjs" 2>/dev/null)
  echo "stop $i: $(echo "$R" | head -c 340)"
done
