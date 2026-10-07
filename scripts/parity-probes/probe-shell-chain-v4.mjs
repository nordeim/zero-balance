// Session-7: measure the shell chain — body, shell, main — plus min-width causes.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const r = (el) => (el ? { w: Math.round(el.getBoundingClientRect().width), x: Math.round(el.getBoundingClientRect().x) } : null);

  out.body = { w: Math.round(document.body.getBoundingClientRect().width), scrollW: document.body.scrollWidth };
  const shell = document.body.querySelector(':scope > div') || document.body.firstElementChild;
  out.shell = { cls: (shell.className || '').toString().slice(0, 90), rect: r(shell), display: cs(shell, 'display'), minW: cs(shell, 'minWidth') };
  const main = document.querySelector('main');
  out.main = {
    cls: main.className.toString().slice(0, 120),
    rect: r(main),
    display: cs(main, 'display'),
    minWidth: cs(main, 'minWidth'),
    flexGrow: cs(main, 'flexGrow'),
    flexBasis: cs(main, 'flexBasis'),
    width: cs(main, 'width'),
  };
  // children of main
  out.mainChildren = [...main.children].map((c) => ({
    tag: c.tagName,
    cls: (c.className || '').toString().slice(0, 70),
    rect: r(c),
    minW: cs(c, 'minWidth'),
    display: cs(c, 'display'),
  }));
  // children of shell
  out.shellChildren = [...shell.children].map((c) => ({
    tag: c.tagName,
    cls: (c.className || '').toString().slice(0, 70),
    rect: r(c),
    display: cs(c, 'display'),
  }));
  // The networth wrap's children min-content: measure with width:min-content trick on a clone? Just report scrollWidths of each wrap child.
  const wrap = [...main.querySelectorAll('div')].find((d) => (d.className || '').toString().includes('max-w-7xl'));
  if (wrap) {
    out.wrapChildren = [...wrap.children].map((c) => ({
      tag: c.tagName,
      cls: (c.className || '').toString().slice(0, 50),
      rect: r(c),
      scrollW: c.scrollWidth,
      clientW: c.clientWidth,
    }));
  }
  return JSON.stringify(out, null, 1);
})()
