(() => {
  const h = [...document.querySelectorAll('h2, h3')].find((e) => /Calculator/i.test(e.textContent || ''));
  let panel = h;
  while (panel.parentElement && !/rounded-2xl/.test(panel.className || '')) panel = panel.parentElement;
  const row = [...panel.querySelectorAll('div')].filter((d) => /Test Item/.test(d.textContent || '')).sort((a, b) => a.querySelectorAll('div').length - b.querySelectorAll('div').length)[0];
  let r = row;
  for (let i = 0; i < 4; i++) { if (getComputedStyle(r).borderTopWidth === '1px') break; r = r.parentElement; }
  const cs = (el) => getComputedStyle(el);
  const btns = [...r.querySelectorAll('button')].map((b) => { const svg = b.querySelector('svg'); const rect = svg?.getBoundingClientRect(); return { color: cs(b).color, iconW: rect ? Math.round(rect.width) : null, d: (svg?.querySelector('path')?.getAttribute('d') || '').slice(0, 20) }; });
  const pills = [...r.querySelectorAll('span')].map((s) => ({ text: (s.textContent || '').trim(), bg: cs(s).backgroundColor, color: cs(s).color, classes: s.className.slice(0, 80) }));
  const amt = [...r.querySelectorAll('p')].map((p) => ({ text: (p.textContent || '').trim(), color: cs(p).color, size: cs(p).fontSize, weight: cs(p).fontWeight }));
  return JSON.stringify({ btns, pills, amt }, null, 1);
})()
