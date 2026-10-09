#!/usr/bin/env bash
# v29: clone-side sweep — details-sheet keyboard semantics, mobile-nav R1-R4 (23rd),
# asset-label hover + breakdown-row hover computed values.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-sweep-v29.sh
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes

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
agent-browser set viewport 1280 800 >/dev/null 2>&1

echo "=== A. details sheet: initial focus + role ==="
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
  cards[0].click();
  await new Promise(r => setTimeout(r, 900));
  const dlg = document.querySelector('[role=dialog], [role=alertdialog]');
  const ae = document.activeElement;
  return JSON.stringify({
    role: dlg ? dlg.getAttribute('role') : null,
    ariaModal: dlg ? dlg.getAttribute('aria-modal') : null,
    initialFocus: (ae && ae !== document.body) ? { tag: ae.tagName, ariaLabel: ae.getAttribute('aria-label'), txt: (ae.textContent||'').trim().slice(0,15) } : 'BODY',
    xFocusable: dlg ? [...dlg.querySelectorAll('button')].length : 0
  });
})()" 2>/dev/null

echo "=== B. Tab walk stops 1-3 (trap check) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
for i in 1 2 3; do
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.4
  agent-browser eval "JSON.stringify({ stop: $i, tag: document.activeElement.tagName, txt: (document.activeElement.getAttribute('aria-label') || document.activeElement.textContent || '').trim().slice(0,20) })" 2>/dev/null
done

echo "=== C. Escape closes (superset) ==="
agent-browser press Escape >/dev/null 2>&1
sleep 0.8
agent-browser eval "JSON.stringify({ sheetGone: !document.querySelector('[role=dialog]') })" 2>/dev/null

echo "=== D. asset label hover (clone — expect static/oklab) ==="
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3
agent-browser eval "JSON.stringify((() => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
  const card = cards[0];
  const label = [...card.querySelectorAll('span,div')].filter(e => { const t = (e.textContent||'').trim(); return t && t.length < 25 && e.children.length === 0 && !/^\$/.test(t); })[0];
  const r = label.getBoundingClientRect();
  return { x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2), bgBefore: getComputedStyle(label).backgroundColor };
})())" 2>/dev/null
agent-browser eval "JSON.stringify((() => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
  const card = cards[0];
  const label = [...card.querySelectorAll('span,div')].filter(e => { const t = (e.textContent||'').trim(); return t && t.length < 25 && e.children.length === 0 && !/^\$/.test(t); })[0];
  const r = label.getBoundingClientRect();
  return JSON.stringify({ x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2) });
})()" >/dev/null 2>&1

echo "=== E. breakdown nested-row hover (clone) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "JSON.stringify((() => {
  const rows = [...document.querySelectorAll('button[aria-expanded]')].filter(r => r.offsetParent !== null && /Total Income|Total Expenses|Total Savings/i.test(r.textContent));
  return { found: rows.length, txt: rows[0] ? rows[0].textContent.trim().slice(0,30) : null };
})())" 2>/dev/null
