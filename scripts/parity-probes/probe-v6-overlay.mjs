(() => {
  const overlay = [...document.querySelectorAll('div')].find((d) => /fixed inset-0/.test(d.className || '') && getComputedStyle(d).backgroundColor !== 'rgba(0, 0, 0, 0)');
  if (!overlay) return JSON.stringify({ err: 'no overlay' });
  const r = overlay.getBoundingClientRect();
  return JSON.stringify({ found: true, x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height), bg: getComputedStyle(overlay).backgroundColor, cls: overlay.className.slice(0, 80) });
})()
