(() => {
  const h = [...document.querySelectorAll('h2, h3')].find((e) => /Calculator/i.test(e.textContent || ''));
  let panel = h;
  while (panel.parentElement && !/rounded-2xl/.test(panel.className || '')) panel = panel.parentElement;
  const row = [...panel.querySelectorAll('div')].filter((d) => /Test Row/.test(d.textContent || '')).sort((a, b) => a.querySelectorAll('div').length - b.querySelectorAll('div').length)[0];
  let r = row;
  for (let i = 0; i < 4; i++) { if (getComputedStyle(r).borderTopWidth === '1px') break; r = r.parentElement; }
  const cs = (el) => getComputedStyle(el);
  const btns = [...r.querySelectorAll('button')].map((b) => { const svg = b.querySelector('svg'); const rect = svg?.getBoundingClientRect(); return { color: cs(b).color, opacity: cs(b).opacity, w: Math.round(b.getBoundingClientRect().width), iconW: rect ? Math.round(rect.width) : null }; });
  const pills = [...r.querySelectorAll('span')].map((s) => ({ text: (s.textContent || '').trim(), bg: cs(s).backgroundColor, color: cs(s).color }));
  return JSON.stringify({ btns, pills }, null, 1);
})()
