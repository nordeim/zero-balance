// Dump quick-action cards + legend + guidelines raw HTML
(() => {
  const out = {};
  // quick-action cards: divs with class containing rounded-2xl and text starting "Add "
  const qa = [...document.querySelectorAll('div')].filter((d) => {
    const cls = d.className || '';
    return typeof cls === 'string' && cls.includes('rounded-2xl') && cls.includes('group') && /^Add /.test((d.textContent || '').trim()) && d.children.length >= 1 && d.closest('[data-quick-action]') === null && !d.querySelector('div.rounded-2xl.group');
  });
  out.quickActions = qa.slice(0, 4).map((d) => ({ text: (d.textContent || '').trim().slice(0, 60), html: d.outerHTML.replace(/\s+/g, ' ').slice(0, 1200) }));

  const sbH = [...document.querySelectorAll('h3')].find((x) => (x.textContent || '').trim() === 'Spending Breakdown');
  if (sbH) {
    // walk up to card root
    let card = sbH;
    while (card.parentElement && !/rounded-2xl/.test(card.className || '')) card = card.parentElement;
    // legend rows: after the chart
    const rows = [...card.querySelectorAll('div')].filter((d) => /rgb\(245, 248, 245\)|#f5f8f5/.test(getComputedStyle(d).backgroundColor));
    out.legendRows = rows.map((r) => r.outerHTML.replace(/\s+/g, ' ').slice(0, 1300));
    const sectors = [...card.querySelectorAll('.recharts-sector')].map((s) => s.getAttribute('fill'));
    out.sectorFills = sectors;
  }
  const glH = [...document.querySelectorAll('h3')].find((x) => (x.textContent || '').trim() === 'Budget Guidelines');
  if (glH) {
    let card = glH;
    while (card.parentElement && !/rounded-2xl/.test(card.className || '')) card = card.parentElement;
    out.guidelinesHTML = card.outerHTML.replace(/\s+/g, ' ').slice(0, 3000);
  }
  return out;
})()
