#!/usr/bin/env bash
# v35: clone-side Surface A CLEAN — fresh-open contract without synthetic toggles.
# Runs INSIDE with-server.sh (the :3200 parity server).
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone35"

agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 4

echo "=== CLONE fresh-open initial focus (programmatic focus + REAL Enter) ==="
agent-browser eval "(async () => {
  const trig = [...document.querySelectorAll('button')].find(b => b.getAttribute('aria-haspopup') === 'menu');
  if (!trig) return JSON.stringify({error: 'no trigger'});
  trig.focus();
  return 'ok';
})()" >/dev/null 2>&1
agent-browser press Enter >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const m = document.querySelector('[role=menu]');
  if (!m) return JSON.stringify({menuOpen: false});
  const ae = document.activeElement;
  return JSON.stringify({
    menuOpen: true,
    initialActive: ae.tagName + ':' + (ae.getAttribute('role') || ae.textContent || '').toString().slice(0, 12),
    items: [...m.querySelectorAll('[role=menuitem]')].map(i => i.textContent.trim()),
  });
})()" 2>/dev/null | tail -1

echo "=== CLONE Home/End + Tab-trap ==="
agent-browser press End >/dev/null 2>&1; sleep 0.5
agent-browser eval "(async () => JSON.stringify({afterEnd: (document.activeElement.getAttribute('role')||'') + ':' + (document.activeElement.textContent||'').trim().slice(0,8)}))()" 2>/dev/null | tail -1
agent-browser press Home >/dev/null 2>&1; sleep 0.5
agent-browser eval "(async () => JSON.stringify({afterHome: (document.activeElement.getAttribute('role')||'') + ':' + (document.activeElement.textContent||'').trim().slice(0,8)}))()" 2>/dev/null | tail -1
agent-browser press Tab >/dev/null 2>&1; sleep 0.6
agent-browser eval "(async () => JSON.stringify({afterTab_menuOpen: !!document.querySelector('[role=menu]'), afterTab_active: (document.activeElement.getAttribute('role')||'') + ':' + (document.activeElement.textContent||'').trim().slice(0,8)}))()" 2>/dev/null | tail -1

echo "=== CLONE trigger fresh-open via REAL ArrowDown (Radix 2.3.8 behavior) ==="
agent-browser press Escape >/dev/null 2>&1; sleep 0.8
agent-browser press ArrowDown >/dev/null 2>&1; sleep 0.8
agent-browser eval "(async () => JSON.stringify({menuOpenAfterArrowDown: !!document.querySelector('[role=menu]'), active: (document.activeElement.getAttribute('role')||document.activeElement.tagName) + ':' + (document.activeElement.textContent||'').trim().slice(0,8)}))()" 2>/dev/null | tail -1
agent-browser press Escape >/dev/null 2>&1; sleep 0.5
echo "closed"
