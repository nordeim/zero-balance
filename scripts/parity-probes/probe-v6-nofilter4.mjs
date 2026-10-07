(() => {
  const h = [...document.querySelectorAll('h3, h4')].find((e) => /No income items yet/i.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'none' });
  let box = h.closest('[class*="rounded-xl"], [class*="rounded-2xl"]') || h.parentElement;
  const cs = getComputedStyle(box);
  const p = [...box.querySelectorAll('p')].map((x) => (x.textContent || '').trim()).filter(Boolean);
  const btn = box.querySelector('button');
  const bcs = btn ? getComputedStyle(btn) : null;
  return JSON.stringify({
    heading: (h.textContent || '').trim(),
    boxClasses: box.className.slice(0, 110),
    border: cs.borderColor, radius: cs.borderRadius, py: cs.paddingTop, bg: cs.backgroundColor,
    p, btn: btn ? { text: (btn.textContent || '').trim(), bg: ((bcs.backgroundImage !== 'none' ? bcs.backgroundImage : bcs.backgroundColor) + '').slice(0, 75) } : null,
    svgs: [...box.querySelectorAll('svg')].filter((s) => !s.closest('button')).length,
  }, null, 1);
})()
