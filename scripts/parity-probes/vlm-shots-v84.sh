#!/usr/bin/env bash
# vlm-shots-v84.sh — the v84 VLM pair RE-RUN, REFERENCE side: BOTH mobile
# 390x844 full-page twins — (1) the /NETWORTH view (the v63-era pair's
# surface, last re-shot by the v78 re-run: "the re-run cadence rotates to
# the mobile 390 twins — both covered in one two-pair iteration, the
# v62/v67 precedent") and (2) the DASHBOARD (the v62-era mobile twin's
# surface). The v84 queue (the v83 plan's own suggestion, now confirmed
# by the rotation ledger: last re-shot v78 = the oldest remaining [v78 <
# v79 items < v80-v83]). READ-ONLY: login + passive navigation only
# (the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm84

export AGENT_BROWSER_SESSION="refvlm84"
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

# (1) The networth view at mobile 390 — full page. The parked-pointer
# lesson: park at (5,5) so no hover-revealed chrome is caught mid-flight.
# NOTE: the reference's own /networth page overflows at 390 (docSW 464,
# its documented R-bug-4) — the full-page shot intentionally captures that
# overflow for the pair (the clone's page fits 390, the superset fix).
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm84/ref-networth-mobile.png 2>/dev/null | tail -1

# (2) The dashboard at mobile 390 — full page (the v62 mobile twin's
# surface; the v61 STRETCH fix + the v62 subtitle census apply).
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm84/ref-dashboard-mobile.png 2>/dev/null | tail -1

echo "ref mobile shots done (networth + dashboard)"
