// probe-r4-v33.mjs — per-route mobile overflow census (the 6s settle discipline)
(async () => {
  const routes = ['/', '/dashboard', '/income', '/expenses', '/savings', '/networth'];
  const out = [];
  for (const r of routes) {
    const url = 'https://zero-balance-4885a8f3.base44.app' + (r === '/' ? '/' : r);
    history.pushState({}, '', url);
    window.dispatchEvent(new PopStateEvent('popstate'));
    await new Promise(res => setTimeout(res, 6000));
    out.push({ r, sw: document.documentElement.scrollWidth, vw: innerWidth });
  }
  return JSON.stringify(out);
})()
