#!/usr/bin/env bash
# v44: the multi-viewport census driver — runs the drill-down expanded-state
# census (exp-vp-v44.mjs) + the donut legend census (legend-v44.mjs) at BOTH
# remaining viewport classes: 390x844 (mobile) and 1280x800 (desktop). The
# v43 session pinned 640x960; this completes the matrix.
# Usage: bash scripts/parity-probes/vp-census-v44.sh <session> <base-url>
# The session must already be logged in (the driver does NOT log in —
# pair it with the ref-v40.sh / clone-v40.sh login idiom).
set -u
S="${1:?session}"
BASE="${2:?base url}"
PB=/home/z/my-project/zero-balance/scripts/parity-probes

for VP in "390 844" "1280 800"; do
  set -- $VP
  agent-browser --session "$S" set viewport "$1" "$2" >/dev/null 2>&1
  agent-browser --session "$S" open "$BASE/" >/dev/null 2>&1
  sleep 3
  echo "=== [$S] drill-down census @ ${1}x${2} ==="
  bash "$PB/run-probe.sh" "$S" "$PB/exp-vp-v44.mjs" 2>/dev/null | tail -1
  echo ""
  echo "=== [$S] donut legend census @ ${1}x${2} ==="
  bash "$PB/run-probe.sh" "$S" "$PB/legend-v44.mjs" 2>/dev/null | tail -1
  echo ""
done
agent-browser --session "$S" set viewport 1280 800 >/dev/null 2>&1
