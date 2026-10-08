// probe-v11-card-badges.mjs — income card badge census v4: any-tag leaf elements, param amount
(() => {
  const out = { url: location.pathname };
  const amount = window.__CARD_AMT || '5000';
  const cands = [...document.querySelectorAll('div')].filter(el => {
    const t = (el.textContent || '');
    const r = el.getBoundingClientRect();
    return /Salary/.test(t) && new RegExp('\\$' + amount + '\\.00').test(t) && /(need|want)/i.test(t) && r.width > 200 && r.height > 80;
  });
  cands.sort((a, b) => (a.textContent || '').length - (b.textContent || '').length);
  const card = cands[0];
  if (!card) { out.card = 'NOT FOUND'; return JSON.stringify(out); }
  out.cardText = (card.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 90);
  const leaves = [...card.querySelectorAll('*')].filter(el => {
    const t = (el.textContent || '').trim();
    return el.children.length === 0 && t.length > 0 && t.length < 22 && el.getBoundingClientRect().height > 0 && el.getBoundingClientRect().height < 26;
  });
  out.badges = leaves.map(el => {
    const cs = getComputedStyle(el); const r = el.getBoundingClientRect();
    return { tag: el.tagName, txt: (el.textContent || '').trim(), color: cs.color, bg: cs.backgroundColor, fs: cs.fontSize, fw: cs.fontWeight, radius: cs.borderRadius, pad: cs.padding, w: Math.round(r.width), h: Math.round(r.height) };
  });
  return JSON.stringify(out, null, 1);
})()
