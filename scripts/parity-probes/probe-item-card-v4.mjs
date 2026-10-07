// Session-7: precise item-card dump scoped to main content.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const main = document.querySelector('main') || document.body;
  // item cards: rounded-xl/2xl white cards inside main that contain a $ amount and a button or badge
  const cards = [...main.querySelectorAll('div')].filter((d) => {
    const c = (d.className || '').toString();
    if (!c.includes('rounded-xl') && !c.includes('rounded-2xl')) return false;
    if (d.closest('[data-sidebar]')) return false;
    const t = txt(d) || '';
    return /\$[\d.]+/.test(t) && (t.includes('ly') || /Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec/.test(t)) && t.length < 300;
  });
  out.count = cards.length;
  const first = cards[0];
  if (first) {
    out.firstCard = {
      cls: first.className.toString().slice(0, 120),
      html: first.outerHTML.replace(/\s+/g, ' ').slice(0, 1400),
    };
  }
  return JSON.stringify(out, null, 1);
})()
