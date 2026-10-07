(() => {
  // find the toast viewport by R1's geometry: top ~32px, z-100, full-width, pointer-events auto
  const cands = [...document.querySelectorAll('body *')].filter((el) => {
    const cs = getComputedStyle(el);
    if (!['fixed', 'absolute'].includes(cs.position)) return false;
    if (parseInt(cs.zIndex || '0') < 90) return false;
    const r = el.getBoundingClientRect();
    return r.width > 500 && r.height < 400 && r.top < 120;
  });
  return JSON.stringify(cands.slice(0, 4).map((el) => {
    const cs = getComputedStyle(el);
    return { tag: el.tagName, cls: (el.className || '').toString().slice(0, 90), pe: cs.pointerEvents, z: cs.zIndex, w: Math.round(el.getBoundingClientRect().width), top: Math.round(el.getBoundingClientRect().top), html: el.innerHTML.slice(0, 120) };
  }), null, 1);
})()
