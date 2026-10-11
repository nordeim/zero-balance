// v43: the drill-down detail probe — the fresh-query chevron rotation (the
// saved node goes stale on re-render), the LABEL spans' fonts at every
// level (the container fonts read the inherited 16px on both sites — the
// labels are the parity surface), and the category dot.
// bash scripts/parity-probes/run-probe.sh <session> scripts/parity-probes/exp-detail-v43.mjs
(async () => {
  const leaf = (txt) =>
    [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(
      (e) => (e.textContent || '').trim() === txt && e.children.length === 0,
    );
  const bdH = leaf('Net Zero Breakdown');
  const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
  if (!card) return JSON.stringify({ found: false });

  // The section button: expand it, then FRESH-query its chevron.
  const sectionBtn = [...card.querySelectorAll('button,[role="button"]')].find(
    (b) => /Total Income/i.test(b.textContent || ''),
  );
  if (!sectionBtn) return JSON.stringify({ found: false, step: 'btn' });
  // Label span: the deepest span holding the literal label text.
  const labelOf = (row) =>
    [...row.querySelectorAll('span')].find((s) => {
      const t = (s.textContent || '').trim();
      return t.length > 1 && s.children.length === 0 && !/^\$/.test(t);
    }) || null;
  const labelChrome = (span) => {
    if (!span) return null;
    const cs = getComputedStyle(span);
    return { font: cs.fontSize, weight: cs.fontWeight, color: cs.color, lh: cs.lineHeight };
  };
  const amountOf = (row) =>
    [...row.querySelectorAll('span')].filter((s) => /^\$/.test((s.textContent || '').trim()) && s.children.length === 0).pop() || null;

  const secLabelBefore = labelChrome(labelOf(sectionBtn));
  const secAmtBefore = labelChrome(amountOf(sectionBtn));
  sectionBtn.click();
  await new Promise((r) => setTimeout(r, 500));

  // FRESH chevron query: the last svg inside the (re-rendered) button.
  const chevsNow = [...sectionBtn.querySelectorAll('svg')];
  const chevNow = chevsNow[chevsNow.length - 1];
  const chevCs = chevNow ? getComputedStyle(chevNow) : null;
  const secLabelAfter = labelChrome(labelOf(sectionBtn));
  const secAmtAfter = labelChrome(amountOf(sectionBtn));

  // Category row: fresh query (the DOM re-rendered).
  const catRows = [...card.querySelectorAll('button,[role="button"]')].filter(
    (b) => b.offsetParent !== null && b !== sectionBtn && /\$/.test(b.textContent || ''),
  );
  const catRow = catRows[0] || null;
  const catLabel = catRow ? labelChrome(labelOf(catRow)) : null;
  const catAmt = catRow ? labelChrome(amountOf(catRow)) : null;
  // Category dot: the smallest rounded span inside the row.
  const catDot = catRow
    ? [...catRow.querySelectorAll('span')].filter((s) => {
        const r = s.getBoundingClientRect();
        return r.width > 0 && r.width <= 10 && getComputedStyle(s).borderRadius === '9999px';
      })[0] || null
    : null;
  const catDotCs = catDot ? { w: Math.round(catDot.getBoundingClientRect().width), bg: getComputedStyle(catDot).backgroundColor } : null;
  const catChev = catRow ? [...catRow.querySelectorAll('svg')].pop() : null;
  const catChevBefore = catChev ? getComputedStyle(catChev).transform : null;
  if (catRow) {
    catRow.click();
    await new Promise((r) => setTimeout(r, 500));
  }
  const catChevAfter = catRow ? (getComputedStyle([...catRow.querySelectorAll('svg')].pop()) || {}).transform : null;

  // Sub row + item row: fresh flex rows inside the opened category.
  const subArea = catRow
    ? [...catRow.parentElement.children].find((c) => c !== catRow && c.getBoundingClientRect().height > 0)
    : null;
  const rows = subArea
    ? [...subArea.querySelectorAll('div')].filter((d) => {
        const cs = getComputedStyle(d);
        return cs.display === 'flex' && d.children.length >= 2 && Math.round(d.getBoundingClientRect().height) >= 16 && !d.closest('button,[role="button"]');
      })
    : [];
  const subRow = rows[0] || null;
  const itemRow = rows[rows.length - 1] || null;
  const subLabel = subRow ? labelChrome(labelOf(subRow)) : null;
  const subAmt = subRow ? labelChrome(amountOf(subRow)) : null;
  const subBg = subRow ? getComputedStyle(subRow).backgroundColor : null;
  const subDot = subRow
    ? [...subRow.querySelectorAll('span')].filter((s) => {
        const r = s.getBoundingClientRect();
        return r.width > 0 && r.width <= 8 && getComputedStyle(s).borderRadius === '9999px';
      })[0] || null
    : null;
  const subDotCs = subDot ? { w: Math.round(subDot.getBoundingClientRect().width), bg: getComputedStyle(subDot).backgroundColor, opacity: getComputedStyle(subDot).opacity } : null;
  const itemLabel = itemRow ? labelChrome(labelOf(itemRow)) : null;
  const itemAmt = itemRow ? labelChrome(amountOf(itemRow)) : null;
  const itemColor = itemRow ? getComputedStyle(itemRow).color : null;
  const itemDot = itemRow
    ? [...itemRow.querySelectorAll('span')].filter((s) => {
        const r = s.getBoundingClientRect();
        return r.width > 0 && r.width <= 6 && getComputedStyle(s).borderRadius === '9999px';
      })[0] || null
    : null;
  const itemDotCs = itemDot ? { w: Math.round(itemDot.getBoundingClientRect().width), opacity: getComputedStyle(itemDot).opacity } : null;

  // The truncate guard on the item label.
  const itemLabelSpan = itemRow ? labelOf(itemRow) : null;
  const truncCs = itemLabelSpan ? getComputedStyle(itemLabelSpan) : null;
  const trunc = truncCs ? { maxW: truncCs.maxWidth, overflow: truncCs.overflow, textOverflow: truncCs.textOverflow } : null;

  return JSON.stringify({
    found: true,
    sec: { labelBefore: secLabelBefore, labelAfter: secLabelAfter, amtBefore: secAmtBefore, amtAfter: secAmtAfter },
    chev: chevCs ? { transform: chevCs.transform, w: Math.round(chevNow.getBoundingClientRect().width), transition: chevCs.transitionProperty, transitionDur: chevCs.transitionDuration } : null,
    cat: { label: catLabel, amt: catAmt, dot: catDotCs, chevBefore: catChevBefore, chevAfter: catChevAfter },
    sub: { label: subLabel, amt: subAmt, bg: subBg, dot: subDotCs },
    item: { label: itemLabel, amt: itemAmt, color: itemColor, dot: itemDotCs, trunc },
  });
})()
