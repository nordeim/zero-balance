// v28 sweep: open the first expense card's details dialog (card click) and
// dump the type-badge/amount/classification colors (the EXPENSE variant).
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const cards = [...document.querySelectorAll("main div.rounded-xl")].filter((c) => c.getBoundingClientRect().width > 200);
  cards[0].click();
  await sleep(900);
  const hdr = [...document.querySelectorAll("div")].filter((d) => /Budget Item Details/.test(d.textContent || "") && d.getBoundingClientRect().width > 0 && d.getBoundingClientRect().height < 100).pop();
  if (!hdr) return JSON.stringify({ error: "no dialog" });
  let dlg = hdr;
  for (let i = 0; i < 8; i++) { dlg = dlg.parentElement; if (getComputedStyle(dlg).position === "fixed" || dlg.tagName === "BODY") break; }
  const panel = [...dlg.children].find((c) => c.getBoundingClientRect().width > 200 && c.textContent.trim().length > 10);
  const badges = [...panel.querySelectorAll(".text-center .flex.items-center.justify-center > *")].map((b) => {
    const cs = getComputedStyle(b);
    return { txt: (b.textContent || "").trim().slice(0, 10), cls: (b.className || "").toString().slice(0, 140), bg: cs.backgroundColor, color: cs.color };
  });
  const amt = [...panel.querySelectorAll("p")].find((p) => /^\$/.test((p.textContent || "").trim()));
  const h3 = panel.querySelector("h3");
  const clsTitle = [...panel.querySelectorAll("p")].find((p) => (p.className || "").includes("font-semibold"));
  return JSON.stringify({
    badges,
    name: h3.textContent.trim(),
    amount: { txt: amt.textContent.trim(), color: getComputedStyle(amt).color },
    clsTitle: { txt: clsTitle.textContent.trim().slice(0, 16), color: getComputedStyle(clsTitle).color },
    facts: panel.innerText.replace(/\s+/g, " | ").slice(0, 300),
  }, null, 1);
})()
