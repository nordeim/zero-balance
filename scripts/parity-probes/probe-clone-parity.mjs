// Clone-side parity evidence: dashboard surfaces after remediation v2.
(() => {
  const out = {};
  const textNode = (txt) => {
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = w.nextNode())) if ((n.textContent || '').trim() === txt) return n.parentElement;
    return null;
  };
  const up = (el, cls, max = 8) => { let c = el; for (let i = 0; i < max && c; i++) { if (c && (c.className || '').includes(cls)) return c; c = c.parentElement; } return null; };

  // --- Money formats (plain, no commas) ---
  out.body = document.body.innerText.replace(/\s+/g, ' ').slice(0, 700);

  // --- Hero ---
  const heroH = [...document.querySelectorAll('h3')].find((x) => (x.textContent || '').trim() === 'NET ZERO GOAL');
  let hero = heroH;
  while (hero && hero !== document.body) { const bg = getComputedStyle(hero).backgroundImage; if (bg && bg !== 'none' && bg.includes('linear-gradient')) break; hero = hero.parentElement; }
  const fill = hero?.querySelector('div.h-3 > div');
  const balP = [...(hero?.querySelectorAll('p') || [])].find((p) => /^\$[\d.]+$/.test((p.textContent || '').trim()));
  out.hero = {
    balance: balP?.textContent?.trim(),
    balanceCls: balP?.className,
    fill: fill ? getComputedStyle(fill).backgroundImage.replace(/\s+/g, ' ') : null,
    status: (hero?.innerText || '').includes('Under Budget') ? 'Under Budget' : 'other',
  };

  // --- Stat cards ---
  out.statAmounts = [...document.querySelectorAll('h3')].filter((h) => /^(Total Income|Total Savings|Total Expenses)$/.test((h.textContent || '').trim())).map((h) => {
    const p = h.nextElementSibling;
    return { title: h.textContent.trim(), cls: p?.className, color: p ? getComputedStyle(p).color : null, text: p?.textContent?.trim() };
  });

  // --- Donut legend ---
  const want = [...document.querySelectorAll('span.font-medium')].find((s) => (s.textContent || '').trim() === 'Want');
  if (want) {
    let row = want; for (let i = 0; i < 10 && row; i++) { row = row.parentElement; if (row && /rounded-lg/.test(row.className || '')) break; }
    out.legendOrder = row?.parentElement ? [...row.parentElement.children].map((r) => (r.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40)) : null;
  }
  out.sectorFills = [...document.querySelectorAll('.recharts-sector')].map((s) => s.getAttribute('fill'));

  // --- Guidelines ---
  const gl = textNode('Budget Guidelines');
  if (gl) { const card = up(gl, 'rounded-xl'); out.guidelinesFirst = card ? getComputedStyle(card.querySelector('div.rounded-lg')).backgroundColor : null; }

  // --- Add buttons ---
  out.addButtons = [...document.querySelectorAll('button')].filter((b) => /^Add /.test((b.textContent || '').trim())).map((b) => ({ text: (b.textContent || '').trim(), bg: getComputedStyle(b).backgroundImage.replace(/\s+/g, ' ').slice(0, 120), cls: (b.className || '').slice(0, 40) }));

  // --- Breakdown net balance ---
  const nb = textNode('Net Balance');
  if (nb) { const amt = nb.closest('div').parentElement.querySelector('span.text-lg, .text-lg'); out.netBalance = { text: amt?.textContent?.trim(), color: amt ? getComputedStyle(amt).color : null }; }

  return out;
})()
