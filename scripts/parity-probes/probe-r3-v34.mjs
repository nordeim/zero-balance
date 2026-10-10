(async () => {
  // R3: navigate to / then check for nav landmark + active link highlighting
  const links = [...document.querySelectorAll('a[href="/"], a[href="/dashboard"], a[href="/income"]')];
  const active = [...document.querySelectorAll('a')].filter(a => {
    const bg = getComputedStyle(a).backgroundColor;
    return bg !== 'rgba(0, 0, 0, 0)' && a.closest('header, aside, div');
  });
  return JSON.stringify({
    path: location.pathname,
    navLandmark: !!document.querySelector('nav'),
    sidebarLinks: links.length,
    activeHighlighted: active.map(a => a.textContent.trim().slice(0, 12)),
  });
})()
