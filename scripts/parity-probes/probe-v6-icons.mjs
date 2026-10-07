(() => {
  const h = [...document.querySelectorAll('h3, h4')].find((e) => /No income items yet/i.test(e.textContent || ''));
  const svg = h.parentElement.querySelector('svg');
  return JSON.stringify({ d: svg?.querySelector('path')?.getAttribute('d') || null, w: svg?.getAttribute('width'), cls: svg?.getAttribute('class') }, null, 1);
})()
