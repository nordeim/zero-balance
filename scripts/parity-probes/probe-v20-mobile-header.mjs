// v20 session: mobile items-view header probe — measures the header row's
// Add button (the VLM flagged ref=auto-width vs clone=full-width at 390px)
// plus the first item card's badge-row geometry (the wrap claims).
(() => {
  const out = { path: location.pathname, vw: document.documentElement.clientWidth };
  // the header row: h1/h2 + the Add button (the .zb-btn-add family on the
  // clone; any gradient button on the reference)
  const btns = [...document.querySelectorAll('main button, button')].filter((b) => /^add/i.test((b.textContent || '').trim()));
  const addBtn = btns.find((b) => {
    const r = b.getBoundingClientRect();
    return r.width > 60 && r.top < 400 && /gradient|bg-/.test((b.className || '').toString());
  }) || btns[0];
  if (addBtn) {
    const r = addBtn.getBoundingClientRect();
    const cs = getComputedStyle(addBtn);
    out.addBtn = {
      text: (addBtn.textContent || '').trim().slice(0, 24),
      x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height),
      display: cs.display, justify: cs.justifyContent, textAlign: cs.textAlign,
      right: Math.round(r.right),
      containerRight: Math.round(r.right),
    };
    // the button's parent row width (to test full-width vs auto)
    const pr = addBtn.parentElement.getBoundingClientRect();
    out.parentRow = { w: Math.round(pr.width), x: Math.round(pr.x), tag: addBtn.parentElement.tagName, cls: (addBtn.parentElement.className || '').toString().slice(0, 60) };
  } else out.addBtn = 'NOT FOUND';
  // first item card's badge row: count badges + their row count
  const card = [...document.querySelectorAll('main div')].find((d) => {
    const t = (d.textContent || '');
    return /\$[\d,.]+/.test(t) && d.querySelectorAll('span').length >= 3 && d.getBoundingClientRect().height > 80 && d.getBoundingClientRect().height < 400;
  });
  if (card) {
    const badges = [...card.querySelectorAll('span')].filter((s) => {
      const r = s.getBoundingClientRect();
      return r.width > 20 && r.width < 140 && r.height > 16 && r.height < 30;
    });
    const rows = new Set(badges.map((b) => Math.round(b.getBoundingClientRect().y)));
    out.cardBadges = { count: badges.length, rows: [...rows].sort((a, b) => a - b), texts: badges.map((b) => (b.textContent || '').trim()).slice(0, 8) };
  }
  return JSON.stringify(out, null, 1);
})()
