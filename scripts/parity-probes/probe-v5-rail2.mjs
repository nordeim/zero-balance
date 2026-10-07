// Session-8 (v5): rail divider — climb from a nav link to the rail container.
(() => {
  const link = [...document.querySelectorAll('a')].find((a) => a.textContent.trim() === 'Dashboard' && a.getBoundingClientRect().width > 50);
  if (!link) return JSON.stringify({ error: 'no link' });
  let rail = link;
  for (let i = 0; i < 10; i++) {
    const p = rail.parentElement;
    if (!p || p === document.body) break;
    rail = p;
    const r = rail.getBoundingClientRect();
    if (Math.round(r.width) === 256 && r.height > 400) break;
  }
  const cs = getComputedStyle(rail);
  let divider = 'none', side = 'none';
  if (cs.borderRightWidth !== '0px') { divider = cs.borderRightColor; side = 'right ' + cs.borderRightWidth; }
  else if (cs.borderLeftWidth !== '0px') { divider = cs.borderLeftColor; side = 'left ' + cs.borderLeftWidth; }
  return JSON.stringify({ divider, side, w: Math.round(rail.getBoundingClientRect().width), cls: (rail.className || '').toString().slice(0, 60) });
})()
