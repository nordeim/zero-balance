#!/usr/bin/env bash
# clone-v52.sh — the clone-side driver for the v52 surfaces, mirroring
# ref-v52.sh's census axes on http://localhost:3200 (the standalone
# parity build): (1) /income at 390, (2) /expenses at 390, (3) the
# item-details sheet's internals at 390.
set -u
BASE="http://localhost:3200"

export AGENT_BROWSER_SESSION="clone52"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4

echo ""
echo "=== CLONE surface 1: the /income VIEW at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const h1 = [...document.querySelectorAll('h1')].find(x => (x.textContent||'').trim() === 'Income');
  if (!h1) return 'no H1';
  let headRow = h1.closest('div.flex') || h1.parentElement;
  for (let i = 0; i < 4 && headRow.parentElement; i++) {
    if (headRow.querySelector('button')) break;
    headRow = headRow.parentElement;
  }
  const chip = headRow.querySelector('div.rounded-xl, [class*=rounded-xl]');
  const addBtn = [...headRow.querySelectorAll('button')].pop();
  const sub = [...headRow.querySelectorAll('p')].find(p => /items/.test(p.textContent||''));
  const hrs = headRow.getBoundingClientRect();
  const csR = getComputedStyle(headRow);
  let filter = null;
  let el = headRow.nextElementSibling;
  while (el && !filter) {
    if (/rounded/.test(el.className || '') && el.querySelector('input')) filter = el;
    el = el.nextElementSibling;
  }
  const fcs = filter ? getComputedStyle(filter) : null;
  const fr = filter ? filter.getBoundingClientRect() : null;
  const search = filter ? filter.querySelector('input[type=text], input:not([type])') : null;
  const h4 = [...document.querySelectorAll('h4')].find(x => /Salary/i.test((x.textContent||'').trim()));
  let card = h4 ? h4.closest('div.rounded-xl') || h4.parentElement : null;
  for (let i = 0; card && i < 5; i++) {
    const cs = getComputedStyle(card.parentElement);
    if (cs.display === 'grid') break;
    card = card.parentElement;
  }
  const grid = card ? card.parentElement : null;
  const gcs = grid ? getComputedStyle(grid) : null;
  const ccs = card ? getComputedStyle(card) : null;
  const cr = card ? card.getBoundingClientRect() : null;
  const cards = grid ? [...grid.children].map(c => { const r = c.getBoundingClientRect(); return { w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y) }; }) : [];
  const amount = card ? [...card.querySelectorAll('p,span,div')].find(p => /^[-+]?[\\\$]?[\\d,]+/.test((p.textContent||'').trim()) && p.children.length <= 1) : null;
  const badge = card ? [...card.querySelectorAll('span,div')].filter(b => /rounded-full|px-2|px-3/.test(b.className||'') && (b.textContent||'').trim().length > 0 && b.children.length === 0).slice(0,1) : [];
  return JSON.stringify({
    headRow: { w: Math.round(hrs.width), h: Math.round(hrs.height), display: csR.display, direction: csR.flexDirection, gap: csR.gap, mb: csR.marginBottom, alignItems: csR.alignItems },
    chip: chip ? { w: Math.round(chip.getBoundingClientRect().width), h: Math.round(chip.getBoundingClientRect().height), radius: getComputedStyle(chip).borderRadius, bg: getComputedStyle(chip).backgroundImage || getComputedStyle(chip).backgroundColor } : null,
    h1: { fs: getComputedStyle(h1).fontSize, fw: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color },
    sub: sub ? { fs: getComputedStyle(sub).fontSize, fw: getComputedStyle(sub).fontWeight, color: getComputedStyle(sub).color, text: sub.textContent.trim().slice(0, 30) } : null,
    addBtn: addBtn ? { w: Math.round(addBtn.getBoundingClientRect().width), h: Math.round(addBtn.getBoundingClientRect().height), radius: getComputedStyle(addBtn).borderRadius, bg: (getComputedStyle(addBtn).backgroundImage || getComputedStyle(addBtn).backgroundColor).slice(0, 80), color: getComputedStyle(addBtn).color, fs: getComputedStyle(addBtn).fontSize, fw: getComputedStyle(addBtn).fontWeight, pad: getComputedStyle(addBtn).padding, text: addBtn.textContent.trim().slice(0, 16) } : null,
    filterCard: fr ? { w: Math.round(fr.width), radius: fcs.borderRadius, pad: fcs.padding, bg: fcs.backgroundColor, border: fcs.border, mb: fcs.marginBottom, children: filter.children.length } : null,
    search: search ? { w: Math.round(search.getBoundingClientRect().width), h: Math.round(search.getBoundingClientRect().height), radius: getComputedStyle(search).borderRadius, pad: getComputedStyle(search).padding, ph: search.placeholder } : null,
    itemGrid: gcs ? { display: gcs.display, cols: gcs.gridTemplateColumns, gap: gcs.gap, children: grid.children.length } : null,
    cards,
    firstCard: cr ? { w: Math.round(cr.width), h: Math.round(cr.height), radius: ccs.borderRadius, pad: ccs.padding, border: ccs.border, bg: ccs.backgroundColor, shadow: (ccs.boxShadow||'none').slice(0, 70) } : null,
    h4: h4 ? { fs: getComputedStyle(h4).fontSize, fw: getComputedStyle(h4).fontWeight, color: getComputedStyle(h4).color, text: h4.textContent.trim().slice(0, 16) } : null,
    amount: amount ? { fs: getComputedStyle(amount).fontSize, fw: getComputedStyle(amount).fontWeight, color: getComputedStyle(amount).color, text: amount.textContent.trim().slice(0, 14) } : null,
    badge: badge.length ? { cls: (badge[0].className||'').toString().slice(0, 60), fs: getComputedStyle(badge[0]).fontSize, fw: getComputedStyle(badge[0]).fontWeight, text: badge[0].textContent.trim() } : null,
    docSW: document.documentElement.scrollWidth
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE surface 2: the /expenses VIEW at 390 ==="
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const h1 = [...document.querySelectorAll('h1')].find(x => (x.textContent||'').trim() === 'Expenses');
  if (!h1) return 'no H1';
  let headRow = h1.closest('div.flex') || h1.parentElement;
  for (let i = 0; i < 4 && headRow.parentElement; i++) {
    if (headRow.querySelector('button')) break;
    headRow = headRow.parentElement;
  }
  const addBtn = [...headRow.querySelectorAll('button')].pop();
  const sub = [...headRow.querySelectorAll('p')].find(p => /items/.test(p.textContent||''));
  let filter = null;
  let el = headRow.nextElementSibling;
  while (el && !filter) {
    if (/rounded/.test(el.className || '') && el.querySelector('input')) filter = el;
    el = el.nextElementSibling;
  }
  const inner = filter ? filter.querySelector('div.grid') : null;
  const ics = inner ? getComputedStyle(inner) : null;
  const triggers = filter ? [...filter.querySelectorAll('button[role=combobox], select')].length : 0;
  const h4 = [...document.querySelectorAll('h4')].find(x => /Rent/i.test((x.textContent||'').trim()));
  let card = h4 ? h4.closest('div.rounded-xl') || h4.parentElement : null;
  for (let i = 0; card && i < 5; i++) {
    const cs = getComputedStyle(card.parentElement);
    if (cs.display === 'grid') break;
    card = card.parentElement;
  }
  const ccs = card ? getComputedStyle(card) : null;
  const cr = card ? card.getBoundingClientRect() : null;
  return JSON.stringify({
    h1: { fs: getComputedStyle(h1).fontSize, fw: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color },
    sub: sub ? { text: sub.textContent.trim().slice(0, 30), fs: getComputedStyle(sub).fontSize, color: getComputedStyle(sub).color } : null,
    addBtn: addBtn ? { w: Math.round(addBtn.getBoundingClientRect().width), h: Math.round(addBtn.getBoundingClientRect().height), bg: (getComputedStyle(addBtn).backgroundImage || getComputedStyle(addBtn).backgroundColor).slice(0, 80), text: addBtn.textContent.trim().slice(0, 16) } : null,
    filterCard: filter ? { w: Math.round(filter.getBoundingClientRect().width), radius: getComputedStyle(filter).borderRadius, pad: getComputedStyle(filter).padding } : null,
    filterGrid: ics ? { display: ics.display, cols: ics.gridTemplateColumns, gap: ics.gap, children: inner.children.length, triggers } : null,
    firstCard: cr ? { w: Math.round(cr.width), h: Math.round(cr.height), radius: ccs.borderRadius, pad: ccs.padding, border: ccs.border, bg: ccs.backgroundColor, shadow: (ccs.boxShadow||'none').slice(0, 70) } : null,
    h4: h4 ? { text: h4.textContent.trim().slice(0, 16), fs: getComputedStyle(h4).fontSize, fw: getComputedStyle(h4).fontWeight } : null,
    docSW: document.documentElement.scrollWidth
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE surface 3: the item-details sheet INTERNALS at 390 ==="
agent-browser eval "(async () => {
  const h4 = [...document.querySelectorAll('h4')].find(x => /Rent/i.test((x.textContent||'').trim()));
  if (!h4) return 'no card title';
  const card = h4.closest('div.rounded-xl') || h4.parentElement;
  card.click();
  await new Promise(r => setTimeout(r, 1200));
  const dlg = document.querySelector('[role=dialog], [role=alertdialog]');
  if (!dlg) return 'no dialog';
  const r = dlg.getBoundingClientRect();
  const cs = getComputedStyle(dlg);
  const kids = [...dlg.children].map(c => ({ tag: c.tagName, cls: (c.className||'').toString().slice(0, 60), h: Math.round(c.getBoundingClientRect().height) }));
  const header = dlg.querySelector('div.sticky') || dlg.children[0];
  const hcs = header ? getComputedStyle(header) : null;
  const title = header ? [...header.querySelectorAll('h2,h3,h1')].find(t => /Details/i.test(t.textContent||'')) : null;
  const closeBtn = header ? [...header.querySelectorAll('button')].pop() : null;
  const body = [...dlg.children].find(c => c !== header && /space-y|p-6/.test((c.className||'').toString()));
  const bcs = body ? getComputedStyle(body) : null;
  const summary = body ? body.firstElementChild : null;
  const sumIn = summary ? [...summary.querySelectorAll('div,span,p')].filter(e => e.children.length <= 1).slice(0, 6).map(e => ({ tag: e.tagName, text: (e.textContent||'').trim().slice(0, 20), fs: getComputedStyle(e).fontSize, fw: getComputedStyle(e).fontWeight, color: getComputedStyle(e).color, cls: (e.className||'').toString().slice(0, 40) })) : [];
  const factRow = body ? [...body.querySelectorAll('div')].filter(d => (d.className||'').toString().includes('flex') && d.querySelector('svg') && (d.textContent||'').trim().length > 0 && d.children.length === 2).slice(0, 3) : [];
  const facts = factRow.map(d => ({ pad: getComputedStyle(d).padding, gap: getComputedStyle(d).gap, label: (d.children[1].textContent||'').trim().slice(0, 30) }));
  const actions = [...dlg.querySelectorAll('button')].filter(b => /Edit|Delete|Calculate|Close/i.test((b.textContent||'')) && b.closest('div.sticky') === null);
  const btns = actions.slice(0, 3).map(b => { const s = getComputedStyle(b); const br = b.getBoundingClientRect(); return { text: (b.textContent||'').trim().slice(0, 10), w: Math.round(br.width), h: Math.round(br.height), fs: s.fontSize, fw: s.fontWeight, color: s.color, bg: (s.backgroundImage || s.backgroundColor).slice(0, 70), radius: s.borderRadius, pad: s.padding }; });
  return JSON.stringify({
    panel: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height), radius: cs.borderRadius, maxH: cs.maxHeight, bg: cs.backgroundColor, overflowY: cs.overflowY, shadow: cs.boxShadow.slice(0, 90), layers: (cs.boxShadow.match(/px, /g) || []).length + 1 },
    kids,
    header: hcs ? { h: Math.round(header.getBoundingClientRect().height), pad: hcs.padding, pos: hcs.position, top: hcs.top, z: hcs.zIndex, borderB: hcs.borderBottom, bg: hcs.backgroundColor } : null,
    title: title ? { fs: getComputedStyle(title).fontSize, fw: getComputedStyle(title).fontWeight, color: getComputedStyle(title).color } : null,
    closeBtn: closeBtn ? { w: Math.round(closeBtn.getBoundingClientRect().width), h: Math.round(closeBtn.getBoundingClientRect().height) } : null,
    body: bcs ? { pad: bcs.padding, cls: (body.className||'').toString().slice(0, 40) } : null,
    summary: sumIn,
    facts,
    btns
  });
})()" 2>/dev/null | tail -1
echo "=== clone-v52 done ==="
