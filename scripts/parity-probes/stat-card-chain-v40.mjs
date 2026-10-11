(async () => {
  // v40: where do the "Total Income" texts live — tag/role/tabindex/rect of
  // every ancestor-ish element whose direct text contains Total Income /
  // Total Savings / Total Expenses, on both sites. Resolves which stat
  // surfaces are focusable on which site.
  const out = [];
  for (const label of ["Total Income", "Total Savings", "Total Expenses"]) {
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const hits = [];
    while (walker.nextNode()) {
      const t = walker.currentNode.textContent || "";
      if (t.includes(label)) {
        const el = walker.currentNode.parentElement;
        if (!el) continue;
        // climb to the card-level ancestor (the clickable one, if any)
        const chain = [];
        let p = el;
        for (let i = 0; i < 4 && p; i++) {
          const r = p.getBoundingClientRect();
          chain.push({
            tag: p.tagName.toLowerCase(),
            role: p.getAttribute("role"),
            ti: p.getAttribute("tabindex"),
            cls: (p.className || "").toString().slice(0, 40),
            rect: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
          });
          p = p.parentElement;
        }
        hits.push(chain);
      }
    }
    out.push({ label, hits: hits.slice(0, 2) });
  }
  return JSON.stringify(out);
})()
