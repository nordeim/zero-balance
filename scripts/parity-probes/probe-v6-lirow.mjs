(() => {
  const h = [...document.querySelectorAll('h2, h3')].find((e) => /Calculator/i.test(e.textContent || ''));
  let panel = h;
  while (panel.parentElement && !/rounded-2xl/.test(panel.className || '')) panel = panel.parentElement;
  // the line-item row: a div containing "Test Item"
  const row = [...panel.querySelectorAll('div')].filter((d) => /Test Item/.test(d.textContent || '')).sort((a, b) => a.querySelectorAll('div').length - b.querySelectorAll('div').length)[0];
  if (!row) return JSON.stringify({ err: 'no row' });
  const cs = (el) => getComputedStyle(el);
  let r = row;
  // climb to the bordered row container
  for (let i = 0; i < 4; i++) { if (cs(r).borderTopWidth === '1px') break; r = r.parentElement; }
  const btns = [...r.querySelectorAll('button')].map((b) => ({ aria: b.getAttribute('aria-label'), opacity: cs(b).opacity, color: cs(b).color, w: cs(b).width, h: cs(b).height, classes: b.className.slice(0, 110) }));
  const badge = r.querySelector('span[class*="rounded"], span[class*="badge"]');
  return JSON.stringify({
    rowClasses: r.className.slice(0, 130),
    rowChrome: { border: cs(r).borderColor, radius: cs(r).borderRadius, bg: cs(r).backgroundColor, padding: cs(r).padding },
    rowText: (r.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 100),
    badge: badge ? { text: (badge.textContent || '').trim(), bg: cs(badge).backgroundColor, color: cs(badge).color, classes: badge.className.slice(0, 100) } : null,
    btns,
  }, null, 1);
})()
