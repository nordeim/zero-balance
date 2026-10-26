#!/usr/bin/env bash
# login-shots-v123.sh — the v123 re-run pair's LOGIN half, REFERENCE side: a
# fresh standing sweep of the /login view at desktop 1280x800 (the re-run
# cycle's v117-era LOGIN + CALCULATOR pair, last re-shot v117 — the pair's
# TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123], the FORTY-SIXTH consecutive
# queue/ledger agreement).
# READ-ONLY: passive navigation only (the logged-out surface — no session).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm123

export AGENT_BROWSER_SESSION="reflogin123"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
# the parked pointer (no hover-revealed chrome on this surface, but the
# discipline holds on every shot)
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot /tmp/vlm123/ref-login.png 2>/dev/null | tail -1
# the census (read-only): the card's chrome + the four-state surface
agent-browser eval "(async () => {
  const form = document.querySelector('form');
  const inputs = [...document.querySelectorAll('input')].map(i => ({ type: i.type, ph: (i.placeholder||'').slice(0,30) }));
  const btn = [...document.querySelectorAll('button')].find(b => /sign in|log in/i.test(b.textContent));
  const h1 = document.querySelector('h1');
  return JSON.stringify({ title: document.title, h1: h1 ? h1.textContent.trim() : null, inputs, btn: btn ? { txt: btn.textContent.trim(), w: Math.round(btn.getBoundingClientRect().width), h: Math.round(btn.getBoundingClientRect().height) } : null, hasForgot: !!document.querySelector('a') });
})()" 2>/dev/null | tail -1
echo "ref login shots done"
