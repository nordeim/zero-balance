#!/usr/bin/env bash
# v28: clone-side mobile-nav R1-R4 standing check (22nd) — burger hit test,
# sheet trap test, rail active state, per-route overflow, at 390x844.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-mobile-nav-v28.sh
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes

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
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3

echo "=== R1 (burger hit) ==="
bash "$PB/run-probe.sh" default "$PB/probe-r1-v19.mjs" 2>/dev/null
echo "=== R2 (sheet trap) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 2
bash "$PB/run-probe.sh" default "$PB/probe-r2-v20.mjs" 2>/dev/null
echo "=== R4 (per-route overflow) ==="
for p in / /income /expenses /savings /networth; do
  agent-browser open "$BASE$p" >/dev/null 2>&1
  sleep 2
  echo -n "$p → "
  agent-browser eval "JSON.stringify({sw: document.documentElement.scrollWidth})" 2>/dev/null
done
