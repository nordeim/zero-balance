// v41: the net-worth summary card's MOBILE geometry (390x844) — the queued
// surface ("the net-worth summary card's gradient chip at the savings-class
// viewports"). Measures the gradient hero card's full structure at mobile:
// the card box (padding/radius/gradient/shadow), the figure's font-size
// (the reference's fixed text-5xl overflow bug), the 64x64 white/20% icon
// chip, the stats grid's column count (the reference's fixed 2-col overflow
// bug), the ratio footer row, and the card's overflow contribution.
// Read-only: measures computed styles + rects, clicks nothing.
(() => {
  const vw = window.innerWidth;
  // The summary card: the gradient hero wrapping the "Total Net Worth" label.
  const label = [...document.querySelectorAll('p, span, h2, div')].find(
    (e) => (e.textContent || '').trim() === 'Total Net Worth' && e.children.length === 0,
  );
  if (!label) return JSON.stringify({ error: 'NO TOTAL NET WORTH LABEL' });
  const card = label.closest('div.rounded-2xl') || label.closest('[class*="rounded"]');
  if (!card) return JSON.stringify({ error: 'NO CARD ANCESTOR' });
  const cr = card.getBoundingClientRect();
  const cs = getComputedStyle(card);

  // The h2 figure (the net-worth amount) — the reference's text-5xl overflow.
  const h2 = [...card.querySelectorAll('h1, h2, h3, p')].find(
    (e) => /-?\$[\d,]+\.\d{2}/.test((e.textContent || '').trim()) && e !== label,
  );
  const h2r = h2 ? h2.getBoundingClientRect() : null;
  const h2cs = h2 ? getComputedStyle(h2) : null;

  // The icon chip: the rounded-full circle wrapping a 24-32px white icon
  // (the reference's h-16 w-16 white/20 circle, the "gradient chip").
  const chip = [...card.querySelectorAll('div')].find(
    (d) => {
      const r = d.getBoundingClientRect();
      const c = getComputedStyle(d);
      return (
        r.width > 40 && r.width < 90 &&
        (c.borderRadius === '9999px' || (parseFloat(c.borderRadius) > 40 && c.borderRadius !== '0px')) &&
        d.querySelector('svg')
      );
    },
  );
  const chr = chip ? chip.getBoundingClientRect() : null;
  const chcs = chip ? getComputedStyle(chip) : null;

  // The stats grid: the container wrapping "Total Assets" + "Total Liabilities".
  const assetsLabel = [...card.querySelectorAll('p, span')].find(
    (e) => (e.textContent || '').trim() === 'Total Assets',
  );
  const grid = assetsLabel ? assetsLabel.closest('[class*="grid"]') : null;
  const gridcs = grid ? getComputedStyle(grid) : null;
  const gridCells = grid
    ? [...grid.children].map((c) => {
        const r = c.getBoundingClientRect();
        return { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x) };
      })
    : [];

  // The ratio footer: the border-t row with "Asset to Liability Ratio".
  const ratioLabel = [...card.querySelectorAll('span, p, div')].find(
    (e) => /Asset to Liability Ratio/.test((e.textContent || '')) && e.children.length === 0,
  );
  const ratioRow = ratioLabel ? ratioLabel.parentElement : null;
  const ratioVal = ratioLabel
    ? [...(ratioLabel.parentElement?.children || [])].find((e) => e !== ratioLabel)
    : null;

  // The header chip (48x48, pinned v14 — re-measured for the complete pair).
  const h1 = [...document.querySelectorAll('main h1')].find(
    (h) => (h.textContent || '').trim() === 'Net Worth',
  );
  const headerChip = h1
    ? [...(h1.parentElement?.parentElement?.children || [])].find(
        (c) => c.tagName === 'DIV' && c !== h1.parentElement,
      )
    : null;
  const hcr = headerChip ? headerChip.getBoundingClientRect() : null;

  // The radial overlay decoration (the absolute white radial circle).
  const overlay = [...card.querySelectorAll('div')].find(
    (d) => getComputedStyle(d).position === 'absolute' && (d.className || '').toString().includes('rounded'),
  );

  return JSON.stringify(
    {
      vw,
      sw: document.documentElement.scrollWidth,
      card: {
        x: Math.round(cr.x),
        y: Math.round(cr.y),
        w: Math.round(cr.width),
        h: Math.round(cr.height),
        pad: cs.padding,
        radius: cs.borderRadius,
        bg: (cs.backgroundImage || '').slice(0, 80),
        shadow: (cs.boxShadow || '').slice(0, 80),
        overflow: cs.overflow,
      },
      figure: h2
        ? {
            text: (h2.textContent || '').trim().slice(0, 16),
            font: h2cs.fontSize,
            weight: h2cs.fontWeight,
            color: h2cs.color,
            w: Math.round(h2r.width),
            right: Math.round(h2r.right),
            pastViewport: Math.round(h2r.right) > vw,
          }
        : null,
      chip: chr
        ? {
            w: Math.round(chr.width),
            h: Math.round(chr.height),
            x: Math.round(chr.x),
            y: Math.round(chr.y),
            radius: chcs.borderRadius,
            bg: chcs.backgroundColor,
            iconW: Math.round(chip.querySelector('svg').getBoundingClientRect().width),
          }
        : null,
      statsGrid: gridcs
        ? { cols: gridcs.gridTemplateColumns, gap: gridcs.gap, cells: gridCells }
        : null,
      ratioFooter: ratioRow
        ? {
            border: getComputedStyle(ratioRow).borderTopWidth + ' ' + getComputedStyle(ratioRow).borderTopColor,
            val: ratioVal ? (ratioVal.textContent || '').trim() : null,
            valFont: ratioVal ? getComputedStyle(ratioVal).fontSize : null,
          }
        : null,
      headerChip: hcr ? { w: Math.round(hcr.width), x: Math.round(hcr.x) } : null,
      overlay: overlay ? { w: Math.round(overlay.getBoundingClientRect().width), opacity: getComputedStyle(overlay).opacity } : null,
    },
    null,
    1,
  );
})()
