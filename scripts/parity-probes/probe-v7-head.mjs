// probe-v7-head.mjs — head metadata + current URL
(() => {
  const metas = [...document.querySelectorAll("meta")];
  const get = (pred) => metas.find(pred)?.content ?? null;
  return JSON.stringify({
    url: location.pathname,
    title: document.title,
    desc: get((m) => m.name === "description")?.slice(0, 50),
    ogTitle: get((m) => m.getAttribute("property") === "og:title"),
    ogUrl: get((m) => m.getAttribute("property") === "og:url"),
    twitterCard: get((m) => m.name === "twitter:card"),
    appleTitle: get((m) => m.name === "apple-mobile-web-app-title"),
    canonical: document.querySelector('link[rel="canonical"]')?.href ?? null,
    manifest: document.querySelector('link[rel="manifest"]')?.href ?? null,
  }, null, 1);
})()
