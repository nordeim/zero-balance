// probe-v11-verify-fix3.mjs — Save focus ring + calculator variants + hover on the clone
(() => {
  const out = {};
  // open the Add Income dialog
  const add = [...document.querySelectorAll('button')].filter(b =>
    /^Add Income/.test((b.textContent || '').trim()) && b.getBoundingClientRect().top < 120 && b.getBoundingClientRect().height > 0)[0];
  if (!add) return 'no add button';
  // reset the search first (the page is filtered to zzz)
  const search = document.querySelector('input[placeholder*="Search" i]');
  if (search) {
    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
    setter.call(search, '');
    search.dispatchEvent(new Event('input', { bubbles: true }));
  }
  return new Promise(resolve => setTimeout(() => {
    add.click();
    setTimeout(() => {
      const dlg = document.querySelector('[role="dialog"]');
      if (!dlg) { resolve('no dialog'); return; }
      const save = [...dlg.querySelectorAll('button')].find(x => (x.textContent || '').trim() === 'Save Item');
      if (save) {
        save.focus({ focusVisible: true });
        const cs = getComputedStyle(save);
        out.saveFocus = {
          shadow: cs.boxShadow,
          outline: cs.outlineStyle + '/' + cs.outlineWidth + '/' + cs.outlineColor,
          offset: cs.outlineOffset
        };
      }
      resolve(JSON.stringify(out, null, 1));
    }, 800);
  }, 400));
})()
