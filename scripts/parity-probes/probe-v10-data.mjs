// probe-v10-data.mjs — reference data drift check + dashboard headline re-verification
(() => {
  const out = { url: location.pathname };
  const txt = document.body.innerText;
  // hero figures
  const grab = (re) => { const m = txt.match(re); return m ? m[0] : null; };
  out.netBalance = grab(/[+\-] ?\$[\d,]+\.\d{2}/);
  out.allocationPct = grab(/\d+(?:\.\d+)?%/);
  // stat cards
  const h2s = [...document.querySelectorAll("h2, h3")].map(h => (h.textContent || "").trim()).filter(t => t.length < 40);
  out.headings = h2s.slice(0, 14);
  // legend rows (donut)
  const legend = [...document.querySelectorAll("li, div")].filter(el => el.children.length <= 3 && /Need|Savings|Want/.test(el.textContent || "") && /\$/.test(el.textContent || "")).slice(0, 6);
  out.legend = legend.map(el => (el.textContent || "").replace(/\s+/g, " ").trim().slice(0, 60));
  // guidelines rows
  const guide = txt.match(/50%[^]*?(?=\$|\bIncome\b|$)/);
  out.guidelinesSnippet = txt.includes("50%") ? txt.slice(txt.indexOf("50%") - 200, txt.indexOf("50%") + 300).replace(/\s+/g, " ") : null;
  return JSON.stringify(out, null, 1);
})()
