// probe-v7-refdata.mjs — dump the reference's current dataset across views
(() => {
  const out = { url: location.pathname };
  // dashboard stat values
  const h1 = document.querySelector("h1");
  out.h1 = h1?.textContent?.trim();
  // hero numbers
  const body = document.body.innerText;
  const grab = (re) => { const m = body.match(re); return m ? m[0] : null; };
  out.netZeroMention = grab(/NET ZERO GOAL[\s\S]{0,80}/);
  // breakdown rows (sign-prefixed)
  const rows = [...document.querySelectorAll("main .border-b, main [class*='border-b']")].slice(0, 3).map(r => r.textContent?.trim().slice(0, 60));
  out.firstRows = rows;
  // income/savings/expenses sections from the breakdown card text
  const bdCard = [...document.querySelectorAll("main h3")].map(h => h.textContent?.trim()).filter(Boolean);
  out.h3s = bdCard.slice(0, 12);
  return JSON.stringify(out, null, 1);
})()
