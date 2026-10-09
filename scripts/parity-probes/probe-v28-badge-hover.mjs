// v28 sweep: all badges in the first expense card — full class strings,
// rest computed colors, and a LIVE hover measurement of the status badge
// (park pointer on it, read the computed bg + transition + cursor).
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const out = { path: location.pathname, badges: [] };
  const editBtns = [...document.querySelectorAll("button")].filter((b) =>
    (b.textContent || "").trim() === "Edit" && b.getBoundingClientRect().width > 0);
  const card = editBtns.length ? editBtns[0].closest("div.rounded-xl") : null;
  if (!card) return JSON.stringify({ error: "no card" });
  [...card.querySelectorAll("span, div")].forEach((el) => {
    const cls = (el.className || "").toString();
    if (!/inline-flex.*rounded-md.*px-2\.5/.test(cls)) return;
    if (el.querySelector(".inline-flex")) return; // outer wrappers only
    const cs = getComputedStyle(el);
    out.badges.push({
      tag: el.tagName, txt: (el.textContent || "").trim().slice(0, 16),
      bg: cs.backgroundColor, color: cs.color,
      cursor: cs.cursor, transition: cs.transitionDuration,
      cls,
    });
  });
  // live hover on the status badge (text starts with 'active'/'pending')
  const status = out.badges.find((b) => /^(active|pending|completed|cancelled)/i.test(b.txt));
  if (status) {
    const el = [...card.querySelectorAll("span, div")].find((e) => {
      const t = (e.textContent || "").trim();
      return /^(active|pending|completed|cancelled)/i.test(t.slice(0, 9)) && /inline-flex/.test((e.className || "").toString());
    });
    if (el) {
      const r = el.getBoundingClientRect();
      const mouse = document.createElement("div");
      // real CDP hover via the browser's own pointer move:
      window.__zbHover = null;
      const ev = new PointerEvent("pointerover", { bubbles: true, cancelable: true, clientX: r.x + 10, clientY: r.y + r.height / 2, pointerId: 2 });
      el.dispatchEvent(ev);
      el.dispatchEvent(new MouseEvent("mouseenter", { bubbles: false, clientX: r.x + 10, clientY: r.y + r.height / 2 }));
      await sleep(400); // transition-colors settle
      const cs = getComputedStyle(el);
      out.hoverProbe = { bg: cs.backgroundColor, transition: cs.transitionDuration + " " + cs.transitionProperty, note: "synthetic pointerover+mouseenter" };
    }
  }
  return JSON.stringify(out);
})()
