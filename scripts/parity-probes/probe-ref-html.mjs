// Dump raw HTML of hero, donut card, guidelines card, and quick-action cards.
(() => {
  const out = {};
  const findCard = (title) => {
    const h = [...document.querySelectorAll('h3')].find((x) => (x.textContent || '').trim() === title);
    return h ? (h.closest('.rounded-2xl') || h.parentElement) : null;
  };
  const heroH = [...document.querySelectorAll('h3')].find((x) => (x.textContent || '').trim() === 'NET ZERO GOAL');
  // hero is the big gradient card — walk up to the card with the gradient bg
  let hero = heroH;
  while (hero && hero !== document.body) {
    const bg = getComputedStyle(hero).backgroundImage;
    if (bg && bg !== 'none' && bg.includes('linear-gradient')) break;
    hero = hero.parentElement;
  }
  out.heroHTML = hero ? hero.outerHTML.replace(/\s+/g, ' ').slice(0, 3000) : null;

  const sb = findCard('Spending Breakdown');
  if (sb) {
    out.legendHTML = sb.outerHTML.replace(/\s+/g, ' ').slice(0, 2500);
  }
  const gl = findCard('Budget Guidelines');
  if (gl) {
    out.guidelinesHTML = gl.outerHTML.replace(/\s+/g, ' ').slice(0, 2200);
  }
  // quick-action cards ("Add Income" etc as cards)
  const qa = [...document.querySelectorAll('div')].filter((d) => /^Add (Income|Savings|Expense)$/.test((d.textContent || '').trim()) && d.className.includes('rounded-2xl'));
  out.quickActions = qa.map((d) => d.outerHTML.replace(/\s+/g, ' ').slice(0, 900));
  return out;
})()
