(() => {
  const panel = document.querySelector('[role="tabpanel"][data-state="active"]') || document;
  const h = [...panel.querySelectorAll('h3, h4')].find((e) => /No liabilities yet/i.test(e.textContent || ''));
  const box = h.parentElement;
  const svgs = [...box.querySelectorAll('svg')].filter((s) => !s.closest('button'));
  return JSON.stringify({ svgCount: svgs.length, first: svgs[0] ? { d: (svgs[0].querySelector('path')?.getAttribute('d') || '').slice(0, 40), w: Math.round(svgs[0].getBoundingClientRect().width), color: getComputedStyle(svgs[0]).color, opacity: getComputedStyle(svgs[0]).opacity } : null }, null, 1);
})()
