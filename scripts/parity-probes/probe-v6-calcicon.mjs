(() => {
  const svg = [...document.querySelectorAll('svg')].find((s) => /opacity-20/.test(s.getAttribute('class') || '') && !s.closest('button'));
  return JSON.stringify({ cls: svg?.getAttribute('class') });
})()
