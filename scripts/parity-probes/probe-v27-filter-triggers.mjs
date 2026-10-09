// v27 sweep: read the focus-family CLASSES of the items-view filter triggers
// (the "All Categories" / "All Frequencies" shadcn Select buttons).
(() => {
  const triggers = [...document.querySelectorAll("button")].filter((b) =>
    /all (categories|frequencies)/i.test((b.textContent || "").trim()),
  );
  const out = triggers.slice(0, 2).map((b) => {
    const cs = getComputedStyle(b);
    const r = b.getBoundingClientRect();
    return {
      txt: (b.textContent || "").trim().slice(0, 16),
      w: Math.round(r.width),
      h: Math.round(r.height),
      cls: (b.className || "").toString(),
      restShadow: cs.boxShadow.slice(0, 60),
    };
  });
  return JSON.stringify(out, null, 1);
})()
