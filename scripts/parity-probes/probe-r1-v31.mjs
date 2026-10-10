(async () => {
  window.scrollTo(0, 0);
  await new Promise(r => setTimeout(r, 300));
  const btn = [...document.querySelectorAll('button')].find(b => {
    const r = b.getBoundingClientRect();
    return r.width > 20 && r.width < 45 && r.top < 60 && b.querySelector('svg');
  });
  if (!btn) return JSON.stringify({ burger: 'not found', scrollWidth: document.documentElement.scrollWidth });
  const r = btn.getBoundingClientRect();
  const cx = Math.round(r.x + r.width / 2), cy = Math.round(r.y + r.height / 2);
  const hit = document.elementFromPoint(cx, cy);
  const hitChain = [];
  let n = hit;
  for (let i = 0; i < 4 && n; i++) { hitChain.push(n.tagName + (n.className && typeof n.className === 'string' ? '.' + n.className.split(' ').slice(0,3).join('.') : '')); n = n.parentElement; }
  return JSON.stringify({
    burgerBox: { w: Math.round(r.width), h: Math.round(r.height) },
    hitTag: hit ? hit.tagName : null,
    hitIsBurgerSvg: hit === btn.querySelector('svg'),
    hitIsBurgerOrChild: hit ? !!hit.closest('button') && hit.closest('button') === btn : false,
    hitChain,
    scrollWidth: document.documentElement.scrollWidth
  });
})()
