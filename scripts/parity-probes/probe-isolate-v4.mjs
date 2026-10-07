// Session-7: binary-search the overflow culprit by toggling display:none.
(() => {
  const out = { bodyScrollW0: document.body.scrollWidth };
  const main = document.querySelector('main');
  const wrap = [...main.querySelectorAll('div')].find((d) => (d.className || '').toString().includes('max-w-7xl'));
  const kids = [...wrap.children];
  out.kids = kids.map((k) => (k.textContent || '').replace(/\s+/g, ' ').slice(0, 30));
  // hide each child in turn
  out.perChild = kids.map((k) => {
    const prev = k.style.display;
    k.style.display = 'none';
    const w = document.body.scrollWidth;
    k.style.display = prev;
    return { hidden: (k.textContent || '').replace(/\s+/g, ' ').slice(0, 24), scrollWWhenHidden: w };
  });
  // hide the header (mobile top bar) too
  const hdr = main.querySelector('header');
  if (hdr) {
    const p = hdr.style.display;
    hdr.style.display = 'none';
    out.whenHeaderHidden = document.body.scrollWidth;
    hdr.style.display = p;
  }
  // deeper: within summary card, hide each child
  const card = kids.find((k) => /Total Net Worth/.test(k.textContent || ''));
  if (card) {
    const inner = [...card.querySelectorAll(':scope > div > div, :scope > div > div > div')];
    out.cardInner = inner.slice(0, 6).map((k) => {
      const prev = k.style.display;
      k.style.display = 'none';
      const w = document.body.scrollWidth;
      k.style.display = prev;
      return { cls: (k.className || '').toString().slice(0, 40), scrollWWhenHidden: w };
    });
  }
  return JSON.stringify(out, null, 1);
})()
