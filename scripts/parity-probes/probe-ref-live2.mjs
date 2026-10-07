// Live DOM dumps: donut legend rows, guidelines card, quick-action buttons, one stat card
(() => {
  const out = {};
  const textNode = (txt) => {
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = w.nextNode())) if ((n.textContent || '').trim() === txt) return n.parentElement;
    return null;
  };
  const up = (el, cls, max = 8) => { let c = el; for (let i = 0; i < max && c; i++) { if (c && (c.className || '').includes(cls)) return c; c = c.parentElement; } return null; };

  // Legend rows: rows with bg rgb(245,248,245) containing piggy-bank svg
  const pig = document.querySelector('svg.lucide-piggy-bank');
  if (pig) {
    const row = up(pig, 'rounded-lg');
    out.legendRow = row?.outerHTML.replace(/\s+/g, ' ').slice(0, 1500);
    // all sibling rows in same container
    const cont = row?.parentElement;
    out.legendOrder = cont ? [...cont.children].map((r) => (r.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40)) : null;
    out.legendContainerCls = cont?.className;
    // card wrapper for title + chart + legend structure
    const card = up(pig, 'rounded-2xl');
    out.donutCardHTML = card?.outerHTML.replace(/\s+/g, ' ').slice(0, 2600);
  }

  // Guidelines card
  const gl = textNode('Budget Guidelines');
  if (gl) { const card = up(gl, 'rounded-2xl'); out.guidelinesHTML = card?.outerHTML.replace(/\s+/g, ' ').slice(0, 2400); }

  // Quick action button (Add Income card-button)
  const qa = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === 'Add Income');
  if (qa) out.quickActionHTML = qa.outerHTML.replace(/\s+/g, ' ').slice(0, 1400);

  // Stat card (Total Income)
  const st = textNode('Total Income');
  if (st) { const card = up(st, 'rounded-2xl'); out.statCardHTML = card?.outerHTML.replace(/\s+/g, ' ').slice(0, 1900); }

  return out;
})()
