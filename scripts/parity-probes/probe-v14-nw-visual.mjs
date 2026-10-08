// probe-v14-nw-visual.mjs — verify the VLM-flagged net-worth diffs in the DOM:
// (1) header icon next to the h1, (2) summary-card divider above the ratio row,
// (3) the ratio row's icon, (4) tab icons in the Assets/Liabilities tab buttons.
(() => {
  const out = {};
  // (1) header row: find the visible h1 (Net Worth) and enumerate its siblings
  const h1 = [...document.querySelectorAll('main h1')].find(h => h.getBoundingClientRect().height > 0);
  if (h1) {
    const row = h1.parentElement;
    out.h1 = h1.textContent.trim();
    out.headerRowChildren = [...row.children].map(c => {
      const r = c.getBoundingClientRect();
      const cs = getComputedStyle(c);
      return { tag: c.tagName, text: c.textContent.trim().slice(0, 20), w: Math.round(r.width), h: Math.round(r.height), bg: cs.backgroundColor, radius: cs.borderRadius, display: cs.display };
    });
    // any svg in the header row?
    const svgs = [...row.querySelectorAll('svg')].filter(s => s.getBoundingClientRect().width > 0);
    out.headerSvgCount = svgs.length;
    out.headerSvgs = svgs.map(s => { const r = s.getBoundingClientRect(); const cs = getComputedStyle(s.closest('div') || s); return { w: Math.round(r.width), h: Math.round(r.height), containerBg: cs.backgroundColor, containerW: Math.round(s.closest('div')?.getBoundingClientRect().width || 0), containerH: Math.round(s.closest('div')?.getBoundingClientRect().height || 0), containerRadius: (s.closest('div') ? getComputedStyle(s.closest('div')).borderRadius : null) }; });
  }
  // (4) tab icons
  const tabs = [...document.querySelectorAll('[role="tab"]')].filter(t => t.getBoundingClientRect().height > 0);
  out.tabSvgs = tabs.map(t => {
    const svgs = [...t.querySelectorAll('svg')].filter(s => s.getBoundingClientRect().width > 0);
    return { text: t.textContent.trim().slice(0, 12), svgCount: svgs.length, svgW: svgs.map(s => Math.round(s.getBoundingClientRect().width)) };
  });
  // (2) summary card: find the ratio row and look for a border-top divider above it
  const ratioEl = [...document.querySelectorAll('main *')].find(e => /Asset to Liability Ratio/i.test(e.textContent) && e.children.length < 6 && e.getBoundingClientRect().height > 10 && e.getBoundingClientRect().height < 60);
  if (ratioEl) {
    let n = ratioEl;
    // walk up to find an element with border-top
    let hops = 0;
    while (n && n !== document.body && hops < 4) {
      const cs = getComputedStyle(n);
      if (cs.borderTopWidth !== '0px' || cs.borderBottomWidth !== '0px') {
        out.divider = { hops, tag: n.tagName, top: cs.borderTopWidth + ' ' + cs.borderTopColor, bottom: cs.borderBottomWidth + ' ' + cs.borderBottomColor };
        break;
      }
      n = n.parentElement; hops++;
    }
    if (!out.divider) out.divider = 'NO border within 4 hops of ratio row';
    // (3) the icon next to the ratio value
    const svgs = [...ratioEl.querySelectorAll('svg')].filter(s => s.getBoundingClientRect().width > 0);
    out.ratioIcons = svgs.map(s => { const r = s.getBoundingClientRect(); return { w: Math.round(r.width), h: Math.round(r.height), stroke: getComputedStyle(s).stroke.slice(0, 40) }; });
  }
  return JSON.stringify(out, null, 1);
})()
