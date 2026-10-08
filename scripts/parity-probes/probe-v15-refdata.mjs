// probe-v15-refdata.mjs — reference data-state drift check (the session-13+ pattern):
// hero figure/allocation, stat cards, legend rows, breakdown totals, net-worth figures.
(() => {
  const out = {};
  const vis = (el) => el && el.getBoundingClientRect().height > 0;
  // hero: the big net figure + allocation line
  const main = document.querySelector('main');
  const allText = main ? [...main.querySelectorAll('h1,h2,h3,p,div,span')].filter(vis) : [];
  const findText = (re) => allText.find((el) => re.test(el.textContent) && el.children.length <= 2);
  const hero = findText(/\+\$?\d[\d,]*\.\d{2}|NET ZERO|Over Budget|Under Budget/i);
  out.hero = hero ? hero.textContent.trim().slice(0, 60) : null;
  const alloc = findText(/\d+(\.\d+)?%/);
  out.allocation = alloc ? alloc.textContent.trim().slice(0, 40) : null;
  // stat cards: Income/Savings/Expenses totals
  for (const label of ['Income', 'Savings', 'Expenses']) {
    const el = allText.reverse().find((e) => e.textContent.trim() === label);
    allText.reverse();
    if (el) {
      const card = el.closest('div');
      out['stat_' + label] = card ? card.textContent.trim().replace(/\s+/g, ' ').slice(0, 50) : null;
    }
  }
  // legend rows (donut)
  out.legend = allText.filter((e) => /^(Need|Want|Savings)\s*\$/.test(e.textContent.replace(/\s+/g, ' ').trim())).map((e) => e.textContent.replace(/\s+/g, ' ').trim().slice(0, 30));
  // count item cards on each visible page anchor is not possible here; capture totals row of breakdown
  const nb = findText(/Net Balance/i);
  out.netBalance = nb ? nb.closest('div')?.textContent.replace(/\s+/g, ' ').slice(0, 40) : null;
  return JSON.stringify(out, null, 1);
})()
