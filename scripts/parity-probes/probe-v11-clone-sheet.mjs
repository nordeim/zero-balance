// probe-v11-clone-sheet.mjs — clone mobile: open sheet, verify geometry + active highlight
(() => {
  const out = { url: location.pathname };
  const sheet = [...document.querySelectorAll('div')].find(d => {
    const r = d.getBoundingClientRect(); const cs = getComputedStyle(d);
    return r.width >= 280 && r.width <= 295 && cs.position === 'fixed' && r.height > 700;
  });
  if (!sheet) { out.sheet = 'NOT OPEN'; return JSON.stringify(out); }
  const r = sheet.getBoundingClientRect(); const cs = getComputedStyle(sheet);
  out.sheet = { w: Math.round(r.width), h: Math.round(r.height), bg: cs.backgroundColor };
  out.links = [...sheet.querySelectorAll('a,button')].filter(el =>
    /Dashboard|Income|Expenses|Savings|Net Worth/i.test(el.textContent || '') &&
    el.getBoundingClientRect().height > 20 && el.getBoundingClientRect().top > 40 && el.getBoundingClientRect().top < 400
  ).map(el => {
    const cs2 = getComputedStyle(el);
    return {
      txt: (el.textContent || '').trim(),
      color: cs2.color,
      bg: cs2.backgroundImage !== 'none' ? cs2.backgroundImage.slice(0, 85) : cs2.backgroundColor,
      fw: cs2.fontWeight
    };
  });
  return JSON.stringify(out, null, 1);
})()
