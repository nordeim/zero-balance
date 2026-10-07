// Session-8 (v5): full class lists — networth TabsList container + active/inactive triggers.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const tabs = [...document.querySelectorAll('main button')].filter((b) => /^(Assets|Liabilities)$/.test(txt(b) || ''));
  if (tabs.length) {
    out.triggerCls = (tabs[0].className || '').toString();
    out.triggerHtml = tabs[0].outerHTML.replace(/\s+/g, ' ').slice(0, 500);
    const list = tabs[0].closest('[role="tablist"]');
    if (list) {
      out.listCls = (list.className || '').toString();
      out.listBg = cs(list, 'backgroundColor');
      out.listPad = cs(list, 'padding');
      out.listRadius = cs(list, 'borderRadius');
      out.listH = Math.round(list.getBoundingClientRect().height);
    }
  }
  return JSON.stringify(out, null, 1);
})()
