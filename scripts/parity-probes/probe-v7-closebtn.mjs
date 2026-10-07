// probe-v7-closebtn.mjs — sheet close button visibility + geometry
(() => {
  const sheet = [...document.querySelectorAll("div")].find(d => d.getAttribute?.("data-state") === "open" && /fixed/.test(d.className?.toString?.() || "") && d.querySelector('a[href="/dashboard"]') && d.getBoundingClientRect().width > 100);
  if (!sheet) return JSON.stringify({ err: "no open sheet" });
  const btn = sheet.querySelector("button.absolute");
  if (!btn) return JSON.stringify({ err: "no close button" });
  const bcs = getComputedStyle(btn);
  const icon = btn.querySelector("svg");
  return JSON.stringify({
    display: bcs.display,
    visibility: bcs.visibility,
    opacity: bcs.opacity,
    w: Math.round(btn.getBoundingClientRect().width),
    h: Math.round(btn.getBoundingClientRect().height),
    x: Math.round(btn.getBoundingClientRect().left),
    y: Math.round(btn.getBoundingClientRect().top),
    iconSize: icon ? getComputedStyle(icon).width + "/" + getComputedStyle(icon).height : null,
    iconColor: icon ? getComputedStyle(icon).color : null,
    zIndex: bcs.zIndex,
  }, null, 1);
})()
