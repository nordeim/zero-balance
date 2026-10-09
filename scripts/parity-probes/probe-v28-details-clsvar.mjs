// v28 sweep: open the Nth expense card's details dialog and dump the
// classification-block colors (want / savings variants).
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const idx = Number(window.__zbCardIdx || 0);
  const cards = [...document.querySelectorAll("main div.rounded-xl")].filter((c) => c.getBoundingClientRect().width > 200);
  if (!cards.length) return JSON.stringify({ error: "no cards" });
  cards[idx].click();
  await sleep(900);
  const hdr = [...document.querySelectorAll("div")].filter((d) => /Budget Item Details/.test(d.textContent || "") && d.getBoundingClientRect().width > 0 && d.getBoundingClientRect().height < 100).pop();
  if (!hdr) return JSON.stringify({ error: "no dialog" });
  let dlg = hdr;
  for (let i = 0; i < 8; i++) { dlg = dlg.parentElement; if (getComputedStyle(dlg).position === "fixed" || dlg.tagName === "BODY") break; }
  const panel = [...dlg.children].find((c) => c.getBoundingClientRect().width > 200 && c.textContent.trim().length > 10);
  const clsBlock = [...panel.querySelectorAll("div")].find((d) => /p-4/.test((d.className || "").toString()) && /rounded-xl/.test((d.className || "").toString()));
  const title = panel.querySelector("p.font-semibold");
  const desc = clsBlock ? [...clsBlock.querySelectorAll("p")][1] : null;
  const icon = clsBlock ? clsBlock.querySelector("svg") : null;
  const badges = [...panel.querySelectorAll(".text-center .flex.items-center.justify-center > *")].map((b) => {
    const cs = getComputedStyle(b);
    return { txt: (b.textContent || "").trim().slice(0, 10), hasIcon: !!b.querySelector("svg"), bg: cs.backgroundColor, color: cs.color };
  });
  return JSON.stringify({
    card: cards[idx].querySelector("h4, h3").textContent.trim(),
    clsBlock: { bg: getComputedStyle(clsBlock).backgroundColor, radius: getComputedStyle(clsBlock).borderRadius, hasIcon: !!icon, iconW: icon ? Math.round(icon.getBoundingClientRect().width) : 0, title: { txt: title.textContent.trim().slice(0, 12), color: getComputedStyle(title).color }, desc: { txt: (desc ? desc.textContent : "").trim().slice(0, 60), color: desc ? getComputedStyle(desc).color : null } },
    badges,
  }, null, 1);
})()
