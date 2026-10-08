// probe-v11-filtered-empty.mjs — the FILTERED empty state (search yields nothing)
(() => {
  const out = {};
  // find the empty-state block: contains "No income items yet" or similar
  const block = [...document.querySelectorAll('div')].filter(el => {
    const t = (el.textContent || '');
    return /No income items|No items|no results/i.test(t) && t.length < 200 && el.getBoundingClientRect().height > 40;
  }).sort((a, b) => (a.textContent || '').length - (b.textContent || '').length)[0];
  if (!block) { out.block = 'NOT FOUND'; out.bodySnippet = document.body.innerText.slice(0, 200); return JSON.stringify(out); }
  const r = block.getBoundingClientRect(); const cs = getComputedStyle(block);
  out.block = { w: Math.round(r.width), h: Math.round(r.height), txt: (block.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 80) };
  // the icon inside
  const svg = block.querySelector('svg');
  if (svg) { const sr = svg.getBoundingClientRect(); const scs = getComputedStyle(svg); out.icon = { w: Math.round(sr.width), h: Math.round(sr.height), color: scs.color, opacity: scs.opacity, mb: scs.marginBottom }; }
  // the heading + description
  const h = block.querySelector('h3, h2, [class*=head]');
  const d = block.querySelector('p');
  if (h) { const hcs = getComputedStyle(h); out.heading = { txt: (h.textContent || '').trim(), fs: hcs.fontSize, fw: hcs.fontWeight, color: hcs.color, mb: hcs.marginBottom }; }
  if (d) { const dcs = getComputedStyle(d); out.desc = { txt: (d.textContent || '').trim().slice(0, 40), fs: dcs.fontSize, color: dcs.color }; }
  // header count
  const hdr = (document.querySelector('main') || document.body).innerText.match(/\d+ items?\s·\s\$[\d,.]+/);
  out.headerCount = hdr ? hdr[0] : null;
  return JSON.stringify(out, null, 1);
})()
