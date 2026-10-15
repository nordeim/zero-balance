#!/usr/bin/env bash
# clone-vlmshots-v61.sh — the v61 VLM pair, CLONE side: the DASHBOARD at
# desktop 1280x800 FULL-PAGE (the Budget Guidelines card + the quick-action
# row — the two v61 queue surfaces). Runs inside with-server.sh (the :3200
# parity server).
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm61

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm61"
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

# The dashboard at desktop 1280 — full page.
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm61/clone-dashboard.png 2>/dev/null | tail -1

echo "clone shots done"
EOF
