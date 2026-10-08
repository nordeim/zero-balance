// probe-v16-refdata.mjs — data-drift check on the reference (tenth consecutive).
// Reads the hero figure + stat totals + item census; compares to the documented
// session-19 state (allocation 30.5%, +$3475.00, income 5000/1, savings 1000/1,
// expenses 525/4).
(() => {
  const out = {};
  const hero = document.querySelector("h1");
  out.h1 = hero ? hero.textContent : null;
  const body = document.body.innerText;
  const grab = (re) => { const m = body.match(re); return m ? m[1] : null; };
  out.allocation = grab(/(\d+(?:\.\d+)?)%\s*(?:of income|allocated)/i);
  out.netBalance = grab(/Net Balance\s*\+?(-?\$[\d,.]+)/i);
  out.incomeStat = grab(/Income\s*\$([\d,.]+)/i);
  out.savingsStat = grab(/Savings\s*\$([\d,.]+)/i);
  out.expensesStat = grab(/Expenses\s*\$([\d,.]+)/i);
  out.textLen = body.length;
  return JSON.stringify(out);
})()
