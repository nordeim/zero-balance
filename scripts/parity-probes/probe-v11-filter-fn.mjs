// probe-v11-filter-fn.mjs — set search value and report visible item cards
(() => {
  const q = window.__FILTER_Q || '';
  const search = document.querySelector('input[placeholder*="Search" i]');
  if (!search) return 'no search input';
  // set value as React would
  const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
  setter.call(search, q);
  search.dispatchEvent(new Event('input', { bubbles: true }));
  return new Promise(resolve => setTimeout(() => {
    const out = { q };
    // item cards: elements with a $ amount and reasonable size
    const cards = [...document.querySelectorAll('div')].filter(el => {
      const r = el.getBoundingClientRect(); const t = (el.textContent || '');
      return r.width > 200 && r.width < 900 && r.height > 80 && r.height < 400 && /\$[\d,]+\.\d{2}/.test(t) && el.querySelectorAll('button').length > 0 && t.length < 300;
    });
    out.matchingCards = cards.length;
    out.cardTitles = cards.map(c => (c.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40));
    // empty state visible?
    const empty = [...document.querySelectorAll('div, p')].filter(el => {
      const t = (el.textContent || '').trim(); const r = el.getBoundingClientRect();
      return /No .* found|no items|Nothing here|No results/i.test(t) && t.length < 120 && r.height > 0;
    });
    out.emptyState = empty.length ? empty[0].textContent.trim().slice(0, 60) : null;
    resolve(JSON.stringify(out, null, 1));
  }, 500));
})()
