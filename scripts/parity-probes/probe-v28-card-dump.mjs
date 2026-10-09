// v28 sweep: expense-card deep dump — the first item card's full interactive
// structure (buttons, selects, divs with click handlers, status chips), with
// full class strings, to find the "Active ▾"-style status trigger and its family.
(() => {
  const out = { path: location.pathname, cards: [] };
  // expense cards live in main; find containers with an Edit button
  const editBtns = [...document.querySelectorAll("button")].filter((b) =>
    (b.textContent || "").trim() === "Edit" && b.getBoundingClientRect().width > 0);
  const card = editBtns.length ? editBtns[0].closest("div.rounded-lg, div.rounded-xl, div.border, div[class*='card'], div[class*='shadow']") || editBtns[0].parentElement.parentElement.parentElement : null;
  if (!card) { out.error = "no card found"; return JSON.stringify(out); }
  out.cardCls = (card.className || "").toString().slice(0, 200);
  // walk the card's descendants: elements with role, click handlers, or text
  const seen = new Set();
  [...card.querySelectorAll("*")].forEach((el) => {
    if (seen.has(el)) return;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) return;
    const tag = el.tagName;
    const role = el.getAttribute("role");
    const hasClick = !!el.onclick || el.getAttributeNames().some((a) => a.startsWith("on") || a === "aria-haspopup" || a === "aria-expanded");
    const cls = (el.className || "").toString().trim();
    const txt = (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 20);
    if (tag === "BUTTON" || tag === "SELECT" || role === "button" || role === "combobox" || hasClick) {
      seen.add(el);
      out.cards.push({
        tag, role: role || null, txt, w: Math.round(r.width), h: Math.round(r.height),
        ariaHas: el.getAttribute("aria-haspopup") || null,
        cls: cls.slice(0, 400),
      });
    }
  });
  // also: any element containing "Active" or a ▾ chevron in the card
  out.statusEls = [...card.querySelectorAll("*")].filter((el) => {
    const t = (el.textContent || "").trim();
    return /^(Active|Pending|Completed|Cancelled)/i.test(t.slice(0, 10)) && el.children.length <= 2;
  }).slice(0, 4).map((el) => ({
    tag: el.tagName, txt: (el.textContent || "").trim().slice(0, 20),
    cls: (el.className || "").toString().slice(0, 300),
  }));
  return JSON.stringify(out);
})()
