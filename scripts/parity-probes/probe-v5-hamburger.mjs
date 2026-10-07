// Session-8 (v5): mobile hamburger hit-test + toast-viewport check.
(() => {
  const out = {};
  const b = [...document.querySelectorAll('button')].find((x) => (x.getAttribute('aria-label') || '') === 'Toggle Sidebar');
  if (!b) return JSON.stringify({ error: 'no burger' });
  const r = b.getBoundingClientRect();
  const top = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2);
  out.hit = { tag: top.tagName, cls: (top.className || '').toString().slice(0, 60) };
  out.isButtonChild = b.contains(top);
  const toast = document.querySelector('[class*="sonner"], [data-sonner-toaster], ol[tabindex]');
  out.toastViewport = toast ? { cls: (toast.className || '').toString().slice(0, 50), pointerEvents: getComputedStyle(toast).pointerEvents, w: Math.round(toast.getBoundingClientRect().width), h: Math.round(toast.getBoundingClientRect().height), top: Math.round(toast.getBoundingClientRect().top) } : null;
  return JSON.stringify(out, null, 1);
})()
