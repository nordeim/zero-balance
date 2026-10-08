// probe-v10-mobile-nav2.mjs — burger geometry + R1 hit test + open sheet + R2 nav behavior
(() => {
  const out = { url: location.pathname };
  window.scrollTo(0, 0);
  const burger = [...document.querySelectorAll("button")].find(b => (b.getAttribute("aria-label") || "").includes("Toggle Sidebar") || (b.getAttribute("aria-label") || "").includes("Menu"));
  if (!burger) return JSON.stringify({ err: "no burger", url: out.url });
  const r = burger.getBoundingClientRect();
  out.burger = { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), label: burger.getAttribute("aria-label") };
  const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
  const hit = document.elementFromPoint(cx, cy);
  out.r1hit = { tag: hit?.tagName, cls: (hit?.className || "").toString().slice(0, 50), isBurger: hit === burger || burger.contains(hit) };
  // top bar geometry
  const bar = burger.closest("div");
  if (bar) { const br = bar.getBoundingClientRect(); const cs = getComputedStyle(bar); out.topbar = { h: Math.round(br.height), y: Math.round(br.y), x: Math.round(br.x), w: Math.round(br.width), bg: cs.backgroundColor, pos: cs.position }; }
  // brand next to burger
  const brand = burger.parentElement?.querySelector("h1, span, div");
  if (brand) { const brr = brand.getBoundingClientRect(); out.brand = { t: (brand.textContent || "").trim().slice(0, 20), fs: getComputedStyle(brand).fontSize, x: Math.round(brr.x), y: Math.round(brr.y), w: Math.round(brr.width) }; }
  return JSON.stringify(out, null, 1);
})()
