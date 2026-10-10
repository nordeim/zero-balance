// v32: the net-worth dropdown menu keyboard census — click-open structure.
// Run with the networth page open: bash scripts/parity-probes/run-probe.sh <session> probe-nw-menu-v32.mjs
(() => {
  const menu = document.querySelector('[role=menu]');
  if (!menu) return JSON.stringify({ menuOpen: false });
  const items = [...menu.querySelectorAll('[role=menuitem]')];
  return JSON.stringify({
    menuOpen: true,
    focused: { tag: document.activeElement.tagName, role: document.activeElement.getAttribute('role'), tabindex: document.activeElement.tabIndex },
    items: items.map(i => ({ text: i.textContent.trim().slice(0, 20), tabindex: i.tabIndex, highlighted: i.getAttribute('data-highlighted') !== null }))
  });
})()
