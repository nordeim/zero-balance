// probe-v10-dialog-scroll.mjs — dialog scroll regions: sticky header/footer, scrollable form
(() => {
  const out = {};
  // find the dialog panel: a fixed-position child with form inside
  const overlay = [...document.querySelectorAll("div")].find(d => { const cs = getComputedStyle(d); return cs.position === "fixed" && (cs.inset || "") !== "" && cs.backgroundColor !== "rgba(0, 0, 0, 0)" && d.querySelector("form"); });
  if (!overlay) return JSON.stringify({ err: "no dialog overlay" });
  const panel = [...overlay.querySelectorAll("div")].filter(d => { const r = d.getBoundingClientRect(); const cs = getComputedStyle(d); return r.width > 400 && r.width < 900 && cs.backgroundColor !== "rgba(0, 0, 0, 0)" && d.querySelector("form"); }).sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width)[0];
  if (!panel) return JSON.stringify({ err: "no panel" });
  const pr = panel.getBoundingClientRect();
  const pcs = getComputedStyle(panel);
  out.panel = { w: Math.round(pr.width), h: Math.round(pr.height), maxH: pcs.maxHeight, overflow: pcs.overflow, radius: pcs.borderRadius, shadow: pcs.boxShadow.slice(0, 50) };
  // header: the sticky block
  const header = [...panel.querySelectorAll("div")].find(d => getComputedStyle(d).position === "sticky");
  if (header) { const hr = header.getBoundingClientRect(); const hcs = getComputedStyle(header); out.header = { h: Math.round(hr.height), pos: hcs.position, top: hcs.top, bg: hcs.backgroundColor, borderB: hcs.borderBottomWidth + " " + hcs.borderBottomColor, y: Math.round(hr.y) }; }
  // footer: the block with Cancel + Save
  const footer = [...panel.querySelectorAll("div")].filter(d => { const t = (d.textContent || ""); return d.querySelector("button") && /Cancel/.test(t) && /Save/.test(t) && d.getBoundingClientRect().height < 120 && d.getBoundingClientRect().height > 30; })[0];
  if (footer) { const fr = footer.getBoundingClientRect(); const fcs = getComputedStyle(footer); out.footer = { h: Math.round(fr.height), y: Math.round(fr.y), panelBottom: Math.round(pr.bottom), gap: Math.round(fr.top - pr.bottom + fr.height), pos: fcs.position, bg: fcs.backgroundColor, borderT: fcs.borderTopWidth + " " + fcs.borderTopColor, pad: fcs.padding }; }
  // the scrollable middle: form or its wrapper
  const form = panel.querySelector("form");
  if (form) { const wr = form.parentElement; const wcs = getComputedStyle(wr); const fr2 = form.getBoundingClientRect(); out.formWrap = { overflow: wcs.overflow, overflowY: wcs.overflowY, scrollH: wr.scrollHeight, clientH: wr.clientHeight, canScroll: wr.scrollHeight > wr.clientHeight, formH: Math.round(fr2.height) }; }
  // panel-level scroll
  out.panelScroll = { scrollH: panel.scrollHeight, clientH: panel.clientHeight, canScroll: panel.scrollHeight > panel.clientHeight };
  return JSON.stringify(out, null, 1);
})()
