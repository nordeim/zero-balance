(() => {
  // find any element containing the "Save Asset" button text
  const btn = [...document.querySelectorAll('button')].find((b) => /Save Asset/.test(b.textContent || ''));
  if (!btn) return JSON.stringify({ err: 'no save asset button' });
  // climb to a large white panel
  let panel = btn;
  while (panel.parentElement && panel.getBoundingClientRect().width < 300) panel = panel.parentElement;
  const r = panel.getBoundingClientRect();
  const cs = getComputedStyle(panel);
  const fields = [...panel.querySelectorAll('input, textarea, button[role="combobox"]')].map((f) => {
    let wrap = f.parentElement, lbl = null;
    for (let i = 0; i < 4 && wrap; i++) {
      const prev = wrap.previousElementSibling;
      if (prev && (prev.tagName === 'LABEL' || prev.querySelector?.('label'))) { lbl = (prev.textContent || '').trim(); break; }
      wrap = wrap.parentElement;
    }
    return {
      tag: f.tagName.toLowerCase(),
      type: f.getAttribute('type'),
      label: lbl || (f.labels?.[0]?.textContent || '').trim() || null,
      value: (f.value || f.textContent || '').toString().slice(0, 32),
      disabled: f.disabled === true || f.getAttribute('aria-disabled') === 'true',
      ph: f.getAttribute('placeholder'),
    };
  });
  return JSON.stringify({ panelW: r.width, panelBg: cs.backgroundColor, fields }, null, 1);
})()
