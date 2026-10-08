// probe-v11-clone-r2.mjs — clone mobile R2: tap Income in sheet, verify close-on-nav + active state
(() => {
  const out = { url: location.pathname };
  // tap Income inside the sheet
  const sheet = [...document.querySelectorAll('div')].find(d => {
    const r = d.getBoundingClientRect(); const cs = getComputedStyle(d);
    return r.width >= 280 && r.width <= 295 && cs.position === 'fixed' && r.height > 700;
  });
  if (!sheet) { out.sheet = 'NOT OPEN — cannot tap'; return JSON.stringify(out); }
  const link = [...sheet.querySelectorAll('a,button')].filter(el =>
    (el.textContent || '').trim() === 'Income' && el.getBoundingClientRect().top > 100)[0];
  if (link) { link.click(); out.tapped = true; } else { out.tapped = false; }
  return JSON.stringify(out);
})()
