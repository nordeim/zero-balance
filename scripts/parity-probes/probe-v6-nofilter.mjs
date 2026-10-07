(() => {
  const main = document.querySelector('main');
  const t = (main.textContent || '').replace(/\s+/g, ' ');
  const h = [...main.querySelectorAll('h3, h4, p')].find((e) => /No |not find|try|match/i.test(e.textContent || ''));
  let empty = null;
  if (h) {
    let box = h.parentElement;
    for (let i = 0; i < 3; i++) { if (getComputedStyle(box).borderTopWidth === '1px') break; box = box.parentElement; }
    const cs = getComputedStyle(box);
    empty = { text: (box.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 140), classes: box.className.slice(0, 100), border: cs.borderColor, radius: cs.borderRadius, py: cs.paddingTop, bg: cs.backgroundColor, svgs: [...box.querySelectorAll('svg')].filter((s) => !s.closest('button')).length };
  }
  return JSON.stringify({ headCount: (t.match(/\d+ items?/g) || [])[0], empty }, null, 1);
})()
