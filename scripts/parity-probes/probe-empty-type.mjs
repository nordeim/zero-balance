// Session-7: empty-search state dump (run after typing garbage in the search box).
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const main = document.querySelector('main');

  // type into search
  const search = main.querySelector('input[placeholder*="Search"]');
  if (search) {
    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
    setter.call(search, 'zzzzqqq');
    search.dispatchEvent(new Event('input', { bubbles: true }));
  }
  return 'typed';
})()
