#!/usr/bin/env bash
# clone-v53b.sh — the follow-up clone-side driver: the calculator at 390
# WITH a line item (the reference's own data carries 1 row — its state is
# unmeasurable-empty-side, read-only rule; the clone can add + census +
# delete on its OWN db). Censuses: the line-item ROW family + the
# NON-EMPTY "Add Item" button. Cleanup: delete the row after.
set -u
BASE="http://localhost:3200"

export AGENT_BROWSER_SESSION="clone53c"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 5
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in? ' + location.href;
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 5

agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 5

echo "=== CLONE: open the Rent calculator at 390 ==="
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div')].filter(d => /rounded/.test(d.className||'') && d.querySelector('h4') && /Rent/i.test(d.textContent||'')).sort((a,b) => a.getBoundingClientRect().y - b.getBoundingClientRect().y)[0];
  if (!card) return 'no card';
  const btn = [...card.querySelectorAll('button')].find(b => /Calculate/i.test(b.textContent||''));
  if (!btn) return 'no calculate button';
  btn.click();
  return 'calculator clicked';
})()" 2>/dev/null | tail -1
sleep 3

echo "=== CLONE: add ONE line item (the v45 F2b flow) ==="
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('[role=\"dialog\"]')].find(d => (d.textContent||'').includes('Total Calculated'));
  if (!panel) return 'no calculator';
  const addBtn = [...panel.querySelectorAll('button')].find(b => /Add Item|Add First Item/i.test(b.textContent||''));
  if (addBtn) { addBtn.click(); return 'add clicked'; }
  return 'no add button';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const lineDialog = [...document.querySelectorAll('[role=\"dialog\"]')].find(d => /Add Line Item/i.test(d.textContent||''));
  if (!lineDialog) return 'no line dialog';
  const name = lineDialog.querySelector('input');
  const amount = [...lineDialog.querySelectorAll('input')].filter(i => i !== name)[0];
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  if (name) set(name, 'Contents Insurance');
  if (amount) set(amount, '25');
  const save = [...lineDialog.querySelectorAll('button')].find(b => /Save Item/i.test(b.textContent||''));
  if (save) { save.click(); return 'saved'; }
  return 'no save';
})()" 2>/dev/null | tail -1
sleep 3

echo "=== CLONE: the calculator census at 390 (WITH 1 row) ==="
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('[role=\"dialog\"]')].find(d => (d.textContent||'').includes('Total Calculated'));
  if (!panel) return 'no calculator';
  const h4 = [...panel.querySelectorAll('h4')].find(h => /Contents Insurance/i.test(h.textContent||''));
  if (!h4) return 'no row h4';
  let row = h4;
  while (row && row !== panel) {
    const rcs = getComputedStyle(row);
    if (parseFloat(rcs.borderTopWidth) > 0 && getComputedStyle(row).backgroundColor === 'rgb(255, 255, 255)') break;
    row = row.parentElement;
  }
  const rcs = row ? getComputedStyle(row) : null;
  const rr = row ? row.getBoundingClientRect() : null;
  const addBtn = [...panel.querySelectorAll('button')].find(b => /^Add Item$/i.test(b.textContent||''));
  const acs = addBtn ? getComputedStyle(addBtn) : null;
  const total = [...panel.querySelectorAll('div')].find(d => (d.textContent||'').includes('Total Calculated') && getComputedStyle(d).backgroundColor !== 'rgba(0, 0, 0, 0)' && d !== panel);
  const pr = panel.getBoundingClientRect();
  const h3 = [...panel.querySelectorAll('h3')].find(h => /Line Items/i.test(h.textContent||''));
  return JSON.stringify({
    panel: { w: Math.round(pr.width), h: Math.round(pr.height) },
    row: rr ? { w: Math.round(rr.width), h: Math.round(rr.height), pad: rcs.padding, bg: rcs.backgroundColor, borderT: rcs.borderTopWidth + ' ' + rcs.borderTopColor, radius: rcs.borderRadius } : null,
    addBtn: acs ? { w: Math.round(addBtn.getBoundingClientRect().width), h: Math.round(addBtn.getBoundingClientRect().height), fs: acs.fontSize, fw: acs.fontWeight, bg: (acs.backgroundImage || acs.backgroundColor).slice(0,80), color: acs.color, text: addBtn.textContent.trim() } : null,
    lineItemsH3: h3 ? { fs: acs2(h3).fontSize, fw: acs2(h3).fontWeight, color: acs2(h3).color } : null,
    docSW: document.documentElement.scrollWidth
  });
  function acs2(el) { return getComputedStyle(el); }
})()" 2>/dev/null | tail -1

echo "=== CLONE: cleanup — delete the row ==="
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('[role=\"dialog\"]')].find(d => (d.textContent||'').includes('Total Calculated'));
  if (!panel) return 'no calculator';
  const del = [...panel.querySelectorAll('button')].find(b => /Delete Contents Insurance/i.test(b.getAttribute('aria-label')||'') || /Delete/i.test(b.textContent||''));
  if (del) { del.click(); return 'delete clicked'; }
  return 'no delete';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const confirm = [...document.querySelectorAll('[role=\"dialog\"], [role=\"alertdialog\"]')].find(d => /Delete/i.test(d.textContent||'') && d.querySelector('button'));
  if (!confirm) return 'no confirm';
  const yes = [...confirm.querySelectorAll('button')].find(b => /^Delete$/i.test(b.textContent||''));
  if (yes) { yes.click(); return 'confirmed'; }
  return 'no yes';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('[role=\"dialog\"]')].find(d => (d.textContent||'').includes('Total Calculated'));
  if (panel) {
    const close = [...panel.querySelectorAll('button')].filter(b => !b.textContent.trim())[0];
    if (close) { close.click(); return 'closed'; }
  }
  return 'done';
})()" 2>/dev/null | tail -1
sleep 1
echo "=== clone-v53b done ==="
