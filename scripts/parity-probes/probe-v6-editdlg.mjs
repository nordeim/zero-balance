// v6: dump the open asset edit dialog — labels, order, chrome, buttons
(() => {
  const dlg = document.querySelector('[role="dialog"]') || [...document.querySelectorAll('div')].find((d) => d.getAttribute('role') === 'dialog');
  if (!dlg) return JSON.stringify({ err: 'no dialog' });
  const cs = (el, p) => getComputedStyle(el)[p];
  const label = (el) => {
    // find the nearest preceding label element or aria-label
    return el.getAttribute('aria-label') || (() => {
      let n = el.closest('div');
      return null;
    })();
  };
  const fields = [...dlg.querySelectorAll('input, textarea, button[role="combobox"], select')].map((f) => {
    const holder = f.closest('div[class*="space-y"], div[class*="grid"], form div');
    // climb to the leaf wrapper that contains a preceding label sibling
    let wrap = f.parentElement;
    let lbl = null;
    for (let i = 0; i < 4 && wrap; i++) {
      const prev = wrap.previousElementSibling;
      if (prev && (prev.tagName === 'LABEL' || prev.querySelector?.('label'))) { lbl = (prev.textContent || '').trim(); break; }
      wrap = wrap.parentElement;
    }
    return {
      tag: f.tagName.toLowerCase(),
      type: f.getAttribute('type'),
      aria: f.getAttribute('aria-label'),
      label: lbl || (f.labels?.[0]?.textContent || '').trim() || null,
      value: (f.value || f.textContent || '').toString().slice(0, 30),
      disabled: f.disabled || f.getAttribute('aria-disabled') === 'true',
      ph: f.getAttribute('placeholder'),
    };
  });
  const btns = [...dlg.querySelectorAll('button')].filter((b) => !b.closest('[role="combobox"]')).map((b) => ({
    text: (b.textContent || '').trim().slice(0, 20),
    aria: b.getAttribute('aria-label'),
    bg: cs(b, 'backgroundImage') !== 'none' ? cs(b, 'backgroundImage').slice(0, 80) : cs(b, 'backgroundColor'),
  }));
  const heading = dlg.querySelector('h1,h2,h3,h4,[class*="text-lg"]');
  return JSON.stringify({ heading: heading?.textContent?.trim(), fields, btns }, null, 1);
})()
