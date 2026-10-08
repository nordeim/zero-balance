// probe-v9-dialog-detail.mjs — verify header structure, label gaps, tile internals
(() => {
  const out = { url: location.pathname };
  let panel = document.querySelector("[role='dialog']");
  if (!panel) {
    const overlay = [...document.querySelectorAll("div")].find(d => { const cls = (d.className || "").toString(); return /fixed\s+inset-0/.test(cls) && /z-50/.test(cls) && getComputedStyle(d).position === "fixed"; });
    if (overlay) panel = [...overlay.querySelectorAll("div")].find(d => { const cs = getComputedStyle(d); const r = d.getBoundingClientRect(); return r.width > 300 && r.width < 900 && cs.backgroundColor !== "rgba(0, 0, 0, 0)"; });
  }
  if (!panel) return JSON.stringify({ err: "no dialog" });
  // heading + subtitle
  const heading = panel.querySelector("h2, h3, [data-radix-dialog-title]");
  if (heading) {
    const hcs = getComputedStyle(heading);
    const hr = heading.getBoundingClientRect();
    out.heading = { text: (heading.textContent || "").trim(), fs: hcs.fontSize, fw: hcs.fontWeight, color: hcs.color, h: Math.round(hr.height) };
  }
  // header block = heading's parent chain up to the sticky div
  let hdr = heading?.parentElement;
  for (let i = 0; i < 4 && hdr && hdr !== panel; i++) {
    const cs = getComputedStyle(hdr);
    if (cs.position === "sticky" || /sticky/.test((hdr.className || "").toString())) break;
    hdr = hdr.parentElement;
  }
  if (hdr) {
    const hcs = getComputedStyle(hdr);
    const hr = hdr.getBoundingClientRect();
    out.headerBlock = { h: Math.round(hr.height), pt: hcs.paddingTop, pb: hcs.paddingBottom, px: hcs.paddingLeft, borderB: hcs.borderBottomWidth + " " + hcs.borderBottomColor, pos: hcs.position, bg: hcs.backgroundColor, text: (hdr.textContent || "").replace(/\s+/g, " ").slice(0, 80) };
    // subtitle in header?
    const subs = [...hdr.querySelectorAll("p, span, div")].filter(el => el.children.length === 0 && (el.textContent || "").trim().length > 8);
    out.headerSubs = subs.slice(0, 2).map(el => { const s = getComputedStyle(el); return { t: (el.textContent || "").trim().slice(0, 50), fs: s.fontSize, c: s.color, fw: s.fontWeight }; });
  }
  // label→input visual gap: find the "Amount" label, measure distance to its input
  const labels = [...panel.querySelectorAll("label")];
  const amountLabel = labels.find(l => /^Amount$/.test((l.textContent || "").trim()));
  if (amountLabel) {
    const lr = amountLabel.getBoundingClientRect();
    // the next input after the label within the same field wrapper
    const wrap = amountLabel.closest("div") || amountLabel.parentElement;
    const input = wrap?.querySelector("input");
    if (input) {
      const ir = input.getBoundingClientRect();
      out.amountGap = Math.round(ir.y - (lr.y + lr.height));
      out.amountLabelStyle = { mb: getComputedStyle(amountLabel).marginBottom, display: getComputedStyle(amountLabel).display };
    }
  }
  // classification tiles: the label wrappers with radio inputs
  const tiles = [...panel.querySelectorAll("label")].filter(l => l.querySelector("input[type='radio']")).slice(0, 3);
  out.tiles = tiles.map(l => {
    const r = l.getBoundingClientRect();
    const cs = getComputedStyle(l);
    const txt = [...l.querySelectorAll("*")].filter(el => el.children.length === 0 && (el.textContent || "").trim()).map(el => ({ t: (el.textContent || "").trim(), fs: getComputedStyle(el).fontSize, fw: getComputedStyle(el).fontWeight, color: getComputedStyle(el).color }));
    // inner icon?
    const icon = l.querySelector("svg");
    const icr = icon ? icon.getBoundingClientRect() : null;
    return { w: Math.round(r.width), h: Math.round(r.height), pad: cs.padding, gap: cs.gap ?? cs.rowGap, flexDir: cs.flexDirection, border: cs.borderColor, bg: cs.backgroundColor, radius: cs.borderRadius, texts: txt.slice(0, 2), iconW: icr ? Math.round(icr.width) : null, iconColor: icon ? getComputedStyle(icon).color : null, inner: (l.innerHTML || "").replace(/\s+/g, " ").slice(0, 150) };
  });
  // X close button in header
  const xbtn = [...panel.querySelectorAll("button")].find(b => (b.getAttribute("aria-label") || "").toLowerCase().includes("close"));
  if (xbtn) {
    const xr = xbtn.getBoundingClientRect();
    const xcs = getComputedStyle(xbtn);
    out.closeBtn = { w: Math.round(xr.width), h: Math.round(xr.height), color: xcs.color, bg: xcs.backgroundColor, hover: xcs.borderColor, svg: xbtn.querySelector("svg") ? Math.round(xbtn.querySelector("svg").getBoundingClientRect().width) : null };
  }
  return JSON.stringify(out, null, 1);
})()
