#!/usr/bin/env bash
# v38: the VLM pair captures — the /savings view (Surface B, first-time
# measured this session) on both sites at 1280x800. The comparison itself
# runs in vlm-compare-v38.mjs (createVision).
set -u
BASE_REF="https://zero-balance-4885a8f3.base44.app"
BASE_CLONE="http://localhost:3200"
mkdir -p /tmp/vlm38

echo "=== REF /savings capture ==="
export AGENT_BROWSER_SESSION="ref38"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE_REF/savings" >/dev/null 2>&1
sleep 3
agent-browser screenshot /tmp/vlm38/ref-savings.png >/dev/null 2>&1
echo "captured: $(ls -la /tmp/vlm38/ref-savings.png 2>/dev/null | awk '{print $5}') bytes"

echo ""
echo "=== CLONE /savings capture (inside with-server.sh when standalone) ==="
