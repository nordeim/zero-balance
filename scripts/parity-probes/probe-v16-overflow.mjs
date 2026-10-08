// probe-v16-overflow.mjs — R4 mobile horizontal overflow check across the six
// routes (the reference scrolls to 395px on `/`+`/dashboard` and 464px on
// `/networth` at 390px; the clone fits 390 on all routes).
(async () => {
  const routes = ["/", "/dashboard", "/income", "/expenses", "/savings", "/networth"];
  const out = [];
  for (const r of routes) {
    const here = location.pathname === r;
    if (!here) {
      history.pushState({}, "", r);
      window.dispatchEvent(new PopStateEvent("popstate"));
      await new Promise((res) => setTimeout(res, 400));
    }
    out.push({
      route: r,
      scrollW: document.documentElement.scrollWidth,
      clientW: document.documentElement.clientWidth,
    });
  }
  return JSON.stringify(out);
})()
