(async () => {
  // dump the fixed overlays + their structure shallowly
  const overlays = [...document.querySelectorAll('div')].filter(d => {
    const cs = getComputedStyle(d);
    return cs.position === 'fixed' && d.querySelector('input, select, textarea, form');
  });
  if (!overlays.length) return 'no overlay with form';
  const o = overlays[overlays.length - 1];
  const describe = (el, depth) => {
    const cs = getComputedStyle(el);
    const tag = el.tagName;
    const txt = (el.childNodes.length === 1 && el.childNodes[0].nodeType === 3) ? el.textContent.trim().slice(0, 20) : '';
    const focusable = /^(BUTTON|INPUT|SELECT|TEXTAREA|A)$/.test(tag) || (el.getAttribute('tabindex') === '0');
    return '  '.repeat(depth) + tag + (txt ? ' "' + txt + '"' : '') + (focusable ? ' [FOCUSABLE]' : '') + (el.getAttribute('role') ? ' role=' + el.getAttribute('role') : '');
  };
  const lines = [];
  const walk = (el, depth) => {
    if (depth > 6 || lines.length > 60) return;
    lines.push(describe(el, depth));
    [...el.children].forEach(c => walk(c, depth + 1));
  };
  walk(o, 0);
  return lines.join('\n').slice(0, 2500);
})()
