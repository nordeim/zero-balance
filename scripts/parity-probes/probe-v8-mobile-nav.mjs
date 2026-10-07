// probe-v8-mobile-nav.mjs — mobile navigation chrome + geometry audit (390×844)
(() => {
  const out = { url: location.pathname, vw: innerWidth };
  // 1. document scroll width (overflow check)
  out.scrollWidth = document.documentElement.scrollWidth;
  // 2. topbar / header
  const header = document.querySelector("main")?.previousElementSibling || document.querySelector("header");
  const headerInMain = document.querySelector("main > div:first-child > div:first-child");
  const bar = header || headerInMain;
  if (bar) {
    const r = bar.getBoundingClientRect();
    const cs = getComputedStyle(bar);
    out.topbar = { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), display: cs.display, tag: bar.tagName };
  }
  // 3. hamburger toggle button (mobile only)
  const toggle = [...document.querySelectorAll("button")].find(b => {
    const r = b.getBoundingClientRect();
    return r.width > 0 && r.width <= 40 && b.querySelector("svg") && (b.getAttribute("aria-label") || "").toLowerCase().includes("menu") || /Open navigation|Toggle|menu/i.test(b.getAttribute("aria-label") || "");
  });
  // fallback: the button inside the header/topbar containing panel-left svg
  const tgl = toggle || (bar ? [...bar.querySelectorAll("button")].find(b => b.querySelector("svg")) : null);
  if (tgl) {
    const r = tgl.getBoundingClientRect();
    const cs = getComputedStyle(tgl);
    const svg = tgl.querySelector("svg");
    const sr = svg ? svg.getBoundingClientRect() : null;
    out.toggle = {
      w: Math.round(r.width), h: Math.round(r.height),
      svgW: sr ? Math.round(sr.width) : null, svgH: sr ? Math.round(sr.height) : null,
      color: cs.color, bg: cs.backgroundColor, pad: cs.padding, radius: cs.borderRadius,
      cls: (tgl.className || "").toString().slice(0, 140),
    };
  }
  // 4. toast container geometry (R1 check)
  const toasts = [...document.querySelectorAll("[data-sonner-toaster], [role='region'][aria-label*='Notification' i], ol[class*='toast'], div[class*='Toaster']")];
  out.toastContainers = toasts.map(t => {
    const cs = getComputedStyle(t);
    const r = t.getBoundingClientRect();
    return { h: Math.round(r.height), pe: cs.pointerEvents, pos: cs.position, top: cs.top, z: cs.zIndex };
  });
  // 5. aside (desktop rail should be hidden at mobile)
  const aside = document.querySelector("aside");
  if (aside) {
    const cs = getComputedStyle(aside);
    out.aside = { display: cs.display, w: Math.round(aside.getBoundingClientRect().width) };
  }
  // 6. sidebar brand (if visible)
  const brand = document.querySelector("aside h2, aside [class*='logo']");
  if (brand && getComputedStyle(brand).display !== "none") {
    out.brandTextSize = getComputedStyle(brand).fontSize;
  }
  return JSON.stringify(out, null, 1);
})()
