#!/usr/bin/env bash
# clone-vlmshots-v58.sh — the v58 VLM pair, CLONE side: the desktop
# 1280x800 state of the SAVINGS view (the items family's remaining view).
# Runs inside with-server.sh (the :3200 parity server). The v56 lesson:
# split the shots into per-view invocations when the 240s timeout bites.
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm58

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm58"
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

agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 4
agent-browser screenshot /tmp/vlm58/clone-savings.png 2>/dev/null | tail -1

echo "clone shots done"
EOF
