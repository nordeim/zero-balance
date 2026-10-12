#!/usr/bin/env bash
# vlm-arbit-v55.sh — DOM-verify the two VLM flags that are NOT
# documented data classes: (1) the calculator dialog's X-close chrome
# (the VLM saw a "square-outlined X" on the clone vs a plain X on the
# reference); (2) the savings cards' amount font size (the VLM read
# the clone's $450 as "smaller font" — the v51 pin asserted 24px/700).
# READ-ONLY.
set -u
BASE="${1:-https://zero-balance-4885a8f3.base44.app}"
SESS="${2:-refarb55}"
SIDE="${3:-ref}"
EMAIL="${4:-sepnetflix2023@outlook.com}"
PASSWORD='${PASSWD:-x}'

export AGENT_BROWSER_SESSION="$SESS"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 4
if [ "$SIDE" = "ref" ]; then
  PWVAL='\$Abcd1234'
else
  PWVAL='Demo1234!'
fi
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, '$EMAIL');
  set(pw, '$PWVAL');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1

echo "=== $SIDE: the calculator dialog's X-close chrome ==="
agent-browser open "$BASE/expenses" >/dev/null 2>&1
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
agent-browser eval "(async () => {
  // The dialog's X-close: the icon-less button in the dialog layer (the
  // v53 walk — the FIRST text-less button inside the dialog).
  const layer = [...document.querySelectorAll('div')].filter(d =>
    d.className && d.className.toString().includes('fixed inset-0') &&
    (d.textContent||'').includes('Total Calculated'))[0];
  if (!layer) return 'no layer';
  const closeBtn = [...layer.querySelectorAll('button')].filter(b => !b.textContent.trim())[0];
  if (!closeBtn) return 'no close';
  const cs = getComputedStyle(closeBtn);
  const r = closeBtn.getBoundingClientRect();
  const svg = closeBtn.querySelector('svg');
  return JSON.stringify({
    w: Math.round(r.width), h: Math.round(r.height),
    bg: cs.backgroundColor, border: cs.borderTopWidth + ' ' + cs.borderTopColor,
    radius: cs.borderRadius, pad: cs.padding,
    svgCls: svg ? (svg.getAttribute('class')||'').slice(0,40) : null,
    svgW: svg ? Math.round(svg.getBoundingClientRect().width) : null
  });
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => {
  const layer = [...document.querySelectorAll('div')].filter(d =>
    d.className && d.className.toString().includes('fixed inset-0') &&
    (d.textContent||'').includes('Total Calculated'))[0];
  if (!layer) return 'no layer';
  const closeBtn = [...layer.querySelectorAll('button')].filter(b => !b.textContent.trim())[0];
  if (closeBtn) { closeBtn.click(); return 'closed'; }
  return 'no close';
})()" 2>/dev/null | tail -1

echo ""
echo "=== $SIDE: the savings cards' amount typography ==="
agent-browser open "$BASE/savings" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const cards = [...document.querySelectorAll('h4')].map((h4) => {
    let card = h4.closest('div.rounded-xl') || h4.parentElement;
    for (let i = 0; card && i < 5; i++) {
      const pcs = getComputedStyle(card.parentElement);
      if (pcs.display === 'grid') break;
      card = card.parentElement;
    }
    return card;
  }).filter(Boolean);
  return JSON.stringify(cards.map((card) => {
    const amount = [...card.querySelectorAll('p')].find((p) =>
      /^[\\\$]?[\\d,]/.test((p.textContent || '').trim()) &&
      parseFloat(getComputedStyle(p).fontSize) >= 20);
    return {
      h4: (card.querySelector('h4')?.textContent || '').trim(),
      amount: amount ? {
        text: amount.textContent.trim(),
        fs: getComputedStyle(amount).fontSize,
        fw: getComputedStyle(amount).fontWeight
      } : null
    };
  }));
})()" 2>/dev/null | tail -1
echo ""
echo "=== $SIDE arbitration done ==="
