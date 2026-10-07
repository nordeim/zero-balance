// Session-8 (v5): networth tab buttons + dialog input chrome.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. Networth tab-like buttons: "Assets (N)" / "Liabilities (N)"
  const tabs = [...document.querySelectorAll('main button')].filter((b) => /^(Assets|Liabilities)/.test(txt(b) || '') && (txt(b) || '').length < 30);
  out.tabs = tabs.slice(0, 4).map((b) => {
    const inner = b.querySelector('span') || b;
    return {
      t: txt(b).slice(0, 26),
      color: cs(inner, 'color'),
      size: cs(inner, 'fontSize'),
      weight: cs(inner, 'fontWeight'),
      bg: cs(b, 'backgroundColor'),
      border: cs(b, 'borderWidth') + ' ' + cs(b, 'borderColor'),
      radius: cs(b, 'borderRadius'),
      pad: cs(b, 'padding'),
      h: Math.round(b.getBoundingClientRect().height),
      cls: (b.className || '').toString().replace(/\s+/g, ' ').slice(0, 140),
    };
  });

  // 2. "1 items · $25,000" tab-panel subtitle
  const sub = [...document.querySelectorAll('main p, main span, main div')].filter((d) => d.querySelectorAll('*').length === 0 && /items? ·/.test(txt(d) || ''));
  out.tabSubtitle = sub.slice(0, 2).map((s) => ({ t: txt(s), color: cs(s, 'color'), size: cs(s, 'fontSize') }));

  return JSON.stringify(out, null, 1);
})()
