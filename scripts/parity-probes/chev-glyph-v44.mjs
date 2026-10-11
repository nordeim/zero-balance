// v44: DOM-verify the VLM's chevron-direction flag — the reference's
// section chevron in COLLAPSED vs EXPANDED states: the svg's lucide class
// (the glyph identity: chevron-down vs chevron-up) + the path shape.
(async () => {
  const leaf = (txt) =>
    [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(
      (e) => (e.textContent || '').trim() === txt && e.children.length === 0,
    );
  const bdH = leaf('Net Zero Breakdown');
  const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
  if (!card) return JSON.stringify({ found: false });
  const out = {};
  const sectionBtn = [...card.querySelectorAll('button,[role="button"]')].find(
    (b) => /Total Income/i.test(b.textContent || ''),
  );
  const readChev = (btn) => {
    const svgs = [...btn.querySelectorAll('svg')];
    const chev = svgs[svgs.length - 1];
    if (!chev) return null;
    return {
      cls: (chev.getAttribute('class') || '').slice(0, 50),
      path: (chev.querySelector('path')?.getAttribute('d') || chev.innerHTML.slice(0, 60)),
      rotate: getComputedStyle(chev).rotate,
      h: Math.round(chev.getBoundingClientRect().height),
    };
  };
  out.collapsed = readChev(sectionBtn);
  sectionBtn.click();
  await new Promise((r) => setTimeout(r, 600));
  out.expanded = readChev(sectionBtn);
  // collapse back and re-read
  sectionBtn.click();
  await new Promise((r) => setTimeout(r, 600));
  out.recollapsed = readChev(sectionBtn);
  return JSON.stringify(out);
})()
