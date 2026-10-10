(async () => {
  const overlays = [...document.querySelectorAll('div')].filter(d => getComputedStyle(d).position === 'fixed' && d.querySelector('input, select, textarea, form'));
  if (!overlays.length) return 'no dialog';
  const o = overlays[overlays.length - 1];
  const inputs = [...o.querySelectorAll('input')];
  const amount = inputs.find(i => i.type === 'number');
  if (!amount) return 'no amount';
  amount.focus();
  await new Promise(r => setTimeout(r, 200));
  const readStop = () => {
    const a = document.activeElement;
    if (!a || a === document.body) return 'BODY';
    return a.tagName + (a.getAttribute('role') ? ':' + a.getAttribute('role') : '') + (a.getAttribute('aria-checked') ? '(checked=' + a.getAttribute('aria-checked') + ')' : '') + ' tb=' + a.tabIndex;
  };
  const stops = [readStop()];
  return JSON.stringify({ start: stops[0], note: 'ready for real Tab press' });
})()
