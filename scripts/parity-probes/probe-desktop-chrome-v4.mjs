// Session-7: desktop chrome geometry — header visibility, sidebar, main padding.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);

  // 1. the header inside main
  const main = document.querySelector('main');
  const header = main ? main.querySelector('header') : document.querySelector('header');
  if (header) {
    const r = header.getBoundingClientRect();
    out.header = {
      visible: r.height > 0 && cs(header, 'display') !== 'none',
      rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      cls: header.className.toString(),
      display: cs(header, 'display'),
      brandText: (header.querySelector('h1') || {}).textContent,
      hasToggle: !!header.querySelector('button'),
    };
  }

  // 2. sidebar rail geometry at desktop
  const rail = [...document.querySelectorAll('div,aside')].find((d) => {
    const c = (d.className || '').toString();
    return /fixed inset-y-0/.test(c) && /sidebar|--sidebar-width/.test(c);
  });
  if (rail) {
    const r = rail.getBoundingClientRect();
    out.rail = { rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) }, cls: rail.className.toString().slice(0, 100), display: cs(rail, 'display') };
  }

  // 3. main geometry + the content wrapper padding
  if (main) {
    const mr = main.getBoundingClientRect();
    out.main = { x: Math.round(mr.x), w: Math.round(mr.width) };
    // content wrapper (first content div below header)
    const wrap = [...main.children].find((c) => c !== header && c.tagName === 'DIV');
    if (wrap) {
      out.contentWrap = { cls: wrap.className.toString().slice(0, 90), padding: cs(wrap, 'padding') };
      const inner = wrap.firstElementChild;
      if (inner) out.contentInner = { cls: inner.className.toString().slice(0, 90), padding: cs(inner, 'padding'), maxW: cs(inner, 'maxWidth') };
    }
  }

  // 4. sidebar rail hidden class / md breakpoint behavior — check computed at current width
  out.viewport = { w: window.innerWidth, h: window.innerHeight };

  // 5. toggle button in header — what does it do (aria)
  if (header) {
    const btn = header.querySelector('button');
    out.toggleBtn = btn ? { cls: btn.className.toString().slice(0, 100), ariaLabel: btn.getAttribute('aria-label'), srOnly: btn.textContent.trim().slice(0, 30) } : null;
  }

  return JSON.stringify(out, null, 1);
})()
