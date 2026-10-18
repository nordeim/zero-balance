#!/usr/bin/env bash
# clone-vlmshots-v86.sh — the v86 standing-pair re-run, CLONE side: the
# SAVINGS view at desktop 1280x800, FULL-PAGE — the fresh sweep of the
# re-run cycle's OLDEST candidate (the v80-era savings pair, last re-shot
# v80, now the oldest remaining [v80 < v81 < v82 < v83 < v84 < v85]; the
# pair's FOURTH re-run [v58 → v65 → v74 → v80 → v86]). Runs inside
# with-server.sh (the :3200 parity server). Read-only.
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm86

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm86"
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
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm86/clone-savings-full.png 2>/dev/null | tail -1

echo "clone savings-pair shots done"
EOF
