(() => {
  const form = [...document.querySelectorAll('form')].find((f) => /Save Asset|Save Liability|Save Changes|Save Item/.test(f.textContent || ''));
  if (!form) return JSON.stringify({ err: 'no form' });
  const save = [...form.querySelectorAll('button[type="submit"], button')].find((b) => /^Save/.test((b.textContent || '').trim()));
  if (!save) return JSON.stringify({ err: 'no save btn' });
  const cs = getComputedStyle(save);
  const svg = save.querySelector('svg');
  return JSON.stringify({
    text: (save.textContent || '').trim(),
    classes: save.className.slice(0, 200),
    bg: cs.backgroundImage.slice(0, 100),
    svgPath: (svg?.querySelector('path')?.getAttribute('d') || svg?.getAttribute('d') || '').slice(0, 60),
    svgCount: save.querySelectorAll('svg').length,
    textColor: cs.color,
  }, null, 1);
})()
