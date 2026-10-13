#!/usr/bin/env bash
# vlm-shots-v57.sh — the v57 VLM pair, REFERENCE side: the desktop 1280x800
# state of (1) the INCOME view (the v55 search-input glyph swap surface + the
# item-card grid at 1280) and (2) the EXPENSES view (the same grid family +
# the payment-method filter row). The session-134 v57 queue's own
# standing-check suggestion — the v56 pair covered the dashboard + networth.
# READ-ONLY: login + passive navigation only — no clicks, no form submits,
# no data mutations (the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm57

export AGENT_BROWSER_SESSION="refvlm57"
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

# PAIR 1: the income view at desktop 1280 — the search filter card + grid
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser screenshot /tmp/vlm57/ref-income.png 2>/dev/null | tail -1

# PAIR 2: the expenses view at desktop 1280 — the grid + payment filter
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser screenshot /tmp/vlm57/ref-expenses.png 2>/dev/null | tail -1

echo "ref shots done"
