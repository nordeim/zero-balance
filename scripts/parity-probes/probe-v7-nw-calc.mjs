// probe-v7-nw-calc.mjs — net-worth + calculator quick spot check
(() => {
  const out = { url: location.pathname };
  // net-worth: tabs + summary
  const tabs = [...document.querySelectorAll('[role="tab"], button')].filter(b => /^Assets$|^Liabilities$/i.test((b.textContent || "").trim()));
  out.tabs = tabs.map(t => {
    const cs = getComputedStyle(t);
    return { text: t.textContent?.trim(), cls: (t.className || "").toString().slice(0, 70), color: cs.color, bg: cs.backgroundColor, w: Math.round(t.getBoundingClientRect().width), h: Math.round(t.getBoundingClientRect().height) };
  });
  // summary card
  const ratio = [...document.querySelectorAll("div,span")].find(el => el.children.length === 0 && /:1/.test(el.textContent || "") && (el.textContent || "").trim().length < 10);
  out.ratio = ratio ? { text: ratio.textContent?.trim(), size: getComputedStyle(ratio).fontSize } : null;
  // net worth big figure
  const big = [...document.querySelectorAll("div,span,h2,h3")].filter(el => el.children.length === 0 && /\$[\d,]+/.test(el.textContent || "")).sort((a, b) => parseFloat(getComputedStyle(b).fontSize) - parseFloat(getComputedStyle(a).fontSize))[0];
  out.bigFigure = big ? { text: big.textContent?.trim(), size: getComputedStyle(big).fontSize } : null;
  // calculator presence (only on expenses view when a calculator dialog is open)
  const calc = [...document.querySelectorAll("h2, h3")].find(h => /Calculator/i.test(h.textContent || ""));
  out.calculatorHeading = calc ? calc.textContent?.trim() : null;
  return JSON.stringify(out, null, 1);
})()
