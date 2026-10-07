// Session-7: networth ratio element + group headers precise dump.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // ratio element
  const ratio = [...document.querySelectorAll('p,span,div,h3')].find((x) => {
    const t = txt(x) || '';
    return x.children.length === 0 && (/^∞:1$/.test(t) || /^\d+\.\d+:1$/.test(t));
  });
  if (ratio) {
    out.ratio = {
      text: txt(ratio),
      tag: ratio.tagName,
      cls: ratio.className.toString(),
      size: cs(ratio, 'fontSize'),
      weight: cs(ratio, 'fontWeight'),
      lineHeight: cs(ratio, 'lineHeight'),
    };
    // its label sibling
    out.ratioLabel = ratio.previousElementSibling ? { text: txt(ratio.previousElementSibling), cls: ratio.previousElementSibling.className.toString().slice(0, 60) } : null;
  }

  // net worth figure (big number)
  const bigNum = [...document.querySelectorAll('p,span,h2,h3,div')].filter((x) => x.children.length === 0 && /^\$[\d,]+\.\d{2}$/.test(txt(x) || ''));
  out.bigNums = bigNum.slice(0, 4).map((x) => ({ text: txt(x), size: cs(x, 'fontSize'), weight: cs(x, 'fontWeight') }));

  // group headers in the active tab panel: find capitalize headers
  const panel = [...document.querySelectorAll('div')].filter((d) => (d.className || '').includes('capitalize')).map((d) => txt(d));
  out.capitalizeEls = panel.slice(0, 6);

  // alternate: h3s inside main
  const main = document.querySelector('main');
  if (main) {
    out.mainH3s = [...main.querySelectorAll('h3')].map((h) => ({ text: txt(h).slice(0, 30), cls: h.className.toString().slice(0, 70) })).slice(0, 8);
    out.mainH4s = [...main.querySelectorAll('h4')].map((h) => ({ text: txt(h).slice(0, 30) })).slice(0, 8);
  }

  return JSON.stringify(out, null, 1);
})()
