// probe-v13-ref-mobile.mjs — task-focus re-verification on the REFERENCE mobile
// (390x844): R4 overflow, R1 burger hit-test + toast-container intercept,
// burger/topbar geometry. Same measurement contract as probe-v10-mobile-nav.
(() => {
  const out = { url: location.pathname };
  window.scrollTo(0, 0);
  out.scrollWidth = document.documentElement.scrollWidth;
  out.clientWidth = document.documentElement.clientWidth;
  const toasts = [...document.querySelectorAll("div,ol,ul,section,[role='region']")].filter(d => {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return cs.position === "fixed" && r.width > 100 && (r.top === 0 || r.top < 60) && parseInt(cs.zIndex || "0") >= 90;
  }).map(d => { const cs = getComputedStyle(d); const r = d.getBoundingClientRect(); return { tag: d.tagName, cls: (d.className || "").toString().slice(0, 60), pe: cs.pointerEvents, top: Math.round(r.top), left: Math.round(r.left), w: Math.round(r.width), h: Math.round(r.height), z: cs.zIndex, childCount: d.children.length }; });
  out.fixedTop = toasts;
  const btn = document.querySelector("button[aria-label*='enu'], button[aria-label*='avigation'], button[aria-label*='toggle']");
  const fallback = [...document.querySelectorAll("button")].filter(b => {
    const r = b.getBoundingClientRect();
    const svg = b.querySelector("svg");
    return r.width <= 44 && r.top < 80 && svg && b.textContent.trim() === "";
  })[0];
  const burger = btn || fallback;
  if (burger) {
    const r = burger.getBoundingClientRect();
    out.burger = { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), label: burger.getAttribute("aria-label") };
    const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
    const hit = document.elementFromPoint(cx, cy);
    out.hit = { tag: hit ? hit.tagName : null, cls: hit ? (hit.className || "").toString().slice(0, 60) : null, isBurger: hit === burger || burger.contains(hit) };
    const tc = out.fixedTop.find(t => t.pe === "auto" && t.childCount === 0);
    out.toastViewportPE = tc ? "AUTO (blocks)" : "none-or-absent";
  } else out.burger = "NOT FOUND";
  return JSON.stringify(out, null, 1);
})()
