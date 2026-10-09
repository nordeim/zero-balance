(async () => {
  const out = { url: location.pathname, vw: innerWidth, hoverMedia: matchMedia("(hover: hover)").matches };
  const h2 = [...document.querySelectorAll("h2")].find(h => /Calculator/i.test(h.textContent || ""));
  if (!h2) return JSON.stringify({ ...out, error: "no calculator heading" });
  const dlg = h2.closest("[class*=fixed]");
  const rows = [...dlg.querySelectorAll("h4")].map(h => {
    const row = h.closest("div").parentElement; // the flex row
    const btns = [...row.querySelectorAll("button")];
    const container = btns.length ? btns[0].parentElement : null;
    return {
      name: h.textContent.trim(),
      rowCls: (row.className || "").toString().slice(0, 70),
      containerCls: container ? (container.className || "").toString().slice(0, 100) : null,
      opacity: container ? getComputedStyle(container).opacity : null,
      pe: container ? getComputedStyle(container).pointerEvents : null,
      btn: btns.length ? {
        labels: btns.map(b => (b.getAttribute("aria-label") || b.textContent || "").trim()),
        w: Math.round(btns[0].getBoundingClientRect().width),
        h: Math.round(btns[0].getBoundingClientRect().height),
        colors: btns.map(b => getComputedStyle(b).color),
      } : null,
    };
  });
  out.rows = rows;
  return JSON.stringify(out, null, 1);
})()
