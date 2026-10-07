// Session-8 (v5): donut legend — inner span colors + slice labels in the chart.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const rows = [...document.querySelectorAll('main div')].filter((d) => {
    const c = (d.className || '').toString();
    return /items-center justify-between/.test(c) && /p-3/.test(c) && (txt(d) || '').includes('%') && (txt(d) || '').length < 40;
  });
  out.spans = rows.slice(0, 3).map((r) =>
    [...r.querySelectorAll('span')].map((s) => ({ t: txt(s), color: cs(s, 'color'), size: cs(s, 'fontSize'), weight: cs(s, 'fontWeight') }))
  );

  // recharts slice labels (inside the SVG)
  const svg = document.querySelector('main svg.recharts-surface');
  if (svg) {
    const labels = [...svg.querySelectorAll('text')];
    out.sliceLabels = labels.slice(0, 8).map((t) => ({
      t: txt(t),
      fill: cs(t, 'fill'),
      size: cs(t, 'fontSize'),
      weight: cs(t, 'fontWeight'),
    }));
  }

  return JSON.stringify(out, null, 1);
})()
