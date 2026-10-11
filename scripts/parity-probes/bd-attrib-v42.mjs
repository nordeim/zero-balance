// v42: attribute the +13px INSIDE the NetZeroBreakdownCard at 640x960
// (ref h=324 vs clone h=337). Measures the card's own box (pad/radius),
// the h3 header, and every band of the space-y-3 stack (the three
// BreakdownSection rows, the Dividers, the Net Balance footer) so the
// drift attributes to an exact element.
(() => {
  const leaf = (txt) =>
    [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(
      (e) => (e.textContent || '').trim() === txt && e.children.length === 0,
    );
  const bdH = leaf('Net Zero Breakdown');
  const card = bdH ? bdH.closest('div.rounded-2xl, [class*="rounded-2xl"]') : null;
  if (!card) return JSON.stringify({ found: false });
  const cs = getComputedStyle(card);
  const cr = card.getBoundingClientRect();
  const h3r = bdH.getBoundingClientRect();
  const h3cs = getComputedStyle(bdH);
  // The stack: the h3's next sibling (the space-y-3 div).
  const stack = bdH.parentElement.children[1] || null;
  const stackCs = stack ? getComputedStyle(stack) : null;
  // Every child of the stack with its height + margins.
  const bands = stack
    ? [...stack.children].map((c) => {
        const r = c.getBoundingClientRect();
        const ccs = getComputedStyle(c);
        return {
          text: (c.textContent || '').trim().slice(0, 24),
          h: Math.round(r.height),
          mt: ccs.marginTop,
          mb: ccs.marginBottom,
        };
      })
    : [];
  // The Net Balance footer row: the last band's internals.
  const netP = leaf('Net Balance');
  const netRow = netP ? netP.closest('div.flex') : null;
  const netR = netRow ? netRow.getBoundingClientRect() : null;
  const netIcon = netP
    ? netP.closest('span').querySelector('span.flex, span[class*="flex"]') || netP.parentElement.querySelector('span.h-8, span[class*="h-8"]')
    : null;
  const netIconR = netIcon ? netIcon.getBoundingClientRect() : null;
  return JSON.stringify({
    found: true,
    card: {
      y: Math.round(cr.y),
      h: Math.round(cr.height),
      pad: cs.padding,
      radius: cs.borderRadius,
      border: cs.borderTopWidth,
    },
    h3: { h: Math.round(h3r.height), mb: h3cs.marginBottom, font: h3cs.fontSize, lh: h3cs.lineHeight },
    stack: { display: stackCs ? stackCs.display : null, mb: stackCs ? stackCs.marginBottom : null },
    bands,
    netRow: netR ? { h: Math.round(netR.height) } : null,
    netIcon: netIconR ? { w: Math.round(netIconR.width), h: Math.round(netIconR.height) } : null,
  });
})()
