#!/usr/bin/env bash
# clone-login-shots-v129.sh — the v129 re-run pair's LOGIN half, CLONE side: a
# fresh standing sweep of the /login view at desktop 1280x800 (the re-run
# cycle's v123-era LOGIN + CALCULATOR pair, last re-shot v123 — the pair's
# ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129]). Runs
# inside with-server.sh (the :3200 parity server). The logged-out surface
# (the parity browser session is a fresh context, no cookie).
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm129

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonelogin129"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot /tmp/vlm129/clone-login.png 2>/dev/null | tail -1
agent-browser eval "(async () => {
  const form = document.querySelector('form');
  const inputs = [...document.querySelectorAll('input')].map(i => ({ type: i.type, ph: (i.placeholder||'').slice(0,30) }));
  const btn = [...document.querySelectorAll('button')].find(b => /sign in|log in/i.test(b.textContent));
  const h1 = document.querySelector('h1');
  return JSON.stringify({ title: document.title, h1: h1 ? h1.textContent.trim() : null, inputs, btn: btn ? { txt: btn.textContent.trim(), w: Math.round(btn.getBoundingClientRect().width), h: Math.round(btn.getBoundingClientRect().height) } : null, hasForgot: !!document.querySelector('a') });
})()" 2>/dev/null | tail -1
echo "clone login shots done"
EOF
