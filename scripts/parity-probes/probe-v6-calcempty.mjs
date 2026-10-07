(() => {
  const h = [...document.querySelectorAll('h3, h4, p')].find((e) => /No line items yet/i.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'no empty' });
  const box = h.closest('div');
  const cs = (el) => getComputedStyle(el);
  const svgs = [...box.querySelectorAll('svg')].filter((s) => !s.closest('button')).map((s) => { const r = s.getBoundingClientRect(); return { w: Math.round(r.width), h: Math.round(r.height), opacity: cs(s).opacity, color: cs(s).color }; });
  const p = h.tagName === 'P' ? h : box.querySelector('p');
  return JSON.stringify({
    emptyText: (p?.textContent || '').trim().slice(0, 80),
    pSize: cs(p).fontSize, pColor: cs(p).color, pMargin: cs(p).margin,
    svgs,
    py: cs(box).paddingTop,
  }, null, 1);
})()
