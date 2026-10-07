(() => {
  const main = document.querySelector('main');
  const inner = main ? main.querySelector('.max-w-7xl, [class*="max-w"]') : null;
  const r = inner ? inner.getBoundingClientRect() : null;
  const nav = document.querySelector('nav');
  const navR = nav ? nav.getBoundingClientRect() : null;
  const doc = document.documentElement;
  const h1 = main ? main.querySelector('h1') : null;
  return JSON.stringify({
    vw: doc.clientWidth,
    scrollW: doc.scrollWidth,
    innerW: r ? Math.round(r.width) : null,
    innerX: r ? Math.round(r.x) : null,
    navW: navR ? Math.round(navR.width) : null,
    h1W: h1 ? Math.round(h1.getBoundingClientRect().width) : null,
  }, null, 1);
})()
