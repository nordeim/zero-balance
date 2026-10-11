// v43: the definitive drill-down micro-probe — reads the CSS `rotate`
// property (Tailwind v4's rotate-* emits the modern `rotate` property, NOT
// `transform` — the transform: none reading on both sites was meaningless,
// the classic v4 trap), the raw row HTML (the dot question: does the
// reference render the leading dots at all?), and the rows' rotate +
// border-radius in full.
// bash scripts/parity-probes/run-probe.sh <session> scripts/parity-probes/exp-rotate-v43.mjs
(async () => {
  const leaf = (txt) =>
    [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(
      (e) => (e.textContent || '').trim() === txt && e.children.length === 0,
    );
  const bdH = leaf('Net Zero Breakdown');
  const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
  if (!card) return JSON.stringify({ found: false });
  const rot = (svg) => {
    const cs = getComputedStyle(svg);
    return { rotate: cs.rotate, transform: cs.transform, scale: cs.scale };
  };

  // Section row: collapsed rotation first.
  const sectionBtn = [...card.querySelectorAll('button,[role="button"]')].find(
    (b) => /Total Income/i.test(b.textContent || ''),
  );
  if (!sectionBtn) return JSON.stringify({ found: false, step: 'btn' });
  const secChevBefore = rot([...sectionBtn.querySelectorAll('svg')].pop());
  const secHTML = sectionBtn.outerHTML.replace(/\s+/g, ' ').slice(0, 400);
  sectionBtn.click();
  await new Promise((r) => setTimeout(r, 500));
  const secChevAfter = rot([...sectionBtn.querySelectorAll('svg')].pop());

  // Category row: raw HTML + the dot hunt + rotation before/after expand.
  const catRows = [...card.querySelectorAll('button,[role="button"]')].filter(
    (b) => b.offsetParent !== null && b !== sectionBtn && /\$/.test(b.textContent || ''),
  );
  const catRow = catRows[0] || null;
  if (!catRow) return JSON.stringify({ found: false, step: 'cat', sec: { secChevBefore, secChevAfter } });
  const catHTML = catRow.outerHTML.replace(/\s+/g, ' ').slice(0, 500);
  const catChevBefore = rot([...catRow.querySelectorAll('svg')].pop());
  // Every child span of the row with its size + radius (the dot hunt).
  const catSpans = [...catRow.querySelectorAll('span')].map((s) => {
    const r = s.getBoundingClientRect();
    const cs = getComputedStyle(s);
    return {
      w: Math.round(r.width), h: Math.round(r.height),
      radius: cs.borderRadius, bg: cs.backgroundColor,
      text: (s.textContent || '').trim().slice(0, 12),
    };
  });
  catRow.click();
  await new Promise((r) => setTimeout(r, 500));
  const catChevAfter = rot([...catRow.querySelectorAll('svg')].pop());

  // Sub + item rows: raw HTML + spans + dots.
  const subArea = [...catRow.parentElement.children].find(
    (c) => c !== catRow && c.getBoundingClientRect().height > 0,
  );
  const flexRows = subArea
    ? [...subArea.querySelectorAll('div')].filter((d) => {
        const cs = getComputedStyle(d);
        return cs.display === 'flex' && d.children.length >= 2 && Math.round(d.getBoundingClientRect().height) >= 16;
      })
    : [];
  const subRow = flexRows[0] || null;
  const itemRow = flexRows[flexRows.length - 1] || null;
  const dump = (row) => {
    if (!row) return null;
    const spans = [...row.querySelectorAll('span')].map((s) => {
      const r = s.getBoundingClientRect();
      const cs = getComputedStyle(s);
      return {
        w: Math.round(r.width), h: Math.round(r.height),
        radius: cs.borderRadius, bg: cs.backgroundColor, opacity: cs.opacity,
        text: (s.textContent || '').trim().slice(0, 12),
      };
    });
    return {
      html: row.outerHTML.replace(/\s+/g, ' ').slice(0, 420),
      spans,
      bg: getComputedStyle(row).backgroundColor,
      ml: getComputedStyle(row).marginLeft,
      mt: getComputedStyle(row).marginTop,
    };
  };

  return JSON.stringify({
    found: true,
    secChevBefore, secChevAfter, secHTML,
    catChevBefore, catChevAfter, catHTML, catSpans,
    sub: dump(subRow),
    item: dump(itemRow),
  });
})()
