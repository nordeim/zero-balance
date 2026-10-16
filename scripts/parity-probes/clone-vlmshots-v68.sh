#!/usr/bin/env bash
# clone-vlmshots-v68.sh — the v68 re-run of the v61-era standing pair, CLONE
# side: the DASHBOARD at desktop 1280x800 FULL-PAGE (the Budget Guidelines
# card + the quick-action row — the two v61-era surfaces, re-proved by the
# v68 re-run after v62-v67). Runs inside with-server.sh (the :3200 parity
# server).
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm68

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm68"
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
agent-browser screenshot --full /tmp/vlm68/clone-dashboard.png 2>/dev/null | tail -1

echo "clone shots done"
EOF
