(() => {
  const main = document.querySelector('main');
  // the first grid/card container inside main's scroll area
  const cards = [...main.querySelectorAll('div')].filter((d) => {
    const cs = getComputedStyle(d);
    return cs.borderTopWidth === '1px' && d.getBoundingClientRect().width > 500;
  }).sort((a, b) => a.getBoundingClientRect().y - b.getBoundingClientRect().y);
  const first = cards[0];
  return JSON.stringify({
    vw: document.documentElement.clientWidth,
    firstCardW: first ? Math.round(first.getBoundingClientRect().width) : null,
    firstCardX: first ? Math.round(first.getBoundingClientRect().x) : null,
  }, null, 1);
})()
