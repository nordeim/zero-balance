// v20 session: breakdown drill-down expander — clicks the first section
// (Income) and then the first category row inside it, so the expanded
// drill-down state renders for screenshotting. Returns the expanded rows.
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const out = {};
  // the breakdown card: the section rows are the chevron buttons
  const breakdown = [...document.querySelectorAll('main div')].find((d) => {
    const t = (d.textContent || '');
    return /NET ZERO BREAKDOWN/i.test(t) && d.getBoundingClientRect().width > 300;
  });
  if (!breakdown) return 'no breakdown card';
  // section button: the row with a chevron (svg) + section label
  const btns = [...breakdown.querySelectorAll('button')];
  const section = btns.find((b) => /income|savings|expenses/i.test(b.textContent || '') && b.querySelectorAll('svg').length > 0);
  if (section) {
    section.click();
    await sleep(900);
    out.section = (section.textContent || '').trim().slice(0, 30);
    // after expansion, find category sub-buttons inside the same card
    const btns2 = [...breakdown.querySelectorAll('button')];
    const cat = btns2.find((b) => b !== section && (b.textContent || '').trim().length > 2 && b.getBoundingClientRect().height < 40);
    if (cat) {
      cat.click();
      await sleep(900);
      out.category = (cat.textContent || '').trim().slice(0, 30);
    }
  }
  return JSON.stringify(out);
})()
