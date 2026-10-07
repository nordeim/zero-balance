// probe-v7-headings.mjs — heading outline + logo placement
(() => {
  const out = { url: location.pathname };
  out.headings = [...document.querySelectorAll("h1,h2,h3,h4")].slice(0, 14).map(h => ({
    tag: h.tagName,
    text: h.textContent?.trim().slice(0, 44),
    cls: (h.className || "").toString().slice(0, 60),
  }));
  // logo block: the element containing the app name in the rail/topbar
  const logo = [...document.querySelectorAll("h1,h2,span,div,a")].find(el => el.children.length === 0 && /^ZeroBalance$/.test(el.textContent?.trim() || ""));
  if (logo) {
    const cs = getComputedStyle(logo);
    out.logo = {
      tag: logo.tagName,
      cls: (logo.className || "").toString().slice(0, 80),
      size: cs.fontSize, weight: cs.fontWeight, color: cs.color,
      parent: (logo.parentElement?.className || "").toString().slice(0, 80),
    };
  }
  return JSON.stringify(out, null, 1);
})()
