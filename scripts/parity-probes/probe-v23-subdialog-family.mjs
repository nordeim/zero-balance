(async () => {
  // v23 session: open the (Add) line-item sub-dialog at the CURRENT viewport
  // and report its family geometry (panel cap + form gap). Assumes the
  // calculator is ALREADY open on the seeded Rent item. Clicks "Add Item".
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const add = [...document.querySelectorAll('button')].find((b) => /add item/i.test((b.textContent || '').trim()));
  if (!add) return 'no Add Item button';
  add.click();
  await sleep(900);
  const h = [...document.querySelectorAll('h1,h2,h3,h4')].find((el) => /(add|edit) line item/i.test(el.textContent || ''));
  if (!h) return 'sub-dialog not open';
  let el = h, panel = null;
  for (let i = 0; i < 12 && el; i++) {
    el = el.parentElement;
    if (!el || el === document.body) break;
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    if ((el.getAttribute('role') === 'dialog' || cs.backgroundColor === 'rgb(255, 255, 255)') && r.width > 300 && r.width < 700 && r.height > 200 && cs.borderRadius !== '0px') { panel = el; break; }
  }
  if (!panel) return 'no panel';
  const r = panel.getBoundingClientRect();
  const cs = getComputedStyle(panel);
  const form = panel.querySelector('form');
  const fk = form ? [...form.children].filter((k) => k.getBoundingClientRect().height > 5) : [];
  return JSON.stringify({
    w: Math.round(r.width), h: Math.round(r.height),
    maxH: cs.maxHeight, overflowY: cs.overflowY,
    formKids: fk.length,
    formGap: fk.length > 1 ? Math.round(fk[1].getBoundingClientRect().top - fk[0].getBoundingClientRect().bottom) : null,
    vw: innerWidth, vh: innerHeight,
  });
})()
