#!/usr/bin/env bash
# v36: clone-side Surface A (action-menu HOVER-highlight family) live probe.
# Runs INSIDE with-server.sh (the :3200 parity server).
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone36"

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

echo "=== CLONE login + census (30th) ==="
bash "$PB/run-probe.sh" clone36 "$PB/census-v35.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE Surface A: hover-highlight family ==="
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3
# open the action menu via CLICK (pointerdown family)
bash "$PB/run-probe.sh" clone36 "$PB/probe-menu-openonly-v36.mjs" 2>/dev/null | tail -1
