#!/usr/bin/env bash
# v35: clone-side Surface A — the item-card action menu's open-state + item focus.
# Runs INSIDE with-server.sh (the :3200 parity server).
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone35"

agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 4

echo "=== CLONE menu census (fresh open via REAL Enter on the trigger) ==="
# land a REAL Tab onto the trigger first (the card menu button), then Enter to open
agent-browser eval "(async () => {
  const trig = [...document.querySelectorAll('button')].find(b => b.getAttribute('aria-haspopup') === 'menu');
  if (!trig) return JSON.stringify({error: 'no trigger'});
  trig.focus();
  return 'focused ' + trig.getAttribute('aria-label');
})()" 2>/dev/null | tail -1
agent-browser press Tab >/dev/null 2>&1
agent-browser press Shift+Tab >/dev/null 2>&1
sleep 1
agent-browser press Enter
sleep 1
bash "$PB/run-probe.sh" clone35 "$PB/probe-menu-full-v35.mjs" 2>/dev/null | tail -1 | head -c 200
echo ""
echo "=== CLONE menu census (structure — direct read) ==="
bash "$PB/run-probe.sh" clone35 "$PB/probe-menu-census-v35.mjs" 2>/dev/null | tail -1 | head -c 700
echo ""
echo "=== CLONE item focus after REAL ArrowDown x2 (rove to Delete) ==="
agent-browser press ArrowDown >/dev/null 2>&1
sleep 0.6
agent-browser press ArrowDown >/dev/null 2>&1
sleep 0.8
bash "$PB/run-probe.sh" clone35 "$PB/probe-menu-itemfocus-v35.mjs" 2>/dev/null | tail -1
echo ""
echo "=== CLONE Escape behavior ==="
agent-browser press Escape >/dev/null 2>&1
sleep 0.8
agent-browser eval "JSON.stringify({menuStillOpen: !!document.querySelector('[role=menu]'), active: document.activeElement.tagName + ':' + (document.activeElement.getAttribute('aria-expanded') || '')})" 2>/dev/null | tail -1
