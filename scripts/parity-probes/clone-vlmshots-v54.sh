#!/usr/bin/env bash
# clone side of vlm-shots-v54.sh — the same two surfaces at 390x844 from
# the clone's standalone server (:3200, with-server boots fresh).
set -u
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm54"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 3
agent-browser screenshot /tmp/vlm54/clone-networth.png 2>/dev/null | tail -1
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 3
agent-browser screenshot /tmp/vlm54/clone-savings.png 2>/dev/null | tail -1
echo "clone shots done"
EOF
