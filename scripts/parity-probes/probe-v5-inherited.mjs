// Session-8 (v5): find any VISIBLE text node that renders with an inherited color
// (no explicit color on self or ancestor-with-color-class) — i.e. text whose color
// comes from the body base. If the counts are 0 on both sides, the base-color
// difference (#0a0a0a vs #3f3f3f) never renders.
(() => {
  const out = { bodyColor: getComputedStyle(document.body).color, inherited: [] };
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  let n;
  while ((n = walker.nextNode())) {
    const t = n.textContent.replace(/\s+/g, ' ').trim();
    if (!t || t.length < 2) continue;
    const el = n.parentElement;
    if (!el) continue;
    // skip script/style
    if (/SCRIPT|STYLE/.test(el.tagName)) continue;
    // visibility check
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    const st = getComputedStyle(el);
    if (st.display === 'none' || st.visibility === 'hidden') continue;
    // does the element or any ancestor up to body carry an explicit color?
    let node = el, explicit = false;
    while (node && node !== document.body) {
      const cs2 = getComputedStyle(node);
      // check inline style attribute first (cheap truth)
      const inline = (node.getAttribute && node.getAttribute('style')) || '';
      const cls = (node.className && node.className.toString) ? node.className.toString() : '';
      if (/color/.test(inline) || /text-(white|black|zinc|gray|neutral|slate|red|green|blue|orange|amber|lime|emerald|forest|orangeDark)/.test(cls) || /(^|\s)(color|fill)-/.test(cls)) { explicit = true; break; }
      node = node.parentElement;
    }
    if (!explicit) {
      const key = t.slice(0, 30);
      if (!seen.has(key)) { seen.add(key); out.inherited.push({ t: t.slice(0, 40), tag: el.tagName, color: st.color, where: (el.closest('main,aside,header') || {}).tagName || 'body' }); }
      if (out.inherited.length > 12) break;
    }
  }
  out.count = out.inherited.length;
  return JSON.stringify(out, null, 1);
})()
