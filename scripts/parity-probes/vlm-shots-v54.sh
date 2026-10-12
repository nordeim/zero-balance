#!/usr/bin/env bash
# vlm-shots-v54.sh — capture the VLM pair surfaces at 390x844 from both
# sites (THE v54 PAIR: (1) the /networth tablist — the v53 F1 surface,
# the session-125 standing-check suggestion; (2) the savings view's
# goal card — THE v54 F1 surface). Reference side READ-ONLY (login +
# passive navigation only — no form submits, no data mutations).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm54

# --- reference side ---
export AGENT_BROWSER_SESSION="refvlm54"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 3
agent-browser screenshot /tmp/vlm54/ref-networth.png 2>/dev/null | tail -1
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 3
agent-browser screenshot /tmp/vlm54/ref-savings.png 2>/dev/null | tail -1
echo "ref shots done"
