// v20 session: item-card badge-row mechanism probe — finds the badge
// clusters (spans with tinted backgrounds) inside item cards and reports
// their flex-wrap, gap, and per-row layout, to test whether the wrap
// MECHANISM matches (data-driven badge counts differ by design).
(() => {
  const out = { path: location.pathname, vw: document.documentElement.clientWidth };
  // badge = small span with a non-transparent tinted background inside a card
  const spans = [...document.querySelectorAll('main span')].filter((s) => {
    const cs = getComputedStyle(s);
    const r = s.getBoundingClientRect();
    if (r.width < 24 || r.width > 160 || r.height < 16 || r.height > 30) return false;
    const bg = cs.backgroundColor;
    return bg && bg !== 'rgba(0, 0, 0, 0)' && !/255, 255, 255/.test(bg);
  });
  // group badges by their shared parent
  const groups = new Map();
  for (const s of spans) {
    const p = s.parentElement;
    if (!groups.has(p)) groups.set(p, []);
    groups.get(p).push(s);
  }
  out.badgeGroups = [...groups.values()].filter((g) => g.length >= 2).map((g) => {
    const p = g[0].parentElement;
    const cs = getComputedStyle(p);
    const rows = new Set(g.map((b) => Math.round(b.getBoundingClientRect().y / 8) * 8));
    return {
      n: g.length,
      texts: g.map((b) => (b.textContent || '').trim()).slice(0, 6),
      flexWrap: cs.flexWrap, gap: cs.gap, display: cs.display,
      rows: [...rows].sort((a, b) => a - b),
      w: Math.round(p.getBoundingClientRect().width),
    };
  }).slice(0, 6);
  return JSON.stringify(out, null, 1);
})()
