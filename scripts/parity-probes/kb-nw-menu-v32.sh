#!/usr/bin/env bash
# v32: the net-worth dropdown menu's FULL keyboard contract (REAL key presses
# via agent-browser press — programmatic focus never proves :focus-visible).
# Verdict measured: byte-identical on both sites — click-open → container
# focus (tabindex -1, items -1, no highlight); Enter-open → first item
# focused + highlighted; ArrowDown/Up rove; NO wrap at ends (clamped);
# Home/End work; NO typeahead; Escape closes + focus returns to the trigger.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/kb-nw-menu-v32.sh   # clone
#        (reference: run the same steps against the live URL, no wrapper)
set -u
BASE="${1:-http://localhost:3200}"
S="${2:-clone32}"

agent-browser --session "$S" open "$BASE/networth" >/dev/null 2>&1
sleep 5
agent-browser --session "$S" click "button[aria-haspopup=menu]" >/dev/null 2>&1
sleep 1
echo "=== click-open structure ==="
agent-browser --session "$S" eval "(() => {
  const menu = document.querySelector('[role=menu]');
  const items = [...(menu ? menu.querySelectorAll('[role=menuitem]') : [])];
  return JSON.stringify({ focusedRole: document.activeElement.getAttribute('role'), items: items.map(i => i.textContent.trim() + (i.getAttribute('data-highlighted') !== null ? '*' : '') + ' tab=' + i.tabIndex) });
})()" 2>/dev/null
echo "--- ArrowDown x2 + clamped 3rd ---"
for i in 1 2 3; do
  agent-browser --session "$S" press ArrowDown >/dev/null 2>&1; sleep 0.4
  agent-browser --session "$S" eval "(() => JSON.stringify({ focused: document.activeElement.textContent.trim() }))()" 2>/dev/null
done
echo "--- ArrowUp + clamped 2nd ---"
for i in 1 2; do
  agent-browser --session "$S" press ArrowUp >/dev/null 2>&1; sleep 0.4
  agent-browser --session "$S" eval "(() => JSON.stringify({ focused: document.activeElement.textContent.trim() }))()" 2>/dev/null
done
echo "--- Home / End / typeahead ---"
agent-browser --session "$S" press Home >/dev/null 2>&1; sleep 0.3
agent-browser --session "$S" eval "(() => JSON.stringify({ afterHome: document.activeElement.textContent.trim() }))()" 2>/dev/null
agent-browser --session "$S" press End >/dev/null 2>&1; sleep 0.3
agent-browser --session "$S" press Home >/dev/null 2>&1; sleep 0.3
agent-browser --session "$S" keyboard type d >/dev/null 2>&1; sleep 0.4
agent-browser --session "$S" eval "(() => JSON.stringify({ typeaheadD: document.activeElement.textContent.trim(), menuStill: !!document.querySelector('[role=menu]') }))()" 2>/dev/null
echo "--- Escape focus-return ---"
agent-browser --session "$S" press Escape >/dev/null 2>&1; sleep 0.5
agent-browser --session "$S" eval "(() => { const ae = document.activeElement; return JSON.stringify({ menuClosed: !document.querySelector('[role=menu]'), focusTag: ae.tagName, focusHasPopup: ae.getAttribute('aria-haspopup'), focusLabel: ae.getAttribute('aria-label') }); })()" 2>/dev/null
echo "--- keyboard-open (Enter on trigger) ---"
agent-browser --session "$S" focus "button[aria-haspopup=menu]" >/dev/null 2>&1
agent-browser --session "$S" press Enter >/dev/null 2>&1; sleep 0.6
agent-browser --session "$S" eval "(() => JSON.stringify({ kbOpenFocus: document.activeElement.getAttribute('role'), text: document.activeElement.textContent.trim() }))()" 2>/dev/null
agent-browser --session "$S" press Escape >/dev/null 2>&1
