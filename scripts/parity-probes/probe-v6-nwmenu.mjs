(() => {
  const menu = document.querySelector('[role="menu"]');
  if (!menu) return JSON.stringify({ err: 'no menu' });
  const cs = (el, p) => getComputedStyle(el)[p];
  return JSON.stringify({
    contentClasses: menu.className,
    border: cs(menu, 'borderColor'), radius: cs(menu, 'borderRadius'), shadow: cs(menu, 'boxShadow').slice(0, 70),
    bg: cs(menu, 'backgroundColor'), minW: cs(menu, 'minWidth'), padding: cs(menu, 'padding'),
    items: [...menu.querySelectorAll('[role="menuitem"]')].map((m) => ({
      text: (m.textContent || '').trim(),
      color: cs(m, 'color'), font: cs(m, 'fontSize') + '/' + cs(m, 'fontWeight'),
      svg: m.querySelectorAll('svg').length,
      classes: m.className.slice(0, 160),
    })),
  }, null, 1);
})()
