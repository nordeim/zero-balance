// probe-v15-select-kb.mjs — the filter-card Select KEYBOARD flow (unmeasured):
// focus the first select trigger (Category), ArrowDown to open + highlight,
// capture the open state (roles, active option, geometry), Enter to select.
// Run on /income. Returns the state after each step.
(() => {
  const out = {};
  const vis = (el) => el && el.getBoundingClientRect().height > 0;
  // find select triggers: role combobox or button with chevron in the filter card
  const triggers = [...document.querySelectorAll('[role="combobox"], button')].filter((b) => {
    if (b.getAttribute('role') === 'combobox') return vis(b);
    return vis(b) && b.querySelector('svg.lucide-chevron-down, svg[class*="chevron"]') && b.closest('main');
  });
  out.triggerCount = triggers.length;
  const t = triggers[0];
  if (!t) return JSON.stringify(out);
  const tr = t.getBoundingClientRect();
  out.trigger = { tag: t.tagName.toLowerCase(), role: t.getAttribute('role'), text: t.textContent.trim().slice(0, 20), w: Math.round(tr.width), h: Math.round(tr.height), ariaExpanded: t.getAttribute('aria-expanded'), ariaHasPopup: t.getAttribute('aria-haspopup') };
  t.focus();
  t.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowDown', bubbles: true }));
  return JSON.stringify({ ...out, afterArrowDown: { focused: document.activeElement === t || document.activeElement?.getAttribute('role') === 'combobox', popover: !!document.querySelector('[role="listbox"]'), listboxOptions: [...document.querySelectorAll('[role="option"]')].filter(vis).length } });
})()
