// Session-8 (v5): donut legend rows leaf-level (icon wrapper breaks div-free filter).
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const rows = [...document.querySelectorAll('main div')].filter((d) => {
    const c = (d.className || '').toString();
    return /items-center justify-between/.test(c) && /p-3/.test(c) && (txt(d) || '').includes('%') && (txt(d) || '').length < 40;
  });
  out.rows = rows.slice(0, 3).map((r) => {
    const kids = [...r.children].map((k) => ({
      tag: k.tagName,
      t: (txt(k) || '').slice(0, 24),
      color: cs(k, 'color'),
      size: cs(k, 'fontSize'),
      weight: cs(k, 'fontWeight'),
    }));
    return { rowCls: (r.className || '').toString().replace(/\s+/g, ' '), kids };
  });

  return JSON.stringify(out, null, 1);
})()
