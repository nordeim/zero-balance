(async () => {
  const layer = document.querySelector('g.recharts-layer.recharts-pie, .recharts-pie');
  if (!layer) return 'no layer';
  const tip = () => {
    const t = document.querySelector('.recharts-tooltip-wrapper');
    if (!t) return { visible: false, text: '' };
    const hasText = t.textContent.trim().length > 0;
    const cs = getComputedStyle(t);
    return { visible: hasText && cs.visibility !== 'hidden' && cs.opacity !== '0', text: hasText ? t.textContent.trim().slice(0, 22) : '' };
  };
  const active = () => {
    const a = document.activeElement;
    if (!a || a === document.body) return 'BODY';
    return a.tagName + '.' + (a.getAttribute('class') || '').replace('recharts-layer ', '').replace('recharts-zIndex-layer ', '').slice(0, 25) + (a.getAttribute('tabindex') !== null ? '[tb=' + a.getAttribute('tabindex') + ']' : '');
  };
  const log = [];
  // settle the donut fully first (animation!)
  await new Promise(r => setTimeout(r, 2000));
  const l2 = document.querySelector('g.recharts-layer.recharts-pie, .recharts-pie');
  l2.focus();
  await new Promise(r => setTimeout(r, 400));
  log.push({ step: 'after-layer.focus', active: active(), tip: tip() });
  for (const key of ['ArrowDown', 'ArrowRight', 'ArrowRight', 'ArrowLeft', 'Enter', 'Escape']) {
    const el = document.activeElement === document.body ? l2 : document.activeElement;
    el.dispatchEvent(new KeyboardEvent('keydown', { key, bubbles: true, cancelable: true }));
    await new Promise(r => setTimeout(r, 450));
    log.push({ step: 'after-' + key, active: active(), tip: tip() });
  }
  return JSON.stringify(log, null, 1);
})()
