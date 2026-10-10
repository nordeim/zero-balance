(async () => {
  // try clicking the overlay to close (reference bug: only X/Cancel closes)
  const fixed = [...document.querySelectorAll('div')].filter(d => getComputedStyle(d).position === 'fixed');
  const overlay = fixed.find(d => (d.getAttribute('style') || '').includes('rgba(0, 0, 0'));
  let closed = false;
  if (overlay) {
    overlay.dispatchEvent(new MouseEvent('click', { bubbles: true }));
    await new Promise(r => setTimeout(r, 800));
    const still = [...document.querySelectorAll('div')].filter(d => getComputedStyle(d).position === 'fixed').some(d => (d.getAttribute('style') || '').includes('rgba(0, 0, 0'));
    closed = !still;
  }
  // find X button if still open
  let xInfo = 'overlay-click-closed: ' + closed;
  if (!closed) {
    const xbtn = [...document.querySelectorAll('button')].find(b => /close/i.test(b.getAttribute('aria-label') || '') || (b.textContent.trim() === '' && b.getBoundingClientRect().width < 45 && b.closest('div.fixed')));
    if (xbtn) { xbtn.click(); await new Promise(r => setTimeout(r, 800)); }
    const stillNow = [...document.querySelectorAll('div')].filter(d => getComputedStyle(d).position === 'fixed').some(d => (d.getAttribute('style') || '').includes('rgba(0, 0, 0'));
    xInfo += ' | x-close-worked: ' + !stillNow + ' | bodyOverflow now: ' + getComputedStyle(document.body).overflow;
  }
  // R3: active nav on /
  agentBrowserNav = null;
  const out = { overlayVerdict: xInfo };
  return JSON.stringify(out);
})()
