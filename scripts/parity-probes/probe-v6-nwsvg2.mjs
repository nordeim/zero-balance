(() => {
  const panel = document.querySelector('[role="tabpanel"][data-state="active"]') || document;
  const h = [...panel.querySelectorAll('h3, h4')].find((e) => /No liabilities yet/i.test(e.textContent || ''));
  const svg = [...h.parentElement.querySelectorAll('svg')].find((s) => !s.closest('button'));
  return JSON.stringify({ cls: svg?.getAttribute('class'), color: svg ? getComputedStyle(svg).color : null });
})()
