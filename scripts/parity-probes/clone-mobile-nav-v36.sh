#!/usr/bin/env bash
# v36: clone-side standing checks (30th) — R1-R4 mobile nav + census.
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

echo "=== CLONE census (30th) ==="
bash "$PB/run-probe.sh" clone36 "$PB/census-v35.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R1 (burger hit) at 390x844 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone36 "$PB/probe-r1-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R2 (sheet opens, nav, closes — the superset) ==="
bash "$PB/run-probe.sh" clone36 "$PB/probe-r2-open-v34.mjs" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" clone36 "$PB/probe-r2-nav-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R3 (active nav on /) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone36 "$PB/probe-r3-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R4 (overflow census) ==="
bash "$PB/run-probe.sh" clone36 "$PB/probe-r4a-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE networth overflow (direct) ==="
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3
agent-browser eval "(() => JSON.stringify({ path: location.pathname, sw: document.documentElement.scrollWidth, vw: window.innerWidth }))()" 2>/dev/null | tail -1
agent-browser set viewport 1280 800 >/dev/null 2>&1
