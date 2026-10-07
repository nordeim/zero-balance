// Session-8 (v5): Add Budget Item dialog — panel chrome, form inputs, labels, buttons.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // dialog panel: the fixed overlay's inner content box
  const overlay = [...document.querySelectorAll('body > div, #root > div, body > [data-state], #root [role="dialog"]')].find((d) => (d.className || '').toString().includes('fixed'));
  let panel = null;
  if (overlay) {
    // find the panel: rounded white box inside
    panel = [...overlay.querySelectorAll('div')].find((d) => {
      const c = (d.className || '').toString();
      const r = d.getBoundingClientRect();
      return /rounded/.test(c) && r.width > 300 && r.width < 900 && cs(d, 'backgroundColor') === 'rgb(255, 255, 255)' && r.height > 300;
    });
  }
  if (panel) {
    const pr = panel.getBoundingClientRect();
    out.panel = { w: Math.round(pr.width), h: Math.round(pr.height), radius: cs(panel, 'borderRadius'), pad: cs(panel, 'padding'), shadow: cs(panel, 'boxShadow').slice(0, 80) };
  }

  // labels
  const labels = [...document.querySelectorAll('[role="dialog"] label, .fixed label, [data-state="open"] label')].filter((l) => (txt(l) || '').length > 0 && (txt(l) || '').length < 30);
  out.labels = labels.slice(0, 6).map((l) => ({ t: txt(l), size: cs(l, 'fontSize'), weight: cs(l, 'fontWeight'), color: cs(l, 'color') }));

  // inputs
  const inputs = [...document.querySelectorAll('.fixed input, [role="dialog"] input')].filter((i) => i.type !== 'radio');
  out.inputs = inputs.slice(0, 4).map((i) => ({
    h: Math.round(i.getBoundingClientRect().height),
    border: cs(i, 'borderWidth') + ' ' + cs(i, 'borderColor'),
    radius: cs(i, 'borderRadius'),
    bg: cs(i, 'backgroundColor'),
    shadow: cs(i, 'boxShadow').slice(0, 50),
    fontSize: cs(i, 'fontSize'),
  }));

  // classification tiles (Need/Want/Savings radio labels)
  const tiles = [...document.querySelectorAll('.fixed label, [role="dialog"] label')].filter((l) => /^(Need|Want|Savings)$/.test(txt(l) || ''));
  out.tiles = tiles.slice(0, 3).map((t) => {
    
    return { t: txt(t), border: cs(t, 'borderWidth') + ' ' + cs(t, 'borderColor'), radius: cs(t, 'borderRadius'), bg: cs(t, 'backgroundColor'), pad: cs(t, 'padding'), cls: (t.className || '').toString().replace(/\s+/g, ' ').slice(0, 150) };
  });

  // footer buttons
  const btns = [...document.querySelectorAll('.fixed button, [role="dialog"] button')].filter((b) => /^(Cancel|Save Item)$/.test(txt(b) || ''));
  out.buttons = btns.map((b) => ({
    t: txt(b),
    h: Math.round(b.getBoundingClientRect().height),
    bg: cs(b, 'backgroundColor'),
    color: cs(b, 'color'),
    radius: cs(b, 'borderRadius'),
    border: cs(b, 'borderWidth') + ' ' + cs(b, 'borderColor'),
    pad: cs(b, 'padding'),
    weight: cs(b, 'fontWeight'),
    cls: (b.className || '').toString().replace(/\s+/g, ' ').slice(0, 120),
  }));

  return JSON.stringify(out, null, 1);
})()
