(async () => {
  const m = document.querySelector('[role="menu"]');
  if (!m) return JSON.stringify({menuOpen: false});
  const items = [...m.querySelectorAll('[role="menuitem"]')];
  return JSON.stringify({
    menuWrapper: m.parentElement ? (m.parentElement.tagName + '.' + (m.parentElement.getAttribute('data-radix-popper-content-wrapper') !== null ? 'popper' : '')) : null,
    itemClasses: items.map(i => (i.className || '').toString()),
  });
})()
