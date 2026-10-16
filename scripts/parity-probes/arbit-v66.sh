#!/usr/bin/env bash
# arbit-v66.sh — the v66 DOM arbitration census, REFERENCE side: the
# calculator dialog at desktop 1280x800 (the fresh v59-era pair re-run's
# arbitration — the VLM flagged the row's hover actions + the total card's
# "Will update category total" span). The census adds the ROW-HEIGHT family
# never measured before v66: the row h, the name h4 block, the badge pill
# row + its pills, the amount P, and the totalCard h (the v59 census pinned
# the panel/totalCard chrome + the row's width/pad; the v45 F2a pin the
# row's class strings — never the computed HEIGHTS). READ-ONLY.
# NOTE the fresh-login boot lesson: the reference's first /expenses fetch
# can exceed the wait window — the Rent card finder RETRIES before the
# hover, and the session is re-used warm on the re-run.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="refcalc66"
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

# the Rent card finder RETRIES — the fresh-login first fetch can be slow
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
# park the pointer FAR from the dialog before the census (the rest state)
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 2

echo "=== THE CALCULATOR DIALOG CENSUS + THE HEIGHT FAMILY AT 1280 (reference, rest state) ==="
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('div')].find(d => getComputedStyle(d).maxWidth === '768px' && d.getBoundingClientRect().width > 300);
  if (!panel) return 'no panel';
  const cs = getComputedStyle(panel);
  const r = panel.getBoundingClientRect();
  const totalCard = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).backgroundColor === 'rgb(255, 247, 245)');
  const tcs = totalCard ? getComputedStyle(totalCard) : null;
  const tr = totalCard ? totalCard.getBoundingClientRect() : null;
  const hasSpan = !!(totalCard && (totalCard.innerText||'').includes('Will update category total'));
  // the row: walk UP from the line-item name leaf to the bordered white card
  const h4 = [...panel.querySelectorAll('h4,h3,div,span')].filter(e => (e.textContent||'').trim() === 'Contents Insurance' && e.children.length === 0)[0];
  if (!h4) return 'no h4';
  const h4cs = getComputedStyle(h4);
  let row = h4;
  while (row && row !== panel) { const c = getComputedStyle(row); if (parseFloat(c.borderTopWidth) > 0 && c.backgroundColor === 'rgb(255, 255, 255)') break; row = row.parentElement; }
  if (!row || row === panel) return 'no row';
  const rowCs = getComputedStyle(row);
  const rowR = row.getBoundingClientRect();
  // the badge pill row: the pill spans' shared parent (the pills carry radius 9999px)
  const pills = [...row.querySelectorAll('span')].filter(s => parseFloat(getComputedStyle(s).borderRadius) > 100 && s.getBoundingClientRect().width > 10);
  const pillRow = pills.length ? pills[0].parentElement : null;
  const prcs = pillRow ? getComputedStyle(pillRow) : null;
  const prR = pillRow ? pillRow.getBoundingClientRect() : null;
  const p1 = pills[0] ? getComputedStyle(pills[0]) : null;
  const p1R = pills[0] ? pills[0].getBoundingClientRect() : null;
  // the amount P: the row's largest-font text leaf (the text-xl orange amount)
  const amountP = [...row.querySelectorAll('p,span,div')].filter(e => e.children.length === 0 && /^\\\$/.test((e.textContent||'').trim())).sort((a,b) => parseFloat(getComputedStyle(b).fontSize) - parseFloat(getComputedStyle(a).fontSize))[0];
  const apcs = amountP ? getComputedStyle(amountP) : null;
  const apR = amountP ? amountP.getBoundingClientRect() : null;
  // the hover-gated action pair
  let actions = null;
  for (const d of row.querySelectorAll('div')) { const c = getComputedStyle(d); if (c.display === 'flex' && d.querySelectorAll('button').length >= 1 && (c.opacity === '0' || c.opacity === '1') && c.transitionProperty.includes('opacity')) { actions = d; break; } }
  return JSON.stringify({
    panel: { w: Math.round(r.width), radius: cs.borderRadius, maxW: cs.maxWidth, shadow: cs.boxShadow.slice(0,130) },
    totalCard: tcs ? { w: Math.round(tr.width), h: Math.round(tr.height), pad: tcs.padding, border: tcs.border, hasWillUpdateSpan: hasSpan } : null,
    row: { w: Math.round(rowR.width), h: Math.round(rowR.height), pad: rowCs.padding, radius: rowCs.borderRadius, borderTop: rowCs.borderTop, bg: rowCs.backgroundColor },
    nameH4: { fs: h4cs.fontSize, fw: h4cs.fontWeight, color: h4cs.color, h: Math.round(h4.getBoundingClientRect().height), mb: h4cs.marginBottom },
    pillRow: prcs ? { display: prcs.display, gap: prcs.gap, fs: prcs.fontSize, h: Math.round(prR.height) } : 'not found',
    pill1: p1 ? { h: Math.round(p1R.height), w: Math.round(p1R.width), pad: p1.padding, radius: p1.borderRadius, fs: p1.fontSize, fw: p1.fontWeight } : 'not found',
    amountP: apcs ? { fs: apcs.fontSize, fw: apcs.fontWeight, color: apcs.color, h: Math.round(apR.height) } : 'not found',
    actionsAtRest: actions ? { opacity: getComputedStyle(actions).opacity, btnCount: actions.querySelectorAll('button').length } : 'not found'
  });
})()" 2>/dev/null | tail -1

echo "=== ref arbit v66 done ==="
