// Session-7: networth summary card full HTML dump.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const sumCard = [...document.querySelectorAll('div')].find((d) => {
    const c = (d.className || '').toString();
    return c.includes('rounded-2xl') && /Total Net Worth/i.test(txt(d) || '');
  });
  if (sumCard) {
    out.html = sumCard.outerHTML.replace(/\s+/g, ' ').slice(0, 2600);
    // every leaf with its computed size
    out.leaves = [...sumCard.querySelectorAll('*')].filter((x) => x.children.length === 0 && (txt(x) || '').length > 0).map((x) => ({
      tag: x.tagName,
      text: txt(x).slice(0, 30),
      size: cs(x, 'fontSize'),
      weight: cs(x, 'fontWeight'),
      color: cs(x, 'color'),
    })).slice(0, 14);
  }
  return JSON.stringify(out, null, 1);
})()
