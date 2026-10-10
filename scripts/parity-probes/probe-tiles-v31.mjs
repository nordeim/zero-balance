(() => {
  const rg = document.querySelector('[role=radiogroup]');
  if (!rg) return 'no radiogroup';
  const dump = (el, depth, out) => {
    if (depth > 4 || out.length > 40) return;
    const tag = el.tagName;
    const role = el.getAttribute('role');
    const tb = el.tabIndex;
    const checked = el.getAttribute('aria-checked') !== null ? ' aria-checked=' + el.getAttribute('aria-checked') : '';
    const txt = (el.childNodes.length && [...el.childNodes].every(n => n.nodeType === 3)) ? '"' + el.textContent.trim().slice(0, 12) + '"' : '';
    out.push('  '.repeat(depth) + tag + (role ? ' role=' + role : '') + (tb !== -1 || el.getAttribute('tabindex') !== null ? ' tabindex=' + tb : '') + checked + ' ' + txt);
    [...el.children].forEach(c => dump(c, depth + 1, out));
    return out;
  };
  const out = [];
  dump(rg, 0, out);
  return out.join('\n').slice(0, 1800);
})()
