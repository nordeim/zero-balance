// Session-8 (v5): dropdown menu chrome — content panel + items + hover bg.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const items = [...document.querySelectorAll('[role="menuitem"]')];
  if (items.length) {
    out.items = items.map((i) => ({
      t: txt(i),
      color: cs(i, 'color'),
      size: cs(i, 'fontSize'),
      pad: cs(i, 'padding'),
      radius: cs(i, 'borderRadius'),
      bg: cs(i, 'backgroundColor'),
    }));
    const content = items[0].closest('[role="menu"]');
    if (content) {
      out.content = {
        bg: cs(content, 'backgroundColor'),
        border: cs(content, 'borderWidth') + ' ' + cs(content, 'borderColor'),
        radius: cs(content, 'borderRadius'),
        shadow: (cs(content, 'boxShadow') || '').slice(0, 70),
        pad: cs(content, 'padding'),
        minW: cs(content, 'minWidth'),
      };
    }
  }
  return JSON.stringify(out, null, 1);
})()
