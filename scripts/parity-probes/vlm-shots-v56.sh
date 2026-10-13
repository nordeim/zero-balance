#!/usr/bin/env bash
# vlm-shots-v56.sh — the v56 VLM pair, REFERENCE side: the desktop 1280x800
# state of (1) the DASHBOARD (the v55 F1 surface post-swap: the stat rows
# carrying the legacy piggy/trending glyphs + the donut + its legend), and
# (2) the NETWORTH view (the trending-up hero/summary swap surfaces).
# The session-131 v56 queue's own standing-check suggestion. READ-ONLY:
# login + passive navigation only — no clicks, no form submits, no data
# mutations (the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm56

export AGENT_BROWSER_SESSION="refvlm56"
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

# PAIR 1: the dashboard at desktop 1280 — the stat rows + donut + legend
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser screenshot /tmp/vlm56/ref-dashboard.png 2>/dev/null | tail -1

# PAIR 2: the networth view at desktop 1280 — the trending hero/summary
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser screenshot /tmp/vlm56/ref-networth.png 2>/dev/null | tail -1

echo "ref shots done"
