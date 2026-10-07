// Session-8 (v5): is a closed dialog still mounted/visible/blocking?
(() => {
  const out = {};
  const h = [...document.querySelectorAll('h2')].find((x) => /Add Budget Item/.test(x.textContent || ''));
  if (h) {
    const r = h.getBoundingClientRect();
    const cs = getComputedStyle(h);
    out.heading = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height), display: cs.display, visibility: cs.visibility, opacity: cs.opacity };
    // climb to the fixed overlay
    let node = h;
    while (node && node !== document.body) {
      const c = (node.className || '').toString();
      if (c.includes('fixed')) {
        const rr = node.getBoundingClientRect();
        const ncs = getComputedStyle(node);
        out.overlay = { cls: c.slice(0, 80), state: node.getAttribute('data-state'), w: Math.round(rr.width), h: Math.round(rr.height), display: ncs.display, visibility: ncs.visibility, pointerEvents: ncs.pointerEvents, opacity: ncs.opacity, parent: (node.parentElement && node.parentElement.id) || (node.parentElement && node.parentElement.className || '').toString().slice(0, 40) };
        break;
      }
      node = node.parentElement;
    }
  } else {
    out.heading = null;
  }
  // count fixed overlays in body
  out.fixedDivs = [...document.querySelectorAll('body > div, #root > div, body > [data-state], #root [data-state]')].filter((d) => (d.className || '').toString().includes('fixed') && d.getBoundingClientRect().width > 100).length;
  return JSON.stringify(out, null, 1);
})()
