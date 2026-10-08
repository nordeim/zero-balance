// v20 session: items-view census — reads the per-view "N items · $X.00"
// summary. ASCII-only source (the middle dot as \u00b7): the base64→atob→eval
// probe transport mangles multi-byte UTF-8 (the v19 file's literal dot became
// two Latin-1 chars and never matched — the empty-counts mystery).
(() => {
  const SEP = String.fromCharCode(0xb7); // U+00B7 MIDDLE DOT
  const texts = [...document.querySelectorAll('h2,h3,p,span,div')].map((el) => (el.textContent || '').trim());
  const re = new RegExp('^\\d+ items? ' + SEP + ' \\$[\\d,.]+$');
  const counts = texts.filter((t) => re.test(t)).slice(0, 6);
  // also the h1/hero-level heading + first cards (type + amount) for context
  const cards = [...document.querySelectorAll('main h3')].map((h) => (h.textContent || '').trim()).slice(0, 8);
  return JSON.stringify({ path: location.pathname, counts, cards }, null, 1);
})()
