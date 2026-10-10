(async () => {
  const routes = ['/expenses', '/savings', '/networth'];
  const out = [];
  for (const r of routes) {
    history.pushState({}, '', r);
    window.dispatchEvent(new PopStateEvent('popstate'));
    await new Promise(res => setTimeout(res, 6000));
    out.push({ r, sw: document.documentElement.scrollWidth, vw: innerWidth });
  }
  return JSON.stringify(out);
})()
