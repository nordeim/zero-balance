// Session-7: dialog geometry via the Add Budget Item heading (ref has no role=dialog).
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const h2 = [...document.querySelectorAll('h2')].find((h) => /Add Budget Item/.test((h.textContent || '')));
  if (h2) {
    // climb to the positioned panel
    let panel = h2;
    while (panel.parentElement && getComputedStyle(panel).position !== 'fixed' && !panel.getAttribute('role')) panel = panel.parentElement;
    const r = panel.getBoundingClientRect();
    out.panel = {
      tag: panel.tagName, role: panel.getAttribute('role'),
      x: Math.round(r.x), w: Math.round(r.width), right: Math.round(r.right),
      maxW: cs(panel, 'maxWidth'), cls: (panel.className || '').toString().slice(0, 90),
    };
    out.docScrollW = document.documentElement.scrollWidth;
    // classification tiles (labels or divs with Need/Want/Savings inside the panel)
    const tiles = [...panel.querySelectorAll('label, div')].filter((el) => /^(Need|Want|Savings)$/.test((el.textContent || '').trim()) && el.children.length <= 1);
    out.tiles = tiles.map((t) => {
      const tile = t.closest('div[class*="border"], label[class*="border"]') || t;
      return { text: (t.textContent || '').trim(), w: Math.round(tile.getBoundingClientRect().width), h: Math.round(tile.getBoundingClientRect().height), cls: tile.className.toString().slice(0, 90) };
    });
  }
  return JSON.stringify(out, null, 1);
})()
