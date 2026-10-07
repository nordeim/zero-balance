(() => {
  const panel = document.querySelector('[role="tabpanel"][data-state="active"]') || document;
  const h = [...panel.querySelectorAll('h3, h4')].find((e) => /No .* yet|no items|nothing/i.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'none', panelHead: (panel.textContent || '').slice(0, 200) });
  const box = h.parentElement;
  const cs = (el) => getComputedStyle(el);
  const desc = [...box.querySelectorAll('p')].map((p) => ({ text: (p.textContent || '').trim(), size: cs(p).fontSize, color: cs(p).color, m: cs(p).margin }));
  const btn = box.querySelector('button');
  const circle = box.querySelector('div[class*="rounded-full"]');
  return JSON.stringify({
    heading: (h.textContent || '').trim(),
    hmb: cs(h).marginBottom,
    desc,
    circle: circle ? 'PRESENT' : 'ABSENT',
    btn: { text: (btn?.textContent || '').trim(), bg: (cs(btn).backgroundImage || 'none').slice(0, 80), h: cs(btn).height, svg: btn?.querySelectorAll('svg').length },
    boxClasses: box.className.slice(0, 100),
  }, null, 1);
})()
