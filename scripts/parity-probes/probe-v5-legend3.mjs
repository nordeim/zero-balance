// Session-8 (v5): donut legend amounts div — inner HTML + per-child colors.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const rows = [...document.querySelectorAll('main div')].filter((d) => {
    const c = (d.className || '').toString();
    return /items-center justify-between/.test(c) && /p-3/.test(c) && (txt(d) || '').includes('%') && (txt(d) || '').length < 40;
  });
  if (rows.length) {
    const amountsDiv = [...rows[0].children].find((k) => /\$/.test(txt(k) || ''));
    out.html = amountsDiv ? amountsDiv.innerHTML.replace(/\s+/g, ' ').slice(0, 400) : null;
    out.children = amountsDiv ? [...amountsDiv.querySelectorAll('*')].map((k) => ({
      tag: k.tagName,
      t: (txt(k) || '').slice(0, 20),
      color: cs(k, 'color'),
      size: cs(k, 'fontSize'),
      weight: cs(k, 'fontWeight'),
    })) : [];
    out.divColor = amountsDiv ? cs(amountsDiv, 'color') : null;
    out.divCls = amountsDiv ? (amountsDiv.className || '').toString() : null;
  }

  return JSON.stringify(out, null, 1);
})()
