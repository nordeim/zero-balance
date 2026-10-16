#!/usr/bin/env bash
# cleanup-fixture-v72.sh — deletes the stray "Probe NoSub" fixture from
# the dev DB. The v72 clone probe's cleanup miss: the Edit dialog carries
# the item name in the Category INPUT VALUE, not textContent — the dialog
# detection must not depend on the name appearing as text.
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneclean72"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
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
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(d => (d.textContent||'').includes('Probe NoSub'));
  if (!card) return 'no probe card (already clean)';
  const edit = [...card.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Edit');
  if (!edit) return 'no Edit button';
  edit.click();
  return 'Edit clicked';
})()" 2>/dev/null | tail -1
sleep 2
# verify the Edit dialog via the Category input VALUE (not textContent)
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('[role=dialog]')].find(d => d.getBoundingClientRect().height > 100);
  if (!dlg) return 'no dialog';
  const cat = dlg.querySelector('#item-category');
  return JSON.stringify({ dialogOpen: true, catVal: cat ? cat.value : null });
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('[role=dialog]')].find(d => d.getBoundingClientRect().height > 100);
  if (!dlg) return 'no dialog';
  const del = [...dlg.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Delete');
  if (!del) return 'no Delete button';
  del.click();
  return 'Delete clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('[role=dialog]')].find(d => (d.textContent||'').includes('Delete this item?'));
  if (!dlg) return 'no confirm';
  const del = [...dlg.querySelectorAll('button')].filter(b => (b.textContent||'').trim() === 'Delete');
  if (!del.length) return 'no confirm Delete';
  del[del.length-1].click();
  return 'confirmed';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const t = (document.querySelector('main')||document.body).textContent;
  const m = t.match(/(\d+)\s*items?\s*·\s*\\\$?([\d,]+\.?\d*)/);
  const gone = ![...document.querySelectorAll('h4')].some(h => (h.textContent||'').trim() === 'Probe NoSub');
  return JSON.stringify({ header: m ? m[0] : 'no match', probeGone: gone });
})()" 2>/dev/null | tail -1
EOF
