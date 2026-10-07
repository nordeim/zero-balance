// Session-7: mobile layout audit at 390x844 — geometry, overflow, chrome.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);

  out.doc = {
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
    bodyScrollW: document.body.scrollWidth,
  };

  const main = document.querySelector('main');
  if (main) {
    const r = main.getBoundingClientRect();
    out.main = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    const header = main.querySelector('header');
    if (header) {
      const hr = header.getBoundingClientRect();
      out.header = { x: Math.round(hr.x), y: Math.round(hr.y), w: Math.round(hr.width), h: Math.round(hr.height), display: cs(header, 'display') };
      const btn = header.querySelector('button');
      if (btn) {
        const br = btn.getBoundingClientRect();
        out.hamburger = { x: Math.round(br.x), y: Math.round(br.y), w: Math.round(br.width), h: Math.round(br.height), cls: btn.className.toString().slice(0, 90) };
      }
    }
    // content wrapper padding at mobile
    const wrap = [...main.children].find((c) => c.tagName === 'DIV');
    if (wrap) out.wrapCls = { cls: wrap.className.toString().slice(0, 90), padding: cs(wrap, 'padding') };
  }

  // rail hidden at mobile?
  const rail = [...document.querySelectorAll('div,aside')].find((d) => /fixed inset-y-0/.test((d.className || '').toString()) && /sidebar|--sidebar-width/.test((d.className || '').toString()));
  if (rail) {
    const r = rail.getBoundingClientRect();
    out.rail = { display: cs(rail, 'display'), w: Math.round(r.width), x: Math.round(r.x) };
  }

  // horizontal overflow offenders
  out.overflow = [...document.querySelectorAll('body *')].filter((el) => {
    const r = el.getBoundingClientRect();
    return r.width > 0 && (r.right > 391 || r.left < -1) && ['DIV', 'MAIN', 'HEADER', 'ASIDE', 'UL', 'NAV'].includes(el.tagName);
  }).slice(0, 5).map((el) => ({ tag: el.tagName, cls: (el.className || '').toString().slice(0, 60), right: Math.round(el.getBoundingClientRect().right), left: Math.round(el.getBoundingClientRect().left) }));

  // hero card fits?
  const hero = [...document.querySelectorAll('h3')].find((h) => /NET ZERO GOAL/i.test((h.textContent || '')));
  if (hero) {
    const card = hero.closest('div[class*="rounded"]');
    const r = card.getBoundingClientRect();
    out.hero = { x: Math.round(r.x), w: Math.round(r.width), right: Math.round(r.right) };
  }

  return JSON.stringify(out, null, 1);
})()
