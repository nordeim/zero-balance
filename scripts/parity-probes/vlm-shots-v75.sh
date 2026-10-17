#!/usr/bin/env bash
# vlm-shots-v75.sh — the v75 re-run pair, REFERENCE side: a fresh standing
# sweep of the CALCULATOR dialog at desktop 1280x800 — the re-run cadence's
# next-oldest candidate (the v59-era calculator + login pair, last re-shot
# v66 — the v64/v65/v70/v74 passes covered the v57/v58 pairs; the session-179
# v75 queue's first item). READ-ONLY: login + hover + dialog-open only — no
# form saves, no data mutations (the v46 incident rule). The reference's OWN
# Rent card ($25.00, need, monthly) carries the single "Contents Insurance"
# $25.00 monthly-active line item (the v45 measurement note) — the clone-side
# twin script pairs against it by adding the SAME line item through the real
# UI then fully restoring.
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm75

export AGENT_BROWSER_SESSION="refvlm75"
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

# PAIR: the calculator dialog at desktop 1280 — hover the Rent card with a
# REAL mouse move (synthetic mouseenter never engages :hover — the trap
# log), then click its Calculate button. The Rent-card finder RETRIES —
# the fresh-login first /expenses fetch can exceed the wait window (the
# v66 lesson: a transient "0 items" state).
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
POS=""
for attempt in 1 2 3 4 5; do
  POS=$(agent-browser eval "(async () => {
    const main = document.querySelector('main')||document.body;
    const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
    if (!card) return 'ERR';
    const r = card.getBoundingClientRect();
    return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
  })()" 2>/dev/null | tail -1 | tr -d '"')
  if [ "$POS" != "ERR" ] && [ -n "$POS" ]; then break; fi
  echo "rent card not ready (attempt $attempt), waiting..."
  sleep 4
done
echo "rent card center: $POS"
X=$(echo "$POS" | cut -d, -f1); Y=$(echo "$POS" | cut -d, -f2)
agent-browser mouse move "$X" "$Y" >/dev/null 2>&1
sleep 1
CALC=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate\$/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
echo "calculate button center: $CALC"
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser screenshot /tmp/vlm75/ref-calculator.png 2>/dev/null | tail -1
# park the pointer after the state swap (the parked-pointer lesson)
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
# the dialog census (read-only): confirm it opened + its line-item state.
# The reference's calculator dialog is a PLAIN fixed div — no role=dialog
# (the documented reference class) — so the census finds it by geometry.
agent-browser eval "(async () => {
  const fixed = [...document.querySelectorAll('div')].filter(d => { const s = getComputedStyle(d); return s.position === 'fixed' && d.getBoundingClientRect().width > 400 && d.getBoundingClientRect().height > 300; });
  const dlg = fixed[fixed.length-1];
  if (!dlg) return 'no dialog';
  const t = dlg.innerText;
  return JSON.stringify({ title: t.split('\n')[0], hasInsurance: /Contents Insurance/.test(t), hasTotal: /Total Calculated/.test(t) });
})()" 2>/dev/null | tail -1

echo "ref v75 calculator shots done"
