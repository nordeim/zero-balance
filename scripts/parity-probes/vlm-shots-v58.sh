#!/usr/bin/env bash
# vlm-shots-v58.sh — the v58 VLM pair, REFERENCE side: the desktop 1280x800
# state of the SAVINGS view (the items family's remaining view — the v57
# pair covered income + expenses; the savings goal-card's 1280 state is
# unpinned at the pair viewport, its internals pinned at 390 only [v54 F1]).
# READ-ONLY: login + passive navigation only — no clicks, no form submits,
# no data mutations (the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm58

export AGENT_BROWSER_SESSION="refvlm58"
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

# PAIR: the savings view at desktop 1280 — the goal-card grid
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser screenshot /tmp/vlm58/ref-savings.png 2>/dev/null | tail -1

echo "ref shots done"
