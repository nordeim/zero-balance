#!/usr/bin/env bash
# clone-vlmshots-v72.sh — the v72 NEW-pair program, CLONE side: the
# DETAILS-SHEET + DRILL-DOWN mobile 390x844 twins — (1) the Rent card's
# WITH-subtitle sheet, (2) the EMPTY-subcategory sheet (a user-created
# Add-Expense fixture — the clone's dev seed carries no empty-subcategory
# item, the v71 F4 discipline; the fixture is DELETED via the Edit dialog
# afterward and the header count verified restored), and (3) the
# dashboard's drill-down EXPANDED state at 390. Runs inside with-server.sh
# (the :3200 parity server).
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm72

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm72"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1

# (1) The Rent card's details sheet (WITH subtitle — "Apartment", the
# same subcategory value the reference's own Rent card carries).
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const h4 = [...document.querySelectorAll('h4')].find(h => (h.textContent||'').trim() === 'Rent');
  const card = h4 ? h4.closest('div.rounded-xl') : null;
  if (!card) return 'no Rent card';
  card.click();
  return 'Rent clicked';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('div')].find(d => {
    const s = getComputedStyle(d);
    return s.position === 'fixed' && parseInt(s.zIndex||'0') >= 50 && (d.textContent||'').trim().startsWith('Budget Item Details');
  });
  return JSON.stringify({ sheetOpen: !!dlg, head: dlg ? (dlg.textContent||'').trim().slice(0, 60) : '' });
})()" 2>/dev/null | tail -1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot /tmp/vlm72/clone-sheet-withsub.png 2>/dev/null | tail -1

# (2) The EMPTY-subcategory details sheet — a fresh navigation resets the
# prior sheet, then the Add-Expense fixture (Amount + Category only; the
# subcategory stays EMPTY; the defaults need/monthly/active match the
# reference's own Miscellaneous card's badge family, the v71 F4 design).
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const btn = [...document.querySelectorAll('button')].find(b => /Add Expense/i.test(b.textContent||''));
  if (!btn) return 'no Add button';
  btn.click();
  return 'Add clicked';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('[role=dialog]')].find(d => d.getBoundingClientRect().height > 100);
  if (!dlg) return 'no dialog';
  const amt = dlg.querySelector('#item-amount');
  const cat = dlg.querySelector('#item-category');
  if (!amt || !cat) return 'no fields';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(amt, '10.00');
  set(cat, 'Probe NoSub');
  const save = [...dlg.querySelectorAll('button')].find(b => /Save Item/i.test(b.textContent||''));
  if (!save) return 'no save';
  save.click();
  return 'saved';
})()" 2>/dev/null | tail -1
sleep 3
# open the probe card's details sheet
agent-browser eval "(async () => {
  const h4 = [...document.querySelectorAll('h4')].find(h => (h.textContent||'').trim() === 'Probe NoSub');
  const card = h4 ? h4.closest('div.rounded-xl') : null;
  if (!card) return 'no probe card';
  card.click();
  return 'probe clicked';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('div')].find(d => {
    const s = getComputedStyle(d);
    return s.position === 'fixed' && parseInt(s.zIndex||'0') >= 50 && (d.textContent||'').trim().startsWith('Budget Item Details');
  });
  return JSON.stringify({ sheetOpen: !!dlg, head: dlg ? (dlg.textContent||'').trim().slice(0, 60) : '' });
})()" 2>/dev/null | tail -1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot /tmp/vlm72/clone-sheet-nosub.png 2>/dev/null | tail -1

# --- cleanup: fresh nav closes the sheet; the fixture rides the Edit
# dialog's Delete path (the superset delete; expense cards carry no
# kebab); the header count must restore to the seed state.
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(d => (d.textContent||'').includes('Probe NoSub'));
  if (!card) return 'no probe card';
  const r = card.getBoundingClientRect();
  return JSON.stringify({ probeCard: true, y: Math.round(r.y), h: Math.round(r.height) });
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(d => (d.textContent||'').includes('Probe NoSub'));
  if (!card) return 'no probe card';
  const edit = [...card.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Edit');
  if (!edit) return 'no Edit button';
  edit.click();
  return 'Edit clicked';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('[role=dialog]')].find(d => d.getBoundingClientRect().height > 100);
  if (!dlg) return 'no edit dialog';
  const cat = dlg.querySelector('#item-category');
  if (!cat || cat.value !== 'Probe NoSub') return 'wrong dialog';
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

# (3) The dashboard's drill-down EXPANDED state at mobile 390 (the v67
# clone pattern re-run at the mobile twin).
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const sec = [...card.querySelectorAll('button')].find(b => /Total Income/i.test(b.textContent||''));
  if (!sec) return 'no section';
  sec.click();
  return 'section clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const cat = [...card.querySelectorAll('button')].find(b => b.offsetParent !== null && /\\\$/.test(b.textContent||'') && !/Total|Net Balance/i.test(b.textContent||''));
  if (!cat) return 'no category';
  cat.click();
  return 'category clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm72/clone-drilldown-mobile.png 2>/dev/null | tail -1

echo "clone v72 shots done (sheet-withsub + sheet-nosub + drilldown-mobile + fixture cleaned)"
EOF
