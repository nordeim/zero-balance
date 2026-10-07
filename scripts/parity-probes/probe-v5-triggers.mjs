// Session-8 (v5): select triggers (filter card) + networth tabs — computed chrome.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. Select trigger buttons in the filter card
  const triggers = [...document.querySelectorAll('main button')].filter((b) => /^(All Categories|All Frequencies|All Payment Methods|All Types)/.test(txt(b) || ''));
  out.selectTriggers = triggers.slice(0, 3).map((b) => {
    const inner = b.querySelector('span');
    return {
      t: txt(b).slice(0, 26),
      h: Math.round(b.getBoundingClientRect().height),
      border: cs(b, 'borderWidth') + ' ' + cs(b, 'borderColor'),
      radius: cs(b, 'borderRadius'),
      bg: cs(b, 'backgroundColor'),
      innerColor: inner ? cs(inner, 'color') : null,
      innerSize: inner ? cs(inner, 'fontSize') : null,
      cls: (b.className || '').toString().replace(/\s+/g, ' ').slice(0, 130),
    };
  });

  // 2. Networth tab triggers
  const tabs = [...document.querySelectorAll('main button[role="tab"], main [role="tab"]')];
  out.tabs = tabs.slice(0, 4).map((t) => {
    const inner = t.querySelector('span') || t;
    return {
      t: txt(t).slice(0, 22),
      color: cs(inner, 'color'),
      size: cs(inner, 'fontSize'),
      weight: cs(inner, 'fontWeight'),
      bg: cs(t, 'backgroundColor'),
      border: cs(t, 'borderWidth') + ' ' + cs(t, 'borderColor'),
      radius: cs(t, 'borderRadius'),
      pad: cs(t, 'padding'),
      selected: t.getAttribute('aria-selected'),
      cls: (t.className || '').toString().replace(/\s+/g, ' ').slice(0, 130),
    };
  });

  return JSON.stringify(out, null, 1);
})()
