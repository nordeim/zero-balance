#!/usr/bin/env bash
# v36: Surface C — the full Tab-order census of /income via REAL Tab presses.
# Usage (inside the right session env): bash tabwalk-v36.sh <session> [n]
# Reads document.activeElement after each real Tab.
set -u
SESSION="${1:?session}"
N="${2:-16}"
PB=/home/z/my-project/zero-balance/scripts/parity-probes

# park the pointer at the corner (the parked-pointer discipline) + blur
agent-browser --session "$SESSION" eval "(() => { document.activeElement && document.activeElement.blur(); window.scrollTo(0, 0); return 'ok'; })()" >/dev/null 2>&1
sleep 0.5

for i in $(seq 1 "$N"); do
  agent-browser --session "$SESSION" press Tab >/dev/null 2>&1
  sleep 0.45
  agent-browser --session "$SESSION" eval "(() => {
    const el = document.activeElement;
    if (!el || el === document.body) { window.__tabstop = null; }
    else {
      const r = el.getBoundingClientRect();
      const c = getComputedStyle(el);
      window.__tabstop = {
        tag: el.tagName.toLowerCase(),
        role: el.getAttribute('role'),
        name: (el.getAttribute('aria-label') || (el.textContent || '').trim().replace(/\s+/g, ' ')).slice(0, 26),
        rect: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
        opacity: c.opacity
      };
    }
    return JSON.stringify(window.__tabstop);
  })()" 2>/dev/null | tail -1
done
