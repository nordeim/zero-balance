// probe-v14-donut-hover.mjs — hover the Spending Breakdown donut sectors and
// capture the tooltip (never measured). Reports sector paths + the tooltip
// content/geometry after a hover at the first sector's midpoint.
(() => {
  const out = {};
  // find the recharts pie sector group
  const sectors = [...document.querySelectorAll('.recharts-pie-sector, path.recharts-pie-sector, [class*="recharts-pie"] path')].filter(p => p.getBoundingClientRect().width > 4);
  out.sectorCount = sectors.length;
  out.sectorFills = sectors.slice(0, 6).map(s => getComputedStyle(s).fill || s.getAttribute('fill'));
  if (sectors.length) {
    const r = sectors[0].getBoundingClientRect();
    out.sector0 = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
    // dispatch hover
    const ev = (type) => new MouseEvent(type, { bubbles: true, cancelable: true, clientX: cx, clientY: cy });
    sectors[0].dispatchEvent(ev('pointermove'));
    sectors[0].dispatchEvent(ev('mouseover'));
    sectors[0].dispatchEvent(ev('mousemove'));
  }
  return JSON.stringify(out, null, 1);
})()
