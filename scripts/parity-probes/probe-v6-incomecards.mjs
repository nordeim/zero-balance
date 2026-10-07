(() => {
  const cards = [...document.querySelectorAll('main h4')].map((h) => {
    let card = h;
    while (card.parentElement && !/hover:shadow/.test(card.className || '') && !(getComputedStyle(card).borderTopWidth === '1px' && getComputedStyle(card).borderTopStyle === 'solid')) card = card.parentElement;
    return (card.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 130);
  }).filter((t) => /\$/.test(t));
  const head = (document.querySelector('main h1')?.textContent || '').trim();
  const counts = (document.querySelector('main')?.textContent || '').match(/\d+ items?/g);
  return JSON.stringify({ page: head, counts, cards }, null, 1);
})()
