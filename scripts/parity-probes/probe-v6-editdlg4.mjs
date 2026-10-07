(() => {
  const btn = [...document.querySelectorAll('button')].find((b) => /Save Asset/.test(b.textContent || ''));
  if (!btn) return JSON.stringify({ err: 'no button' });
  // find the scrollable panel: climb until we get a white bg or a large div
  let chain = [];
  let p = btn;
  for (let i = 0; i < 12 && p.parentElement; i++) {
    p = p.parentElement;
    const cs = getComputedStyle(p);
    const r = p.getBoundingClientRect();
    chain.push({ tag: p.tagName, cls: (p.className || '').toString().slice(0, 50), w: Math.round(r.width), h: Math.round(r.height), pos: cs.position, bg: cs.backgroundColor, scroll: cs.overflowY });
  }
  return JSON.stringify(chain, null, 1);
})()
