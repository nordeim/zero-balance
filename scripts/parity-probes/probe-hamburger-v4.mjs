// Session-7: mobile hamburger hit-test — does the toast viewport block the button?
(async () => {
  const out = {};
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. toast viewport geometry + pointer-events
  const toasts = [...document.querySelectorAll('ol,ul,div')].filter((el) => /sonner|Toaster|toast/i.test((el.className || '').toString() + (el.getAttribute('aria-label') || '')));
  const viewport = toasts.find((el) => getComputedStyle(el).position === 'fixed') || toasts[0];
  if (viewport) {
    const r = viewport.getBoundingClientRect();
    out.toastViewport = {
      cls: (viewport.className || '').toString().slice(0, 60),
      rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      pointerEvents: getComputedStyle(viewport).pointerEvents,
      zIndex: getComputedStyle(viewport).zIndex,
    };
  } else {
    out.toastViewport = null;
  }

  // 2. elementFromPoint over the hamburger center — is it the button?
  const btn = [...document.querySelectorAll('header button')].find((b) => /Toggle Sidebar/i.test((b.textContent || '')) || b.querySelector('svg[class*="panel-left"], svg[class*="menu"]'));
  if (btn) {
    const r = btn.getBoundingClientRect();
    const cx = Math.round(r.x + r.width / 2);
    const cy = Math.round(r.y + r.height / 2);
    const topEl = document.elementFromPoint(cx, cy);
    out.hitTest = {
      btnRect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
      point: [cx, cy],
      topElement: topEl ? topEl.tagName + '.' + (topEl.className || '').toString().slice(0, 40) : null,
      isButtonOrChild: !!(topEl && (topEl === btn || btn.contains(topEl))),
    };
  }

  return JSON.stringify(out, null, 1);
})()
