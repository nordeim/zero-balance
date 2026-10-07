// Session-8 (v5): sidebar rail divider color.
(() => {
  const rail = document.querySelector('aside') || [...document.querySelectorAll('div')].find((d) => (d.className || '').toString().includes('w-64') && d.textContent.includes('Dashboard'));
  if (!rail) return JSON.stringify({ error: 'no rail' });
  const cs = getComputedStyle(rail);
  let divider = 'none';
  if (cs.borderRightWidth !== '0px') divider = cs.borderRightColor;
  else if (cs.borderLeftWidth !== '0px') divider = cs.borderLeftColor;
  return JSON.stringify({ divider, w: Math.round(rail.getBoundingClientRect().width) });
})()
