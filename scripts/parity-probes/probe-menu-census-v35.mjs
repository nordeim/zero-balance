(async () => {
  // v35 Surface A: item-card action menu OPEN-STATE structure + initial focus.
  // Census: portal, roles, item count, initial focus, hasFocus gate.
  const menu = document.querySelector('[role="menu"]');
  if (!menu) return JSON.stringify({menuOpen: false});
  const items = [...menu.querySelectorAll('[role="menuitem"]')];
  const trig = document.activeElement;
  const out = {
    menuOpen: true,
    portal: !document.body.contains(menu) || !!menu.closest('[data-radix-popper-content-wrapper]') || menu.parentElement === document.body,
    role: menu.getAttribute('role'),
    itemCount: items.length,
    itemTexts: items.map(i => i.textContent.trim()),
    initialActive: (document.activeElement?.tagName || 'none') + ':' +
      (document.activeElement?.getAttribute('role') || document.activeElement?.className?.toString?.().split(' ')[0] || ''),
    hasFocus: document.hasFocus(),
    menuClass: (menu.className || '').toString().slice(0, 200),
    itemCls0: (items[0]?.className || '').toString().slice(0, 220),
    itemCls1: (items[1]?.className || '').toString().slice(0, 220),
  };
  return JSON.stringify(out);
})()
