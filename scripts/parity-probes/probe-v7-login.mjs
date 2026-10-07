// probe-v7-login.mjs — login card chrome dump
(() => {
  const out = {};
  const h1 = document.querySelector("h1");
  if (!h1) return JSON.stringify({ err: "no h1" });
  const hcs = getComputedStyle(h1);
  out.h1 = { text: h1.textContent, size: hcs.fontSize, weight: hcs.fontWeight, color: hcs.color, tracking: hcs.letterSpacing };
  // card container: walk up to the white rounded card
  let card = h1;
  while (card && card !== document.body) {
    const c = card.className?.toString?.() || "";
    const b = getComputedStyle(card).backgroundColor;
    if (/rounded/.test(c) && (b === "rgb(255, 255, 255)" || /bg-white/.test(c))) break;
    card = card.parentElement;
  }
  if (card && card !== document.body) {
    const ccs = getComputedStyle(card);
    out.card = {
      cls: (card.className || "").toString().slice(0, 110),
      w: Math.round(card.getBoundingClientRect().width),
      radius: ccs.borderRadius, border: ccs.borderTopWidth + " " + ccs.borderTopColor,
      shadow: ccs.boxShadow.slice(0, 60), padding: ccs.padding, bg: ccs.backgroundColor,
    };
  }
  // buttons in order
  out.buttons = [...document.querySelectorAll("button")].slice(0, 6).map(b => {
    const bc = getComputedStyle(b);
    return {
      text: (b.textContent || "").trim().slice(0, 28),
      w: Math.round(b.getBoundingClientRect().width), h: Math.round(b.getBoundingClientRect().height),
      bg: bc.backgroundColor, bgImage: bc.backgroundImage !== "none" ? "gradient" : "none",
      color: bc.color, radius: bc.borderRadius,
    };
  });
  // inputs
  out.inputs = [...document.querySelectorAll("input")].map(i => {
    const cs = getComputedStyle(i);
    return { type: i.type, ph: (i.placeholder || "").slice(0, 30), h: Math.round(i.getBoundingClientRect().height), radius: cs.borderRadius };
  });
  // page background + outer layout
  const body = document.body;
  out.page = { bg: getComputedStyle(body).backgroundColor, minH: getComputedStyle(body).minHeight };
  // footer links (sign up / forgot)
  out.links = [...document.querySelectorAll("button, a")].filter(el => /sign up|forgot|password/i.test(el.textContent || "")).map(el => ({ text: (el.textContent || "").trim().slice(0, 40), tag: el.tagName, cls: (el.className || "").toString().slice(0, 60) }));
  // brand image at top?
  const img = document.querySelector("img");
  out.img = img ? { src: img.src.split("/").pop()?.slice(0, 40), w: Math.round(img.getBoundingClientRect().width), alt: img.alt } : null;
  return JSON.stringify(out, null, 1);
})()
