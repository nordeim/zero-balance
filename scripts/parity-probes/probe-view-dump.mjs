// View dumper: main content innerText (normalized) + select trigger labels + card badge dump.
(() => {
  const main = document.querySelector('main') || document.body;
  const cards = [...main.querySelectorAll(':scope div[class*="border"][class*="rounded"]')].filter((c) => {
    const t = c.textContent || '';
    return /\$\d/.test(t) && (c.querySelector('h3') || c.querySelector('h4')) && t.length < 600 && !/All Categories/.test(t);
  });
  const dumpCard = (c) => {
    const badges = [...c.querySelectorAll('span')].filter((s) => {
      const t = (s.textContent || '').trim();
      return t && t.length < 22 && !/^\$/.test(t) && /border|rounded-full|bg-/.test(s.className || '') && !s.querySelector('span');
    });
    return {
      title: (c.querySelector('h3,h4') || {}).textContent?.trim(),
      catLine: (() => { const h = c.querySelector('h3,h4'); return h ? [...h.parentElement.children].filter((x) => x !== h).map((x) => x.textContent.trim()).join('|') : null; })(),
      amount: (() => { const a = [...c.querySelectorAll('p,span,h3,h4,div')].find((x) => /^\$[\d,.]+$/.test((x.textContent || '').trim())); return a ? { t: a.textContent.trim(), cls: (a.className || '').slice(0, 60), color: getComputedStyle(a).color } : null; })(),
      badges: badges.map((s) => ({
        t: s.textContent.trim(),
        cls: (s.className || '').replace(/\s+/g, ' ').slice(0, 100),
        icon: s.querySelector('svg') ? ((s.querySelector('svg').getAttribute('class') || '').match(/lucide-([\w-]+)/) || [])[1] : null,
      })),
      footer: c.textContent.replace(/\s+/g, ' ').match(/((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[^|]*?)(Bank|Cash|Credit)?\s*$/) ? c.textContent.replace(/\s+/g, ' ').trim().slice(-70) : null,
    };
  };
  return JSON.stringify({
    path: location.pathname,
    text: main.innerText.replace(/\s+/g, ' ').slice(0, 600),
    selects: [...main.querySelectorAll('button[role="combobox"]')].map((s) => s.textContent.trim()),
    cardCount: cards.length,
    firstCard: cards[0] ? dumpCard(cards[0]) : null,
    secondCard: cards[1] ? dumpCard(cards[1]) : null,
  }, null, 1);
})()
