// probe-v11-verify-fix.mjs — the v11 fix verification: empty heading 20px, Add button icon/width/shadow
(() => {
  const out = { url: location.pathname };
  // 1. The topbar Add button: icon 16, width, rest shadow
  const add = [...document.querySelectorAll('button')].filter(b =>
    /^Add Income/.test((b.textContent || '').trim()) && b.getBoundingClientRect().top < 120 && b.getBoundingClientRect().height > 0)[0];
  if (add) {
    const svg = add.querySelector('svg'); const r = add.getBoundingClientRect(); const cs = getComputedStyle(add);
    out.addBtn = { w: Math.round(r.width), svgW: svg ? Math.round(svg.getBoundingClientRect().width) : null, shadow: cs.boxShadow, opacity: cs.opacity };
  }
  return JSON.stringify(out, null, 1);
})()
