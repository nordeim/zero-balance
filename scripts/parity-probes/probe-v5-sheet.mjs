// Session-8 (v5): sheet state — width + overlay + which links visible.
(() => {
  const out = {};
  const overlay = [...document.querySelectorAll('div')].find((d) => {
    const c = (d.className || '').toString();
    return /fixed/.test(c) && /bg-black|background-color:\s*rgba\(0,\s*0,\s*0/.test(c + (d.getAttribute('style') || '')) && d.getBoundingClientRect().width > 300;
  });
  out.overlayOpen = !!overlay;
  const sheet = [...document.querySelectorAll('div')].find((d) => {
    const c = (d.className || '').toString();
    return /fixed/.test(c) && d.getBoundingClientRect().width > 200 && d.getBoundingClientRect().width < 320 && d.textContent.includes('Dashboard');
  });
  if (sheet) {
    const r = sheet.getBoundingClientRect();
    out.sheet = { x: Math.round(r.x), w: Math.round(r.width), h: Math.round(r.height) };
    const link = [...sheet.querySelectorAll('a')].find((a) => a.textContent.trim() === 'Income');
    out.sheetLink = link ? { y: Math.round(link.getBoundingClientRect().y), w: Math.round(link.getBoundingClientRect().width) } : null;
  }
  return JSON.stringify(out, null, 1);
})()
