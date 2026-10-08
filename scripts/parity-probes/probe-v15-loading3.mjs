// probe-v15-loading3.mjs — reconcile the spinner census: dump EVERY element
// with a spin animation (class + computed box + border), plus the fixed
// overlay census, right after navigation.
(() => {
  const out = { spinners: [], fixedOverlays: [] };
  for (const el of document.querySelectorAll('body *')) {
    if (!el.isConnected) continue;
    const cs = getComputedStyle(el);
    if (cs.animationName === 'spin' && el.getBoundingClientRect().width > 0) {
      const r = el.getBoundingClientRect();
      out.spinners.push({
        tag: el.tagName.toLowerCase(),
        cls: el.getAttribute('class'),
        w: Math.round(r.width), h: Math.round(r.height),
        borderW: [cs.borderTopWidth, cs.borderRightWidth, cs.borderBottomWidth, cs.borderLeftWidth],
        borderTopColor: cs.borderTopColor,
        radius: cs.borderRadius,
        dur: cs.animationDuration,
      });
    }
    if (cs.position === 'fixed' && ((el.getAttribute('class') || '').includes('inset-0')) && el.getBoundingClientRect().width > 100) {
      const cls = el.getAttribute('class') || '';
      if (el.children.length <= 2 && !/toast|sheet|dialog|overlay/i.test(cls)) {
        out.fixedOverlays.push({ cls: cls.slice(0, 60), display: cs.display, children: el.children.length });
      }
    }
  }
  out.dataLoaded = /\$[\d,]+\.\d{2}/.test(document.body.textContent);
  return JSON.stringify(out, null, 1);
})()
