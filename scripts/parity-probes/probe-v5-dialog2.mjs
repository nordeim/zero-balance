// Session-8 (v5): dialog Save/Cancel button gradients + tile wrappers + dialog panel.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const scope = [...document.querySelectorAll('.fixed [role="dialog"], [role="dialog"], .fixed')];
  const root = scope[scope.length - 1] || document.body;

  const btns = [...root.querySelectorAll('button')].filter((b) => /^(Cancel|Save Item|Add Item|Save)$/.test(txt(b) || ''));
  out.buttons = btns.map((b) => ({
    t: txt(b),
    bgImage: (cs(b, 'backgroundImage') || 'none').slice(0, 90),
    bgColor: cs(b, 'backgroundColor'),
    color: cs(b, 'color'),
    h: Math.round(b.getBoundingClientRect().height),
    w: Math.round(b.getBoundingClientRect().width),
  }));

  // tile wrappers: divs that contain the Need/Want/Savings radio inputs
  const radio = root.querySelector('input[type="radio"]');
  if (radio) {
    let wrap = radio.closest('div');
    while (wrap && (txt(wrap) || '').replace(/Need|Want|Savings/g, '').trim().length > 0 && wrap.querySelectorAll('input').length < 2) wrap = wrap.parentElement;
    const tileWrap = radio.parentElement;
    let tile = tileWrap;
    for (let i = 0; i < 3; i++) { const p = tile.parentElement; if (!p || p === root) break; if ((p.className || '').toString().includes('border') || (p.className || '').toString().includes('rounded')) { tile = p; break; } tile = p; }
    out.tile = { cls: (tile.className || '').toString().replace(/\s+/g, ' ').slice(0, 160), border: cs(tile, 'borderWidth') + ' ' + cs(tile, 'borderColor'), bg: cs(tile, 'backgroundColor'), radius: cs(tile, 'borderRadius'), pad: cs(tile, 'padding') };
  }

  // panel
  const panel = [...root.querySelectorAll('div')].find((d) => {
    const c = (d.className || '').toString();
    const r = d.getBoundingClientRect();
    return /rounded/.test(c) && r.width > 300 && r.width < 900 && cs(d, 'backgroundColor') === 'rgb(255, 255, 255)' && r.height > 300;
  });
  if (panel) {
    const pr = panel.getBoundingClientRect();
    out.panel = { w: Math.round(pr.width), h: Math.round(pr.height), radius: cs(panel, 'borderRadius'), pad: cs(panel, 'padding') };
  }
  return JSON.stringify(out, null, 1);
})()
