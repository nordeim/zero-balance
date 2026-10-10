(async () => {
  const readState = () => {
    const opts = [...document.querySelectorAll('[role=option]')];
    const highlighted = opts.find(o => o.getAttribute('data-highlighted') !== null || o.getAttribute('aria-selected') === 'true' || (document.activeElement && o.contains(document.activeElement)));
    const lb = document.querySelector('[role=listbox]');
    return {
      open: !!lb,
      hl: highlighted ? opts.indexOf(highlighted) : -1,
      hlText: highlighted?.textContent?.trim().slice(0, 14),
      hlAttr: highlighted ? (highlighted.getAttribute('data-highlighted') !== null ? 'data-highlighted' : (highlighted.getAttribute('aria-selected') === 'true' ? 'aria-selected' : 'activeElement')) : null,
      active: (document.activeElement?.textContent || '').trim().slice(0, 14),
      activeTag: document.activeElement?.tagName,
    };
  };
  const out = [];
  out.push({ step: 'open', ...readState() });
  return JSON.stringify(out);
})()
