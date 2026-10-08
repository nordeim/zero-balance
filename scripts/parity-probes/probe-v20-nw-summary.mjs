// v20 session: net-worth mobile summary-card probe — measures the summary
// card's amount font size/position, the trend icon, the tab triggers' bg,
// and the Add button text/width (VLM claims to verify).
(() => {
  const out = { path: location.pathname, vw: document.documentElement.clientWidth };
  // the big net-worth figure (text-2xl/text-5xl family)
  const figs = [...document.querySelectorAll('main h2, main h3, main div, main p')].filter((el) => {
    const t = (el.textContent || '').trim();
    return /^-?\$[\d,.]+$/.test(t) && el.children.length === 0;
  });
  const big = figs.map((el) => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return { t: (el.textContent || '').trim(), fs: cs.fontSize, x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height), align: cs.textAlign };
  });
  out.figures = big.slice(0, 4);
  // tab triggers + their computed backgrounds
  const tabs = [...document.querySelectorAll('[role="tab"]')].map((el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return { t: (el.textContent || '').trim(), bg: cs.backgroundColor, w: Math.round(r.width), h: Math.round(r.height) };
  });
  out.tabs = tabs;
  // the Add button
  const addBtn = [...document.querySelectorAll('main button')].find((b) => /^add/i.test((b.textContent || '').trim()));
  if (addBtn) {
    const r = addBtn.getBoundingClientRect();
    out.addBtn = { text: (addBtn.textContent || '').trim(), w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y) };
  }
  // any svg near the summary card (trend icon)
  const svgs = [...document.querySelectorAll('main svg')].filter((s) => {
    const r = s.getBoundingClientRect();
    return r.width >= 20 && r.width <= 64 && r.top < 500;
  }).map((s) => {
    const r = s.getBoundingClientRect();
    return { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y) };
  });
  out.summarySvgs = svgs.slice(0, 5);
  return JSON.stringify(out, null, 1);
})()
