// Session-7: page outline — main children with headers.
(() => {
  const out = {};
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const outline = (root, depth, maxDepth) => {
    if (depth > maxDepth) return [];
    return [...root.children].flatMap((el) => {
      const t = txt(el) || '';
      const head = el.querySelector('h1,h2,h3,h4');
      return [{
        depth,
        tag: el.tagName,
        cls: (el.className || '').toString().split(' ').slice(0, 4).join(' '),
        head: head ? head.tagName + ':' + txt(head).slice(0, 24) : null,
        text40: t.slice(0, 40),
      }].concat(outline(el, depth + 1, maxDepth));
    });
  };
  const main = document.querySelector('main');
  out.outline = main ? outline(main, 0, 2).slice(0, 40) : null;

  // h1 of the page
  const h1 = document.querySelector('main h1, h1');
  out.h1 = h1 ? { text: txt(h1), cls: h1.className.toString() } : null;

  return JSON.stringify(out, null, 1);
})()
