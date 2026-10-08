// probe-v10-sheet-internals.mjs — mobile sheet brand block, nav container, user footer
(() => {
  const out = { url: location.pathname };
  const sheet = [...document.querySelectorAll("div,aside")].find(d => { const cs = getComputedStyle(d); const r = d.getBoundingClientRect(); return cs.position === "fixed" && r.width >= 250 && r.width <= 350 && r.height > 600; });
  if (!sheet) return JSON.stringify({ err: "no sheet", url: out.url });
  // brand block: the sheet's first bordered block with the logo
  const brand = [...sheet.querySelectorAll("h1, h2")].filter(h => /ZeroBalance/i.test(h.textContent || ""))[0];
  if (brand) { const br = brand.getBoundingClientRect(); const bcs = getComputedStyle(brand); out.brand = { fs: bcs.fontSize, fw: bcs.fontWeight, color: bcs.color, x: Math.round(br.x), y: Math.round(br.y), w: Math.round(br.width), h: Math.round(br.height) }; }
  const logoTile = brand?.closest("div")?.querySelector("div");
  if (logoTile) { const lr = logoTile.getBoundingClientRect(); const lcs = getComputedStyle(logoTile); out.logoTile = { w: Math.round(lr.width), h: Math.round(lr.height), radius: lcs.borderRadius, bgImg: lcs.backgroundImage.slice(0, 45) }; const icon = logoTile.querySelector("svg"); if (icon) { const ir = icon.getBoundingClientRect(); out.logoIcon = { w: Math.round(ir.width), color: getComputedStyle(icon).color }; } }
  // subtitle
  const sub = [...sheet.querySelectorAll("p")].filter(p => /Budget Planner/i.test(p.textContent || ""))[0];
  if (sub) { const scs = getComputedStyle(sub); out.brandSub = { fs: scs.fontSize, color: scs.color }; }
  // user footer: the bottom block with avatar + Budget Pro
  const avatar = [...sheet.querySelectorAll("div")].filter(d => { const r = d.getBoundingClientRect(); const t = (d.textContent || ""); return r.width <= 40 && r.height <= 40 && r.width > 20 && /^[A-Z]$/.test((d.textContent || "").trim()); })[0];
  if (avatar) { const ar = avatar.getBoundingClientRect(); const acs = getComputedStyle(avatar); out.avatar = { w: Math.round(ar.width), h: Math.round(ar.height), radius: acs.borderRadius, bg: acs.backgroundColor, color: acs.color, fs: acs.fontSize }; }
  const pro = [...sheet.querySelectorAll("p")].filter(p => /Budget Pro/i.test(p.textContent || ""))[0];
  if (pro) { const pcs = getComputedStyle(pro); out.pro = { fs: pcs.fontSize, fw: pcs.fontWeight, color: pcs.color }; }
  return JSON.stringify(out, null, 1);
})()
