(() => {
  const h = [...document.querySelectorAll('h2, h3')].find((e) => /Calculator/i.test(e.textContent || ''));
  const btn = [...document.querySelectorAll('button')].find((b) => /Add First Item|Add Item/.test((b.textContent || '').trim()));
  return JSON.stringify({
    calcTitle: h?.textContent?.trim() || null,
    emptyBtn: btn ? { text: (btn.textContent || '').trim(), bg: (getComputedStyle(btn).backgroundImage || 'none').slice(0, 60), svg: btn.querySelectorAll('svg').length, border: getComputedStyle(btn).borderColor, bw: getComputedStyle(btn).borderWidth, color: getComputedStyle(btn).color } : null,
    bodyHasCalc: /Calculator/.test(document.body.textContent || ''),
  }, null, 1);
})()
