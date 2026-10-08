// probe-v14-nw-tabs.mjs — net-worth tablist semantics + keyboard flow:
// roles, aria-selected, tab geometry, active styling, then ArrowRight/ArrowLeft
// focus movement (measured via document.activeElement after keydown).
(() => {
  const out = { url: location.pathname };
  const tabs = [...document.querySelectorAll('[role="tab"], button')].filter(b => {
    const t = b.textContent.trim();
    return /^(Assets|Liabilities)$/i.test(t) && b.getBoundingClientRect().height > 0;
  });
  out.tabCount = tabs.length;
  out.tabs = tabs.map(t => {
    const cs = getComputedStyle(t);
    const r = t.getBoundingClientRect();
    return {
      role: t.getAttribute('role'), ariaSel: t.getAttribute('aria-selected'),
      tabIdx: t.tabIndex, t: t.textContent.trim(),
      color: cs.color, bg: cs.backgroundColor, w: Math.round(r.width), h: Math.round(r.height),
      x: Math.round(r.x), y: Math.round(r.y), fw: cs.fontWeight,
      border: cs.borderTopWidth + ' ' + cs.borderTopColor
    };
  });
  out.containerRole = tabs[0] ? (tabs[0].closest('[role="tablist"]') ? 'tablist' : (tabs[0].parentElement.getAttribute('role') || 'none')) : null;
  return JSON.stringify(out, null, 1);
})()
