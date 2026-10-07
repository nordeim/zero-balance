// v6: net-worth asset list full structure (groups, order, items) + card border widths + hover state
(() => {
  const out = { groups: [] };
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);

  // walk the active panel; find type-group headers (h3/h4 or bold capitalize rows)
  const panel = document.querySelector('[role="tabpanel"][data-state="active"]') || document;
  const heads = [...panel.querySelectorAll('h3, h4, [class*="capitalize"]')].map((h) => (h.textContent || '').replace(/\s+/g, ' ').trim()).filter((t) => t && t.length < 30);
  out.headers = [...new Set(heads)].slice(0, 12);

  // capture group order by scanning text of successive blocks
  out.panelText = (panel.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 400);

  // first card border WIDTH (not just color)
  const card = [...panel.querySelectorAll('div')].filter((d) => /hover:shadow-lg/.test(d.className)).sort((a, b) => a.querySelectorAll('div').length - b.querySelectorAll('div').length)[0];
  if (card) {
    out.cardBorderWidth = cs(card, 'borderWidth');
    out.cardBorderStyle = cs(card, 'borderStyle');
    out.cardBorderTopWidth = cs(card, 'borderTopWidth');
    // the hover shadow value (class attribute)
    out.hoverShadowClass = /hover:shadow-\S+/.exec(card.className)?.[0] || null;
  }
  return JSON.stringify(out, null, 1);
})()
