// probe-v7-mobile-topbar.mjs — mobile top bar geometry (61px header, toggle, brand)
(() => {
  const out = { vw: innerWidth };
  // the header containing the PanelLeft toggle + brand
  const btn = [...document.querySelectorAll("button")].find(b => (b.querySelector("svg")?.getAttribute("class") || "").includes("panel-left"));
  if (!btn) return JSON.stringify({ err: "no panel-left toggle" });
  const header = btn.closest("header") || btn.parentElement?.parentElement;
  const hcs = getComputedStyle(header);
  out.header = {
    tag: header.tagName, cls: (header.className || "").toString().slice(0, 90),
    h: Math.round(header.getBoundingClientRect().height),
    padding: hcs.padding, borderB: hcs.borderBottomWidth + " " + hcs.borderBottomColor,
    bg: hcs.backgroundColor, display: hcs.display,
  };
  const bcs = getComputedStyle(btn);
  const icon = btn.querySelector("svg");
  out.toggle = {
    cls: (btn.className || "").toString().slice(0, 100),
    w: Math.round(btn.getBoundingClientRect().width), h: Math.round(btn.getBoundingClientRect().height),
    iconW: icon ? getComputedStyle(icon).width : null, iconColor: icon ? getComputedStyle(icon).color : null,
    ariaLabel: btn.getAttribute("aria-label"),
  };
  // brand next to toggle
  const brand = [...header.querySelectorAll("h1,h2,span,div")].find(el => el.children.length === 0 && /^ZeroBalance$/.test(el.textContent?.trim() || ""));
  if (brand) {
    const gcs = getComputedStyle(brand);
    out.brand = { tag: brand.tagName, cls: (brand.className || "").toString().slice(0, 60), size: gcs.fontSize, weight: gcs.fontWeight, color: gcs.color };
  }
  // the toast container (ref bug R1) — fixed top-0 w-full
  const toast = [...document.querySelectorAll("div")].find(d => {
    const c = d.className?.toString?.() || "";
    return /fixed/.test(c) && /top-0/.test(c) && !d.closest("header") && d !== document.body;
  });
  out.toastContainer = toast ? {
    cls: toast.className.toString().slice(0, 90),
    pe: getComputedStyle(toast).pointerEvents,
    h: Math.round(toast.getBoundingClientRect().height),
  } : null;
  // horizontal overflow check
  out.scrollWidth = document.documentElement.scrollWidth;
  return JSON.stringify(out, null, 1);
})()
