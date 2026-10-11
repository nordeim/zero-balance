// v43: the drill-down + summary-card hover census — REAL pointer hovers
// (agent-browser mouse move) reading the computed hover backgrounds:
// (1) the breakdown section row (hover:bg-gray-50),
// (2) the breakdown category row (hover:bg-gray-100),
// (3) the net-worth gradient summary card (the queued "summary card's
//     hover/interaction states" — expected static on both sites).
// bash scripts/parity-probes/run-probe.sh <session> scripts/parity-probes/hover-v43.mjs
// NOTE: the hover POINTS are printed by the caller; this probe only READS
// the current computed styles — run it AFTER the mouse move.
(() => {
  const leaf = (txt) =>
    [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(
      (e) => (e.textContent || '').trim() === txt && e.children.length === 0,
    );
  const bdH = leaf('Net Zero Breakdown');
  const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
  const sectionBtn = card
    ? [...card.querySelectorAll('button,[role="button"]')].find((b) => /Total Income/i.test(b.textContent || ''))
    : null;
  const catRows = card
    ? [...card.querySelectorAll('button,[role="button"]')].filter(
        (b) => b.offsetParent !== null && b !== sectionBtn && /\$/.test(b.textContent || '') && !/Total|Net Balance/i.test(b.textContent || ''),
      )
    : [];
  const secCs = sectionBtn ? getComputedStyle(sectionBtn) : null;
  const catCs = catRows[0] ? getComputedStyle(catRows[0]) : null;
  // The net-worth summary card: only on /networth (null elsewhere).
  const nwLabel = [...document.querySelectorAll('p')].find((e) => (e.textContent || '').trim() === 'Total Net Worth');
  const nwCard = nwLabel ? nwLabel.closest('div[class*="rounded-2xl"]') : null;
  const nwCs = nwCard ? getComputedStyle(nwCard) : null;
  return JSON.stringify({
    section: secCs ? { bg: secCs.backgroundColor, boxShadow: secCs.boxShadow.slice(0, 60), cursor: secCs.cursor } : null,
    cat: catCs ? { bg: catCs.backgroundColor, cursor: catCs.cursor } : null,
    catCount: catRows.length,
    nwCard: nwCs ? { bg: nwCs.backgroundImage.slice(0, 50), shadow: nwCs.boxShadow.slice(0, 80), cursor: nwCs.cursor, transition: nwCs.transitionProperty } : 'NOT ON THIS PAGE',
  });
})()
