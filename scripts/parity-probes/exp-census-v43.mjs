// v43: the drill-down EXPANDED-state census — the v42 session's queued
// surface: the collapsed-state pin exists (the v42 F2 census), but the
// expanded categories/subcategories/items bands were never measured.
// Expands the Total Income section + its first category, then reads the
// per-row chrome on BOTH sites (row CHROME, not row COUNT — the datasets
// differ; the chrome is the parity surface). UI-state-only clicks: the
// drill-down expansion mutates no data (the same discipline as v29/v32).
// bash scripts/parity-probes/run-probe.sh <session> scripts/parity-probes/exp-census-v43.mjs
(async () => {
  const leaf = (txt) =>
    [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(
      (e) => (e.textContent || '').trim() === txt && e.children.length === 0,
    );
  const bdH = leaf('Net Zero Breakdown');
  const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
  if (!card) return JSON.stringify({ found: false, step: 'card' });
  const collapsedH = Math.round(card.getBoundingClientRect().height);

  // The section toggle: the clickable row containing "Total Income".
  const sectionBtn = [...card.querySelectorAll('button,[role="button"]')].find(
    (b) => /Total Income/i.test(b.textContent || ''),
  );
  if (!sectionBtn) return JSON.stringify({ found: false, step: 'sectionBtn' });
  const sR = sectionBtn.getBoundingClientRect();
  const sCs = getComputedStyle(sectionBtn);
  const sectionChrome = {
    h: Math.round(sR.height),
    pad: sCs.padding,
    ml: sCs.marginLeft,
    mr: sCs.marginRight,
    radius: sCs.borderRadius,
    font: sCs.fontSize,
    weight: sCs.fontWeight,
    cursor: sCs.cursor,
    transition: sCs.transitionProperty,
    bg: sCs.backgroundColor,
    ariaExpanded: sectionBtn.getAttribute('aria-expanded'),
  };
  const chevs = [...sectionBtn.querySelectorAll('svg')];
  const chev = chevs[chevs.length - 1];
  const chevBefore = chev
    ? {
        w: Math.round(chev.getBoundingClientRect().width),
        h: Math.round(chev.getBoundingClientRect().height),
        transform: getComputedStyle(chev).transform,
        color: getComputedStyle(chev).color,
      }
    : null;

  // EXPAND the section (UI-state only).
  sectionBtn.click();
  await new Promise((r) => setTimeout(r, 500));

  const secExpandedH = Math.round(card.getBoundingClientRect().height);
  const chevAfter = chev
    ? { transform: getComputedStyle(chev).transform, ariaExpanded: sectionBtn.getAttribute('aria-expanded') }
    : null;

  // The expanded area: whatever appeared after the button inside its wrapper.
  const wrap = sectionBtn.parentElement;
  const expArea = wrap ? [...wrap.children].find((c) => c !== sectionBtn && c.getBoundingClientRect().height > 0) : null;
  if (!expArea) return JSON.stringify({ found: false, step: 'expArea' });
  // The inner band container (the clone: overflow-hidden > ml-10 div).
  const inner = expArea.children.length ? expArea : expArea;
  const innerCs = getComputedStyle(inner);
  const expBox = {
    w: Math.round(expArea.getBoundingClientRect().width),
    h: Math.round(expArea.getBoundingClientRect().height),
    ml: innerCs.marginLeft,
    mt: innerCs.marginTop,
    mb: innerCs.marginBottom,
  };

  // Category rows: the clickable rows inside the expanded area.
  const catRows = [...inner.querySelectorAll('button,[role="button"]')].filter(
    (b) => b.offsetParent !== null && b !== sectionBtn,
  );
  const catChrome = (row) => {
    const r = row.getBoundingClientRect();
    const cs = getComputedStyle(row);
    const dot = row.querySelector('span[class*="rounded"], span > span');
    const dotR = dot ? dot.getBoundingClientRect() : null;
    const ch = [...row.querySelectorAll('svg')];
    const lastCh = ch[ch.length - 1];
    return {
      h: Math.round(r.height),
      pad: cs.padding,
      radius: cs.borderRadius,
      bg: cs.backgroundColor,
      font: cs.fontSize,
      weight: cs.fontWeight,
      color: cs.color,
      cursor: cs.cursor,
      transition: cs.transitionProperty,
      dot: dotR ? { w: Math.round(dotR.width), h: Math.round(dotR.height), radius: getComputedStyle(dot).borderRadius } : null,
      chev: lastCh ? { w: Math.round(lastCh.getBoundingClientRect().width), transform: getComputedStyle(lastCh).transform } : null,
      ariaExpanded: row.getAttribute('aria-expanded'),
      text: (row.textContent || '').replace(/\s+/g, ' ').slice(0, 28),
    };
  };
  const catList = catRows.slice(0, 4).map(catChrome);

  // EXPAND the first category (UI-state only).
  if (catRows.length) {
    catRows[0].click();
    await new Promise((r) => setTimeout(r, 500));
  }
  const fullExpandedH = Math.round(card.getBoundingClientRect().height);

  // The subcategory band: the rows that appeared under the first category.
  const firstCatWrap = catRows.length ? catRows[0].parentElement : null;
  const subArea = firstCatWrap
    ? [...firstCatWrap.children].find((c) => c !== catRows[0] && c.getBoundingClientRect().height > 0)
    : null;
  const subBox = subArea
    ? {
        w: Math.round(subArea.getBoundingClientRect().width),
        h: Math.round(subArea.getBoundingClientRect().height),
        ml: getComputedStyle(subArea).marginLeft,
        mt: getComputedStyle(subArea).marginTop,
      }
    : null;
  // Sub rows + item rows: the flex rows inside the sub band, read directly.
  const flexRows = subArea
    ? [...subArea.querySelectorAll('*')].filter((el) => {
        const cs = getComputedStyle(el);
        return cs.display === 'flex' && el.children.length >= 2 && Math.round(el.getBoundingClientRect().height) >= 16;
      })
    : [];
  const rowChrome = (row) => {
    const r = row.getBoundingClientRect();
    const cs = getComputedStyle(row);
    const dot = row.querySelector('span');
    const dotR = dot ? dot.getBoundingClientRect() : null;
    return {
      h: Math.round(r.height),
      pad: cs.padding,
      bg: cs.backgroundColor,
      font: cs.fontSize,
      weight: cs.fontWeight,
      color: cs.color,
      ml: cs.marginLeft,
      dot: dotR ? { w: Math.round(dotR.width), h: Math.round(dotR.height), opacity: getComputedStyle(dot).opacity } : null,
      text: (row.textContent || '').replace(/\s+/g, ' ').slice(0, 28),
      childCount: row.children.length,
    };
  };
  const subList = flexRows.slice(0, 3).map(rowChrome);
  const itemList = flexRows.slice(3, 6).map(rowChrome);

  // The section footer: the "N categories" row.
  const footP = [...card.querySelectorAll('p,span')].find((e) =>
    /categor/i.test(e.textContent || '') && e.children.length === 0 && e.closest('div') !== card,
  );
  const footRow = footP ? footP.closest('div') : null;
  const footChrome = footRow
    ? (() => {
        const r = footRow.getBoundingClientRect();
        const cs = getComputedStyle(footRow);
        return {
          h: Math.round(r.height),
          pad: cs.padding,
          borderTop: cs.borderTopWidth,
          font: getComputedStyle(footP).fontSize,
          weight: getComputedStyle(footP).fontWeight,
          text: (footRow.textContent || '').replace(/\s+/g, ' ').slice(0, 32),
        };
      })()
    : null;

  // The truncate guard: the item label max-width class check (clone-only
  // chrome — the reference item labels read computed too).
  const trunc = [...card.querySelectorAll('span')].find((s) => {
    const cs = getComputedStyle(s);
    return cs.textOverflow === 'ellipsis' && cs.overflow === 'hidden' && s.closest('div') === (flexRows[4] || flexRows[2] || card);
  });
  const truncChrome = trunc
    ? { maxW: getComputedStyle(trunc).maxWidth, w: Math.round(trunc.getBoundingClientRect().width), font: getComputedStyle(trunc).fontSize }
    : null;

  return JSON.stringify({
    found: true,
    card: { collapsedH, secExpandedH, fullExpandedH },
    section: sectionChrome,
    chev: { before: chevBefore, after: chevAfter },
    expBox,
    cats: { count: catRows.length, list: catList },
    subBox,
    subList,
    itemList,
    foot: footChrome,
    trunc: truncChrome,
    sw: document.documentElement.scrollWidth,
  });
})()
