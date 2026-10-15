#!/usr/bin/env bash
# vlm-shots-v63.sh — the v63 VLM pair, REFERENCE side: the /NETWORTH view
# at mobile 390x844, FULL-PAGE — the standing-pair program's LAST un-paired
# viewport × view combination (v56 PAIR 2 covered the desktop networth;
# v62's mobile twin covered the dashboard; this closes the matrix).
# READ-ONLY: login + passive navigation only (the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm63

export AGENT_BROWSER_SESSION="refvlm63"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1

# The networth view at mobile 390 — full page. The parked-pointer lesson:
# park at (5,5) so no hover-revealed chrome is caught mid-flight. NOTE:
# the reference's own /networth page overflows at 390 (docSW 464, its
# documented R-bug-4) — the full-page shot intentionally captures that
# overflow for the pair (the clone's page fits 390, the superset fix).
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm63/ref-networth-mobile.png 2>/dev/null | tail -1

echo "ref networth mobile shot done"
