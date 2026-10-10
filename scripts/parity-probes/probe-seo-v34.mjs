(async () => {
  const m = {};
  ['description', 'og:title', 'og:description', 'og:type', 'og:image',
    'twitter:card', 'twitter:title', 'twitter:description',
    'apple-mobile-web-app-title'].forEach(n => {
    const el = document.querySelector(`meta[property="${n}"], meta[name="${n}"]`);
    m[n] = el ? el.content : null;
  });
  const can = document.querySelector('link[rel=canonical]');
  return JSON.stringify({ title: document.title, canonical: can ? can.href : null, ...m });
})()
