// probe-v10-mobile-nav.mjs — R1 toast-block hit test + hamburger geometry + viewport fit
(() => {
  const out = { url: location.pathname };
  window.scrollTo(0, 0);
  // 1. document horizontal overflow (R4)
  out.scrollWidth = document.documentElement.scrollWidth;
  out.clientWidth = document.documentElement.clientWidth;
  // 2. toast/notification containers (R1 source)
  const toasts = [...document.querySelectorAll("div,ol,ul,section,[role='region']")].filter(d => {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return cs.position === "fixed" && r.width > 100 && (r.top === 0 || r.top < 60) && parseInt(cs.zIndex || "0") >= 90;
  }).map(d => { const cs = getComputedStyle(d); const r = d.getBoundingClientRect(); return { tag: d.tagName, cls: (d.className || "").toString().slice(0, 60), pe: cs.pointerEvents, top: Math.round(r.top), left: Math.round(r.left), w: Math.round(r.width), h: Math.round(r.height), z: cs.zIndex, childCount: d.children.length }; });
  out.fixedTop = toasts;
  // 3. hamburger button (aria-label or visible text)
  const btn = document.querySelector("button[aria-label*='enu'], button[aria-label*='avigation'], button[aria-label*='toggle']");
  const fallback = [...document.querySelectorAll("button")].filter(b => {
    const r = b.getBoundingClientRect();
    const svg = b.querySelector("svg");
    return r.width <= 44 && r.top < 80 && svg && b.textContent.trim() === "";
  })[0];
  const burger = btn || fallback;
  if (burger) {
    const r = burger.getBoundingClientRect();
    const cs = getComputedStyle(burger);
    out.burger = { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), label: burger.getAttribute("aria-label"), cls: (burger.className || "").toString().slice(0, 70) };
    // hit test at center
    const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
    const hit = document.elementFromPoint(cx, cy);
    out.hit = { tag: hit ? hit.tagName : null, cls: hit ? (hit.className || "").toString().slice(0, 60) : null, isBurger: hit === burger || burger.contains(hit), aria: hit && hit.getAttribute ? (hit.getAttribute("aria-label") || "").slice(0, 30) : null, role: hit && hit.getAttribute ? hit.getAttribute("role") : null };
    // toast container specifics
    const tc = out.fixedTop.find(t => t.pe === "auto" && t.childCount === 0);
    out.toastViewportPE = tc ? "AUTO (blocks)" : "none-or-absent";
  } else out.burger = "NOT FOUND";
  return JSON.stringify(out, null, 1);
})()
