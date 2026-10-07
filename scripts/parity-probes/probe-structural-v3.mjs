// Session-5 deep probe: structural details not covered by the v2 probes.
(() => {
  const out = {};
  const cs = (el, prop) => (el ? getComputedStyle(el)[prop] : null);

  // 1. Dashboard h1 + subtitle
  const h1 = [...document.querySelectorAll('h1')].find((h) => (h.textContent || '').trim() === 'Budget Dashboard');
  out.h1 = h1 ? { cls: h1.className, size: cs(h1, 'fontSize'), weight: cs(h1, 'fontWeight') } : null;
  out.h1Sub = h1?.nextElementSibling ? { text: h1.nextElementSibling.textContent.trim(), cls: h1.nextElementSibling.className } : null;

  // 2. Quick-action card computed styles (first one)
  const qa = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim().startsWith('Add Income'));
  if (qa) {
    const chip = qa.querySelector('.rounded-xl, [class*="rounded-xl"]');
    out.quickAction = {
      cardCls: qa.className,
      border: cs(qa, 'borderColor'), radius: cs(qa, 'borderRadius'), padding: cs(qa, 'padding'),
      chipCls: chip ? chip.className : null, chipBg: chip ? cs(chip, 'backgroundColor') : null,
      icon: chip ? (chip.querySelector('svg') ? (chip.querySelector('svg').getAttribute('class') || '') : null) : null,
      plusIconColor: (() => { const p = [...qa.querySelectorAll('svg')].pop(); return p ? cs(p, 'color') : null; })(),
    };
  }

  // 3. Stat card count row (first stat)
  const ti = [...document.querySelectorAll('h3')].find((h) => (h.textContent || '').trim() === 'Total Income');
  if (ti) {
    const card = ti.closest('div[class*="rounded"]') || ti.parentElement.parentElement;
    const countRow = [...card.querySelectorAll('div')].find((d) => /item/.test(d.textContent || '') && d.children.length >= 2 && (d.className || '').includes('text-sm'));
    const div = countRow ? [...countRow.querySelectorAll('div')].find((x) => (x.className || '').includes('h-px')) : null;
    out.statCount = {
      text: countRow ? countRow.textContent.replace(/\s+/g, ' ').trim() : null,
      divH: div ? cs(div, 'height') : null, divBg: div ? cs(div, 'backgroundColor') : null,
      trendColor: (() => { const s = countRow?.querySelectorAll('svg'); const last = s && s.length ? s[s.length - 1] : null; return last ? cs(last, 'color') : null; })(),
      chevOpacity: (() => { const sv = card.querySelectorAll('svg'); const c = [...sv].find((x) => (x.getAttribute('class') || '').includes('chevron-right')); return c ? c.parentElement.className : null; })(),
    };
  }

  // 4. Breakdown first section button + drill-down structure
  const bd = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').includes('Total Income') && (b.className || '').includes('w-full'));
  if (bd) {
    out.breakdownBtn = { cls: bd.className.slice(0, 160), text: bd.textContent.replace(/\s+/g, ' ').trim().slice(0, 60) };
    const amt = [...bd.querySelectorAll('span,p,div')].find((x) => /^\$[\d.]+$/.test((x.textContent || '').trim()));
    out.breakdownAmt = amt ? { text: amt.textContent.trim(), weight: cs(amt, 'fontWeight'), color: cs(amt, 'color') } : null;
    const chev = bd.querySelector('svg[class*="chevron"]');
    out.breakdownChev = chev ? chev.getAttribute('class') : null;
  }

  // 5. Search placeholder
  const search = document.querySelector('input[type="search"], input[placeholder*="Search"]');
  out.searchPlaceholder = search ? search.placeholder : null;
  out.searchCls = search ? search.className.slice(0, 120) : null;

  // 6. Sidebar nav (active link + order)
  out.navLinks = [...document.querySelectorAll('nav a')].map((a) => ({
    text: a.textContent.trim(),
    active: /white|font-semibold/.test(getComputedStyle(a).color + a.className) && (a.className || '').includes('bg-') ? true : undefined,
    bg: cs(a, 'backgroundImage') !== 'none' ? cs(a, 'backgroundImage').slice(0, 80) : cs(a, 'backgroundColor'),
  })).slice(0, 6);

  // 7. Guidelines rows text (all 3)
  out.guidelines = [...document.querySelectorAll('h3')].filter((h) => /~\d+%/.test(h.textContent || '')).map((h) => {
    const card = h.closest('[class*="rounded-lg"]');
    return { title: h.textContent.trim(), bg: card ? cs(card, 'backgroundColor') : null, border: card ? cs(card, 'borderColor') : null };
  });

  // 8. Avatar area (topbar)
  const avatar = document.querySelector('[class*="rounded-full"]');
  out.avatarCls = avatar ? avatar.className.slice(0, 100) : null;

  // 9. Donut slice label format
  out.sliceLabels = [...document.querySelectorAll('.recharts-pie text, .recharts-pie tspan')].map((t) => t.textContent.trim()).filter(Boolean).slice(0, 5);

  // 10. Legend row structure (icon + swatch)
  const wantRow = (() => { const w = [...document.querySelectorAll('span')].find((s) => (s.textContent || '').trim() === 'Want'); return w ? w.closest('[class*="flex"]') : null; })();
  if (wantRow) {
    const icons = [...wantRow.querySelectorAll('svg')].map((s) => (s.getAttribute('class') || '').match(/lucide-([\w-]+)/)?.[1] || s.getAttribute('class')?.slice(0, 30));
    const swatch = wantRow.querySelector('[class*="w-4"], .rounded-full.w-\\[10px\\], [style*="background"]');
    out.legendRow = { icons, swatchCls: swatch ? swatch.className : null, swatchBg: swatch ? cs(swatch, 'backgroundColor') : null, text: wantRow.textContent.replace(/\s+/g, ' ').trim() };
  }

  return JSON.stringify(out, null, 1);
})()
