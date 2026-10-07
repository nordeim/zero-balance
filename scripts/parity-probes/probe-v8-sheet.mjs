// probe-v8-sheet.mjs — mobile nav sheet geometry + content (sheet should be open)
(() => {
  const out = { url: location.pathname };
  // the sheet: fixed-position element taller than 200px (the slide-in rail)
  const fixed = [...document.querySelectorAll("body *")].filter(el => {
    const cs = getComputedStyle(el);
    if (cs.position !== "fixed" || cs.display === "none" || cs.visibility === "hidden") return false;
    const r = el.getBoundingClientRect();
    return r.height > 200 && r.width > 100 && r.width < 400;
  });
  out.sheets = fixed.map(el => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x),
      bg: cs.backgroundColor, borderRight: cs.borderRightWidth + " " + cs.borderRightColor,
      z: cs.zIndex, cls: (el.className || "").toString().slice(0, 80),
      h_svh: cs.height,
    };
  });
  // overlay: fixed full-viewport dark layer
  const overlay = [...document.querySelectorAll("body *")].filter(el => {
    const cs = getComputedStyle(el);
    if (cs.position !== "fixed" || cs.display === "none") return false;
    const r = el.getBoundingClientRect();
    return r.width > 300 && r.height > 300 && cs.backgroundColor !== "rgba(0, 0, 0, 0)";
  }).map(el => {
    const cs = getComputedStyle(el);
    return { w: Math.round(el.getBoundingClientRect().width), h: Math.round(el.getBoundingClientRect().height), bg: cs.backgroundColor, z: cs.zIndex, pe: cs.pointerEvents };
  });
  out.overlays = overlay;
  // nav links inside the sheet
  const sheet = fixed[0];
  if (sheet) {
    out.navLinks = [...sheet.querySelectorAll("a")].map(a => {
      const r = a.getBoundingClientRect();
      const cs = getComputedStyle(a);
      return { text: a.textContent?.trim(), href: a.getAttribute("href"), h: Math.round(r.height), size: cs.fontSize, weight: cs.fontWeight, color: cs.color };
    });
    const brand = sheet.querySelector("h1, h2");
    out.sheetBrand = brand ? { text: brand.textContent?.trim().slice(0, 20), size: getComputedStyle(brand).fontSize } : null;
  }
  return JSON.stringify(out, null, 1);
})()
