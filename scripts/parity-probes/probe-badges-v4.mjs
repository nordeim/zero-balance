// Session-7: badge-row dump for the first expense card.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const main = document.querySelector('main') || document.body;
  const cards = [...main.querySelectorAll('div')].filter((d) => {
    const c = (d.className || '').toString();
    return c.includes('rounded-xl') && c.includes('p-5') && /\$[\d.]+/.test(txt(d) || '');
  });
  const first = cards[0];
  if (first) {
    const badgeRow = [...first.querySelectorAll('div')].filter((d) => (d.className || '').includes('flex-wrap') && d.children.length >= 2).pop();
    if (badgeRow) {
      out.badges = [...badgeRow.children].map((b) => ({
        tag: b.tagName,
        text: txt(b),
        bg: cs(b, 'backgroundColor'),
        color: cs(b, 'color'),
        border: cs(b, 'borderColor'),
        cls: b.className.toString().slice(0, 90),
        hasIcon: !!b.querySelector('svg'),
        iconCls: b.querySelector('svg') ? (b.querySelector('svg').getAttribute('class') || '').slice(0, 40) : null,
        textTransform: cs(b, 'textTransform'),
        fontWeight: cs(b, 'fontWeight'),
      }));
    }
    // footer row
    const footer = [...first.querySelectorAll('div')].filter((d) => {
      const t = txt(d) || '';
      return /Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec/.test(t) && t.length < 80 && d.children.length >= 1 && !d.className.includes('rounded-xl');
    }).pop();
    out.footer = footer ? { text: txt(footer).slice(0, 60), cls: footer.className.toString().slice(0, 80) } : null;
    // amount color + size
    const amt = [...first.querySelectorAll('p,span,h4')].find((x) => /^\$[\d.]+$/.test(txt(x) || ''));
    out.amount = amt ? { text: txt(amt), color: cs(amt, 'color'), size: cs(amt, 'fontSize'), weight: cs(amt, 'fontWeight') } : null;
  }
  return JSON.stringify(out, null, 1);
})()
