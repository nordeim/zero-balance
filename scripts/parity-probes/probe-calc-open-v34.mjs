(async () => {
  const btns = [...document.querySelectorAll('button')].filter(b => /^Calculate$/i.test(b.textContent.trim()));
  if (!btns.length) return JSON.stringify({error: 'no calculate button'});
  btns[0].click();
  await new Promise(r => setTimeout(r, 1200));
  const overlay = [...document.querySelectorAll('div')].filter(d => {
    const c = (d.className || '').toString();
    return c.includes('fixed') && c.includes('z-5') && d.getBoundingClientRect().width > 200;
  });
  return JSON.stringify({
    calculateButtons: btns.length,
    overlayOpen: overlay.length > 0,
    dialogText: overlay[0]?.innerText?.split('\n').slice(0, 6),
    hasAddItem: !!overlay[0]?.innerText?.match(/add (first )?item/i),
  });
})()
