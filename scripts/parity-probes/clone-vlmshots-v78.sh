#!/usr/bin/env bash
# clone-vlmshots-v78.sh — the v78 VLM pair RE-RUN, CLONE side: BOTH mobile
# 390x844 full-page twins — (1) the /NETWORTH view (the v63-era pair's
# surface, the v78 queue item) and (2) the DASHBOARD (the v62-era mobile
# twin's surface). Runs inside with-server.sh (the :3200 parity server).
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm78

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm78"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1

# (1) The networth view at mobile 390 — full page (the parked pointer).
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm78/clone-networth-mobile.png 2>/dev/null | tail -1

# (2) The dashboard at mobile 390 — full page.
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm78/clone-dashboard-mobile.png 2>/dev/null | tail -1

echo "clone mobile shots done (networth + dashboard)"
EOF
