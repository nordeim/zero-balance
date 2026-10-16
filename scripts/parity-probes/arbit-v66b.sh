#!/usr/bin/env bash
# arbit-v66b.sh — the v66 DOM arbitration census, CLONE side: the
# calculator dialog at desktop 1280x800 (the same axes as arbit-v66.sh —
# the VLM's two flags: the row's hover actions + the total card's span).
# Adds the matching "Contents Insurance" \$25 line item through the real UI
# (a clone-side write — allowed), parks the pointer, censuses, then FULLY
# RESTORES the fixture (delete + restore Rent's \$1850 + verify the
# \$2235.00 page total). The census JS avoids every dollar sequence (the
# String.fromCharCode(36) finder — the unquoted-heredoc rule satisfied by
# construction).
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonecalc66"
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
# verify the seed state before the flow (3 items — the clone's expenses seed)
agent-browser eval "(async () => {
  const t = (document.querySelector('main')||document.body).innerText;
  return JSON.stringify({ page: (t.match(/3 items · \\\$[\d,]+\.\d\d/)||['no match'])[0] });
})()" 2>/dev/null | tail -1
POS=$(agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$1850'));
  if (!card) return 'ERR';
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
X=$(echo "$POS" | cut -d, -f1); Y=$(echo "$POS" | cut -d, -f2)
agent-browser mouse move "$X" "$Y" >/dev/null 2>&1
sleep 1
CALC=$(agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$1850'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate\$/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
agent-browser mouse up >/dev/null 2>&1
sleep 3
# add the matching line item (clone-side write)
agent-browser eval "(async () => {
  const btns = [...document.querySelectorAll('button')].filter(b => b.textContent.trim() === 'Add Item' && b.getBoundingClientRect().width > 0);
  if (!btns.length) return 'no add item';
  btns[btns.length-1].click();
  return 'add clicked';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const dlgs = [...document.querySelectorAll('[role=dialog]')];
  const line = dlgs.find(d => (d.innerText||'').includes('Add Line Item'));
  if (!line) return 'no line dialog';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  const name = line.querySelector('#line-name');
  const amt = line.querySelector('#line-amount');
  if (!name || !amt) return 'no inputs';
  set(name, 'Contents Insurance');
  set(amt, '25');
  const save = [...line.querySelectorAll('button')].find(b => /save/i.test(b.textContent));
  if (save) save.click();
  return 'saved';
})()" 2>/dev/null | tail -1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 2

echo "=== THE CALCULATOR DIALOG CENSUS + THE HEIGHT FAMILY AT 1280 (clone, rest state) ==="
agent-browser eval "(async () => {
  const D = String.fromCharCode(36);
  const panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!panel) return 'no panel';
  const cs = getComputedStyle(panel);
  const r = panel.getBoundingClientRect();
  const totalCard = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).backgroundColor === 'rgb(255, 247, 245)');
  const tcs = totalCard ? getComputedStyle(totalCard) : null;
  const tr = totalCard ? totalCard.getBoundingClientRect() : null;
  const hasSpan = !!(totalCard && (totalCard.innerText||'').includes('Will update category total'));
  const h4 = [...panel.querySelectorAll('h4,h3,div,span')].filter(e => (e.textContent||'').trim() === 'Contents Insurance' && e.children.length === 0)[0];
  if (!h4) return 'no h4';
  const h4cs = getComputedStyle(h4);
  let row = h4;
  while (row && row !== panel) { const c = getComputedStyle(row); if (parseFloat(c.borderTopWidth) > 0 && c.backgroundColor === 'rgb(255, 255, 255)') break; row = row.parentElement; }
  if (!row || row === panel) return 'no row';
  const rowCs = getComputedStyle(row);
  const rowR = row.getBoundingClientRect();
  const pills = [...row.querySelectorAll('span')].filter(s => parseFloat(getComputedStyle(s).borderRadius) > 100 && s.getBoundingClientRect().width > 10);
  const pillRow = pills.length ? pills[0].parentElement : null;
  const prcs = pillRow ? getComputedStyle(pillRow) : null;
  const prR = pillRow ? pillRow.getBoundingClientRect() : null;
  const p1 = pills[0] ? getComputedStyle(pills[0]) : null;
  const p1R = pills[0] ? pills[0].getBoundingClientRect() : null;
  const amountP = [...row.querySelectorAll('p,span,div')].filter(e => e.children.length === 0 && (e.textContent||'').trim().startsWith(D)).sort((a,b) => parseFloat(getComputedStyle(b).fontSize) - parseFloat(getComputedStyle(a).fontSize))[0];
  const apcs = amountP ? getComputedStyle(amountP) : null;
  const apR = amountP ? amountP.getBoundingClientRect() : null;
  let actions = null;
  for (const d of row.querySelectorAll('div')) { const c = getComputedStyle(d); if (c.display === 'flex' && d.querySelectorAll('button').length >= 1 && (c.opacity === '0' || c.opacity === '1') && c.transitionProperty.includes('opacity')) { actions = d; break; } }
  return JSON.stringify({
    panel: { w: Math.round(r.width), radius: cs.borderRadius, maxW: cs.maxWidth, shadow: cs.boxShadow.slice(0,130) },
    totalCard: tcs ? { w: Math.round(tr.width), h: Math.round(tr.height), pad: tcs.padding, border: tcs.border, hasWillUpdateSpan: hasSpan } : null,
    row: { w: Math.round(rowR.width), h: Math.round(rowR.height), pad: rowCs.padding, radius: rowCs.borderRadius, borderTop: rowCs.borderTop, bg: rowCs.backgroundColor },
    nameH4: { fs: h4cs.fontSize, fw: h4cs.fontWeight, color: h4cs.color, h: Math.round(h4.getBoundingClientRect().height), mb: h4cs.marginBottom },
    pillRow: prcs ? { display: prcs.display, gap: prcs.gap, fs: prcs.fontSize, h: Math.round(prR.height) } : 'not found',
    pill1: p1 ? { h: Math.round(p1R.height), w: Math.round(p1R.width), pad: p1.padding, radius: p1.borderRadius, fs: p1.fontSize, fw: p1.fontWeight } : 'not found',
    amountP: apcs ? { fs: apcs.fontSize, fw: apcs.fontWeight, color: apcs.color, h: Math.round(apR.height) } : 'not found',
    actionsAtRest: actions ? { opacity: getComputedStyle(actions).opacity, btnCount: actions.querySelectorAll('button').length } : 'not found'
  });
})()" 2>/dev/null | tail -1

# --- FULL cleanup: delete the line item, close, restore Rent, verify
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!dlg) return 'no dialog';
  const del = [...dlg.querySelectorAll('button')].find(b => (b.getAttribute('aria-label')||'').includes('Delete Contents Insurance'));
  if (del) { del.click(); return 'delete clicked'; }
  return 'no delete btn';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const conf = [...document.querySelectorAll('button')].find(b => b.textContent.trim() === 'Delete' && b.getBoundingClientRect().width > 0);
  if (conf) { conf.click(); return 'confirmed'; }
  return 'no confirm';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!dlg) return 'no dialog';
  const close = [...dlg.querySelectorAll('button')].find(b => (b.getAttribute('aria-label')||'') === 'Close');
  if (close) { close.click(); return 'closed'; }
  return 'no close';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent'));
  if (!card) return 'no card';
  const edit = [...card.querySelectorAll('button')].find(b => b.textContent.trim() === 'Edit');
  if (edit) { edit.click(); return 'edit clicked'; }
  return 'no edit';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const dlgs = [...document.querySelectorAll('[role=dialog]')];
  const edit = dlgs.find(d => (d.innerText||'').includes('Edit Budget Item'));
  if (!edit) return 'no edit dialog';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  const amt = [...edit.querySelectorAll('input')].find(i => /amount/i.test((i.id||'') + (i.placeholder||'')));
  if (amt) set(amt, '1850');
  const save = [...edit.querySelectorAll('button')].find(b => /save/i.test(b.textContent));
  if (save) save.click();
  return 'restored 1850';
})()" 2>/dev/null | tail -1
sleep 3
agent-browser eval "(async () => {
  const t = (document.querySelector('main')||document.body).innerText;
  return JSON.stringify({ total: (t.match(/3 items · \\\$[\d,]+\.\d\d/)||['no match'])[0], rent: (t.match(/\\\$1,?850\.00/)||['no rent'])[0] });
})()" 2>/dev/null | tail -1
echo "=== clone arbit v66 done ==="
EOF
