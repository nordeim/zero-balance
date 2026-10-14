#!/usr/bin/env bash
# vlm-shots-v59.sh — the v59 VLM pair, REFERENCE side: the desktop 1280x800
# state of the CALCULATOR dialog (the session-139 v59 queue's first item —
# the panel + row surfaces; the v45/v49 pins cover the 1280/640 chrome, no
# VLM pair yet). READ-ONLY: login + hover + dialog-open only — no form
# saves, no data mutations (the v46 incident rule). The reference's OWN
# Rent card ($25.00, need, monthly) carries the same empty-state line-item
# list the clone's Rent card does (neither seed creates line items).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm59

export AGENT_BROWSER_SESSION="refvlm59"
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
# log), then click its Calculate button.
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
POS=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
  if (!card) return 'ERR';
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1)
echo "rent card center: $POS"
POS=${POS//\"/}
X=$(echo "$POS" | cut -d, -f1)
Y=$(echo "$POS" | cut -d, -f2)
agent-browser mouse move "$X" "$Y" >/dev/null 2>&1
sleep 1
CALC=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate$/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1)
echo "calculate button center: $CALC"
CALC=${CALC//\"/}
CX=$(echo "$CALC" | cut -d, -f1)
CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser screenshot /tmp/vlm59/ref-calculator.png 2>/dev/null | tail -1
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
  return JSON.stringify({ title: t.split('\n')[0], hasEmpty: /No line items yet/i.test(t), hasTotal: /Total Calculated/.test(t) });
})()" 2>/dev/null | tail -1

echo "ref v59 calculator shots done"
