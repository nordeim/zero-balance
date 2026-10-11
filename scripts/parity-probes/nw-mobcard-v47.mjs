(async () => {
  // v47: the net-worth ASSET CARD's MOBILE census at 390 (the v46 fix's
  // mobile follow-up). On the CLONE: the grid is found by its
  // grid-cols-1 + md:grid-cols-2 + lg:grid-cols-3 class family; the
  // value margin lives ON the P (the v46 fix). On the REFERENCE: the
  // grid is `grid md:grid-cols-2 lg:grid-cols-3 gap-4` (NO grid-cols-1
  // — see ref-v47.sh's finder) and the value is wrapped in div.mb-4 —
  // the computed geometry is the contract, the DOM shape is not.
  const grid = [...document.querySelectorAll("div")].find(
    (d) =>
      d.className.toString().includes("md:grid-cols-2") &&
      d.className.toString().includes("lg:grid-cols-3") &&
      d.querySelector("button"),
  );
  if (!grid) return "no grid";
  const card = grid.children[0];
  const cs = getComputedStyle(card);
  const r = card.getBoundingClientRect();
  const vp = card.querySelector("p.text-2xl");
  const facts = vp ? vp.nextElementSibling : null;
  return JSON.stringify({
    grid: {
      w: Math.round(grid.getBoundingClientRect().width),
      gap: getComputedStyle(grid).gap,
      cols: getComputedStyle(grid).gridTemplateColumns.split(" ").length,
    },
    card: {
      w: Math.round(r.width),
      h: Math.round(r.height),
      pad: cs.padding,
      radius: cs.borderRadius,
      border: cs.border,
      shadow: cs.boxShadow,
      transition: cs.transition,
    },
    value: vp
      ? {
          mb: getComputedStyle(vp).marginBottom,
          fs: getComputedStyle(vp).fontSize,
          lh: getComputedStyle(vp).lineHeight,
          color: getComputedStyle(vp).color,
          // the wrap-aware gap (the clone: P.mb; the reference: div.mb-4)
          wrapGap: (() => {
            const gapHost = vp.classList.contains("mb-4") ? vp : vp.parentElement;
            return gapHost ? getComputedStyle(gapHost).marginBottom : null;
          })(),
        }
      : null,
    facts: facts
      ? {
          fs: getComputedStyle(facts).fontSize,
          color: getComputedStyle(facts).color,
          gap: Math.round(facts.getBoundingClientRect().y - vp.getBoundingClientRect().bottom),
        }
      : null,
    docSW: document.documentElement.scrollWidth,
    mainSW: document.querySelector("main") ? document.querySelector("main").scrollWidth : null,
  });
})()
