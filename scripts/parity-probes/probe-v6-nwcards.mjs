// v6: net-worth asset card structure + actions (fresh angle — individual cards,
// not the summary). Dumps the first asset card's tag tree, classes, chrome, and
// any action buttons (resting + after hover).
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);

  // find asset cards: look under the Assets tab panel for the first grouped card
  const panel = document.querySelector('[data-state="active"][data-orientation="vertical"], [role="tabpanel"][data-state="active"]') || document;
  // cards = bordered divs containing an amount; take elements whose text has a $ and are direct children of a list-ish container
  const all = [...panel.querySelectorAll('div')].filter((d) => {
    const t = d.textContent || '';
    return /\$[\d,]+\.\d\d/.test(t) && d.querySelectorAll('div').length >= 2 && d.querySelectorAll('div').length <= 30;
  });
  // smallest such divs = the leaf cards
  const sorted = all.sort((a, b) => a.querySelectorAll('div').length - b.querySelectorAll('div').length);
  const card = sorted.find((c) => (c.textContent || '').includes('$'));

  if (card) {
    out.classes = card.className;
    out.chrome = { border: cs(card, 'borderColor'), radius: cs(card, 'borderRadius'), bg: cs(card, 'backgroundColor'), padding: cs(card, 'padding'), shadow: cs(card, 'boxShadow').slice(0, 60) };
    out.buttons = [...card.querySelectorAll('button')].map((b) => ({ label: (b.getAttribute('aria-label') || b.textContent || '').trim().slice(0, 30), visible: cs(b, 'opacity') !== '0', classes: b.className.slice(0, 120) }));
    out.text = (card.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 150);
  }

  // how many $-cards total under the panel
  out.dollarDivs = sorted.length;
  return JSON.stringify(out, null, 1);
})()
