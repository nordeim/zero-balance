// v44 debug: dump the reference's drill-down sub-band + the donut legend DOM
// structure so the census filters can be structure-agnostic-correct.
(async () => {
  const leaf = (txt) =>
    [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(
      (e) => (e.textContent || '').trim() === txt && e.children.length === 0,
    );
  const out = {};

  // --- drill-down sub band ---
  const bdH = leaf('Net Zero Breakdown');
  const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
  if (card) {
    const sectionBtn = [...card.querySelectorAll('button,[role="button"]')].find(
      (b) => /Total Income/i.test(b.textContent || ''),
    );
    if (sectionBtn) {
      sectionBtn.click();
      await new Promise((r) => setTimeout(r, 400));
      const catBtn = [...card.querySelectorAll('button,[role="button"]')].find(
        (b) => /Salary/i.test(b.textContent || '') && b !== sectionBtn,
      );
      if (catBtn) {
        catBtn.click();
        await new Promise((r) => setTimeout(r, 400));
        out.catWrapTag = catBtn.parentElement.tagName;
        out.catWrapChildren = [...catBtn.parentElement.children].map((c) => ({
          tag: c.tagName,
          cls: (c.className || '').toString().slice(0, 60),
          h: Math.round(c.getBoundingClientRect().height),
          text: (c.textContent || '').replace(/\s+/g, ' ').slice(0, 30),
        }));
        const subArea = [...catBtn.parentElement.children].find(
          (c) => c !== catBtn && c.getBoundingClientRect().height > 0,
        );
        if (subArea) {
          out.subAreaTag = subArea.tagName;
          out.subAreaCls = (subArea.className || '').toString().slice(0, 60);
          out.subAreaHTML = subArea.outerHTML.slice(0, 1200);
        }
      }
    }
  }

  // --- donut legend ---
  const head = [...document.querySelectorAll('div,p,span,h1,h2,h3,h4')].find(
    (e) => (e.textContent || '').trim() === 'Spending Breakdown' && e.children.length === 0,
  );
  const dcard = head ? head.closest('div[class*="rounded"]') : null;
  if (dcard) {
    // the rows below the donut: any element whose text contains a label + a $ amount
    const rowish = [...dcard.querySelectorAll('div')].filter((d) => {
      const t = (d.textContent || '').replace(/\s+/g, ' ');
      return /(Need|Want|Savings)/.test(t) && /\$\d/.test(t);
    });
    // the OUTERMOST rowish containers
    const outer = rowish.filter((d) => !rowish.includes(d.parentElement));
    out.legendOuter = outer.slice(0, 3).map((d) => ({
      tag: d.tagName,
      cls: (d.className || '').toString().slice(0, 80),
      h: Math.round(d.getBoundingClientRect().height),
      kids: d.children.length,
      text: (d.textContent || '').replace(/\s+/g, ' ').slice(0, 30),
    }));
    if (outer.length) {
      out.legendFirstHTML = outer[0].outerHTML.slice(0, 1400);
      out.legendParentCls = (outer[0].parentElement.className || '').toString().slice(0, 80);
    }
  }
  return JSON.stringify(out);
})()
