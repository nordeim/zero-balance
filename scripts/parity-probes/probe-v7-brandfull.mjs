// probe-v7-brandfull.mjs — full brand block + nav label + user footer dump
(() => {
  const out = {};
  const h2 = [...document.querySelectorAll("h2")].find(h => h.textContent?.trim() === "ZeroBalance");
  const container = h2?.closest("div.flex.flex-col") || h2?.parentElement?.parentElement;
  if (container) {
    out.containerHTML = container.innerHTML.replace(/\s+/g, " ").slice(0, 900);
    // subtitle under the row?
    const kids = [...container.children].map(k => ({
      tag: k.tagName, cls: (k.className || "").toString().slice(0, 70),
      text: k.textContent?.trim().slice(0, 40),
    }));
    out.containerChildren = kids;
  }
  // nav section label above the links
  const nav = document.querySelector("nav");
  if (nav) {
    const firstDiv = nav.querySelector("div");
    if (firstDiv) {
      const cs = getComputedStyle(firstDiv);
      out.navLabel = {
        text: firstDiv.textContent?.trim(),
        cls: (firstDiv.className || "").toString().slice(0, 90),
        size: cs.fontSize, weight: cs.fontWeight, color: cs.color,
        tracking: cs.letterSpacing, transform: cs.textTransform, h: firstDiv.getBoundingClientRect().height,
      };
    }
  }
  // user footer
  const footer = [...document.querySelectorAll("aside div")].find(d => /border-t/.test(d.className || ""));
  if (footer) out.footerText = footer.textContent?.trim().replace(/\s+/g, " ").slice(0, 80);
  return JSON.stringify(out, null, 1);
})()
