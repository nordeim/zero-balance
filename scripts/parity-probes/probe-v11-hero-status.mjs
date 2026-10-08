// probe-v11-hero-status.mjs — the hero's status BADGE (exact-text match, excluding the heading)
(() => {
  const out = {};
  const hero = [...document.querySelectorAll('div,section')].filter(el => {
    const t = (el.textContent || '');
    return /NET ZERO GOAL/.test(t) && t.length < 600 && el.getBoundingClientRect().height > 150;
  })[0];
  if (!hero) return 'hero not found';
  // exact status-badge candidates
  const cands = [...hero.querySelectorAll('span, div, p, h3, strong, button')].filter(el => {
    const t = (el.textContent || '').trim();
    return (t === 'Under Budget' || t === 'NET ZERO' || t === 'Over Budget');
  });
  out.badges = cands.map(el => {
    const cs = getComputedStyle(el); const r = el.getBoundingClientRect();
    return {
      txt: (el.textContent || '').trim(), tag: el.tagName,
      color: cs.color, bg: cs.backgroundColor,
      fs: cs.fontSize, fw: cs.fontWeight, w: Math.round(r.width), h: Math.round(r.height),
      radius: cs.borderRadius, pad: cs.padding, border: cs.borderColor + ' ' + cs.borderWidth
    };
  });
  return JSON.stringify(out, null, 1);
})()
