// probe-v7-asidehtml.mjs — the full rail structure between brand and footer
(() => {
  const aside = document.querySelector("aside") || [...document.querySelectorAll("div")].find(d => /fixed/.test(d.className || "") && d.querySelector('a[href="/dashboard"]'));
  if (!aside) return JSON.stringify({ err: "no rail" });
  // from the rail root, dump the skeleton: element tree with classes, depth 5
  const lines = [];
  const walk = (el, depth) => {
    if (depth > 5 || lines.length > 40) return;
    const cls = (el.className && el.className.toString ? el.className.toString() : "").replace(/\s+/g, " ").slice(0, 84);
    const txt = el.children.length === 0 ? (el.textContent || "").trim().slice(0, 26) : "";
    lines.push("  ".repeat(depth) + el.tagName.toLowerCase() + (cls ? " ." + cls.split(" ").join(".") : "") + (txt ? ` "${txt}"` : ""));
    [...el.children].forEach((c) => walk(c, depth + 1));
  };
  walk(aside, 0);
  return lines.join("\n");
})()
