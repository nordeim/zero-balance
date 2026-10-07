// Follow-up probe: avatar, donut slice labels, nav structure.
(() => {
  const out = {};
  const cs = (el, prop) => (el ? getComputedStyle(el)[prop] : null);

  // Avatar — find element with 'D' or 'U' initial near topbar
  const av = [...document.querySelectorAll('div,span')].find((x) => /^[DU]$/u.test((x.textContent || '').trim()) && /rounded-full/.test(x.className || '') && (x.className || '').includes('h-9'));
  out.avatar = av ? { cls: av.className, bg: cs(av, 'backgroundColor'), bgImg: cs(av, 'backgroundImage').slice(0, 90), color: cs(av, 'color'), size: cs(av, 'width') } : null;

  // Donut slice labels — dump all text inside the recharts pie layer
  const pie = document.querySelector('.recharts-pie');
  if (pie) {
    out.pieTexts = [...pie.querySelectorAll('text, tspan')].map((t) => t.textContent.trim()).filter(Boolean);
    // structure of one label
    const l = pie.querySelector('text');
    out.pieLabelCls = l ? { cls: l.getAttribute('class'), fill: l.getAttribute('fill'), fontSize: cs(l, 'fontSize'), fontWeight: cs(l, 'fontWeight') } : null;
    // sector count + innerRadius estimate via sector path bbox
    out.sectorCount = pie.querySelectorAll('.recharts-sector').length;
  }

  // Donut wrapper: is there a center label?
  const surface = pie ? pie.closest('div[class*="relative"]') : null;
  out.donutCenter = surface ? [...surface.children].map((c) => ({ tag: c.tagName, cls: (c.className || '').slice(0, 60), text: (c.textContent || '').trim().slice(0, 30) })) : null;

  // Nav: find the sidebar links regardless of markup
  const sidebar = [...document.querySelectorAll('div')].filter((d) => /NAVIGATION/i.test(d.textContent || '') && d.children.length < 30).pop();
  if (sidebar) {
    let nav = sidebar;
    for (let i = 0; i < 6 && nav; i++) { nav = nav.parentElement; if (nav && (nav.textContent || '').includes('Dashboard') && (nav.textContent || '').includes('Net Worth') && (nav.textContent || '').length < 400) break; }
    const links = nav ? [...nav.querySelectorAll('a, button, [role="link"], div[class*="cursor"], span[class*="cursor"]')].filter((x) => /^(Dashboard|Income|Expenses|Savings|Net Worth)$/.test((x.textContent || '').trim())) : [];
    out.nav = links.map((x) => ({
      tag: x.tagName, text: x.textContent.trim(),
      bg: cs(x, 'backgroundImage') !== 'none' ? cs(x, 'backgroundImage').slice(0, 90) : cs(x, 'backgroundColor'),
      color: cs(x, 'color'), radius: cs(x, 'borderRadius'), fontWeight: cs(x, 'fontWeight'),
      cls: (x.className || '').slice(0, 90),
    }));
  }

  // Guidelines rows — the previous selector missed; find by text
  const gh = [...document.querySelectorAll('h3, p, span, div')].find((x) => (x.textContent || '').trim() === 'Needs' && (x.textContent || '') !== '');
  if (gh) {
    let card = gh; for (let i = 0; i < 8 && card; i++) { card = card.parentElement; if (card && /rounded-lg/.test(card.className || '')) break; }
    const gparent = card ? card.parentElement : null;
    out.guidelines = gparent ? [...gparent.children].slice(0, 3).map((c) => {
      const inner = c.querySelector('.rounded-lg') || c;
      return { title: (c.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40), bg: cs(inner, 'backgroundColor'), border: cs(inner, 'borderColor') };
    }) : null;
  }

  // Breakdown: expand Total Income and capture category row structure
  const bdBtn = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').includes('Total Income') && (b.className || '').includes('w-full'));
  if (bdBtn) {
    bdBtn.click();
    return new Promise((resolve) => setTimeout(() => {
      const r2 = { ...out };
      // find the expanded container right below
      let cont = bdBtn.nextElementSibling;
      r2.bdExpanded = cont ? {
        contCls: (cont.className || '').slice(0, 80),
        firstRowCls: cont.querySelector('button') ? cont.querySelector('button').className.slice(0, 140) : null,
        firstRowText: cont.querySelector('button') ? cont.querySelector('button').textContent.replace(/\s+/g, ' ').trim().slice(0, 70) : null,
        footer: cont.textContent.includes('categor') ? cont.textContent.replace(/\s+/g, ' ').match(/[\d]+ categor\w*/)?.[0] : null,
      } : null;
      // expand first category too (level 3)
      const catBtn = cont?.querySelector('button');
      if (catBtn) catBtn.click();
      setTimeout(() => {
        if (cont) {
          r2.bdLevel3 = {
            subCls: cont.querySelector('.ml-4 button, button.ml-2') ? (cont.querySelector('.ml-4 button') || {}).className?.slice(0, 120) : null,
            texts: cont.textContent.replace(/\s+/g, ' ').trim().slice(0, 260),
          };
        }
        resolve(JSON.stringify(r2, null, 1));
      }, 350);
    }, 350));
  }
  return JSON.stringify(out, null, 1);
})()
