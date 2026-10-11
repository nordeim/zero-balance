// v44: the section-band mount semantics — the exact outerHTML of the
// section root when collapsed vs expanded (truncated), so the clone's
// fix can match the reference's mount behavior precisely.
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
  const root = sectionBtn.parentElement;
  out.collapsed = {
    childCount: root.children.length,
    childTags: [...root.children].map((c) => c.tagName),
    html: root.outerHTML.slice(0, 700),
  };
  sectionBtn.click();
  await new Promise((r) => setTimeout(r, 600));
  const expandedChildren = [...root.children];
  out.expanded = {
    childCount: expandedChildren.length,
    childTags: expandedChildren.map((c) => c.tagName),
    bandStyle: expandedChildren
      .filter((c) => c !== sectionBtn)
      .map((c) => ({
        cls: (c.className || '').toString().slice(0, 40),
        style: (c.getAttribute('style') || '').slice(0, 80),
        h: Math.round(c.getBoundingClientRect().height),
      })),
  };
  // The inner structure of the band: its children + the inner indented div.
  const band = expandedChildren.find((c) => c !== sectionBtn);
  if (band) {
    out.bandChildren = [...band.children].map((c) => ({
      cls: (c.className || '').toString().slice(0, 60),
      style: (c.getAttribute('style') || '').slice(0, 60),
      h: Math.round(c.getBoundingClientRect().height),
    }));
  }
  // Collapse again and dump DURING the animation (~100ms in): the band's
  // style mid-collapse.
  sectionBtn.click();
  await new Promise((r) => setTimeout(r, 110));
  const midBand = [...root.children].find((c) => c !== sectionBtn);
  out.midCollapseBand = midBand
    ? {
        style: (midBand.getAttribute('style') || '').slice(0, 80),
        h: Math.round(midBand.getBoundingClientRect().height),
        opacity: getComputedStyle(midBand).opacity,
      }
    : 'UNMOUNTED ALREADY';
  await new Promise((r) => setTimeout(r, 500));
  const endBand = [...root.children].find((c) => c !== sectionBtn);
  out.endCollapseBand = endBand ? { style: (endBand.getAttribute('style') || '').slice(0, 80) } : 'UNMOUNTED';
  return JSON.stringify(out);
})()
