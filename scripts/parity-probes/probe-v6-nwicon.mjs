(() => {
  const panel = document.querySelector('[role="tabpanel"][data-state="active"]') || document;
  const card = [...panel.querySelectorAll('div')].filter((d) => /hover:shadow-lg/.test(d.className)).sort((a, b) => a.querySelectorAll('div').length - b.querySelectorAll('div').length)[0];
  if (!card) return JSON.stringify({ err: 'no card' });
  const svg = card.querySelector('button svg');
  const r = svg.getBoundingClientRect();
  const cs = getComputedStyle(svg);
  return JSON.stringify({ w: r.width, h: r.height, attrW: svg.getAttribute('width'), attrH: svg.getAttribute('height'), cssW: cs.width, cssH: cs.height }, null, 1);
})()
