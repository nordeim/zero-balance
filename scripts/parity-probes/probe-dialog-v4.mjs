// Session-7: dialog geometry at mobile — width, position, overflow.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const dlg = document.querySelector('[role="dialog"]');
  if (dlg) {
    const r = dlg.getBoundingClientRect();
    out.dialog = {
      x: Math.round(r.x), w: Math.round(r.width),
      right: Math.round(r.right),
      maxW: cs(dlg, 'maxWidth'),
      cls: dlg.className.toString().slice(0, 110),
    };
    const content = dlg.querySelector('div[class*="max-h"], div[class*="overflow-y"]');
    if (content) out.scrollBody = { cls: content.className.toString().slice(0, 80), scrollH: content.scrollHeight, clientH: content.clientHeight };
    out.docScrollW = document.documentElement.scrollWidth;
    // classification tiles
    const tiles = [...dlg.querySelectorAll('label')].filter((l) => /Need|Want|Savings/.test((l.textContent || '').trim()));
    out.tiles = tiles.map((t) => {
      const tile = t.closest('div[class*="border"]') || t;
      return { text: (t.textContent || '').trim(), w: Math.round(tile.getBoundingClientRect().width), h: Math.round(tile.getBoundingClientRect().height), cls: tile.className.toString().slice(0, 90) };
    });
  }
  return JSON.stringify(out, null, 1);
})()
