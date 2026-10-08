// Items-view census: count cards + header totals on the reference (v17 drift check)
(async () => {
  const main = document.querySelector("main") || document.body;
  const text = main.innerText;
  const header = text.match(/(\d+)\s*items?\s*·\s*(-?\$[\d,.]+)/i);
  const out = {
    url: location.pathname,
    headerItems: header ? header[1] : null,
    headerTotal: header ? header[2] : null,
    emptyState: /No\s|nothing|Add your first/i.test(text) && !header ? "EMPTY" : "has-cards",
  };
  return JSON.stringify(out);
})()
