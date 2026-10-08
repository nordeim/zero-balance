// probe-v15-loading.mjs — loading/spinner state census during the data-fetch
// window: run immediately after navigation; collect any skeleton/spinner/busy
// indicators in the DOM (aria-busy, role=progressbar, skeleton class names,
// animate-spin, "Loading…" text) plus what's in main at that moment.
(() => {
  const out = { url: location.pathname, t: Date.now() };
  const busy = [];
  for (const el of document.querySelectorAll('body *')) {
    if (!el.isConnected || el.children.length > 6) continue;
    const cs = getComputedStyle(el);
    const cls = el.getAttribute('class') || '';
    const aria = el.getAttribute('aria-busy');
    const role = el.getAttribute('role');
    const anim = cs.animationName !== 'none' || (cs.animationDuration !== '0s' && cs.animationIterationCount.includes('infinite'));
    if (aria === 'true' || role === 'progressbar' || /skeleton|shimmer|loading|spinner/i.test(cls) || (anim && /spin|pulse|fade|shimmer/i.test(cs.animationName))) {
      busy.push({ tag: el.tagName.toLowerCase(), cls: cls.slice(0, 60), aria, role, anim: cs.animationName, text: el.textContent.trim().slice(0, 30) });
      if (busy.length > 5) break;
    }
  }
  out.busyIndicators = busy;
  // any "Loading" text visible?
  const loadingText = [...document.querySelectorAll('main *, body > div *')].find((el) => el.getBoundingClientRect().height > 0 && /^(loading|chargement|l\u00e4dt)/i.test(el.textContent.trim()));
  out.loadingText = loadingText ? loadingText.textContent.trim().slice(0, 40) : null;
  // what does main contain right now?
  const main = document.querySelector('main');
  out.mainChildCount = main ? [...main.querySelectorAll('h1,h2,h3,button')].filter((el) => el.getBoundingClientRect().height > 0).length : 0;
  out.h1s = main ? [...main.querySelectorAll('h1,h2')].filter((el) => el.getBoundingClientRect().height > 0).slice(0, 3).map((el) => el.textContent.trim().slice(0, 30)) : [];
  out.dataLoaded = /\$[\d,]+\.\d{2}/.test(document.body.textContent);
  return JSON.stringify(out, null, 1);
})()
