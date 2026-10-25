#!/usr/bin/env bash
# clone-vlmshots-v121.sh — the v121 standing-pair re-run, CLONE side: the
# ITEMS view (income + expenses) at desktop 1280x800, FULL-PAGE — the
# fresh re-run of the OLDEST re-run candidate (the v57-era items pair,
# last re-shot v115 — the TENTH re-run of the pair [v57 → v64 → v70 → v79 → v85
# → v91 → v97 → v103 → v109 → v115 → v121]).
# Runs inside with-server.sh (the :3200 parity server). The v56 lesson:
# split the shots into per-view invocations when the 240s timeout bites.
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm121

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm121"
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
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm121/clone-income-full.png 2>/dev/null | tail -1

agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm121/clone-expenses-full.png 2>/dev/null | tail -1

echo "clone items-pair shots done"
EOF
