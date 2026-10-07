// Session-8 (v5): networth tabs geometry — list width, gap to next sibling, trigger widths.
(() => {
  const out = {};
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const tabs = [...document.querySelectorAll('main button')].filter((b) => /^(Assets|Liabilities)$/.test(txt(b) || ''));
  if (tabs.length) {
    const list = tabs[0].closest('[role="tablist"]');
    const lr = list.getBoundingClientRect();
    out.list = { x: Math.round(lr.x), y: Math.round(lr.y), w: Math.round(lr.width), h: Math.round(lr.height) };
    out.triggers = tabs.map((t) => { const r = t.getBoundingClientRect(); return { t: txt(t), x: Math.round(r.x), w: Math.round(r.width), h: Math.round(r.height) }; });
    // gap below list: next element top
    const next = list.nextElementSibling;
    if (next) {
      const nr = next.getBoundingClientRect();
      out.gapBelowList = Math.round(nr.top - lr.bottom);
      out.nextElement = { tag: next.tagName, cls: (next.className || '').toString().replace(/\s+/g, ' ').slice(0, 80), text: (txt(next) || '').slice(0, 40) };
    }
    // parent of list
    const parent = list.parentElement;
    out.parent = { tag: parent.tagName, cls: (parent.className || '').toString().replace(/\s+/g, ' ').slice(0, 90) };
  }
  return JSON.stringify(out, null, 1);
})()
