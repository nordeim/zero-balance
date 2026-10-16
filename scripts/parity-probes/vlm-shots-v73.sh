#!/usr/bin/env bash
# vlm-shots-v73.sh — the v73 NEW-pair program, REFERENCE side: the LAST
# never-shot mobile 390x844 twins —
#   (1) the LOGIN page at 390 (the simplest never-shot pair — the fresh
#       logged-out surface, no auth needed; the v59/v66 login pairs were
#       desktop 1280 only),
#   (2) the CALCULATOR dialog at 390 (the dialog-state surface — the
#       v66 desktop pair's mobile twin; the hover-reveal + Calculate
#       click at the mobile viewport, the reference's OWN Rent card
#       $25.00 with its single Contents Insurance line item).
# READ-ONLY: login + passive navigation + hover + dialog-open only — no
# form saves, no data mutations (the v46 incident rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
mkdir -p /tmp/vlm73

export AGENT_BROWSER_SESSION="refvlm73"

# (1) The LOGIN page at mobile 390 — the fresh logged-out session (the
# shot must precede any login submit).
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 2
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div')].find(d => d.querySelector && d.querySelector('input[type=email]'));
  return JSON.stringify({
    hasLoginCard: !!card,
    docSW: document.documentElement.scrollWidth,
    vw: window.innerWidth,
    title: document.title
  });
})()" 2>/dev/null | tail -1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot /tmp/vlm73/ref-login-mobile.png 2>/dev/null | tail -1

# (2) The CALCULATOR dialog at mobile 390 — login, then the v66 flow
# (hover the Rent card with a REAL mouse move — synthetic mouseenter
# never engages :hover — then click its Calculate button).
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
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
# the mobile fold: the Rent card sits BELOW the fold in the 1-col grid at
# 390 (card center y > 844) — scroll it into view FIRST, then the hover.
agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
  if (!card) return 'ERR';
  card.scrollIntoView({ block: 'center' });
  return 'scrolled';
})()" 2>/dev/null | tail -1
sleep 1
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
# park the pointer after the state swap (the parked-pointer lesson —
# the v66 flag: the row actions rest at opacity 0 and a resting pointer
# inside the dialog reveals them mid-shot)
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot /tmp/vlm73/ref-calculator-mobile.png 2>/dev/null | tail -1

# the dialog census (read-only): confirm it opened + its line-item state
# + its mobile geometry. The reference's calculator dialog is a PLAIN
# fixed div — no role=dialog (the documented reference class) — so the
# census finds it by geometry.
agent-browser eval "(async () => {
  const fixed = [...document.querySelectorAll('div')].filter(d => { const s = getComputedStyle(d); return s.position === 'fixed' && d.getBoundingClientRect().width > 300 && d.getBoundingClientRect().height > 200; });
  const dlg = fixed[fixed.length-1];
  if (!dlg) return 'no dialog';
  const t = dlg.innerText;
  const r = dlg.getBoundingClientRect();
  return JSON.stringify({
    title: t.split('\n')[0],
    hasEmpty: /No line items yet/i.test(t),
    hasInsurance: /Contents Insurance/i.test(t),
    hasTotal: /Total Calculated/.test(t),
    rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) }
  });
})()" 2>/dev/null | tail -1

echo "ref v73 shots done (login-mobile + calculator-mobile)"
