// probe-v11-verify-fix2.mjs — empty heading 20px + Save focus ring + calculator variants + hover
(() => {
  const out = { url: location.pathname };
  // filter to zero → empty heading
  const search = document.querySelector('input[placeholder*="Search" i]');
  if (search) {
    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
    setter.call(search, 'zzz');
    search.dispatchEvent(new Event('input', { bubbles: true }));
  }
  return new Promise(resolve => setTimeout(() => {
    const h = [...document.querySelectorAll('main h3, main h4')].find(x => /No income items yet/.test(x.textContent || ''));
    if (h) { const cs = getComputedStyle(h); out.emptyHeading = { fs: cs.fontSize, fw: cs.fontWeight, lh: cs.lineHeight }; }
    resolve(JSON.stringify(out));
  }, 500));
})()
