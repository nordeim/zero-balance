// Session-7: nav link chrome + sidebar header/footer (avatar) computed geometry.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const rect = (el) => (el ? JSON.parse(JSON.stringify(el.getBoundingClientRect())) : null);

  // 1. All nav links: geometry + typography
  const links = [...document.querySelectorAll('aside a, nav a, [class*="w-64"] a, [class*="sidebar"] a')].filter((a) => /^(Dashboard|Income|Expenses|Savings|Net Worth)$/.test(txt(a) || ''));
  out.navLinks = links.map((a) => ({
    text: txt(a),
    padding: cs(a, 'padding'),
    gap: cs(a, 'columnGap') || cs(a, 'gap'),
    fontSize: cs(a, 'fontSize'),
    fontWeight: cs(a, 'fontWeight'),
    height: Math.round(a.getBoundingClientRect().height),
    radius: cs(a, 'borderRadius'),
    iconSize: (() => { const s = a.querySelector('svg'); return s ? cs(s, 'width') : null; })(),
    rect: rect(a) ? { x: Math.round(a.getBoundingClientRect().x), w: Math.round(a.getBoundingClientRect().width) } : null,
  }));

  // 2. Sidebar header (brand block)
  const side = (document.querySelector('aside') || [...document.querySelectorAll('div')].find((d) => (d.className || '').toString().includes('w-64') && (d.textContent || '').includes('Dashboard')));
  if (side) {
    out.sideHead = {
      html: (() => { const first = side.querySelector(':scope > div'); return first ? first.outerHTML.replace(/\s+/g, ' ').slice(0, 300) : null; })(),
    };
    // avatar: bottom rounded-full
    const av = [...side.querySelectorAll('div,span,img')].filter((x) => {
      const c = (x.className || '').toString();
      return c.includes('rounded-full') && !c.includes('rounded-full-');
    }).pop();
    out.sideAvatar = av ? { tag: av.tagName, text: txt(av).slice(0, 20), bg: cs(av, 'backgroundColor'), size: cs(av, 'width'), color: cs(av, 'color') } : null;
    // user name/email near avatar
    const userBlock = av ? av.closest('div[class*="flex"]') : null;
    out.sideUser = userBlock ? txt(userBlock).slice(0, 60) : null;
  }

  return JSON.stringify(out, null, 1);
})()
