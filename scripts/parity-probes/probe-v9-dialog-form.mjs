// probe-v9-dialog-form.mjs — form-dialog internals at computed depth (labels, inputs, radios, switch, descriptions)
// Run with the ADD budget-item dialog open. Climbs from the dialog heading.
(() => {
  const out = { url: location.pathname };
  // find the dialog: Radix uses [role=dialog]; ref has none — use the fixed overlay z-50, then its panel child
  let panel = document.querySelector("[role='dialog']");
  if (!panel) {
    const overlay = [...document.querySelectorAll("div")].find(d => {
      const cls = (d.className || "").toString();
      return /fixed\s+inset-0/.test(cls) && /z-50/.test(cls) && getComputedStyle(d).position === "fixed";
    });
    if (overlay) {
      // panel = first descendant with a bg + rounded (the card)
      panel = [...overlay.querySelectorAll("div")].find(d => {
        const cs = getComputedStyle(d);
        const r = d.getBoundingClientRect();
        return r.width > 300 && r.width < 900 && cs.backgroundColor !== "rgba(0, 0, 0, 0)" && (parseInt(cs.borderRadius) > 0 || /rounded/.test((d.className || "").toString()));
      });
    }
  }
  if (!panel) {
    const h = [...document.querySelectorAll("h2, h3")].find(x => /^Add (Income|Expense|Savings|Budget)|^Edit/.test((x.textContent || "").trim()));
    panel = h?.closest("div[class*='rounded'], div[class*='bg-white']") || undefined;
  }
  if (!panel) return JSON.stringify({ err: "no dialog open" });
  const pr = panel.getBoundingClientRect();
  out.panel = { w: Math.round(pr.width), h: Math.round(pr.height) };
  const cs = getComputedStyle(panel);
  out.panelBg = cs.backgroundColor;
  // header (sticky)
  const head = panel.querySelector("header") || panel.querySelector("div[class*='sticky']");
  if (head) {
    const hr = head.getBoundingClientRect();
    const hcs = getComputedStyle(head);
    out.header = { h: Math.round(hr.height), pos: hcs.position, bg: hcs.backgroundColor, pt: hcs.paddingTop, pb: hcs.paddingBottom, px: hcs.paddingLeft };
  }
  // form field labels (lucide Label = label tag or [data-radix-label])
  out.labels = [...panel.querySelectorAll("label")].slice(0, 10).map(l => {
    const lcs = getComputedStyle(l);
    return { text: (l.textContent || "").trim().slice(0, 30), fs: lcs.fontSize, fw: lcs.fontWeight, color: lcs.color, mb: lcs.marginBottom, display: lcs.display };
  });
  // text inputs
  out.inputs = [...panel.querySelectorAll("input:not([type='hidden'])")].slice(0, 8).map(i => {
    const ics = getComputedStyle(i);
    return {
      type: i.type, ph: (i.placeholder || "").slice(0, 20),
      h: Math.round(i.getBoundingClientRect().height), w: Math.round(i.getBoundingClientRect().width),
      fs: ics.fontSize, color: ics.color, bg: ics.backgroundColor,
      border: ics.borderColor, bw: ics.borderWidth, radius: ics.borderRadius,
      phColor: ics.color, pad: ics.padding, tag: i.tagName,
    };
  });
  // textareas
  out.textareas = [...panel.querySelectorAll("textarea")].map(t => {
    const tcs = getComputedStyle(t);
    return { h: Math.round(t.getBoundingClientRect().height), w: Math.round(t.getBoundingClientRect().width), fs: tcs.fontSize, rows: t.rows, ph: (t.placeholder || "").slice(0, 30), color: tcs.color };
  });
  // selects (radix Select trigger = button with chevron; native = select)
  const selTriggers = [...panel.querySelectorAll("button[role='combobox'], select")];
  out.selects = selTriggers.slice(0, 5).map(s => {
    const scs = getComputedStyle(s);
    const sr = s.getBoundingClientRect();
    return { tag: s.tagName, role: s.getAttribute("role"), text: (s.textContent || "").trim().slice(0, 24), h: Math.round(sr.height), w: Math.round(sr.width), fs: scs.fontSize, color: scs.color, bg: scs.backgroundColor, border: scs.borderColor, radius: scs.borderRadius, pad: scs.padding };
  });
  // classification radio tiles (role=radio or input[type=radio] wrapped in labels)
  const radios = [...panel.querySelectorAll("[role='radio'], input[type='radio']")];
  out.radios = radios.slice(0, 5).map(rd => {
    const wrap = rd.closest("label, div[class*='cursor-pointer']") || rd;
    const wcs = getComputedStyle(wrap);
    const wr = wrap.getBoundingClientRect();
    return {
      value: rd.getAttribute("value") || rd.getAttribute("data-value") || "",
      checked: rd.getAttribute("aria-checked") === "true" || rd.checked,
      wrapW: Math.round(wr.width), wrapH: Math.round(wr.height),
      wrapBg: wcs.backgroundColor, wrapBorder: wcs.borderColor, wrapRadius: wcs.borderRadius,
      text: (wrap.textContent || "").trim().slice(0, 16), fw: wcs.fontWeight,
    };
  });
  // the recurring switch
  const sw = panel.querySelector("[role='switch'], button[aria-haspopup]");
  if (sw && sw.getAttribute("role") === "switch") {
    const swcs = getComputedStyle(sw);
    const swr = sw.getBoundingClientRect();
    out.switch = { w: Math.round(swr.width), h: Math.round(swr.height), bg: swcs.backgroundColor, radius: swcs.borderRadius, checked: sw.getAttribute("aria-checked") };
    const thumb = sw.querySelector("[data-state], span[class*='translate']");
    if (thumb) {
      const tcs = getComputedStyle(thumb);
      const tr = thumb.getBoundingClientRect();
      out.switchThumb = { w: Math.round(tr.width), h: Math.round(tr.height), bg: tcs.backgroundColor };
    }
  } else {
    out.switch = null;
  }
  // helper/description texts
  out.descriptions = [...panel.querySelectorAll("p, span, div")].filter(el => el.children.length === 0 && (el.className || "").toString().match(/text-xs|text-\[10px\]|text-muted|text-gray|text-zinc|text-slate/i)).slice(0, 6).map(el => {
    const ecs = getComputedStyle(el);
    return { text: (el.textContent || "").trim().slice(0, 40), fs: ecs.fontSize, color: ecs.color, cls: (el.className || "").toString().slice(0, 80) };
  });
  // footer row (v8 pin — regression check)
  const footerBtns = [...panel.querySelectorAll("footer button, div[class*='pt-4'] button, button")].filter(b => /^(Cancel|Save|Delete)/.test((b.textContent || "").trim())).slice(0, 4);
  out.footerButtons = footerBtns.map(b => {
    const bcs = getComputedStyle(b);
    const br = b.getBoundingClientRect();
    return { text: (b.textContent || "").trim().slice(0, 18), w: Math.round(br.width), h: Math.round(br.height), bg: bcs.backgroundColor, color: bcs.color, border: bcs.borderColor, radius: bcs.borderRadius, fw: bcs.fontWeight };
  });
  return JSON.stringify(out, null, 1);
})()
