#!/usr/bin/env bash
# v47: clone-side driver — the three v47 surfaces against :3200 (run
# inside with-server.sh). Read-only on the data (the dialog opens +
# cancels; the sheet opens + escapes).
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone47"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already?';
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

echo "=== CLONE dialog input focus composite at 1280 (Add Income) ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('Add Income')); if (b) { b.click(); return 'clicked'; } return 'not found'; })()" 2>/dev/null | tail -1
sleep 2
bash "$PB/run-probe.sh" clone47 "$PB/dlg-focus-v47.mjs" 2>/dev/null | tail -1
agent-browser eval "(() => { document.querySelector('[role=dialog]')?.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true })); return 'esc'; })()" >/dev/null 2>&1
sleep 1

echo ""
echo "=== CLONE net-worth card mobile census at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone47 "$PB/nw-mobcard-v47.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE mobile sheet chrome census at 390 ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('Toggle Sidebar')); if (b) { b.click(); return 'opened'; } return 'no toggle'; })()" 2>/dev/null | tail -1
sleep 2
bash "$PB/run-probe.sh" clone47 "$PB/sheet-chrome-v47.mjs" 2>/dev/null | tail -1
agent-browser eval "(() => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('Toggle Sidebar')); if (b) { b.click(); return 'closed'; } return 'no toggle'; })()" 2>/dev/null | tail -1
