#!/usr/bin/env bash
# vlm-shots-v74.sh — the v74 standing-pair re-run, REFERENCE side: the
# SAVINGS view at desktop 1280x800, FULL-PAGE — the fresh sweep of the
# re-run cycle's OLDEST candidate (the v58-era savings pair, last re-shot
# v65 — the only pre-v70 pair not re-run since; the session-177 v74 queue's
# first item). READ-ONLY: login + passive navigation only (the v46 rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm74

export AGENT_BROWSER_SESSION="refvlm74"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1

# PAIR: the savings view at desktop 1280 — the goal-card grid, FULL-PAGE.
# The parked-pointer lesson (v22): park at (5,5) so no hover-revealed
# chrome (the card kebabs, the row actions) is caught mid-flight.
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm74/ref-savings-full.png 2>/dev/null | tail -1

echo "ref savings-pair shots done"
