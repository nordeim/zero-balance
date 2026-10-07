// probe-v7-navstruct.mjs — nav element structure + label + list on both sides
(() => {
  const out = {};
  out.hasNav = !!document.querySelector("nav");
  out.navAriaLabel = document.querySelector("nav")?.getAttribute("aria-label");
  // find the "Navigation" label text anywhere in the fixed rail
  const all = [...document.querySelectorAll("aside *, body > div.fixed *")];
  const label = all.find(el => el.children.length === 0 && /^Navigation$/i.test(el.textContent?.trim() || ""));
  if (label) {
    const cs = getComputedStyle(label);
    out.navLabel = {
      tag: label.tagName, cls: (label.className || "").toString().slice(0, 90),
      size: cs.fontSize, weight: cs.fontWeight, color: cs.color,
      tracking: cs.letterSpacing, transform: cs.textTransform,
      h: label.getBoundingClientRect().height, w: label.getBoundingClientRect().width,
    };
    out.navLabelParent = (label.parentElement?.className || "").toString().slice(0, 90);
  } else out.navLabel = null;
  // the ul list container
  const ul = document.querySelector("nav ul") || [...document.querySelectorAll("ul")].find(u => u.querySelector('a[href="/dashboard"]'));
  if (ul) {
    const cs = getComputedStyle(ul);
    out.ul = { cls: (ul.className || "").toString().slice(0, 90), gap: cs.gap, display: cs.display, count: ul.children.length };
  }
  return JSON.stringify(out, null, 1);
})()
