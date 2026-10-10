(() => {
  const txt = (sel) => [...document.querySelectorAll(sel)].map(e => e.textContent.trim()).slice(0, 8);
  const h1 = document.querySelector('h1');
  // hero figures
  const main = document.querySelector('main') || document.body;
  const allText = main.innerText.replace(/\n+/g, '|').slice(0, 1500);
  // allocation %
  const alloc = (main.innerText.match(/(\d+(?:\.\d+)?)%/g) || []).slice(0, 6);
  // balance figure
  const bal = (main.innerText.match(/\$[\d,]+\.\d{2}/g) || []).slice(0, 10);
  return JSON.stringify({
    url: location.pathname,
    h1: h1 ? h1.textContent.trim() : null,
    percents: alloc,
    dollars: bal,
    navCount: document.querySelectorAll('nav a, aside a').length,
    textHead: allText.slice(0, 400)
  });
})()
