#!/usr/bin/env bash
# v36: clone-side Surface C — the Tab-order census of /income (REAL Tab presses).
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

agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3

echo "=== CLONE Tab walk on /income (18 stops) ==="
bash "$PB/tabwalk-v36.sh" clone36 18 2>/dev/null
