// Session-7: quick overflow check per view.
(() => JSON.stringify({
  path: location.pathname,
  scrollW: document.documentElement.scrollWidth,
  mainW: Math.round((document.querySelector('main') || document.body).getBoundingClientRect().width),
}))()
