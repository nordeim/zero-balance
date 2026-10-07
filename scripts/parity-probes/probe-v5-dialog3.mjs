// Session-8 (v5): dialog buttons + tiles — global scope (only one dialog open).
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const btns = [...document.querySelectorAll('button')].filter((b) => /^(Cancel|Save Item)$/.test(txt(b) || '') && b.getBoundingClientRect().height > 20);
  out.buttons = btns.map((b) => ({
    t: txt(b),
    bgImage: (cs(b, 'backgroundImage') || 'none').slice(0, 95),
    color: cs(b, 'color'),
    h: Math.round(b.getBoundingClientRect().height),
  }));

  const radio = document.querySelector('.fixed input[type="radio"], [data-state="open"] input[type="radio"], input[type="radio"]:not([tabindex="-1"])');
  if (radio) {
    let tile = radio.parentElement;
    for (let i = 0; i < 4; i++) {
      const p = tile.parentElement;
      if (!p) break;
      const c = (p.className || '').toString();
      if (c.includes('border') && c.includes('rounded')) { tile = p; break; }
      tile = p;
    }
    out.tile = {
      cls: (tile.className || '').toString().replace(/\s+/g, ' ').slice(0, 170),
      border: cs(tile, 'borderWidth') + ' ' + cs(tile, 'borderColor'),
      bg: cs(tile, 'backgroundColor'),
      radius: cs(tile, 'borderRadius'),
      pad: cs(tile, 'padding'),
      text: (txt(tile) || '').slice(0, 20),
    };
  }
  return JSON.stringify(out, null, 1);
})()
