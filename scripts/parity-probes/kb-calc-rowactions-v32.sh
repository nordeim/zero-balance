#!/usr/bin/env bash
# v32: the calculator row actions' REAL-Tab walk + the focused-chrome read
# (the G1 evidence + the post-fix verification). Prereq: the calculator open
# on an expense with one line item; pointer parked at (5,5); the X focused.
# The focused read MUST settle ≥350ms — transition-colors' v4 property list
# includes outline-color, so an immediate read catches the transparent
# settle mid-flight (oklab-interpolated; the v23 G1 lesson, v32 rediscovery).
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/kb-calc-rowactions-v32.sh
set -u
S="${1:-clone32}"
agent-browser --session "$S" mouse move 5 5 >/dev/null 2>&1
sleep 0.4
agent-browser --session "$S" eval "(() => { const calc = [...document.querySelectorAll('[role=dialog]')].find(d => /Calculator/.test(d.textContent)); calc.querySelectorAll('button')[0].focus(); return 'X focused'; })()" 2>/dev/null
for i in 1 2 3 4; do
  agent-browser --session "$S" press Tab >/dev/null 2>&1
  sleep 0.5
  agent-browser --session "$S" eval "(() => {
    const ae = document.activeElement;
    const cs = getComputedStyle(ae);
    return JSON.stringify({ stop: ae.tagName + ':' + (ae.getAttribute('aria-label') || (ae.textContent||'').trim().slice(0,16) || 'anon'),
      contOp: getComputedStyle(ae.parentElement).opacity,
      outline: cs.outlineStyle + ' ' + cs.outlineWidth + ' ' + cs.outlineColor,
      shadow: cs.boxShadow.slice(0, 160) });
  })()" 2>/dev/null
done
