// Session-8 (v5): calculator dialog — banner card, empty state, line-item rows.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // find the calculator panel: heading "X Calculator"
  const h = [...document.querySelectorAll('h2')].find((x) => /Calculator/.test(x.textContent || ''));
  if (!h) return JSON.stringify({ error: 'no calculator' });
  let panel = h;
  for (let i = 0; i < 8; i++) { const p = panel.parentElement; if (!p || p === document.body) break; panel = p; }
  out.heading = { t: txt(h), size: cs(h, 'fontSize'), weight: cs(h, 'fontWeight'), color: cs(h, 'color') };

  // description line
  const desc = [...panel.querySelectorAll('p, span, div')].find((d) => /Break down your/.test(txt(d) || '') && d.querySelectorAll('*').length === 0);
  out.desc = desc ? { t: txt(desc), size: cs(desc, 'fontSize'), color: cs(desc, 'color') } : null;

  // Total Calculated banner card
  const tc = [...panel.querySelectorAll('div')].find((d) => /^Total Calculated$/.test(txt(d) || ''));
  if (tc) {
    let card = tc;
    for (let i = 0; i < 5; i++) { const p = card.parentElement; if (!p || p === panel) break; const c = (p.className || '').toString(); if (/rounded/.test(c) && /border/.test(c)) { card = p; break; } card = p; }
    const amt = [...card.querySelectorAll('span, div, p')].find((d) => /^\$/.test(txt(d) || '') && d.querySelectorAll('*').length === 0);
    const based = [...card.querySelectorAll('span, div, p')].find((d) => /Based on/.test(txt(d) || '') && d.querySelectorAll('*').length === 0);
    out.banner = {
      cardCls: (card.className || '').toString().replace(/\s+/g, ' ').slice(0, 140),
      bg: cs(card, 'backgroundColor'),
      border: cs(card, 'borderWidth') + ' ' + cs(card, 'borderColor'),
      amount: amt ? { t: txt(amt), color: cs(amt, 'color'), size: cs(amt, 'fontSize'), weight: cs(amt, 'fontWeight') } : null,
      based: based ? { t: txt(based), color: cs(based, 'color'), size: cs(based, 'fontSize') } : null,
    };
  }

  // empty state / rows
  const addFirst = [...panel.querySelectorAll('button')].find((b) => /Add First Item/.test(txt(b) || ''));
  out.emptyState = addFirst ? { t: txt(addFirst), bg: cs(addFirst, 'backgroundColor'), border: cs(addFirst, 'borderWidth') + ' ' + cs(addFirst, 'borderColor'), radius: cs(addFirst, 'borderRadius'), color: cs(addFirst, 'color'), cls: (addFirst.className || '').toString().replace(/\s+/g, ' ').slice(0, 120) } : null;

  // Line Items section header + Add Item button
  const li = [...panel.querySelectorAll('h3')].find((x) => /Line Items/.test(x.textContent || ''));
  out.lineItemsHeader = li ? { size: cs(li, 'fontSize'), weight: cs(li, 'fontWeight'), color: cs(li, 'color') } : null;

  return JSON.stringify(out, null, 1);
})()
