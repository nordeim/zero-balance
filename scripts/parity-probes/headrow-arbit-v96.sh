#!/usr/bin/env bash
# headrow-arbit-v96.sh — the ONE-SHOT census for the v96 pin's own
# axes, REFERENCE half (the v87..v95 supplemental precedent, BUILT
# TWO-HALF from the start): the networth summary card's HEAD-ROW
# typography + the FIGURE-FIT contract at mobile 390 — the label's
# family {fs/fw/color/mb} + the figure's family {fs/fw/color/lh} (the
# fw/color never pinned at 390 — the 640/1280 tiers hold them) + the
# figure's in-bounds fit (the v96 figclip arbitration's own axes).
# Read-only (login + passive navigation — the v46 rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const out = { view: 'headrow-390-v96' };
  const cards = [...document.querySelectorAll('main div, div')].filter(d => {
    const s = getComputedStyle(d);
    return d.getBoundingClientRect().height > 100 && d.getBoundingClientRect().width > 200
      && s.backgroundImage && s.backgroundImage.includes('linear-gradient');
  });
  const card = cards.find(c => c.getBoundingClientRect().width < 500) || cards[0];
  if (!card) return JSON.stringify({ err: 'no summary card' });
  const cr = card.getBoundingClientRect();
  const cs = getComputedStyle(card);
  const label = [...card.querySelectorAll('p, span')].find(
    (e) => (e.textContent || '').trim() === 'Total Net Worth' && e.children.length === 0
  );
  let fig = null; let figFs = 0;
  for (const el of card.querySelectorAll('h1,h2,h3,p,span,div')) {
    const s = getComputedStyle(el);
    const fs = parseFloat(s.fontSize);
    const t = (el.textContent || '').trim();
    if (!t || t.length > 40) continue;
    if (/^[-]?\s*[$]/.test(t) && fs > figFs) { fig = el; figFs = fs; }
  }
  if (!fig || !label) return JSON.stringify({ err: 'no head row', hasLabel: !!label, hasFig: !!fig });
  const fr = fig.getBoundingClientRect();
  const fcs = getComputedStyle(fig);
  const lr = label.getBoundingClientRect();
  const lcs = getComputedStyle(label);
  const range = document.createRange();
  range.selectNodeContents(fig);
  const tr = range.getBoundingClientRect();
  const padL = parseFloat(cs.paddingLeft); const padR = parseFloat(cs.paddingRight);
  const contentL = cr.left + padL; const contentR = cr.right - padR;
  out.card = { x: Math.round(cr.x), w: Math.round(cr.width), padL: padL, padR: padR, contentL: Math.round(contentL), contentR: Math.round(contentR) };
  out.label = { fs: lcs.fontSize, fw: lcs.fontWeight, color: lcs.color, mb: lcs.marginBottom, h: Math.round(lr.height) };
  out.figure = {
    text: (fig.textContent || '').trim(),
    fs: fcs.fontSize, fw: fcs.fontWeight, color: fcs.color, lh: fcs.lineHeight,
    el: { x: Math.round(fr.x), w: Math.round(fr.width), h: Math.round(fr.height) },
    textRect: { x: Math.round(tr.x), w: Math.round(tr.width) }
  };
  out.fit = {
    textLeftOverhang: Math.round(contentL - tr.x),
    textRightMargin: Math.round(contentR - tr.right),
    figureScrolls: fig.scrollWidth > fig.clientWidth,
    docSW: document.documentElement.scrollWidth
  };
  return JSON.stringify(out);
})()"

export AGENT_BROWSER_SESSION="refhr96"
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
  echo "ref login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 5
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== PART H: REF head-row + figure-fit census at 390 ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== ref headrow v96 half done ==="
