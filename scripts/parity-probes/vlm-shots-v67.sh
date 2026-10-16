#!/usr/bin/env bash
# vlm-shots-v67.sh — the v67 VLM pair, REFERENCE side: a fresh re-run of the
# v60-era pair (the re-run cadence's rotation — the oldest remaining standing
# pair after v64/v65/v66 covered the v57/v58/v59-era pairs): the desktop
# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's
# drill-down EXPANDED state. The v60 originals predate the v61 dashboard fix
# and the v62/v63 mobile twins; this re-run re-proves the documented classes
# live. READ-ONLY: login + passive navigation + VIEW-STATE expansion clicks
# only (the drill-down rows mutate no data — the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm67

export AGENT_BROWSER_SESSION="refvlm67"
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

# PAIR 1: the networth view at desktop 1280 — full page (the gradient
# summary card + the tablist + the type-grouped card grids).
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
# The parked-pointer lesson: park at (5,5) so no hover-revealed chrome
# (the card kebabs) is caught mid-flight.
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm67/ref-networth.png 2>/dev/null | tail -1

# PAIR 2: the dashboard's drill-down EXPANDED state at desktop 1280 —
# expand the Total Income section, then its first category (view-state
# clicks only — no data mutation), park, full-page shot.
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const sec = [...card.querySelectorAll('button')].find(b => /Total Income/i.test(b.textContent||''));
  if (!sec) return 'no section';
  sec.click();
  return 'section clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const cat = [...card.querySelectorAll('button')].find(b => b.offsetParent !== null && /\\\$/.test(b.textContent||'') && !/Total|Net Balance/i.test(b.textContent||''));
  if (!cat) return 'no category';
  cat.click();
  return 'category clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm67/ref-drilldown.png 2>/dev/null | tail -1

echo "ref shots done"
