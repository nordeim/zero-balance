// v6: dump the ref's open edit dialog (fixed overlay, no role=dialog)
(() => {
  const fixed = [...document.querySelectorAll('body > div, body > div > div')].filter((d) => getComputedStyle(d).position === 'fixed' && d.textContent.trim().length > 20);
  const overlay = fixed.find((d) => d.querySelector('input, textarea')) || fixed[0];
  if (!overlay) return JSON.stringify({ err: 'no overlay', fixedCount: fixed.length });
  const panel = [...overlay.querySelectorAll('div')].filter((d) => getComputedStyle(d).backgroundColor === 'rgb(255, 255, 255)' && d.querySelector('input')).sort((a, b) => b.getBoundingClientRect().width - a.getBoundingClientRect().width)[0] || overlay;
  const fields = [...panel.querySelectorAll('input, textarea, button[role="combobox"], select')].map((f) => {
    let wrap = f.parentElement, lbl = null;
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
      value: (f.value || f.textContent || '').toString().slice(0, 32),
      disabled: f.disabled === true || f.getAttribute('aria-disabled') === 'true',
      ph: f.getAttribute('placeholder'),
    };
  });
  const btns = [...panel.querySelectorAll('button')].filter((b) => !b.closest('[role="combobox"]') && !b.querySelector('input')).map((b) => {
    const cs = getComputedStyle(b);
    return { text: (b.textContent || '').trim().slice(0, 22), aria: b.getAttribute('aria-label'), bg: cs.backgroundImage !== 'none' ? cs.backgroundImage.slice(0, 90) : cs.backgroundColor, border: cs.borderColor };
  });
  const heading = panel.querySelector('h1,h2,h3,h4');
  return JSON.stringify({ heading: heading?.textContent?.trim(), fieldCount: fields.length, fields, btnCount: btns.length, btns }, null, 1);
})()
