// Session-7: find the mobile networth overflow culprits (in-flow elements past viewport).
(() => {
  const out = { vw: window.innerWidth };
  const main = document.querySelector('main') || document.body;
  const wide = [];
  const walk = (el, depth) => {
    for (const c of el.children) {
      const r = c.getBoundingClientRect();
      const cls = (c.className || '').toString();
      const cs = getComputedStyle(c);
      if (r.width > 0 && r.right > out.vw + 0.5 && !cls.includes('absolute') && cs.position !== 'fixed') {
        wide.push({
          depth,
          tag: c.tagName,
          cls: cls.slice(0, 70),
          w: Math.round(r.width),
          right: Math.round(r.right),
          text: (c.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 30),
          scrollW: c.scrollWidth,
          clientW: c.clientWidth,
        });
      }
      if (depth < 6) walk(c, depth + 1);
    }
  };
  walk(main, 0);
  out.culprits = wide.slice(0, 12);
  return JSON.stringify(out, null, 1);
})()
