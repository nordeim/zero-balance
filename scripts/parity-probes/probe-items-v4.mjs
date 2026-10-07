// Session-7: items-view structural dump — header, filter card, item cards, badges, buttons.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. Page header: h1 + subtitle + Add button
  const h1 = [...document.querySelectorAll('h1')].find((h) => /Income|Savings|Expenses/i.test(txt(h) || ''));
  if (h1) {
    const hdr = h1.closest('div');
    out.header = {
      h1: txt(h1),
      h1Cls: h1.className,
      sub: h1.nextElementSibling ? txt(h1.nextElementSibling) : null,
      addBtn: (() => {
        const b = [...(hdr ? hdr.querySelectorAll('button') : [])].find((x) => /Add/.test(txt(x) || ''));
        return b ? { text: txt(b), bg: cs(b, 'backgroundImage').slice(0, 90) } : null;
      })(),
    };
  }

  // 2. Filter card
  const search = document.querySelector('input[placeholder*="Search"]');
  if (search) {
    const card = search.closest('div[class*="rounded-2xl"], div[class*="bg-white"]');
    const sel = card ? [...card.querySelectorAll('select')].map((s) => s.getAttribute('aria-label') || s.className.slice(0, 30)) : [];
    out.filterCard = {
      found: !!card,
      cls: card ? card.className.toString().slice(0, 100) : null,
      searchPh: search.placeholder,
      searchCls: search.className.slice(0, 90),
      iconSize: (() => { const s = card ? card.querySelector('svg') : null; return s ? cs(s, 'width') : null; })(),
      selects: sel,
    };
  }

  // 3. Item cards: first card — title, amount, badges, footer, buttons
  const cardEls = [...document.querySelectorAll('div[class*="rounded-2xl"]')].filter((d) => {
    const t = txt(d) || '';
    return /\$/.test(t) && d.querySelector('button') === null ? false : /\$/.test(t) && (d.querySelectorAll('button').length > 0);
  });
  // better: cards with a hover-visible button (Edit) OR with badges
  const itemCards = [...document.querySelectorAll('div[class*="group"]')].filter((d) => /\$[\d.]+/.test(txt(d) || '') && d.querySelectorAll('button').length >= 1);
  const first = itemCards[0];
  if (first) {
    out.itemCard = {
      cls: first.className.toString().slice(0, 110),
      texts: [...first.querySelectorAll('h3,p,span,div')].filter((x) => x.children.length === 0).map(txt).filter(Boolean).slice(0, 10),
      badges: [...first.querySelectorAll('span')].filter((s) => (s.className || '').includes('rounded-full')).map((s) => ({ text: txt(s), bg: cs(s, 'backgroundColor'), color: cs(s, 'color'), border: cs(s, 'borderColor') })),
      buttons: [...first.querySelectorAll('button')].map((b) => ({ text: txt(b) || b.getAttribute('aria-label'), cls: b.className.toString().slice(0, 80) })),
      footerText: (() => { const f = [...first.querySelectorAll('div')].filter((d) => /20\d\d/.test(txt(d) || '')).pop(); return f ? txt(f).slice(0, 60) : null; })(),
    };
  }
  out.cardCount = itemCards.length;

  // 4. Empty state (if no cards)
  if (!itemCards.length) {
    const empty = [...document.querySelectorAll('div')].find((d) => /No |Get started|first/i.test(txt(d) || '') && (d.textContent || '').length < 200 && d.querySelector('button'));
    out.empty = empty ? txt(empty).slice(0, 80) : null;
  }

  return JSON.stringify(out, null, 1);
})()
