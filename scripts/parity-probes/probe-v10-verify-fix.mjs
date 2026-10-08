// probe-v10-verify-fix.mjs — live verification: sheet active highlighting on the FIXED build
(() => {
  const out = { url: location.pathname };
  window.scrollTo(0, 0);
  const burger = [...document.querySelectorAll("button")].find(b => {
    const r = b.getBoundingClientRect();
    return r.top < 100 && r.width <= 44 && (b.textContent || "").includes("Toggle") && b.querySelector("svg");
  });
  if (!burger) return JSON.stringify({ err: "no burger", url: out.url });
  burger.click();
  return "sheet opened — run the measure probe next";
})()
