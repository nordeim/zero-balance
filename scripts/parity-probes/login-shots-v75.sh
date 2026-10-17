#!/usr/bin/env bash
# login-shots-v75.sh — the v75 re-run pair's LOGIN half, REFERENCE side: a
# fresh standing sweep of the /login view at desktop 1280x800 (the re-run
# cadence's v59-era pair, last re-shot v66 — the session-179 v75 queue).
# READ-ONLY: passive navigation only (the logged-out surface — no session).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm75

export AGENT_BROWSER_SESSION="reflogin75"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
# the parked pointer (no hover-revealed chrome on this surface, but the
# discipline holds on every shot)
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot /tmp/vlm75/ref-login.png 2>/dev/null | tail -1
# the census (read-only): the card's chrome + the four-state surface
agent-browser eval "(async () => {
  const form = document.querySelector('form');
  const inputs = [...document.querySelectorAll('input')].map(i => ({ type: i.type, ph: (i.placeholder||'').slice(0,30) }));
  const btn = [...document.querySelectorAll('button')].find(b => /sign in|log in/i.test(b.textContent));
  const h1 = document.querySelector('h1');
  return JSON.stringify({ title: document.title, h1: h1 ? h1.textContent.trim() : null, inputs, btn: btn ? { txt: btn.textContent.trim(), w: Math.round(btn.getBoundingClientRect().width), h: Math.round(btn.getBoundingClientRect().height) } : null, hasForgot: !!document.querySelector('a') });
})()" 2>/dev/null | tail -1
echo "ref login shots done"
