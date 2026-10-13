#!/usr/bin/env bash
# clone-vlmshots-v57.sh — the v57 VLM pair, CLONE side: the desktop
# 1280x800 state of (1) the INCOME view (the v55 search-input glyph swap
# surface + the item-card grid at 1280), (2) the EXPENSES view (the same
# grid family + the payment-method filter row).
# Runs inside with-server.sh (the :3200 parity server). The v56 lesson:
# split the shots into per-view invocations when the 240s timeout bites.
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm57

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm57"
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

agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
agent-browser screenshot /tmp/vlm57/clone-income.png 2>/dev/null | tail -1

agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser screenshot /tmp/vlm57/clone-expenses.png 2>/dev/null | tail -1

echo "clone shots done"
EOF
