#!/usr/bin/env bash
# calc-census-ref-v59.sh — the v59 DOM arbitration census, REFERENCE side:
# the calculator dialog at desktop 1280x800. Arbitrates the two VLM flags:
# (1) the total card's conditional "Will update category total" span —
#     the reference's own Rent is \$25.00 and its single line item sums to
#     \$25.00, so lineTotal === parentAmount and the span is HIDDEN (the
#     conditional itself is the pinned contract — calculator.spec.ts
#     "0 !== 1850 → shown");
# (2) the row's hover-gated action pair — the reference's shot caught the
#     actions mid-hover (the pointer rested inside the dialog); at rest
#     BOTH sites gate the pair at opacity 0 (the v6 G9/G10 + v45 F2a
#     pins). The census measures both axes read-only.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="refcalc59"
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
POS=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
  if (!card) return 'ERR';
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
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
# park the pointer FAR from the dialog before the census (the rest state)
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 2

echo "=== THE FULL CALCULATOR CENSUS AT 1280 (reference, rest state) ==="
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('div')].find(d => getComputedStyle(d).maxWidth === '768px' && d.getBoundingClientRect().width > 300);
  if (!panel) return 'no panel';
  const cs = getComputedStyle(panel);
  const r = panel.getBoundingClientRect();
  const totalCard = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).backgroundColor === 'rgb(255, 247, 245)');
  const tcs = totalCard ? getComputedStyle(totalCard) : null;
  const tr = totalCard ? totalCard.getBoundingClientRect() : null;
  const closeBtn = [...panel.querySelectorAll('button')].find(b => (b.getAttribute('aria-label')||'') === 'Close' || !(b.textContent||'').trim());
  const hdr = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).borderBottomWidth !== '0px');
  const h4 = [...dlg0(panel).querySelectorAll('h4,h3,div')].find(e => (e.textContent||'').trim() === 'Contents Insurance' && e.children.length === 0);
  let row = h4;
  while (row && row !== panel) { const c = getComputedStyle(row); if (parseFloat(c.borderTopWidth) > 0 && c.backgroundColor === 'rgb(255, 255, 255)') break; row = row.parentElement; }
  const rowCs = row ? getComputedStyle(row) : null;
  const rowR = row ? row.getBoundingClientRect() : null;
  let actions = null;
  if (row) { for (const d of row.querySelectorAll('div')) { const c = getComputedStyle(d); if (c.display === 'flex' && d.querySelectorAll('button').length >= 1 && (c.opacity === '0' || c.opacity === '1') && c.transitionProperty.includes('opacity')) { actions = d; break; } } }
  return JSON.stringify({
    panel: { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), radius: cs.borderRadius, maxW: cs.maxWidth, maxH: cs.maxHeight, bg: cs.backgroundColor, overflow: cs.overflow, shadow: cs.boxShadow.slice(0,130) },
    totalCard: tcs ? { w: Math.round(tr.width), h: Math.round(tr.height), bg: tcs.backgroundColor, radius: tcs.borderRadius, pad: tcs.padding, border: tcs.border } : null,
    closeBtn: closeBtn ? { w: Math.round(closeBtn.getBoundingClientRect().width), h: Math.round(closeBtn.getBoundingClientRect().height) } : null,
    hdrBorder: hdr ? getComputedStyle(hdr).borderBottom : null,
    row: rowCs ? { w: Math.round(rowR.width), pad: rowCs.padding, radius: rowCs.borderRadius, border: rowCs.borderTop, bg: rowCs.backgroundColor, transition: rowCs.transitionProperty + ' ' + rowCs.transitionDuration } : null,
    actionsAtRest: actions ? { opacity: getComputedStyle(actions).opacity, btnCount: actions.querySelectorAll('button').length, btnW: Math.round(actions.querySelector('button').getBoundingClientRect().width) } : 'not found'
  });
  function dlg0(p) { return p; }
})()" 2>/dev/null | tail -1

echo "=== ref calc census v59 done ==="
