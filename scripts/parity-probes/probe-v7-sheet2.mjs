// probe-v7-sheet2.mjs — mobile sheet via dialog portal
(() => {
  const out = {};
  // Radix portal: [role=dialog] or data-[state=open] fixed panel at body level
  const dlg = document.querySelector('[role="dialog"][data-state="open"], div[data-state="open"].fixed');
  const panels = [...document.querySelectorAll("div")].filter(d => {
    const c = d.className?.toString?.() || "";
    return /fixed/.test(c) && d.getAttribute("data-state") === "open" && d.getBoundingClientRect().width > 100 && d.getBoundingClientRect().width < 500 && d.querySelector('a[href="/dashboard"]');
  });
  const sheet = panels[0];
  if (!sheet) return JSON.stringify({ err: "no open sheet panel", dlgFound: !!dlg });
  const scs = getComputedStyle(sheet);
  out.sheet = {
    cls: (sheet.className || "").toString().slice(0, 130),
    w: Math.round(sheet.getBoundingClientRect().width),
    h: Math.round(sheet.getBoundingClientRect().height),
    x: Math.round(sheet.getBoundingClientRect().left),
    bg: scs.backgroundColor, z: scs.zIndex,
    borderR: scs.borderRightWidth + " " + scs.borderRightColor,
    shadow: scs.boxShadow.slice(0, 50),
    role: sheet.getAttribute("role"),
  };
  // close button presence
  const closeBtn = [...sheet.querySelectorAll("button")].find(b => /close/i.test(b.getAttribute("aria-label") || "") || /Close/.test(b.textContent || "")) || (sheet.querySelector("button.absolute") || null);
  out.closeBtn = closeBtn ? {
    cls: (closeBtn.className || "").toString().slice(0, 100),
    aria: closeBtn.getAttribute("aria-label"), srOnly: closeBtn.querySelector(".sr-only")?.textContent,
    pos: closeBtn.className.includes("right-4") && closeBtn.className.includes("top-4") ? "right-4 top-4" : "other",
    w: Math.round(closeBtn.getBoundingClientRect().width),
  } : null;
  // overlay bg (computed)
  const ov = [...document.querySelectorAll("div")].find(d => /fixed/.test(d.className?.toString?.() || "") && /inset-0/.test(d.className?.toString?.() || "") && !sheet.contains(d) && getComputedStyle(d).backgroundColor !== "rgba(0, 0, 0, 0)");
  out.overlay = ov ? { bg: getComputedStyle(ov).backgroundColor, z: getComputedStyle(ov).zIndex } : null;
  return JSON.stringify(out, null, 1);
})()
