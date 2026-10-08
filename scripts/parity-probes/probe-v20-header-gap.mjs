// v20 session: items-view header→filter-card spacing probe. The reference's
// header row carries mb-8 + items-start; the clone mb-6. Measures the y-gap
// between the header row's bottom and the filter card's top + the Add button
// width, at the CURRENT viewport.
(() => {
  const out = { path: location.pathname, vw: document.documentElement.clientWidth };
  const addBtn = [...document.querySelectorAll('main button')].find((b) => /^add/i.test((b.textContent || '').trim()));
  if (addBtn) {
    const r = addBtn.getBoundingClientRect();
    out.addBtn = { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y) };
    const row = addBtn.parentElement;
    out.rowCls = (row.className || '').toString();
    out.rowBottom = Math.round(row.getBoundingClientRect().bottom);
    // the next sibling card (the filter card)
    const next = row.nextElementSibling;
    if (next) {
      out.nextTop = Math.round(next.getBoundingClientRect().top);
      out.gap = out.nextTop - out.rowBottom;
      out.nextCls = (next.className || '').toString().slice(0, 80);
    }
  }
  return JSON.stringify(out, null, 1);
})()
