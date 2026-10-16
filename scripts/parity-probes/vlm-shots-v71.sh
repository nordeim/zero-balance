#!/usr/bin/env bash
# vlm-shots-v71.sh — the v71 NEW-pair program, REFERENCE side: the ITEMS
# views' MOBILE 390x844 full-page twins — (1) /INCOME, (2) /EXPENSES and
# (3) /SAVINGS — the below-the-fold 390 surfaces never individually shot
# (the v62/v63 precedent extending the standing-pair matrix to the
# remaining views; the desktop items pairs were covered by v57/v64/v70).
# READ-ONLY: login + passive navigation only (the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm71

export AGENT_BROWSER_SESSION="refvlm71"
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

# (1) The income view at mobile 390 — full page. The parked-pointer
# lesson: park at (5,5) so no hover-revealed chrome is caught mid-flight.
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm71/ref-income-mobile.png 2>/dev/null | tail -1

# (2) The expenses view at mobile 390 — full page.
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm71/ref-expenses-mobile.png 2>/dev/null | tail -1

# (3) The savings view at mobile 390 — full page.
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm71/ref-savings-mobile.png 2>/dev/null | tail -1

echo "ref mobile shots done (income + expenses + savings)"
