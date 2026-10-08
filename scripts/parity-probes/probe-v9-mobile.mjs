// probe-v9-mobile.mjs — mobile navigation stack audit at 390×844 (task focus)
(() => {
  const out = { url: location.pathname, vw: innerWidth, scrollWidth: document.documentElement.scrollWidth };
  // topbar
  const headerInMain = document.querySelector("main > div:first-child > div:first-child");
  const bar = document.querySelector("header") || headerInMain;
  if (bar) {
    const r = bar.getBoundingClientRect();
    out.topbar = { w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y) };
  }
  // hamburger toggle + hit-test
  const tgl = bar ? [...bar.querySelectorAll("button")].find(b => b.querySelector("svg")) : null;
  if (tgl) {
    const r = tgl.getBoundingClientRect();
    const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
    const hit = document.elementFromPoint(cx, cy);
    out.toggle = {
      w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y),
      hitIsToggle: hit === tgl || tgl.contains(hit),
      hitTag: hit ? `${hit.tagName}.${(hit.className || "").toString().slice(0, 60)}` : null,
    };
  }
  // toast container R1 check
  const toasts = [...document.querySelectorAll("[data-sonner-toaster], [role='region'][aria-label*='Notification' i], ol[class*='toast'], div[class*='Toaster']")];
  out.toastContainers = toasts.map(t => {
    const cs = getComputedStyle(t);
    return { pe: cs.pointerEvents, pos: cs.position, top: cs.top, z: cs.zIndex };
  });
  return JSON.stringify(out, null, 1);
})()
