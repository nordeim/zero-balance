// Session-8 (v5): calculator — Total Calculated banner card + Add Item header button.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const h = [...document.querySelectorAll('h2')].find((x) => /Calculator/.test(x.textContent || ''));
  if (!h) return JSON.stringify({ error: 'no calculator' });
  let panel = h;
  for (let i = 0; i < 10; i++) { const p = panel.parentElement; if (!p || p === document.body) break; if ((panel.className || '').toString().includes('fixed')) break; panel = p; }

  // banner card: the ancestor of "Total Calculated" that has border+rounded
  const tc = [...panel.querySelectorAll('span, div, p')].find((d) => /^Total Calculated$/.test(txt(d) || ''));
  if (tc) {
    let card = tc;
    for (let i = 0; i < 6; i++) {
      const p = card.parentElement;
      if (!p || p === document.body) break;
      card = p;
      const c = (card.className || '').toString();
      const hasBorder = getComputedStyle(card).borderWidth !== '0px';
      if (/rounded/.test(c) && hasBorder) break;
    }
    const kids = [...card.querySelectorAll('span, p, div')].filter((d) => d.querySelectorAll('*').length === 0 && (txt(d) || '').length > 0);
    out.banner = {
      cardCls: (card.className || '').toString().replace(/\s+/g, ' ').slice(0, 150),
      bg: cs(card, 'backgroundColor'),
      border: cs(card, 'borderWidth') + ' ' + cs(card, 'borderColor'),
      radius: cs(card, 'borderRadius'),
      pad: cs(card, 'padding'),
      leaves: kids.slice(0, 5).map((k) => ({ t: txt(k).slice(0, 26), color: cs(k, 'color'), size: cs(k, 'fontSize'), weight: cs(k, 'fontWeight') })),
    };
  }

  // "Add Item" button next to Line Items header
  const addBtn = [...panel.querySelectorAll('button')].find((b) => txt(b) === 'Add Item');
  if (addBtn) {
    out.addItemBtn = {
      h: Math.round(addBtn.getBoundingClientRect().height),
      bg: cs(addBtn, 'backgroundColor'),
      color: cs(addBtn, 'color'),
      border: cs(addBtn, 'borderWidth') + ' ' + cs(addBtn, 'borderColor'),
      radius: cs(addBtn, 'borderRadius'),
      cls: (addBtn.className || '').toString().replace(/\s+/g, ' ').slice(0, 130),
    };
  }

  return JSON.stringify(out, null, 1);
})()
