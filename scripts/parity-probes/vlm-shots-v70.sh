#!/usr/bin/env bash
# vlm-shots-v70.sh — the v70 standing-pair re-run, REFERENCE side: the
# ITEMS view (income + expenses) at desktop 1280x800, FULL-PAGE — the fresh
# re-run of the OLDEST re-run candidate (the v57-era items pair, last
# re-shot by v64 itself — every other desktop pair re-ran later [savings
# v65, calculator+login v66, networth+drill-down v67, dashboard v68] and
# BOTH mobile twins re-ran at v69; the session-167/168 v70 queue's first
# item: the re-run cadence returns to the DESKTOP pairs).
# READ-ONLY: login + passive navigation only (the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm70

export AGENT_BROWSER_SESSION="refvlm70"
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

# PAIR 1: the income view at desktop 1280 — the search filter card + grid.
# The parked-pointer lesson (v22): park at (5,5) so no hover-revealed
# chrome (the card kebabs, the row actions) is caught mid-flight.
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm70/ref-income-full.png 2>/dev/null | tail -1

# PAIR 2: the expenses view at desktop 1280 — the grid + payment filter.
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm70/ref-expenses-full.png 2>/dev/null | tail -1

echo "ref items-pair shots done"
