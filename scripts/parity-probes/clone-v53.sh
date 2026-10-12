#!/usr/bin/env bash
# clone-v53.sh — the clone-side driver for the v53 surfaces (against
# :3200 via with-server.sh): (1) the /networth view's TABLIST at 390 —
# the list + the active/inactive trigger pair + the 16px currentColor
# icons; (2) the CALCULATOR DIALOG at 390 — the panel + the header +
# the total card + the line-item rows + the Add button. The clone uses
# role=tab/tablist landmarks (the superset a11y fix) — the same census
# walks the roles. READ-ONLY: the Calculate OPEN click + the close
# click only — no saves, no deletes.
set -u
BASE="http://localhost:3200"

export AGENT_BROWSER_SESSION="clone53"
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
})()" >/dev/null 2>&1
sleep 3

echo ""
echo "=== CLONE surface 1: the /networth TABLIST at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const triggers = [...document.querySelectorAll('button[role=\"tab\"]')].filter(b => b.getBoundingClientRect().width > 0);
  if (!triggers.length) return 'no triggers';
  const list = triggers[0].closest('[role=\"tablist\"]') || triggers[0].parentElement;
  const grab = (t) => {
    const cs = getComputedStyle(t);
    const r = t.getBoundingClientRect();
    const icon = t.querySelector('svg');
    return {
      w: Math.round(r.width), h: Math.round(r.height),
      radius: cs.borderRadius, fs: cs.fontSize, fw: cs.fontWeight,
      color: cs.color, bg: cs.backgroundColor, shadow: (cs.boxShadow||'none').slice(0,90),
      pad: cs.padding, x: Math.round(r.x),
      icon: icon ? { w: Math.round(icon.getBoundingClientRect().width), h: Math.round(icon.getBoundingClientRect().height), color: getComputedStyle(icon).color, mr: getComputedStyle(icon).marginRight } : null
    };
  };
  const lcs = getComputedStyle(list);
  const lr = list.getBoundingClientRect();
  return JSON.stringify({
    list: { w: Math.round(lr.width), h: Math.round(lr.height), x: Math.round(lr.x), display: lcs.display, gridCols: lcs.gridTemplateColumns, gap: lcs.gap, bg: lcs.backgroundColor, radius: lcs.borderRadius, pad: lcs.padding, maxW: lcs.maxWidth },
    trigger0: grab(triggers[0]),
    trigger1: grab(triggers[1]),
    pageSW: document.documentElement.scrollWidth
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE surface 2: the CALCULATOR DIALOG at 390 ==="
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div')].filter(d => /rounded/.test(d.className||'') && d.querySelector('h4') && /Rent|Grocery|Utilit/i.test(d.textContent||'')).sort((a,b) => a.getBoundingClientRect().y - b.getBoundingClientRect().y)[0];
  if (!card) return 'no card';
  const btn = [...card.querySelectorAll('button')].find(b => /Calculate/i.test(b.textContent||'') || /calculator/i.test(b.getAttribute('aria-label')||''));
  if (!btn) return 'no calculate button';
  btn.click();
  return 'calculator clicked';
})()" 2>/dev/null | tail -1
sleep 3
agent-browser eval "(async () => {
  // The clone's calculator layer: role=dialog + the forest scrim.
  const panel = [...document.querySelectorAll('[role=\"dialog\"]')].find(d => (d.textContent||'').includes('Total Calculated'));
  if (!panel) return 'no calculator layer';
  const layer = panel.closest('div.fixed') || panel.parentElement;
  const cs = getComputedStyle(panel);
  const r = panel.getBoundingClientRect();
  const lcs = getComputedStyle(layer);
  const hdr = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).borderBottomWidth !== '0px');
  const h2 = panel.querySelector('h2');
  const desc = panel.querySelector('p');
  const closeBtn = [...panel.querySelectorAll('button')].filter(b => !b.textContent.trim())[0];
  const chip = panel.querySelector('div.rounded-xl, [class*=rounded-xl]');
  const total = [...panel.querySelectorAll('div')].find(d => (d.textContent||'').includes('Total Calculated') && getComputedStyle(d).backgroundColor !== 'rgba(0, 0, 0, 0)' && d !== panel);
  const tcs = total ? getComputedStyle(total) : null;
  const h4 = panel.querySelector('h4');
  let row = h4;
  while (row && row !== panel) {
    const rcs = getComputedStyle(row);
    if (parseFloat(rcs.borderTopWidth) > 0) break;
    row = row.parentElement;
  }
  const rcs2 = row && row !== panel ? getComputedStyle(row) : null;
  const addBtn = [...panel.querySelectorAll('button')].filter(b => /Add/i.test(b.textContent||'')).pop();
  return JSON.stringify({
    layer: { display: lcs.display, pad: lcs.padding, bg: lcs.backgroundColor },
    panel: { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), radius: cs.borderRadius, maxW: cs.maxWidth, maxH: cs.maxHeight, shadow: (cs.boxShadow||'none').slice(0,110), bg: cs.backgroundColor, overflow: cs.overflow, display: cs.display },
    header: hdr ? { h: Math.round(hdr.getBoundingClientRect().height), pad: getComputedStyle(hdr).padding, borderB: getComputedStyle(hdr).borderBottomWidth + ' ' + getComputedStyle(hdr).borderBottomColor } : null,
    h2: h2 ? { fs: getComputedStyle(h2).fontSize, fw: getComputedStyle(h2).fontWeight, color: getComputedStyle(h2).color, text: h2.textContent.trim().slice(0,20) } : null,
    desc: desc ? { fs: getComputedStyle(desc).fontSize, color: getComputedStyle(desc).color, text: desc.textContent.trim().slice(0,30) } : null,
    chip: chip ? { w: Math.round(chip.getBoundingClientRect().width), h: Math.round(chip.getBoundingClientRect().height), radius: getComputedStyle(chip).borderRadius, bg: (getComputedStyle(chip).backgroundImage || getComputedStyle(chip).backgroundColor).slice(0,80) } : null,
    close: closeBtn ? { w: Math.round(closeBtn.getBoundingClientRect().width), h: Math.round(closeBtn.getBoundingClientRect().height) } : null,
    totalCard: tcs ? { bg: tcs.backgroundColor, radius: tcs.borderRadius, pad: tcs.padding, w: Math.round(total.getBoundingClientRect().width), h: Math.round(total.getBoundingClientRect().height) } : null,
    row: rcs2 ? { w: Math.round(row.getBoundingClientRect().width), pad: rcs2.padding, bg: rcs2.backgroundColor, borderT: rcs2.borderTopWidth + ' ' + rcs2.borderTopColor } : null,
    addBtn: addBtn ? { w: Math.round(addBtn.getBoundingClientRect().width), h: Math.round(addBtn.getBoundingClientRect().height), fs: getComputedStyle(addBtn).fontSize, bg: (getComputedStyle(addBtn).backgroundImage || getComputedStyle(addBtn).backgroundColor).slice(0,80), text: addBtn.textContent.trim().slice(0,12) } : null,
    docSW: document.documentElement.scrollWidth
  });
})()" 2>/dev/null | tail -1
# Close the calculator (the close button).
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('[role=\"dialog\"]')].find(d => (d.textContent||'').includes('Total Calculated'));
  if (!panel) return 'no layer';
  const closeBtn = [...panel.querySelectorAll('button')].filter(b => !b.textContent.trim())[0];
  if (closeBtn) { closeBtn.click(); return 'closed'; }
  return 'no close';
})()" 2>/dev/null | tail -1
sleep 2
echo ""
echo "=== clone-v53 done ==="
