#!/usr/bin/env bash
# v44: the clone-side measurement — login + the multi-viewport census (the
# drill-down at 390/1280 + the donut legend) + the collapse-direction probe,
# all INSIDE one with-server.sh invocation (the server dies between tool
# calls). Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-v44.sh
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone44"

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

bash "$PB/vp-census-v44.sh" clone44 "$BASE"

echo "=== [clone44] collapse-direction probe @ 390x844 ==="
agent-browser --session clone44 set viewport 390 844 >/dev/null 2>&1
agent-browser --session clone44 open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone44 "$PB/collapse-ref-v44.mjs" 2>/dev/null | tail -1
echo ""
echo "=== [clone44] band-mount probe @ 390x844 ==="
bash "$PB/run-probe.sh" clone44 "$PB/band-mount-v44.mjs" 2>/dev/null | tail -1
agent-browser --session clone44 set viewport 1280 800 >/dev/null 2>&1
