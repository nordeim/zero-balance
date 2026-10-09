// v28 sweep: details-dialog leaf styles — fact-row inner split, summary
// name/amount colors, classification block text styles.
(() => {
  const hdr = [...document.querySelectorAll("div")].filter((d) => /Budget Item Details/.test(d.textContent || "") && d.getBoundingClientRect().width === 512).pop();
  let dlg = hdr;
  for (let i = 0; i < 8; i++) { dlg = dlg.parentElement; const cs = getComputedStyle(dlg); if (cs.position === "fixed" || dlg.tagName === "BODY") break; }
  const panel = [...dlg.children].find((c) => c.getBoundingClientRect().width > 200 && c.textContent.trim().length > 10);
  const out = {};
  const factRow = [...panel.querySelectorAll("div")].find((d) => (d.className || "").toString().includes("py-2") && /Date/.test(d.textContent || ""));
  const flex1 = factRow.querySelector(".flex-1");
  out.factInner = [...flex1.children].map((c) => {
    const cs = getComputedStyle(c);
    return { txt: (c.textContent || "").trim().slice(0, 22), cls: (c.className || "").toString().slice(0, 90), color: cs.color, fw: cs.fontWeight, fs: cs.fontSize };
  });
  const h3 = panel.querySelector("h3");
  const amt = [...panel.querySelectorAll("p")].find((p) => /^\$/.test((p.textContent || "").trim()));
  out.name = { txt: h3.textContent.trim(), cls: h3.className, color: getComputedStyle(h3).color, fs: getComputedStyle(h3).fontSize };
  out.amount = { txt: amt.textContent.trim(), cls: amt.className, color: getComputedStyle(amt).color, fs: getComputedStyle(amt).fontSize };
  const clsBlock = [...panel.querySelectorAll("div")].find((d) => /Essential expenses/.test(d.textContent || "") && d.className.includes("rounded-xl"));
  out.clsText = [...clsBlock.querySelectorAll("p, span, strong, div")].filter((e) => e.children.length === 0).slice(0, 3).map((e) => {
    const cs = getComputedStyle(e);
    return { txt: (e.textContent || "").trim().slice(0, 30), tag: e.tagName, cls: (e.className || "").toString().slice(0, 80), color: cs.color, fw: cs.fontWeight, fs: cs.fontSize };
  });
  return JSON.stringify(out, null, 1);
})()
