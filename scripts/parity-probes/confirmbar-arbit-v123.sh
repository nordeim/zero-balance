#!/usr/bin/env bash
# confirmbar-arbit-v123.sh — the ONE-SHOT clone census for the v123
# candidate pin family: the CALCULATOR line-item DELETE-CONFIRM BAR at
# 1280x800 on /expenses — the never-pinned FOURTH member of the
# confirm-bar family (the v121 pin holds the ITEM-CARD's bar; the
# net-worth twins are held BY CONSTRUCTION via the identical class
# strings; the CALCULATOR's bar — the mt-3 variant inside the row card —
# held by NO spec; the behavioral calculator tests assert the text +
# the click flow only, never the chrome).
# The CLONE-ONLY form (the v121 adapted precedent): the reference's
# calculator row delete destroys IMMEDIATELY (its R6 bug — no confirm
# bar exists on the reference), and a reference-side measurement would
# require a DESTRUCTIVE click (the v46 read-only rule) — so no
# both-sides census is possible; the pin locks the clone's own superset
# chrome. The family chrome = the v121 pinned contract BY CONSTRUCTION
# (the identical class strings: calculator-dialog.tsx:277-297 vs
# item-card.tsx:209-220 — flex/items-center/justify-between/rounded-lg/
# p-3 + rgb(254,242,242) + the Cancel/Delete pill pair); the
# calculator-specific axis: mt-3 (12px — the family's mt-4 is 16px).
# The census walks the full confirm ladder: the twin state seeded
# (Add "Contents Insurance" $25 through the REAL UI — the
# clone-vlmshots-v123.sh working forms) -> the row's at-rest height
# (the v66 contract: 102) -> the trash click opens the bar -> THE BAR
# CENSUS (box + label + Cancel/Delete pills + the shadow-sm VISIBLE
# layer) + the BAR-OPEN DELTA (the row card's height growth) -> the
# Cancel read (the bar closes, the row returns to rest) -> the fixture
# restore (the destructive Delete + restoreRent through the REAL edit
# flow + the $2235.00 page verification).
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonebar123"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3

echo "=== open the Rent calculator (real mouse: hover card, click Calculate) ==="
X=$(agent-browser eval "(async () => {
  const rent = [...document.querySelectorAll('div.rounded-xl')].find(d => (d.textContent||'').includes('Rent'));
  if (!rent) return '0,0';
  const r = rent.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
echo "rent card center: $X"
RX=$(echo "$X" | cut -d, -f1); RY=$(echo "$X" | cut -d, -f2)
agent-browser mouse move "$RX" "$RY" >/dev/null 2>&1
sleep 1
CX=$(agent-browser eval "(async () => {
  const rent = [...document.querySelectorAll('div.rounded-xl')].find(d => (d.textContent||'').includes('Rent'));
  const btn = rent ? [...rent.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Calculate') : null;
  if (!btn) return '0,0';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
echo "calculate button center: $CX"
CXX=$(echo "$CX" | cut -d, -f1); CYY=$(echo "$CX" | cut -d, -f2)
agent-browser mouse move "$CXX" "$CYY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== add Contents Insurance \$25 (the working eval-click forms) ==="
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
  if (!name || !amt) return 'no inputs ' + !!name + ' ' + !!amt;
  set(name, 'Contents Insurance');
  set(amt, '25');
  const save = [...line.querySelectorAll('button')].find(b => /save/i.test(b.textContent));
  if (save) save.click();
  return 'saved';
})()" 2>/dev/null | tail -1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== the at-rest row height (the v66 contract: 102) ==="
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.textContent||'').includes('Rent Calculator'));
  const h4 = panel ? [...panel.querySelectorAll('h4')].find(h => (h.textContent||'').trim() === 'Contents Insurance') : null;
  if (!h4) return 'no row';
  let row = h4;
  while (row) {
    const cs = getComputedStyle(row);
    if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === 'rgb(255, 255, 255)') break;
    row = row.parentElement;
  }
  return JSON.stringify({ rowH: Math.round(row.getBoundingClientRect().height) });
})()" 2>/dev/null | tail -1

echo "=== click the row trash — the bar opens (synthetic click: pointer stays parked) ==="
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!dlg) return 'no dialog';
  const del = [...dlg.querySelectorAll('button')].find(b => (b.getAttribute('aria-label')||'').includes('Delete Contents Insurance'));
  if (del) { del.click(); return 'trash clicked'; }
  return 'no trash';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== THE BAR CENSUS (box + label + pills + shadow-sm + the bar-open delta) ==="
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.textContent||'').includes('Rent Calculator'));
  if (!panel) return 'no panel';
  const bar = [...panel.querySelectorAll('div')].find(d => {
    const bcs = getComputedStyle(d);
    if (bcs.backgroundColor !== 'rgb(254, 242, 242)') return false;
    const btns = [...d.querySelectorAll('button')];
    return btns.length === 2 && (btns[0].textContent||'').trim() === 'Cancel' && (btns[1].textContent||'').trim() === 'Delete';
  });
  if (!bar) return 'no bar';
  const bcs = getComputedStyle(bar);
  const br = bar.getBoundingClientRect();
  const label = bar.querySelector('p');
  const lcs = label ? getComputedStyle(label) : null;
  const cancel = [...bar.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Cancel');
  const del = [...bar.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Delete');
  const ccs = cancel ? getComputedStyle(cancel) : null;
  const cbr = cancel ? cancel.getBoundingClientRect() : null;
  const dcs = del ? getComputedStyle(del) : null;
  const dbr = del ? del.getBoundingClientRect() : null;
  let row = bar;
  while (row) {
    const cs = getComputedStyle(row);
    if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === 'rgb(255, 255, 255)') break;
    row = row.parentElement;
  }
  const rowH = row ? Math.round(row.getBoundingClientRect().height) : null;
  return JSON.stringify({
    bar: { mt: bcs.marginTop, display: bcs.display, align: bcs.alignItems, justify: bcs.justifyContent, radius: bcs.borderRadius, pad: bcs.padding, w: Math.round(br.width), h: Math.round(br.height) },
    label: lcs ? { fs: lcs.fontSize, fw: lcs.fontWeight, txt: (label.textContent||'').trim() } : null,
    cancelPill: ccs ? { pad: ccs.padding, radius: ccs.borderRadius, fs: ccs.fontSize, fw: ccs.fontWeight, h: Math.round(cbr.height), shadow: ccs.boxShadow } : null,
    deletePill: dcs ? { pad: dcs.padding, radius: dcs.borderRadius, fs: dcs.fontSize, fw: dcs.fontWeight, h: Math.round(dbr.height) } : null,
    rowOpenH: rowH
  });
})()" 2>/dev/null | tail -1

echo "=== Cancel closes the bar (the row returns to rest) ==="
agent-browser eval "(async () => {
  const panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.textContent||'').includes('Rent Calculator'));
  const bar = panel ? [...panel.querySelectorAll('div')].find(d => {
    const bcs = getComputedStyle(d);
    if (bcs.backgroundColor !== 'rgb(254, 242, 242)') return false;
    const btns = [...d.querySelectorAll('button')];
    return btns.length === 2 && (btns[0].textContent||'').trim() === 'Cancel';
  }) : null;
  if (!bar) return 'no bar';
  const cancel = [...bar.querySelectorAll('button')].find(b => (b.textContent||'').trim() === 'Cancel');
  cancel.click();
  await new Promise(r => setTimeout(r, 400));
  const gone = ![...panel.querySelectorAll('div')].some(d => getComputedStyle(d).backgroundColor === 'rgb(254, 242, 242)');
  let row = [...panel.querySelectorAll('h4')].find(h => (h.textContent||'').trim() === 'Contents Insurance');
  while (row) {
    const cs = getComputedStyle(row);
    if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === 'rgb(255, 255, 255)') break;
    row = row.parentElement;
  }
  return JSON.stringify({ barGone: gone, rowRestH: row ? Math.round(row.getBoundingClientRect().height) : null });
})()" 2>/dev/null | tail -1

echo "=== fixture restore: destructive Delete (recalc to 0) + restoreRent 1850 ==="
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!dlg) return 'no dialog';
  const del = [...dlg.querySelectorAll('button')].find(b => (b.getAttribute('aria-label')||'').includes('Delete Contents Insurance'));
  if (del) { del.click(); return 'trash clicked'; }
  return 'no trash';
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
  return JSON.stringify({ total: (t.match(/3 items . \$[\d,]+\.\d\d/)||['no match'])[0], rent: (t.match(/\\\$1,?850\.00/)||['no rent'])[0] });
})()" 2>/dev/null | tail -1

echo "=== seedcheck (env -u DATABASE_URL — the documented pollution discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs
echo "=== confirmbar arbit v123 done ==="
EOF
