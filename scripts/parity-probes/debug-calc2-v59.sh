#!/usr/bin/env bash
# debug-calc2-v59.sh — second debug attempt using the high-level click/hover
# commands (they handle actionability + real input events).
set -u
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clone59db2"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
# hover the rent card via the high-level hover (a real pointer move)
agent-browser hover "div.rounded-xl:has-text('Rent'):has-text('\$1850')" 2>&1 | tail -1
sleep 1
# click the Calculate button via the high-level click
agent-browser click "div.rounded-xl:has-text('Rent') button:has-text('Calculate')" 2>&1 | tail -1
sleep 3
agent-browser eval "(async () => {
  const dlgs = [...document.querySelectorAll('[role=dialog]')];
  return JSON.stringify({ dlgCount: dlgs.length, texts: dlgs.map(d => (d.innerText||'').split('\n')[0]), bodyHasCalc: /Rent Calculator/.test(document.body.innerText) });
})()" 2>/dev/null | tail -1
EOF
