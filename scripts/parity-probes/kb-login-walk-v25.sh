#!/usr/bin/env bash
# v25: the login page's FULL keyboard focus walk — REAL Tab presses (CDP)
# with a focus-chrome read after each stop, covering every focusable on the
# page (inputs, swap buttons, submit). Pointer parked at (5,5) first.
# Usage: kb-login-walk-v25.sh <login-url> <tab-count>
set -u
SITE="$1"
TABS="${2:-10}"

agent-browser open "$SITE" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => { const sleep = (ms) => new Promise((r) => setTimeout(r, ms)); window.scrollTo(0, 0); await sleep(100); return 'parked'; })()" >/dev/null 2>&1

for i in $(seq 1 "$TABS"); do
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.35   # the 200ms transition family + settle (the v23 65%-opacity lesson)
  echo "--- stop #$i ---"
  bash /home/z/my-project/zero-balance/scripts/parity-probes/run-probe.sh default /home/z/my-project/zero-balance/scripts/parity-probes/probe-v25-focus-stop.mjs 2>/dev/null | head -1
done
