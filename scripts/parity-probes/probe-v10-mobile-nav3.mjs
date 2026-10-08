// probe-v10-mobile-nav3.mjs — burger by text content + R1 hit test + topbar + brand
(() => {
  const out = { url: location.pathname };
  window.scrollTo(0, 0);
  const burger = [...document.querySelectorAll("button")].find(b => {
    const r = b.getBoundingClientRect();
    return r.top < 100 && r.width <= 44 && (b.textContent || "").includes("Toggle") && b.querySelector("svg");
  });
  if (!burger) return JSON.stringify({ err: "no burger", url: out.url, btns: [...document.querySelectorAll('button')].filter(b=>b.getBoundingClientRect().top<100).map(b=>({t:(b.textContent||'').trim().slice(0,25),w:Math.round(b.getBoundingClientRect().width)})) });
  const r = burger.getBoundingClientRect();
  out.burger = { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), txt: (burger.textContent || "").trim().slice(0, 20) };
  const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
  const hit = document.elementFromPoint(cx, cy);
  out.r1hit = { tag: hit?.tagName, cls: (hit?.className || "").toString().slice(0, 55), isBurger: hit === burger || burger.contains(hit), txt: (hit?.textContent || "").trim().slice(0, 20) };
  // svg icon
  const svg = burger.querySelector("svg");
  if (svg) { const sr = svg.getBoundingClientRect(); out.icon = { w: Math.round(sr.width), h: Math.round(sr.height), color: getComputedStyle(svg).color }; }
  // topbar container
  const bar = burger.parentElement;
  if (bar) { const br = bar.getBoundingClientRect(); const cs = getComputedStyle(bar); out.topbar = { h: Math.round(br.height), y: Math.round(br.y), w: Math.round(br.width), bg: cs.backgroundColor, pos: cs.position, pad: cs.padding }; }
  // brand heading next to burger
  const brand = [...(bar?.parentElement?.querySelectorAll("h1, h2") || [])].filter(h => h.getBoundingClientRect().top < 80)[0];
  if (brand) { const brr = brand.getBoundingClientRect(); out.brand = { t: (brand.textContent || "").trim().slice(0, 20), fs: getComputedStyle(brand).fontSize, fw: getComputedStyle(brand).fontWeight, x: Math.round(brr.x), y: Math.round(brr.y), w: Math.round(brr.width), h: Math.round(brr.height) }; }
  return JSON.stringify(out, null, 1);
})()
