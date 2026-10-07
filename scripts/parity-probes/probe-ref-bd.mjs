// Focused dumps: breakdown card full, legend rows, guidelines cards, quick-action buttons, one stat card
(() => {
  const out = {};
  const textNode = (txt) => {
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = w.nextNode())) if ((n.textContent || '').trim() === txt) return n.parentElement;
    return null;
  };
  const up = (el, cls) => { let c = el; for (let i = 0; i < 8 && c; i++) { c = c.parentElement; if (c && (c.className || '').includes(cls)) return c; } return null; };

  // Breakdown card full
  const bdH = textNode('Net Zero Breakdown');
  if (bdH) { const card = up(bdH, 'rounded-2xl'); out.breakdown = card?.outerHTML.replace(/\s+/g, ' '); }
  return out;
})()
