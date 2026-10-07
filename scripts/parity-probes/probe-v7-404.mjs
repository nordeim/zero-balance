// probe-v7-404.mjs — ref 404 page structure
(() => {
  const out = {};
  out.title = document.title;
  const root = document.getElementById("root") || document.body;
  // main container
  const main = document.querySelector("main") || root;
  const lines = [];
  const walk = (el, depth) => {
    if (depth > 6 || lines.length > 24) return;
    const cls = (el.className?.toString?.() || "").replace(/\s+/g, " ").slice(0, 76);
    const txt = el.children.length === 0 ? (el.textContent || "").trim().slice(0, 40) : "";
    lines.push("  ".repeat(depth) + el.tagName.toLowerCase() + (cls ? " ." + cls.split(" ").slice(0, 6).join(".") : "") + (txt ? ` "${txt}"` : ""));
    [...el.children].forEach((c) => walk(c, depth + 1));
  };
  walk(main, 0);
  out.skeleton = lines.join("\n");
  // heading + button/link styles
  const h = main.querySelector("h1, h2");
  if (h) {
    const cs = getComputedStyle(h);
    out.heading = { tag: h.tagName, text: h.textContent, size: cs.fontSize, weight: cs.fontWeight, color: cs.color };
  }
  const link = [...main.querySelectorAll("a, button")].find(b => /Go Home/i.test(b.textContent || ""));
  if (link) {
    const cs = getComputedStyle(link);
    out.goHome = {
      tag: link.tagName, text: link.textContent, href: link.getAttribute("href"),
      color: cs.color, size: cs.fontSize, weight: cs.fontWeight,
      underline: cs.textDecorationLine, bg: cs.backgroundColor,
    };
  }
  // message paragraph
  const p = [...main.querySelectorAll("p, div")].find(el => el.children.length === 0 && /could not be found/.test(el.textContent || ""));
  if (p) {
    const cs = getComputedStyle(p);
    out.message = { size: cs.fontSize, color: cs.color, text: p.textContent?.slice(0, 90) };
  }
  // page bg
  out.bodyBg = getComputedStyle(document.body).backgroundColor;
  return JSON.stringify(out, null, 1);
})()
