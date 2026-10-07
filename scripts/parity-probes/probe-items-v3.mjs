// Items-view structural probe (income/expenses/savings).
(() => {
  const out = { path: location.pathname };
  const cs = (el, prop) => (el ? getComputedStyle(el)[prop] : null);

  // Header: h1 + chip + subtitle
  const h1 = document.querySelector('h1');
  out.h1 = h1 ? { text: h1.textContent.trim(), cls: h1.className, size: cs(h1, 'fontSize') } : null;
  const chip = h1 ? h1.parentElement.querySelector('.rounded-xl, [class*="rounded-xl"]') : null;
  if (chip) {
    out.chip = {
      cls: chip.className.slice(0, 90), bg: cs(chip, 'backgroundImage') !== 'none' ? cs(chip, 'backgroundImage').slice(0, 100) : cs(chip, 'backgroundColor'),
      size: cs(chip, 'width'),
      iconColor: chip.querySelector('svg') ? cs(chip.querySelector('svg'), 'color') : null,
      iconCls: chip.querySelector('svg') ? (chip.querySelector('svg').getAttribute('class') || '').slice(0, 40) : null,
    };
  }
  const sub = h1 ? [...h1.parentElement.children].find((c) => /item/.test(c.textContent || '') && c !== h1) : null;
  out.subtitle = sub ? { text: sub.textContent.replace(/\s+/g, ' ').trim(), cls: (sub.className || '').slice(0, 60) } : null;

  // Add button
  const addBtn = [...document.querySelectorAll('button')].find((b) => /^Add (Income|Savings|Expense|Asset|Liability)/.test((b.textContent || '').trim()));
  out.addBtn = addBtn ? { text: addBtn.textContent.trim(), bg: cs(addBtn, 'backgroundImage').slice(0, 110) } : null;

  // Search + filters
  const search = document.querySelector('input[placeholder*="Search"], input[type="search"]');
  out.search = search ? { ph: search.placeholder, cls: (search.className || '').slice(0, 80) } : null;
  out.selects = [...document.querySelectorAll('select')].map((s) => ({ value: s.value, cls: (s.className || '').slice(0, 50) }));

  // First item card
  const cards = [...document.querySelectorAll('[data-item-id], div.rounded-xl.border')].filter((c) => {
    const t = c.textContent || '';
    return /(\$[\d,]+(\.\d{2})?)/.test(t) && c.querySelector('h3, h4') && !/Sign in/.test(t);
  });
  const card = cards[0];
  if (card) {
    out.card = {
      cls: (card.className || '').slice(0, 90),
      title: (card.querySelector('h3, h4') || {}).textContent?.trim(),
      // category line (first text-sm gray with a dot?)
      badges: [...card.querySelectorAll('span')].filter((s) => (s.textContent || '').trim().length > 0 && (s.textContent || '').trim().length < 24 && /border|badge|rounded|bg-|text-/.test(s.className || '')).slice(0, 8).map((s) => ({
        text: s.textContent.trim(),
        cls: (s.className || '').replace(/\s+/g, ' ').slice(0, 110),
        bg: cs(s, 'backgroundColor'), color: cs(s, 'color'), borderColor: cs(s, 'borderColor'),
        icon: s.querySelector('svg') ? ((s.querySelector('svg').getAttribute('class') || '').match(/lucide-([\w-]+)/) || [])[1] : null,
      })),
      amountEl: (() => { const a = [...card.querySelectorAll('p, span, div')].find((x) => /^\$[\d.]+$/.test((x.textContent || '').trim())); return a ? { text: a.textContent.trim(), cls: (a.className || '').slice(0, 70), color: cs(a, 'color'), size: cs(a, 'fontSize') } : null; })(),
      footer: (() => { const f = [...card.querySelectorAll('div')].filter((d) => /calendar|Updated|credit|card/i.test(d.innerHTML || '') && d.children.length && d.textContent.length < 120).pop(); return f ? f.textContent.replace(/\s+/g, ' ').trim().slice(0, 100) : null; })(),
      hoverButtons: (() => { const btns = [...card.querySelectorAll('button')].filter((b) => { const r = b.getBoundingClientRect(); const o = cs(b.parentElement, 'opacity'); return b.textContent.trim() === '' || /Edit|Calculate|Delete/.test(b.getAttribute('title') || ''); }); return btns.map((b) => ({ title: b.getAttribute('title'), aria: b.getAttribute('aria-label'), cls: (b.className || '').replace(/\s+/g, ' ').slice(0, 90), icon: b.querySelector('svg') ? ((b.querySelector('svg').getAttribute('class') || '').match(/lucide-([\w-]+)/) || [])[1] : null })).slice(0, 4); })(),
      hasEllipsis: !!card.querySelector('button[aria-label*="More"], button .lucide-ellipsis, button.lucide-more-horizontal, [aria-label*="more" i]'),
    };
  }

  // Empty state (if no cards)
  out.cardCount = cards.length;
  return JSON.stringify(out, null, 1);
})()
