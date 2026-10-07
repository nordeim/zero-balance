// Session-7: net worth view structural dump.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. Summary card
  const sumCard = [...document.querySelectorAll('div')].find((d) => {
    const c = (d.className || '').toString();
    return c.includes('rounded-2xl') && /Net Worth/i.test(txt(d) || '') && /\$/.test(txt(d) || '') && (d.textContent || '').includes('Assets');
  });
  if (sumCard) {
    out.summary = {
      bg: cs(sumCard, 'backgroundImage').slice(0, 100),
      texts: [...sumCard.querySelectorAll('p,span,h3,div')].filter((x) => x.children.length === 0).map(txt).filter(Boolean).slice(0, 10),
    };
    const ratio = [...sumCard.querySelectorAll('*')].find((x) => /:1$|∞/.test(txt(x) || '') && x.children.length === 0);
    out.ratio = ratio ? { text: txt(ratio), size: cs(ratio, 'fontSize'), weight: cs(ratio, 'fontWeight') } : null;
  }

  // 2. Tabs
  const tabs = [...document.querySelectorAll('[role="tab"]')].map((t) => ({ text: txt(t), active: t.getAttribute('aria-selected'), cls: t.className.toString().slice(0, 80) }));
  out.tabs = tabs;

  // 3. Active tab content: type group headers + cards
  const activePanel = document.querySelector('[role="tabpanel"][data-state="active"], [data-state="active"][role="tabpanel"]');
  const panel = activePanel || document.querySelector('main');
  if (panel) {
    const headers = [...panel.querySelectorAll('h3,h4,p')].filter((x) => {
      const t = txt(x) || '';
      return /^[A-Z][a-z]+ \(\d+\)$/.test(t) || /^(Assets|Liabilities) \(/.test(t);
    }).map((x) => ({ text: txt(x), tag: x.tagName, cls: x.className.toString().slice(0, 60) }));
    out.groupHeaders = headers.slice(0, 6);
    // first asset/liability card
    const card = [...panel.querySelectorAll('div[class*="rounded-xl"], div[class*="rounded-lg"]')].filter((d) => /\$[\d,]+/.test(txt(d) || '')).slice(1, 4)[0];
    if (card) out.firstCard = { texts: [...card.querySelectorAll('p,span,h4,div')].filter((x) => x.children.length === 0).map(txt).filter(Boolean).slice(0, 8), cls: card.className.toString().slice(0, 90) };
  }

  return JSON.stringify(out, null, 1);
})()
