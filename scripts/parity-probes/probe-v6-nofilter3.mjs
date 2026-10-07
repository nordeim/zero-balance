(() => {
  const h = [...document.querySelectorAll('h3, h4')].find((e) => /No income items yet/i.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'none' });
  let box = h.parentElement;
  for (let i = 0; i < 3; i++) { const c = box.className || ''; if (/rounded/.test(c)) break; box = box.parentElement; }
  const cs = getComputedStyle(box);
  const btn = box.querySelector('button');
  const bcs = btn ? getComputedStyle(btn) : null;
  return JSON.stringify({
    heading: (h.textContent || '').trim(),
    boxClasses: box.className.slice(0, 110),
    border: cs.borderColor, bw: cs.borderWidth, radius: cs.borderRadius, py: cs.paddingTop, bg: cs.backgroundColor,
    desc: (box.querySelector('p')?.textContent || '').trim(),
    btn: btn ? { text: (btn.textContent || '').trim(), bg: ((bcs.backgroundImage !== 'none' ? bcs.backgroundImage : bcs.backgroundColor) + '').slice(0, 70), color: bcs.color } : null,
    svgs: [...box.querySelectorAll('svg')].filter((s) => !s.closest('button')).length,
  }, null, 1);
})()
