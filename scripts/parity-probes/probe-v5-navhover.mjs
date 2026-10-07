// Session-8 (v5): nav link hover text color (inactive link).
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const link = [...document.querySelectorAll('a')].find((a) => txt(a) === 'Income' && a.getBoundingClientRect().width > 50);
  if (!link) return JSON.stringify({ error: 'no link' });
  out.rest = { color: cs(link, 'color') };
  // hover via synthetic mouseenter? Use agent-browser hover instead — here read the hover class expectation:
  out.cls = (link.className || '').toString().replace(/\s+/g, ' ').slice(0, 160);
  return JSON.stringify(out, null, 1);
})()
