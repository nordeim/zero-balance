(async () => {
  // v47: the MOBILE SHEET chrome census at 390 (the session-104 queue's
  // sheet item — the shadow-scale net's sixth site). Works on BOTH
  // sites: the sheet = the fixed left panel containing nav links; the
  // overlay = the fixed dim layer without links. The clone's sheet is
  // [data-state=open].fixed.inset-y-0; the reference's is a plain fixed
  // div — the structural finder (fixed + 250–330 wide + has links)
  // covers both.
  const sheet = [...document.querySelectorAll("div")].find(
    (d) => {
      const cs = getComputedStyle(d);
      return (
        cs.position === "fixed" &&
        d.getBoundingClientRect().width >= 250 &&
        d.getBoundingClientRect().width <= 330 &&
        d.querySelector("a")
      );
    },
  );
  if (!sheet) return "no sheet";
  const cs = getComputedStyle(sheet);
  const r = sheet.getBoundingClientRect();
  const overlay = [...document.querySelectorAll("div")].find(
    (d) => {
      const cs2 = getComputedStyle(d);
      return (
        cs2.position === "fixed" &&
        cs2.backgroundColor !== "rgba(0, 0, 0, 0)" &&
        d.querySelectorAll("a").length === 0 &&
        d !== sheet &&
        !d.contains(sheet) &&
        d.getBoundingClientRect().width > 300
      );
    },
  );
  const layerCount = (cs.boxShadow.match(/px, /g) || []).length + 1;
  return JSON.stringify({
    sheet: {
      w: Math.round(r.width),
      h: Math.round(r.height),
      x: Math.round(r.x),
      bg: cs.backgroundColor,
      shadow: cs.boxShadow,
      layers: layerCount,
      transform: cs.transform,
    },
    overlay: overlay
      ? { bg: getComputedStyle(overlay).backgroundColor, z: getComputedStyle(overlay).zIndex }
      : null,
  });
})()
