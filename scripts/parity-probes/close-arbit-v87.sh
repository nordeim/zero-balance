#!/usr/bin/env bash
# close-arbit-v87.sh — the v87 one-shot arbitration: the REFERENCE
# calculator dialog's button inventory (the arbit-v87.sh census's close
# finder returned no match on the ref side this run — the v81 census had
# the close 36x36 on BOTH sides; this probe dumps every button in the
# ref's panel: aria-label, textContent, geometry, display — read-only).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="refclose87"
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
  sleep 4
done
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
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 2

echo "=== REF panel button inventory (read-only) ==="
agent-browser eval "(async () => {
  let panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!panel) panel = [...document.querySelectorAll('div')].find(d => getComputedStyle(d).maxWidth === '768px' && d.getBoundingClientRect().width > 300);
  if (!panel) return 'no panel';
  const btns = [...panel.querySelectorAll('button')].map(b => {
    const s = getComputedStyle(b);
    const r = b.getBoundingClientRect();
    return { aria: (b.getAttribute('aria-label')||'').slice(0,30), txt: (b.textContent||'').trim().slice(0,20), w: Math.round(r.width), h: Math.round(r.height), radius: s.borderRadius, bg: s.backgroundColor, border: s.borderTopWidth + ' ' + s.borderTopColor, display: s.display };
  });
  return JSON.stringify(btns);
})()" 2>/dev/null | tail -1
echo "=== close-arbit v87 done ==="
