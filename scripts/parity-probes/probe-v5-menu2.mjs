// Session-8 (v5): menu item hover mechanism — does hovering apply focus/highlight?
(() => {
  const out = {};
  const items = [...document.querySelectorAll('[role="menuitem"]')];
  if (!items.length) return JSON.stringify({ error: 'menu not open' });
  out.itemCls = (items[0].className || '').toString().slice(0, 160);
  out.hasFocusStyles = /focus:bg-accent/.test(out.itemCls);
  out.hasDataHighlighted = /data-\[highlighted\]/.test(out.itemCls);
  return JSON.stringify(out, null, 1);
})()
