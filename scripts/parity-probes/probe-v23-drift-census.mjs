// v23 session: data-drift census — the reference data changed for the first
// time since session 19 (allocation 62.8%, balance $2065). Census every view
// the drift check tracks: per-type totals, item counts, item names+amounts.
(() => {
  const out = { path: location.pathname };
  const main = document.querySelector('main');
  const txt = (sel, root) => { const el = (root || document).querySelector(sel); return el ? el.textContent.trim() : null; };
  // stat cards: the items views render "N items" + "$X" headers per card
  const cards = [...document.querySelectorAll('main h3')].map((h) => {
    const card = h.closest('div');
    const cs = getComputedStyle(card);
    return { h3: h.textContent.trim().slice(0, 40) };
  });
  out.h3s = cards.slice(0, 12).map((c) => c.h3);
  // full visible text of main, first 2000 chars
  const t = (main || document.body).innerText.replace(/\s+/g, ' ').trim();
  out.mainText = t.slice(0, 1500);
  return JSON.stringify(out, null, 1);
})()
