(() => {
  // is a fixed white sheet + dark overlay still open on /income?
  const fixed = [...document.querySelectorAll('div')].filter(d => getComputedStyle(d).position === 'fixed');
  const sheet = fixed.find(d => getComputedStyle(d).backgroundColor === 'rgb(255, 255, 255)' && d.getBoundingClientRect().width >= 250);
  const overlay = fixed.find(d => {
    const st = d.getAttribute('style') || '';
    return /rgba\(0,\s*0,\s*0/i.test(st) || getComputedStyle(d).backgroundColor === 'rgba(0, 0, 0, 0.8)';
  });
  const navLinks = [...document.querySelectorAll('a')].filter(a => a.getBoundingClientRect().width > 0).map(a => a.textContent.trim()).slice(0, 6);
  return JSON.stringify({
    url: location.pathname,
    sheetStillOpen: !!sheet,
    sheetRect: sheet ? (r => ({ x: Math.round(r.x), w: Math.round(r.width) }))(sheet.getBoundingClientRect()) : null,
    overlayStillOpen: !!overlay,
    visibleLinks: navLinks,
    bodyOverflow: getComputedStyle(document.body).overflow
  });
})()
