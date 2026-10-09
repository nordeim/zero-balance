// v30: head metadata census (SEO pair deep check)
(() => {
  const out = {};
  const names = ['description', 'og:title', 'og:description', 'og:image', 'og:type', 'twitter:card', 'twitter:title', 'twitter:description', 'theme-color', 'apple-mobile-web-app-capable', 'apple-mobile-web-app-title'];
  names.forEach(name => {
    const meta = document.querySelector(`meta[name="${name}"], meta[property="${name}"]`);
    out[name] = meta ? (meta.content || meta.getAttribute('content')) : null;
  });
  ['canonical', 'manifest', 'icon', 'apple-touch-icon'].forEach(rel => {
    const link = document.querySelector(`link[rel="${rel}"]`);
    out['link:' + rel] = link ? link.href : null;
  });
  out.title = document.title;
  out.charset = !!document.querySelector('meta[charset]');
  out.viewport = !!document.querySelector('meta[name="viewport"]');
  return JSON.stringify(out, null, 1);
})()
