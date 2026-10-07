// Session-7: exact nav link class + line-height + active state on /dashboard.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const links = [...document.querySelectorAll('a')].filter((a) => /^(Dashboard|Income|Expenses|Savings|Net Worth)$/.test(txt(a) || ''));
  out.count = links.length;
  if (links.length) {
    out.firstLink = {
      cls: links[0].className.toString(),
      lineHeight: cs(links[0], 'lineHeight'),
      height: Math.round(links[0].getBoundingClientRect().height),
      boxSizing: cs(links[0], 'boxSizing'),
      color: cs(links[0], 'color'),
    };
    // active link (if any): bg image/color + weight
    out.activeStates = links.map((a) => ({
      text: txt(a),
      bgImg: (cs(a, 'backgroundImage') !== 'none' ? cs(a, 'backgroundImage').slice(0, 70) : 'none'),
      color: cs(a, 'color'),
      weight: cs(a, 'fontWeight'),
    }));
  }

  // sidebar header structure (brand block)
  const rail = [...document.querySelectorAll('div')].find((d) => {
    const c = (d.className || '').toString();
    return /fixed inset-y-0/.test(c) && c.includes('sidebar');
  });
  if (!rail) {
    // fallback: the container holding the Dashboard link
    const l = links[0];
    out.railViaLink = l ? l.closest('div.fixed, div[class*="fixed"]')?.className.toString().slice(0, 120) : null;
  }
  // brand: the icon-text row at the top of the sidebar
  const brandRow = (() => {
    if (!links.length) return null;
    let node = links[0];
    while (node.parentElement) {
      node = node.parentElement;
      if ((node.textContent || '').includes('ZeroBalance') && (node.textContent || '').includes('Dashboard')) {
        // brand row = first child of the scroll container's parent's first div
        const head = node.querySelector('div > div:first-child');
        if (head && /ZeroBalance/.test(head.textContent || '') && !head.textContent.includes('Dashboard')) return head;
      }
    }
    return null;
  })();
  if (brandRow) {
    out.brandRow = {
      html: brandRow.outerHTML.replace(/\s+/g, ' ').slice(0, 420),
    };
  }

  // avatar block at the sidebar bottom
  const avs = [...document.querySelectorAll('div,span')].filter((x) => (x.className || '').toString().includes('rounded-full') && (x.textContent || '').trim().length <= 2 && (x.textContent || '').trim().length > 0);
  out.avatars = avs.map((a) => {
    const block = a.closest('div.flex');
    return { text: txt(a), bg: cs(a, 'backgroundColor'), size: cs(a, 'width'), blockText: block ? txt(block).slice(0, 70) : null };
  }).slice(0, 3);

  return JSON.stringify(out, null, 1);
})()
