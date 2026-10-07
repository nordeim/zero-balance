(() => {
  const h = [...document.querySelectorAll('h3, h4')].find((e) => /No income items yet/i.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'none' });
  const box = h.parentElement; // py-16 text-center
  const card = box.closest('[class*="border"], [style*="border"]') || box.parentElement;
  const ccs = getComputedStyle(card);
  const svg = box.querySelector('svg');
  const scs = svg ? getComputedStyle(svg) : null;
  const r = svg ? svg.getBoundingClientRect() : null;
  return JSON.stringify({
    cardClasses: card.className.slice(0, 110),
    cardBorder: ccs.borderColor, cardRadius: ccs.borderRadius, cardBg: ccs.backgroundColor, cardPy: ccs.paddingTop,
    svg: svg ? { w: Math.round(r.width), h: Math.round(r.height), color: scs.color, opacity: scs.opacity, mb: scs.marginBottom, d: (svg.querySelector('path')?.getAttribute('d') || '').slice(0, 24) } : null,
    hmb: getComputedStyle(h).marginBottom,
    descSize: getComputedStyle(box.querySelector('p')).fontSize,
  }, null, 1);
})()
