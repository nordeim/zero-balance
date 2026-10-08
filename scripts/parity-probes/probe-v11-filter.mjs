// probe-v11-filter.mjs — filter card geometry + functional behavior on /income
(() => {
  const out = { url: location.pathname };
  // the search input
  const search = document.querySelector('input[type="text"], input[type="search"], input[placeholder*="earch" i]');
  if (search) {
    const r = search.getBoundingClientRect(); const cs = getComputedStyle(search);
    out.search = { w: Math.round(r.width), h: Math.round(r.height), ph: search.getAttribute('placeholder'), fs: cs.fontSize, color: cs.color, bg: cs.backgroundColor, border: cs.borderColor + ' ' + cs.borderWidth, radius: cs.borderRadius };
  }
  // select-like triggers (combobox buttons)
  const triggers = [...document.querySelectorAll('button')].filter(b => {
    const r = b.getBoundingClientRect();
    const cs = getComputedStyle(b);
    return r.height >= 30 && r.height <= 42 && r.width > 90 && r.top > 100 && (b.getAttribute('role') === 'combobox' || !!b.querySelector('svg') || /All|Any|cate|freq/i.test(b.textContent || ''));
  }).slice(0, 4);
  out.triggers = triggers.map(b => {
    const r = b.getBoundingClientRect(); const cs = getComputedStyle(b);
    return { txt: (b.textContent || '').trim().slice(0, 24), w: Math.round(r.width), h: Math.round(r.height), fs: cs.fontSize, justify: cs.justifyContent };
  });
  // card count before filtering
  out.cardCount = [...document.querySelectorAll('[class*="card"], article')].filter(el => {
    const r = el.getBoundingClientRect(); const t = (el.textContent || '');
    return r.width > 200 && r.height > 60 && /\$/.test(t) && el.children.length > 1;
  }).length;
  return JSON.stringify(out, null, 1);
})()
