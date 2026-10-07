// Session-8 (v5): dialog footer buttons — broader text match (Save/Add/Cancel variants).
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const btns = [...document.querySelectorAll('button')].filter((b) => /^(Cancel|Save|Save Item|Add Asset|Add Liability|Save Asset|Save Line Item|Add Item|Save Changes)$/.test(txt(b) || '') && b.getBoundingClientRect().height > 20 && b.getBoundingClientRect().top > 100);
  out.buttons = btns.map((b) => ({
    t: txt(b),
    bgImage: (cs(b, 'backgroundImage') || 'none').slice(0, 95),
    bgColor: cs(b, 'backgroundColor'),
    color: cs(b, 'color'),
    border: cs(b, 'borderWidth') + ' ' + cs(b, 'borderColor'),
    radius: cs(b, 'borderRadius'),
    h: Math.round(b.getBoundingClientRect().height),
    weight: cs(b, 'fontWeight'),
  }));
  return JSON.stringify(out, null, 1);
})()
