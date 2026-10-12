#!/usr/bin/env bash
# vlm-shots-v55.sh — capture the VLM pair surfaces at 390x844 from the
# REFERENCE (THE v55 PAIR: (1) the calculator dialog's WITH-ROW state —
# the v53 F2 surface, the session-128 standing-check suggestion; (2) the
# savings view's goal card — THE v55 F1 surface, now carrying the
# legacy-glyph swap). Reference side READ-ONLY (login + passive
# navigation + a DIALOG OPEN only — no form submits, no data mutations;
# the calculator closes via its X, the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm55

export AGENT_BROWSER_SESSION="refvlm55"
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

# PAIR 1: the calculator dialog's with-row state (the expense view's
# Rent card → Calculate — the v53 walk).
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div')].filter(d => /rounded/.test(d.className||'') && d.querySelector('h4') && /Rent|Grocery/i.test(d.textContent||'')).sort((a,b) => a.getBoundingClientRect().y - b.getBoundingClientRect().y)[0];
  if (!card) return 'no card';
  const btn = [...card.querySelectorAll('button')].find(b => /Calculate/i.test(b.textContent||''));
  if (!btn) return 'no calculate button';
  btn.click();
  return 'calculator clicked';
})()" 2>/dev/null | tail -1
sleep 3
agent-browser screenshot /tmp/vlm55/ref-calculator.png 2>/dev/null | tail -1
agent-browser eval "(async () => {
  const layer = [...document.querySelectorAll('div')].find(d => d.className && d.className.toString().includes('fixed inset-0') && (d.textContent||'').includes('Total Calculated'));
  if (!layer) return 'no layer';
  const closeBtn = [...layer.querySelectorAll('button')].filter(b => !b.textContent.trim())[0];
  if (closeBtn) { closeBtn.click(); return 'closed'; }
  return 'no close';
})()" 2>/dev/null | tail -1

# PAIR 2: the savings goal card (THE v55 F1 surface).
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 3
agent-browser screenshot /tmp/vlm55/ref-savings.png 2>/dev/null | tail -1
echo "ref shots done"
