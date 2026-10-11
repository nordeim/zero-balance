#!/usr/bin/env bash
# v45: clone-side driver — the items-view CARD census at 1280 (/income +
# /expenses, + the REAL hover via agent-browser hover) and the CALCULATOR
# row census + REAL hover at 1280 (the queue's surfaces, mirrored against
# ref-v45.sh). The Rent calculator's line item is created via the API
# (the seed ships none) and DELETED after — the fixture-restore discipline
# (the calculator rule: the parent's amount becomes the line-items SUM —
# the restore PATCHes it back to 1850; deleting alone recalcs to 0).
# Runs INSIDE with-server.sh (the :3200 parity server).
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone45"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
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

echo "=== CLONE items-card census at 1280 — /income ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone45 "$PB/items-card-v45.mjs" 2>/dev/null | tail -1
echo "--- real hover (income card) ---"
agent-browser hover '[data-v45-card="first"]' >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const c = document.querySelector('[data-v45-card=\"first\"]');
  return JSON.stringify({ boxShadow: getComputedStyle(c).boxShadow, translateY: getComputedStyle(c).translate });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE items-card census at 1280 — /expenses ==="
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone45 "$PB/items-card-v45.mjs" 2>/dev/null | tail -1
echo "--- real hover (expense card: shadow + action reveal) ---"
agent-browser hover '[data-v45-card="first"]' >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const c = document.querySelector('[data-v45-card=\"first\"]');
  const ar = [...c.querySelectorAll('div')].find((d) => getComputedStyle(d).position === 'absolute' && d.children.length > 0 && d.querySelectorAll('button').length >= 1);
  return JSON.stringify({ boxShadow: getComputedStyle(c).boxShadow, actionOpacity: ar ? getComputedStyle(ar).opacity : null, translateY: getComputedStyle(c).translate });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE calculator row census + REAL hover (Rent) ==="
# Create a line item on the Rent item via the API (the browser carries the
# session cookie; the seed ships no line items). NOTE the calculator rule:
# the parent's amount becomes the line-items SUM — the restore PATCHes it
# back to 1850 after (deleting alone recalcs to 0).
agent-browser eval "(async () => {
  const items = await (await fetch('/api/budget-items')).json();
  const rent = items.data.find((i) => i.type === 'expense' && i.category === 'Rent');
  if (!rent) return 'NO RENT ITEM';
  const res = await fetch('/api/line-items', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ budgetItemId: rent.id, name: 'Contents Insurance', amount: 25, frequency: 'monthly', status: 'active', provider: 'UniTrust' }),
  });
  const j = await res.json();
  return JSON.stringify({ rentId: rent.id, created: j.ok });
})()" 2>/dev/null | tail -1

# Open the RENT calculator (the Calculate button INSIDE the Rent card — the
# clone's expense cards are name-keyed: h4 'Rent').
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div')].find((d) => {
    const h4 = d.querySelector('h4');
    return h4 && (h4.textContent || '').trim() === 'Rent' && String(d.className).match(/rounded/);
  });
  if (!card) return 'NO RENT CARD';
  const btn = [...card.querySelectorAll('button')].find((b) => /Calculate/i.test((b.textContent || '').trim()));
  if (!btn) return 'NO CALC BUTTON';
  btn.click();
  return 'clicked';
})()" 2>/dev/null | tail -1
sleep 2
# Tag the row + read the rest census (the clone's calculator is a Radix
# [role=dialog], not the reference's overlay-wrapping-panel).
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('[role=dialog]')].pop();
  if (!panel) return 'NO PANEL';
  const h4 = [...panel.querySelectorAll('h4')].find((h) => (h.textContent || '').trim() === 'Contents Insurance');
  if (!h4) return 'NO ROW H4';
  let row = h4;
  while (row && row !== panel) {
    const cs = getComputedStyle(row);
    if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === 'rgb(255, 255, 255)' && cs.padding === '16px') break;
    row = row.parentElement;
  }
  if (!row || row === panel) return 'NO ROW';
  row.setAttribute('data-v45-row', 'rent');
  const cs = getComputedStyle(row);
  const r = row.getBoundingClientRect();
  const actions = [...row.querySelectorAll('div')].find((d) => getComputedStyle(d).display === 'flex' && getComputedStyle(d).opacity === '0' && d.querySelectorAll('button').length >= 1);
  return JSON.stringify({
    panelW: Math.round(panel.getBoundingClientRect().width),
    rowClass: String(row.className),
    row: { w: Math.round(r.width), h: Math.round(r.height), pad: cs.padding, radius: cs.borderRadius, border: cs.borderTopWidth + ' ' + cs.borderTopStyle + ' ' + cs.borderTopColor, boxShadow: cs.boxShadow, bg: cs.backgroundColor, transition: cs.transitionProperty + ' ' + cs.transitionDuration },
    restActions: actions ? { opacity: getComputedStyle(actions).opacity, btnW: Math.round(actions.querySelector('button').getBoundingClientRect().width) } : null,
  });
})()" 2>/dev/null | tail -1
echo "--- real hover on the row ---"
agent-browser hover '[data-v45-row="rent"]' >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const row = document.querySelector('[data-v45-row=\"rent\"]');
  if (!row) return 'ROW LOST';
  const cs = getComputedStyle(row);
  const actions = [...row.querySelectorAll('div')].find((d) => getComputedStyle(d).display === 'flex' && d.querySelectorAll('button').length >= 1 && getComputedStyle(d).transitionProperty.includes('opacity'));
  return JSON.stringify({ boxShadow: cs.boxShadow, actionOpacity: actions ? getComputedStyle(actions).opacity : null });
})()" 2>/dev/null | tail -1

# Close the dialog (Escape — the superset dismissal).
agent-browser key Escape >/dev/null 2>&1
sleep 1

echo ""
echo "=== CLONE fixture restore (delete the line item + PATCH the parent back) ==="
agent-browser eval "(async () => {
  const items = await (await fetch('/api/budget-items')).json();
  const rent = items.data.find((i) => i.type === 'expense' && i.category === 'Rent');
  const lis = await (await fetch('/api/line-items?budgetItemId=' + rent.id)).json();
  const li = lis.data.find((l) => l.name === 'Contents Insurance');
  let deleted = false;
  if (li) deleted = (await (await fetch('/api/line-items/' + li.id, { method: 'DELETE' })).json()).ok;
  const patched = (await (await fetch('/api/budget-items/' + rent.id, { method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ amount: 1850 }) })).json()).ok;
  const after = await (await fetch('/api/budget-items')).json();
  const rentAfter = after.data.find((i) => i.type === 'expense' && i.category === 'Rent');
  const expenses = after.data.filter((i) => i.type === 'expense').reduce((s, i) => s + i.amount, 0);
  return JSON.stringify({ deleted, patched, rentAmountRestored: rentAfter.amount, expenseTotal: expenses });
})()" 2>/dev/null | tail -1
