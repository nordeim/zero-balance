// v20 session: R4 per-route probe — reports the document's scrollWidth
// (390 = fits; 395/464 = the reference's horizontal overflow).
(() => {
  return JSON.stringify({
    path: location.pathname,
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
  });
})()
