// Session-7: networth tab-panel asset card dump.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const panel = document.querySelector('[data-state="active"][role="tabpanel"]') || document.querySelector('[role="tabpanel"]');
  if (panel) {
    // count line at top of panel
    const head = [...panel.querySelectorAll('div,p,span')].filter((x) => /items? ·/.test(txt(x) || '')).slice(0, 2).map((x) => ({ text: txt(x), cls: x.className.toString().slice(0, 60) }));
    out.panelHead = head;
    // group headers
    out.groups = [...panel.querySelectorAll('h3')].map((h) => ({ text: txt(h), cls: h.className.toString().slice(0, 60), color: cs(h, 'color') }));
    // first card
    const card = panel.querySelector('div[class*="rounded-xl"]');
    if (card) {
      out.card = {
        cls: card.className.toString().slice(0, 110),
        html: card.outerHTML.replace(/\s+/g, ' ').slice(0, 1100),
      };
    }
    // Add button in panel
    const addBtn = [...panel.querySelectorAll('button')].find((b) => /Add Asset|Add Liability/.test(txt(b) || ''));
    out.addBtn = addBtn ? { text: txt(addBtn), bg: cs(addBtn, 'backgroundImage').slice(0, 90) } : null;
  }
  return JSON.stringify(out, null, 1);
})()
