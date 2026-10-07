// probe-v7-iconbg.mjs — what sits behind the ref sidebar icon
(() => {
  const svg = [...document.querySelectorAll("aside svg, [class*='fixed'] svg")].find(s => /lucide-target/.test(s.getAttribute("class") || ""));
  if (!svg) return JSON.stringify({ err: "no lucide-target found" });
  const chain = [];
  let el = svg.parentElement;
  for (let i = 0; i < 3 && el && el !== document.body; i++) {
    const cs = getComputedStyle(el);
    chain.push({
      tag: el.tagName, cls: (el.className || "").toString().slice(0, 90),
      bg: cs.backgroundColor, bgImage: cs.backgroundImage.slice(0, 60),
      w: el.getBoundingClientRect().width, h: el.getBoundingClientRect().height,
      radius: cs.borderRadius,
    });
    el = el.parentElement;
  }
  return JSON.stringify(chain, null, 1);
})()
