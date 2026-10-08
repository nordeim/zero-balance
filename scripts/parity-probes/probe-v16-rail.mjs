// probe-v16-rail.mjs — R3 root-route nav highlight on the clone's desktop rail
// (the reference marks nothing active on `/`; the clone highlights Dashboard).
(() => {
  const links = [...document.querySelectorAll("a")].filter(
    (a) => /dashboard|income|expenses|savings|net worth/i.test(a.textContent)
      && (a.closest("aside") || a.closest("nav"))
  );
  return JSON.stringify(
    links.map((a) => {
      const cs = getComputedStyle(a);
      return {
        t: a.textContent.trim().slice(0, 12),
        color: cs.color,
        fw: cs.fontWeight,
        bg: cs.backgroundImage.slice(0, 60),
      };
    })
  );
})()
