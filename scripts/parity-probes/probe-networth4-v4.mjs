// Session-7: networth page below the summary card — tabs, counts, updated footer.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  const sumCard = [...document.querySelectorAll('div')].find((d) => {
    const c = (d.className || '').toString();
    return c.includes('rounded-2xl') && /Total Net Worth/i.test(txt(d) || '');
  });
  if (sumCard && sumCard.parentElement) {
    const below = [...sumCard.parentElement.children].filter((el) => el !== sumCard);
    out.siblingCount = below.length;
    out.siblings = below.map((el) => ({ tag: el.tagName, cls: (el.className || '').toString().slice(0, 70), text: txt(el).slice(0, 120) }));
  }

  // tabs list with counts
  out.tabsRaw = [...document.querySelectorAll('[role="tab"]')].map((t) => ({ text: txt(t), html: t.outerHTML.replace(/\s+/g, ' ').slice(0, 300) }));

  // Updated footer
  const upd = [...document.querySelectorAll('div,p,span')].find((x) => /Updated/i.test(txt(x) || '') && x.children.length === 0);
  out.updated = upd ? { text: txt(upd), cls: upd.className.toString().slice(0, 70), color: cs(upd, 'color'), size: cs(upd, 'fontSize') } : null;

  // items count line ("1 items · $25,000")
  const cnt = [...document.querySelectorAll('p,span')].find((x) => /items? ·/.test(txt(x) || ''));
  out.countLine = cnt ? { text: txt(cnt), cls: cnt.className.toString().slice(0, 70) } : null;

  return JSON.stringify(out, null, 1);
})()
