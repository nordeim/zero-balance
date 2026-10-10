(async () => {
  await new Promise(r => setTimeout(r, 300));
  // R1: the burger hit test — what element sits at the burger's center?
  const burger = [...document.querySelectorAll('button')].find(b =>
    (b.getAttribute('aria-label') || '').includes('Toggle Sidebar') ||
    (b.querySelector('.sr-only')?.textContent || '').includes('Toggle Sidebar'));
  if (!burger) return JSON.stringify({R1: 'no burger found'});
  const r = burger.getBoundingClientRect();
  const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
  const hit = document.elementFromPoint(cx, cy);
  const hitDesc = hit ? hit.tagName + '.' + (hit.className?.toString?.() || '').toString().split(' ').slice(0, 3).join('.') : 'none';
  return JSON.stringify({
    R1_hit: hitDesc,
    hit_is_burger: hit === burger || burger.contains(hit),
    viewport: document.documentElement.clientWidth,
    scrollW: document.documentElement.scrollWidth,
  });
})()
