// Dashboard evidence dump: hero card, stat cards, breakdown rows, donut legend,
// guidelines, add buttons — computed styles + structure.
(() => {
  const out = {};

  // ---- HERO (NET ZERO GOAL) ----
  const hero = [...document.querySelectorAll('h3')].find((h) => h.textContent?.trim() === 'NET ZERO GOAL')?.closest('div');
  if (hero) {
    const bal = [...hero.querySelectorAll('p')].find((p) => p.previousElementSibling?.textContent?.includes('Balance'));
    const balP = [...hero.querySelectorAll('p')].find((p) => /Balance/.test(p.textContent || ''));
    // status chip / label: any span with font-semibold or the chip
    const chips = [...hero.querySelectorAll('span')].map((s) => ({
      text: (s.textContent || '').trim().slice(0, 40),
      cls: s.className,
      color: getComputedStyle(s).color,
      bg: getComputedStyle(s).backgroundColor,
    })).filter((x) => x.text && x.text.length < 40 && !x.cls.includes('sr-only'));
    // allocation bar fill
    const track = [...hero.querySelectorAll('div')].find((d) => d.className.includes('rounded-full') && d.parentElement?.textContent?.includes('Allocation'));
    const fill = track ? [...track.children].find((c) => c.className.includes('rounded-full')) : null;
    out.hero = {
      text: hero.innerText.replace(/\n+/g, ' | ').slice(0, 300),
      balanceText: balP?.textContent?.trim(),
      balanceColor: balP ? getComputedStyle(balP).color : null,
      balanceCls: balP?.className,
      chips,
      fill: fill ? { bg: getComputedStyle(fill).background.replace(/\s+/g, ' ').slice(0, 220), width: getComputedStyle(fill).width } : null,
    };
  }

  // ---- STAT CARDS (Total Income/Savings/Expenses grid) ----
  const statTitles = [...document.querySelectorAll('h3')].filter((h) => /^(Total Income|Total Savings|Total Expenses)$/.test((h.textContent || '').trim()));
  out.statCards = statTitles.slice(0, 3).map((t) => {
    const card = t.closest('div.rounded-2xl') || t.parentElement?.parentElement?.parentElement;
    if (!card) return null;
    const amount = t.nextElementSibling;
    const countP = [...card.querySelectorAll('p')].find((p) => /items?/.test(p.textContent || ''));
    // h-px divider?
    const hpx = [...card.querySelectorAll('div')].find((d) => d.className.split(/\s+/).includes('h-px'));
    return {
      title: t.textContent?.trim(),
      amountText: amount?.textContent?.trim(),
      amountCls: amount?.className,
      amountColor: amount ? getComputedStyle(amount).color : null,
      countText: countP?.textContent?.trim(),
      countCls: countP?.className,
      hasHpxDivider: !!hpx,
    };
  });

  // ---- BREAKDOWN CARD ----
  const bdTitle = [...document.querySelectorAll('h3')].find((h) => (h.textContent || '').trim() === 'Net Zero Breakdown');
  if (bdTitle) {
    const card = bdTitle.closest('div.rounded-2xl') || bdTitle.parentElement;
    const rows = [...card.querySelectorAll('button')].map((b) => ({
      text: (b.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 60),
      aria: b.getAttribute('aria-expanded'),
      hasChevron: !!b.querySelector('svg[class*="chevron"], svg.lucide-chevron-down, svg.lucide-chevron-right'),
      chevronCls: b.querySelector('svg')?.getAttribute('class')?.slice(0, 80) || null,
    }));
    out.breakdown = { rows, html: card.innerHTML.length };
  }

  // ---- DONUT LEGEND ----
  const sbTitle = [...document.querySelectorAll('h3')].find((h) => (h.textContent || '').trim() === 'Spending Breakdown');
  if (sbTitle) {
    const card = sbTitle.closest('div.rounded-2xl') || sbTitle.parentElement;
    const legendRows = [...card.querySelectorAll('div')].filter((d) => d.className.includes('rounded-lg') && d.querySelector('p') && d.querySelectorAll('p').length >= 2 && !d.querySelector('svg.recharts-sector'));
    out.legend = legendRows.map((r) => {
      const label = [...r.querySelectorAll('span')].find((s) => !s.className.includes('h-4'));
      const icon = r.querySelector('svg[class*="lucide"]');
      return {
        label: label?.textContent?.trim(),
        iconClass: icon?.getAttribute('class')?.slice(0, 90) || null,
        bg: getComputedStyle(r).backgroundColor,
        amount: [...r.querySelectorAll('p')][0]?.textContent?.trim(),
        pct: [...r.querySelectorAll('p')][1]?.textContent?.trim(),
        html: r.innerHTML.replace(/\s+/g, ' ').slice(0, 400),
      };
    });
    // sector order
    const sectors = [...card.querySelectorAll('.recharts-sector')].map((s) => s.getAttribute('fill'));
    out.sectorFills = sectors;
  }

  // ---- GUIDELINES ----
  const glTitle = [...document.querySelectorAll('h3')].find((h) => (h.textContent || '').trim() === 'Budget Guidelines');
  if (glTitle) {
    const card = glTitle.closest('div.rounded-2xl') || glTitle.parentElement;
    const rows = [...card.children].filter((c) => c.tagName === 'DIV' && c !== card.querySelector('h3'));
    out.guidelines = [...card.querySelectorAll('div')].filter((d) => d.className.match(/rounded-(lg|xl)/) && d.querySelector('span')).slice(0, 4).map((r) => ({
      bg: getComputedStyle(r).backgroundColor,
      border: getComputedStyle(r).borderColor + ' ' + getComputedStyle(r).borderWidth,
      html: r.innerHTML.replace(/\s+/g, ' ').slice(0, 420),
    }));
  }

  // ---- ADD BUTTONS on dashboard ----
  out.addButtons = [...document.querySelectorAll('button')].filter((b) => /^Add /.test((b.textContent || '').trim())).map((b) => {
    const cs = getComputedStyle(b);
    return {
      text: (b.textContent || '').trim(),
      bg: cs.background.replace(/\s+/g, ' ').slice(0, 200),
      color: cs.color,
      radius: cs.borderRadius,
      cls: b.className.slice(0, 150),
    };
  });

  return out;
})()
