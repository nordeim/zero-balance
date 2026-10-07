(() => {
  // find the calculator panel (contains "Calculator" heading)
  const h = [...document.querySelectorAll('h2, h3')].find((e) => /Calculator/i.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'no calc' });
  let panel = h;
  while (panel.parentElement && !/rounded-2xl/.test(panel.className || '')) panel = panel.parentElement;
  const t = (panel.textContent || '').replace(/\s+/g, ' ').trim();
  const btns = [...panel.querySelectorAll('button')].map((b) => {
    const cs = getComputedStyle(b);
    return { text: (b.textContent || '').trim().slice(0, 24), bg: (cs.backgroundImage !== 'none' ? cs.backgroundImage : cs.backgroundColor).toString().slice(0, 70), svg: b.querySelectorAll('svg').length, color: cs.color, bw: cs.borderWidth };
  });
  return JSON.stringify({ text: t.slice(0, 320), btns }, null, 1);
})()
