#!/usr/bin/env bash
# v25 session: the auth submit button's FOCUS-VISIBLE ring sweep (the
# session-48 log's suggestion 2 — the submit buttons' keyboard-focus chrome
# was never swept; the inputs' focus ring was, v13 G3). Opens /login fresh,
# parks the pointer at (5,5) (the v22 parked-pointer discipline — a hover
# mid-flight would tint the read), then presses REAL Tab keys (CDP events
# move focus; synthetic dispatch does not) until the SUBMIT button is
# focused, then reads its FULL computed box-shadow (multi-layer — compared
# in full), border, outline, and class list.
# Usage: kb-auth-ring-v25.sh <login-url>
set -u
SITE="$1"

agent-browser open "$SITE" >/dev/null 2>&1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
# park the pointer (hover avoidance) + confirm the surface
agent-browser eval "(() => { const s = document.querySelector('button[type=submit]'); return JSON.stringify({ path: location.pathname, submit: s ? (s.textContent || '').trim().slice(0, 20) : null }); })()"

read_focused () {
  agent-browser eval "(() => {
    const el = document.activeElement;
    if (!el || el === document.body) return JSON.stringify({ body: true });
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return JSON.stringify({
      t: el.tagName,
      type: el.getAttribute('type'),
      label: (el.textContent || el.getAttribute('placeholder') || '').trim().slice(0, 22),
      boxShadow: cs.boxShadow,
      border: cs.borderTopWidth + ' ' + cs.borderTopColor,
      outline: (cs.outlineStyle + ' ' + cs.outlineWidth + ' ' + cs.outlineColor).slice(0, 60)
    });
  })()"
}

# Tab until the submit button is focused (max 12 steps)
for i in $(seq 1 12); do
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.12
  IS_SUBMIT=$(agent-browser eval "(() => { const el = document.activeElement; return el && el.tagName === 'BUTTON' && el.getAttribute('type') === 'submit' ? 'yes' : 'no'; })()" 2>&1 | tr -d '"')
  if [ "$IS_SUBMIT" = "yes" ]; then
    sleep 0.35   # ring/transition settle (the 200ms family + the v23 65%-opacity lesson)
    echo "--- focus on SUBMIT after Tab #$i ---"
    read_focused
    agent-browser eval "(() => { const el = document.activeElement; return JSON.stringify({ cls: (el.className || '').toString().slice(0, 260), bg: getComputedStyle(el).backgroundColor }); })()"
    break
  fi
done

echo "--- focus on FIRST input (for the pair context) ---"
agent-browser eval "(async () => { const sleep = (ms) => new Promise((r) => setTimeout(r, ms)); const inp = document.querySelector('input[type=email], input[name=email]'); if (!inp) return 'no input'; inp.focus(); await sleep(300); const cs = getComputedStyle(inp); return JSON.stringify({ boxShadow: cs.boxShadow, border: cs.borderTopWidth + ' ' + cs.borderTopColor }); })()"
