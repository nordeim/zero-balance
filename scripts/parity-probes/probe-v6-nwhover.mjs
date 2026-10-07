// v6: hover an asset card → dump revealed action buttons (labels, chrome, icons)
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const panel = document.querySelector('[role="tabpanel"][data-state="active"]') || document;
  const card = [...panel.querySelectorAll('div')].filter((d) => /hover:shadow-lg/.test(d.className)).sort((a, b) => a.querySelectorAll('div').length - b.querySelectorAll('div').length)[0];
  if (!card) return JSON.stringify({ err: 'no card' });
  const btns = [...card.querySelectorAll('button')];
  out.buttons = btns.map((b) => ({
    aria: b.getAttribute('aria-label'),
    text: (b.textContent || '').trim().slice(0, 20),
    opacity: cs(b, 'opacity'),
    w: cs(b, 'width'), h: cs(b, 'height'),
    svg: b.querySelectorAll('svg').length,
    svgPath: (b.querySelector('svg path')?.getAttribute('d') || '').slice(0, 24),
    title: b.getAttribute('title'),
  }));
  return JSON.stringify(out, null, 1);
})()
