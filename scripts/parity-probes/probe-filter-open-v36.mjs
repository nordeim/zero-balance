// probe-filter-open-v36.mjs — v36 Surface B: open the CATEGORY filter Select on
// /income via the trigger (pointerdown family) and read the fresh-open state:
// the listbox roles, the options, which option carries the highlight (:focus),
// and the aria state of the trigger. The reference's filter-card Selects were
// never measured (v34 covered only the calculator dialog's frequency instance).
(async () => {
  const vis = (el) => el && el.getBoundingClientRect().height > 0;
  const triggers = [...document.querySelectorAll('[role="combobox"], button')].filter((b) => {
    if (b.getAttribute('role') === 'combobox') return vis(b);
    return vis(b) && b.querySelector('svg.lucide-chevron-down, svg[class*="chevron"]') && b.closest('main');
  });
  if (!triggers.length) return JSON.stringify({ error: 'no triggers', url: location.pathname });
  const t = triggers[0];
  const tr = t.getBoundingClientRect();
  const triggerInfo = {
    tag: t.tagName.toLowerCase(), role: t.getAttribute('role'),
    text: t.textContent.trim().slice(0, 24),
    w: Math.round(tr.width), h: Math.round(tr.height),
    ariaExpanded: t.getAttribute('aria-expanded'),
    ariaHasPopup: t.getAttribute('aria-haspopup'),
    ariaControls: t.getAttribute('aria-controls'),
  };
  // open via the pointer family (Radix Select triggers open on pointerdown)
  t.dispatchEvent(new PointerEvent('pointerdown', { bubbles: true, pointerId: 1 }));
  t.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
  t.click();
  await new Promise(r => setTimeout(r, 700));
  const lb = document.querySelector('[role="listbox"]');
  if (!lb) return JSON.stringify({ triggerInfo, opened: false });
  const opts = [...lb.querySelectorAll('[role="option"]')];
  const readOpt = (o) => {
    const c = getComputedStyle(o);
    const r2 = o.getBoundingClientRect();
    return {
      t: o.textContent.trim().slice(0, 18),
      hl: o.getAttribute('data-highlighted'),
      sel: o.getAttribute('aria-selected'),
      focusMatch: o.matches(':focus'),
      bg: c.backgroundColor, color: c.color,
      h: Math.round(r2.height),
    };
  };
  return JSON.stringify({
    triggerInfo,
    opened: true,
    hasFocus: document.hasFocus(),
    active: document.activeElement === lb ? 'LISTBOX' : (document.activeElement.getAttribute('role') || document.activeElement.tagName) + ':' + (document.activeElement.textContent || '').trim().slice(0, 10),
    triggerExpanded: t.getAttribute('aria-expanded'),
    optionCount: opts.length,
    opts: opts.slice(0, 6).map(readOpt),
  });
})()
