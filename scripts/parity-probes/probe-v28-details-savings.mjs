// v28 sweep: open the first savings card's details dialog — the SAVINGS
// type-badge/amount colors + the savings-classification block colors.
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const cards = [...document.querySelectorAll("main div.rounded-xl")].filter((c) => c.getBoundingClientRect().width > 200);
  if (!cards.length) return JSON.stringify({ error: "no cards", path: location.pathname });
  cards[0].click();
  await sleep(900);
  const hdr = [...document.querySelectorAll("div")].filter((d) => /Budget Item Details/.test(d.textContent || "") && d.getBoundingClientRect().width > 0 && d.getBoundingClientRect().height < 100).pop();
  if (!hdr) return JSON.stringify({ error: "no dialog" });
  let dlg = hdr;
  for (let i = 0; i < 8; i++) { dlg = dlg.parentElement; if (getComputedStyle(dlg).position === "fixed" || dlg.tagName === "BODY") break; }
  const panel = [...dlg.children].find((c) => c.getBoundingClientRect().width > 200 && c.textContent.trim().length > 10);
  const badges = [...panel.querySelectorAll(".text-center .flex.items-center.justify-center > *")].map((b) => {
    const cs = getComputedStyle(b);
    const icon = b.querySelector("svg");
    return { txt: (b.textContent || "").trim().slice(0, 10), hasIcon: !!icon, iconW: icon ? Math.round(icon.getBoundingClientRect().width) : 0, cls: (b.className || "").toString().slice(0, 140), bg: cs.backgroundColor, color: cs.color };
  });
  const amt = [...panel.querySelectorAll("p")].find((p) => /^\$/.test((p.textContent || "").trim()));
  const clsBlock = [...panel.querySelectorAll("div")].find((d) => /p-4/.test((d.className || "").toString()) && /rounded-xl/.test((d.className || "").toString()));
  const clsTitle = panel.querySelector("p.font-semibold");
  const clsDesc = clsBlock ? [...clsBlock.querySelectorAll("p")][1] : null;
  return JSON.stringify({
    path: location.pathname,
    badges,
    name: panel.querySelector("h3").textContent.trim(),
    amount: { txt: amt.textContent.trim(), color: getComputedStyle(amt).color },
    clsBlock: clsBlock ? { bg: getComputedStyle(clsBlock).backgroundColor, title: { txt: clsTitle.textContent.trim().slice(0, 14), color: getComputedStyle(clsTitle).color }, desc: clsDesc ? { txt: clsDesc.textContent.trim().slice(0, 60), color: getComputedStyle(clsDesc).color } : null } : null,
    facts: panel.innerText.replace(/\s+/g, " | ").slice(0, 280),
  }, null, 1);
})()
