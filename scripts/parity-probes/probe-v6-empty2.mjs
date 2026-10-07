(() => {
  const panel = document.querySelector('[role="tabpanel"][data-state="active"]') || document;
  const h = [...panel.querySelectorAll('h3, h4')].find((e) => /No liabilities yet/i.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'none' });
  const box = h.parentElement;
  const cs = (el) => getComputedStyle(el);
  const desc = [...box.querySelectorAll('p')].map((p) => ({ text: (p.textContent || '').trim(), color: cs(p).color, size: cs(p).fontSize, m: cs(p).margin }));
  const btn = box.querySelector('button');
  const hcs = cs(h);
  // icon circle?
  const circle = box.querySelector('div[class*="rounded-full"]');
  return JSON.stringify({
    heading: { text: (h.textContent || '').trim(), size: hcs.fontSize, weight: hcs.fontWeight, color: hcs.color, mb: hcs.marginBottom },
    desc,
    circle: circle ? { w: cs(circle).width, bg: cs(circle).backgroundColor, svg: circle.querySelectorAll('svg').length } : null,
    btn: { text: (btn.textContent || '').trim(), bg: cs(btn).backgroundColor, border: cs(btn).borderColor, color: cs(btn).color, h: cs(btn).height, radius: cs(btn).borderRadius, svg: btn.querySelectorAll('svg').length },
    boxText: (box.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 120),
  }, null, 1);
})()
