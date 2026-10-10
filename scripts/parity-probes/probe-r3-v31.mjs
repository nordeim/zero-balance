(async () => {
  // R3: on / — which nav item is active? Does a <nav> landmark exist?
  const links = [...document.querySelectorAll('a')].filter(a => a.offsetParent !== null && /dashboard|income|expenses|savings|net worth/i.test(a.textContent));
  const census = links.map(a => {
    const cs = getComputedStyle(a);
    return { text: a.textContent.trim().slice(0, 12), hasGradient: cs.backgroundImage !== 'none', color: cs.color };
  });
  return JSON.stringify({
    url: location.pathname,
    navLandmark: !!document.querySelector('nav'),
    links: census
  });
})()
