// Session-7: full footer dump for all expense cards.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const main = document.querySelector('main') || document.body;
  const cards = [...main.querySelectorAll('div')].filter((d) => {
    const c = (d.className || '').toString();
    return c.includes('rounded-xl') && c.includes('p-5') && /\$[\d.]+/.test(txt(d) || '');
  });
  out.cards = cards.map((card) => {
    const title = card.querySelector('h4');
    // footer: the last div containing a date
    const footer = [...card.querySelectorAll('div')].filter((d) => {
      const t = txt(d) || '';
      return /Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec/.test(t) && t.length < 90;
    }).pop();
    return {
      title: txt(title),
      footerHtml: footer ? footer.outerHTML.replace(/\s+/g, ' ').slice(0, 500) : null,
      footerCls: footer ? footer.className.toString() : null,
      footerColor: footer ? cs(footer, 'color') : null,
      footerSize: footer ? cs(footer, 'fontSize') : null,
    };
  });
  return JSON.stringify(out, null, 1);
})()
