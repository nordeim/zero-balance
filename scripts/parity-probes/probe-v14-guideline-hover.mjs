// probe-v14-guideline-hover.mjs — the 50/30/20 guideline rows: rest + hover
// states (computed styles) — v11 swept rail/filter/hero but not these rows.
(() => {
  const out = {};
  const rows = [...document.querySelectorAll('main div')].filter(d => {
    const t = d.textContent || '';
    return /\$[\d,]+\.\d{2}/.test(t) && /(50|30|20)/.test(t) && d.querySelectorAll('div').length >= 1 && d.querySelectorAll('div').length <= 6 && d.getBoundingClientRect().height > 20 && d.getBoundingClientRect().height < 90;
  }).slice(0, 3);
  out.rowCount = rows.length;
  out.rows = rows.map(row => {
    const cs = getComputedStyle(row);
    const r = row.getBoundingClientRect();
    const before = { bg: cs.backgroundColor, cursor: cs.cursor, transform: cs.transform, shadow: cs.boxShadow.slice(0, 60), h: Math.round(r.height) };
    row.dispatchEvent(new MouseEvent('mouseover', { bubbles: true }));
    row.dispatchEvent(new MouseEvent('mouseenter', { bubbles: false }));
    const cs2 = getComputedStyle(row);
    const after = { bg: cs2.backgroundColor, transform: cs2.transform, shadow: cs2.boxShadow.slice(0, 60) };
    row.dispatchEvent(new MouseEvent('mouseout', { bubbles: true }));
    return { text: row.textContent.trim().replace(/\s+/g, ' ').slice(0, 60), rest: before, hover: after };
  });
  return JSON.stringify(out, null, 1);
})()
