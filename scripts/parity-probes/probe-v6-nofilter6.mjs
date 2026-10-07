(() => {
  const h = [...document.querySelectorAll('h3, h4')].find((e) => /No income items yet/i.test(e.textContent || ''));
  const box = h.parentElement;
  let chain = [];
  let p = box;
  for (let i = 0; i < 5 && p.parentElement; i++) {
    p = p.parentElement;
    const cs = getComputedStyle(p);
    chain.push({ cls: (p.className || '').toString().slice(0, 70), border: cs.borderTopWidth + ' ' + cs.borderColor, radius: cs.borderRadius, bg: cs.backgroundColor });
  }
  return JSON.stringify(chain, null, 1);
})()
