(() => {
  // empty state under the Liabilities tab panel
  const panel = document.querySelector('[role="tabpanel"][data-state="active"]') || document;
  const h = [...panel.querySelectorAll('h3, h4, p')].find((e) => /No liabilities yet|No assets yet|No items|nothing/i.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'no empty state' });
  const box = h.parentElement;
  const cs = getComputedStyle(box);
  const btn = box.querySelector('button');
  return JSON.stringify({
    heading: (h.textContent || '').trim(),
    boxClasses: box.className.slice(0, 140),
    boxBorder: cs.borderColor, boxBg: cs.backgroundColor, boxRadius: cs.borderRadius, boxBorderW: cs.borderWidth,
    btn: btn ? { text: (btn.textContent || '').trim(), classes: btn.className.slice(0, 150), bg: getComputedStyle(btn).backgroundColor, border: getComputedStyle(btn).borderColor } : null,
  }, null, 1);
})()
