// probe-v16-burger.mjs — R1 burger hit-test (v16 re-verification).
// The reference's toast containers (fixed, z-100, full-width, pe:auto) cover
// the top half of the mobile hamburger — document.elementsFromHit at the
// burger center must show the containers intercepting on the REF, a direct
// svg hit on the CLONE.
(() => {
  const out = {};
  const btn = [...document.querySelectorAll("button")].find(
    (b) => /toggle/i.test(b.getAttribute("aria-label") || "") || /toggle/i.test(b.textContent || "")
  );
  if (!btn) return JSON.stringify({ error: "no burger button" });
  const r = btn.getBoundingClientRect();
  out.burger = { x: r.x, y: r.y, w: r.width, h: r.height };
  const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
  out.center = [cx, cy];
  const hits = document.elementsFromPoint(cx, cy);
  out.hitChain = hits.slice(0, 6).map((el) => {
    const cs = getComputedStyle(el);
    return {
      tag: el.tagName.toLowerCase(),
      pe: cs.pointerEvents,
      pos: cs.position,
      z: cs.zIndex,
      cls: (el.className && el.className.baseVal !== undefined
        ? el.className.baseVal : el.className || "").toString().slice(0, 40),
    };
  });
  out.svgDirect = hits[0] && hits[0].tagName.toLowerCase() === "svg";
  return JSON.stringify(out);
})()
