// v44: the reference's collapse-direction probe — does the expansion band
// animate when COLLAPSING too, and does the wrapper stay mounted (height 0)
// or unmount when collapsed? Drives the fix's mount semantics.
(async () => {
  const leaf = (txt) =>
    [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(
      (e) => (e.textContent || '').trim() === txt && e.children.length === 0,
    );
  const bdH = leaf('Net Zero Breakdown');
  const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
  if (!card) return JSON.stringify({ found: false });
  const out = {};

  // COLLAPSED DOM: does the section's expansion band exist before clicking?
  const sectionBtn = [...card.querySelectorAll('button,[role="button"]')].find(
    (b) => /Total Income/i.test(b.textContent || ''),
  );
  const wrap = sectionBtn.parentElement;
  const bandBefore = [...wrap.children].filter((c) => c !== sectionBtn);
  out.collapsedBand = bandBefore.map((c) => ({
    tag: c.tagName,
    h: Math.round(c.getBoundingClientRect().height),
    style: (c.getAttribute('style') || '').slice(0, 60),
    text: (c.textContent || '').replace(/\s+/g, ' ').slice(0, 20),
  }));
  out.collapsedCardH = Math.round(card.getBoundingClientRect().height);

  // Expand fully (section + category), then COLLAPSE the section while
  // sampling the card height — the collapse animation check.
  sectionBtn.click();
  await new Promise((r) => setTimeout(r, 600));
  const catBtn = [...card.querySelectorAll('button,[role="button"]')].find(
    (b) => /Salary/i.test(b.textContent || '') && b !== sectionBtn,
  );
  if (catBtn) {
    catBtn.click();
    await new Promise((r) => setTimeout(r, 600));
  }
  out.preCollapseH = Math.round(card.getBoundingClientRect().height);

  // COLLAPSE the section (second click) — sample.
  sectionBtn.click();
  const samples = [];
  for (let i = 0; i < 10; i++) {
    samples.push(Math.round(card.getBoundingClientRect().height));
    await new Promise((r) => setTimeout(r, 40));
  }
  out.collapseSamples = samples;
  out.postCollapseH = Math.round(card.getBoundingClientRect().height);

  // After collapse: is the band still in the DOM?
  const bandAfter = [...wrap.children].filter((c) => c !== sectionBtn);
  out.bandAfterCollapse = bandAfter.map((c) => ({
    tag: c.tagName,
    h: Math.round(c.getBoundingClientRect().height),
    style: (c.getAttribute('style') || '').slice(0, 60),
    text: (c.textContent || '').replace(/\s+/g, ' ').slice(0, 20),
  }));

  // The category-level wrapper when the SECTION is collapsed: still there?
  // (Re-expand the section, collapse only the category, check its wrapper.)
  sectionBtn.click();
  await new Promise((r) => setTimeout(r, 600));
  if (catBtn) {
    const catWrap = catBtn.parentElement;
    const before = [...catWrap.children].filter((c) => c !== catBtn);
    out.catBandBeforeCollapse = before.map((c) => ({
      h: Math.round(c.getBoundingClientRect().height),
      style: (c.getAttribute('style') || '').slice(0, 60),
    }));
    catBtn.click(); // collapse the category
    const catSamples = [];
    for (let i = 0; i < 8; i++) {
      catSamples.push(Math.round(card.getBoundingClientRect().height));
      await new Promise((r) => setTimeout(r, 40));
    }
    out.catCollapseSamples = catSamples;
    const after = [...catWrap.children].filter((c) => c !== catBtn);
    out.catBandAfterCollapse = after.map((c) => ({
      h: Math.round(c.getBoundingClientRect().height),
      style: (c.getAttribute('style') || '').slice(0, 60),
      text: (c.textContent || '').replace(/\s+/g, ' ').slice(0, 20),
    }));
  }
  return JSON.stringify(out);
})()
