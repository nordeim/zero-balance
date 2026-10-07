(() => {
  // sonner-style toasts: li[data-sonner-toast] or [data-sooner] or ol[tabindex] children
  const toasts = [...document.querySelectorAll('li[data-sonner-toast], [data-sonner-toast], ol li[class*="toast"], [data-sooner]')];
  const viewport = document.querySelector('ol[tabindex="-1"], section[aria-label*="toast" i], div[class*="toaster"]');
  return JSON.stringify({
    toastCount: toasts.length,
    viewportClasses: viewport ? viewport.className.slice(0, 100) : null,
    viewportPE: viewport ? getComputedStyle(viewport).pointerEvents : null,
    first: toasts[0] ? { text: (toasts[0].textContent || '').trim().slice(0, 60), bg: getComputedStyle(toasts[0]).backgroundColor, classes: toasts[0].className.slice(0, 80) } : null,
  }, null, 1);
})()
