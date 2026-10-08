// probe-v15-loading2.mjs — the reference's data-fetch spinner, full chrome:
// the spinner element + its container chain (positioning, centering) + the
// animation + when it disappears.
(() => {
  const out = {};
  const find = () => [...document.querySelectorAll('div, span')].find((el) => {
    const cs = getComputedStyle(el);
    return cs.animationName === 'spin' && el.getBoundingClientRect().width > 0;
  });
  const sp = find();
  if (!sp) return JSON.stringify({ spinner: null, note: 'gone — data landed?' });
  const r = sp.getBoundingClientRect();
  const cs = getComputedStyle(sp);
  out.spinner = {
    tag: sp.tagName.toLowerCase(),
    w: Math.round(r.width), h: Math.round(r.height),
    x: Math.round(r.x), y: Math.round(r.y),
    border: cs.borderTopWidth + ' ' + cs.borderTopColor + ' / ' + cs.borderRightColor + ' / ' + cs.borderBottomColor + ' / ' + cs.borderLeftColor,
    radius: cs.borderRadius,
    anim: cs.animationName + ' ' + cs.animationDuration + ' ' + cs.animationTimingFunction + ' ' + cs.animationIterationCount,
  };
  // container chain (up to 5 hops)
  out.chain = [];
  let n = sp.parentElement;
  for (let i = 0; i < 5 && n && n !== document.body; i++) {
    const c = getComputedStyle(n);
    const rr = n.getBoundingClientRect();
    out.chain.push({
      tag: n.tagName.toLowerCase(),
      cls: (n.getAttribute('class') || '').slice(0, 70),
      display: c.display, jc: c.justifyContent, ai: c.alignItems,
      w: Math.round(rr.width), h: Math.round(rr.height),
      minH: c.minHeight, padding: c.padding,
    });
    n = n.parentElement;
  }
  // what sibling content exists beside it?
  out.docHasData = /\$[\d,]+\.\d{2}/.test(document.body.textContent);
  return JSON.stringify(out, null, 1);
})()
