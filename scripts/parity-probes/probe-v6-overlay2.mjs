(() => {
  const h = [...document.querySelectorAll('h2')].find((e) => /Edit Budget Item/.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'dialog not open' });
  let p = h;
  while (p.parentElement && !/fixed/.test(getComputedStyle(p).position)) p = p.parentElement;
  const r = p.getBoundingClientRect();
  const cs = getComputedStyle(p);
  return JSON.stringify({ cls: (p.className || '').toString().slice(0, 90), pos: cs.position, bg: cs.backgroundColor, x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) });
})()
