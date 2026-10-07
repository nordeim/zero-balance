(() => {
  const el = [...document.querySelectorAll('#root div, body > div > div')].find((d) => {
    const cs = getComputedStyle(d);
    return cs.position === 'fixed' && cs.top === '0px' && parseInt(cs.zIndex || '0') >= 90 && d.getBoundingClientRect().width > 300;
  });
  if (!el) return JSON.stringify({ err: 'not found' });
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  return JSON.stringify({
    cls: (el.className || '').toString().slice(0, 120),
    pe: cs.pointerEvents, z: cs.zIndex, w: Math.round(r.width), h: Math.round(r.height), top: Math.round(r.top),
    childCount: el.children.length,
    html: el.innerHTML.slice(0, 150),
  }, null, 1);
})()
