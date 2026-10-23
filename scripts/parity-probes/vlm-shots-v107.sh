#!/usr/bin/env bash
# vlm-shots-v107.sh — the v107 VLM pair, REFERENCE side: a fresh re-run of the
# v101-era pair (the re-run cadence's rotation — the oldest remaining standing
# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v101 — now
# the oldest remaining [v101 < v102 < v103 < v104 < v105 < v106]; the pair's SEVENTH
# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107] — the THIRTIETH consecutive
# queue/ledger agreement). Both v61 target surfaces live below the fold on
# the same view: (1) the BUDGET GUIDELINES card — the tinted, bordered
# 50/30/20 rows [the v51 F4 mobile census's desktop twin never VLM-paired
# before v61] — and (2) the QUICK-ACTION card row — the three Add Income /
# Add Savings / Add Expense card buttons [the v45 F3 hover-shadow pin covers
# the hover state only; the resting chrome at the 1280 pair viewport
# unpaired before v61]. The v107 re-run re-proves the v61-era surfaces after
# v101-v106 (the mobile twins, the height pins, the stat-card divider pin).
# READ-ONLY: login + passive navigation only (no clicks beyond navigation —
# the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm107

export AGENT_BROWSER_SESSION="refvlm107"
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

# The dashboard at desktop 1280 — full page (the guidelines card + the
# quick-action row sit below the 800 fold). The parked-pointer lesson:
# park at (5,5) so no hover-revealed chrome is caught mid-flight.
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm107/ref-dashboard.png 2>/dev/null | tail -1

echo "ref shots done"
