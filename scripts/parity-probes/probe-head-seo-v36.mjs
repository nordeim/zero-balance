// probe-head-seo-v36.mjs — the reference's head-metadata census (standing SEO pair).
// Returns the pinned values for cross-site comparison.
(async () => {
  const m = (sel) => {
    const el = document.querySelector(sel);
    return el ? (el.content || el.getAttribute('href')) : null;
  };
  const out = {
    title: document.title,
    desc: m('meta[name="description"]'),
    canonical: m('link[rel="canonical"]'),
    ogTitle: m('meta[property="og:title"]'),
    ogDesc: m('meta[property="og:description"]'),
    ogUrl: m('meta[property="og:url"]'),
    twitterCard: m('meta[name="twitter:card"]'),
    appleTitle: m('meta[name="apple-mobile-web-app-title"]'),
    manifest: m('link[rel="manifest"]')
  };
  return JSON.stringify(out);
})()
