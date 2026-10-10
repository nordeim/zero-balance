(async () => {
  const links = [...document.querySelectorAll('nav a, a')].filter(a => /dashboard|income|expenses|savings|net worth/i.test(a.textContent));
  return JSON.stringify(links.slice(0, 6).map(a => ({
    t: a.textContent.trim().slice(0, 10),
    cls: (a.className || '').toString().split(' ').slice(0, 6).join('.'),
    bg: getComputedStyle(a).backgroundColor,
    color: getComputedStyle(a).color,
    weight: getComputedStyle(a).fontWeight,
  })));
})()
