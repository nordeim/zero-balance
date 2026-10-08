// probe-v11-rail-hover.mjs — dispatch real mouseover on the rail's Income link, read hover state
(() => {
  const link = [...document.querySelectorAll('a')].filter(a =>
    (a.textContent || '').trim() === 'Income' && a.getBoundingClientRect().height > 0)[0];
  if (!link) return 'link not found';
  const r = link.getBoundingClientRect();
  const opts = { bubbles: true, cancelable: true, clientX: r.x + r.width / 2, clientY: r.y + r.height / 2, view: window };
  link.dispatchEvent(new MouseEvent('pointerover', opts));
  link.dispatchEvent(new MouseEvent('mouseover', opts));
  link.dispatchEvent(new MouseEvent('mouseenter', { bubbles: false, cancelable: true, ...opts }));
  // wait a frame for React/Tailwind hover to apply, then read
  return new Promise(resolve => setTimeout(() => {
    const cs = getComputedStyle(link);
    resolve(JSON.stringify({
      color: cs.color,
      bg: cs.backgroundImage !== 'none' ? cs.backgroundImage.slice(0, 80) : cs.backgroundColor,
      fw: cs.fontWeight,
      transition: cs.transitionDuration
    }));
  }, 350));
})()
