#!/usr/bin/env bash
# totalcard-clone-v93.sh — the ONE-SHOT census for the v93 pin's own
# axes, CLONE half (the v87/v88/v89/v90/v91/v92 supplemental precedent,
# BUILT TWO-HALF from the start — the census JS byte-identical to the
# reference half's, the md5 line-block contract): the CALCULATOR
# DIALOG's TOTAL-CARD inner-text census at desktop 1280 — the v73 390
# family's DESKTOP twin + the "Total Calculated" LABEL leaf's chrome
# (never pinned at ANY viewport). To pair against the reference's OWN
# 1-row calculator state, the clone adds the SAME "Contents Insurance"
# \$25 line item through the real UI (a CLONE-side write — allowed
# under the v46 read-only rule, which protects only the reference),
# censuses, then FULLY RESTORES the fixture (delete the line item +
# restore Rent's \$1850 seed amount through the edit flow + verify the
# \$2235.00 page total). Runs inside with-server.sh (the :3200 parity
# server). The QUOTED heredoc (the v73 lesson); no literal dollar
# sequences in the census JS (the v64 rule).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS="(async () => {
  const out = {};
  let panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!panel) panel = [...document.querySelectorAll('div')].find(d => getComputedStyle(d).maxWidth === '768px' && d.getBoundingClientRect().width > 300);
  if (!panel) return JSON.stringify({ panel: 'not found' });
  const totalCard = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).backgroundColor === 'rgb(255, 247, 245)');
  if (!totalCard) return JSON.stringify({ totalCard: 'not found' });
  const D = String.fromCharCode(36);
  const leaf = (scope, test) => [...scope.querySelectorAll('*')].find(e => e.children.length === 0 && test((e.textContent||'').trim()));
  const labelEl = leaf(totalCard, t => t === 'Total Calculated');
  const amountEl = leaf(totalCard, t => t === D + '25.00');
  const basedOnEl = leaf(totalCard, t => /^Based on 1 item$/.test(t));
  const willUpdateEl = leaf(totalCard, t => /Will update category total/.test(t));
  if (labelEl) { const s = getComputedStyle(labelEl); out.label = { fs: s.fontSize, fw: s.fontWeight, lh: s.lineHeight, color: s.color }; }
  if (amountEl) { const s = getComputedStyle(amountEl); out.amount = { fs: s.fontSize, fw: s.fontWeight, lh: s.lineHeight, color: s.color }; }
  if (basedOnEl) { const s = getComputedStyle(basedOnEl); out.basedOn = { fs: s.fontSize, lh: s.lineHeight, color: s.color }; }
  out.willUpdate = willUpdateEl ? (() => { const s = getComputedStyle(willUpdateEl); return { fs: s.fontSize, fw: s.fontWeight, color: s.color }; })() : 'absent';
  const topRow = labelEl ? labelEl.parentElement : null;
  if (topRow) { const s = getComputedStyle(topRow); out.topRow = { display: s.display, justify: s.justifyContent, align: s.alignItems, mb: s.marginBottom }; }
  const bottomRow = basedOnEl ? basedOnEl.parentElement : null;
  if (bottomRow) { const s = getComputedStyle(bottomRow); out.bottomRow = { display: s.display, justify: s.justifyContent, fs: s.fontSize, color: s.color }; }
  const tcs = getComputedStyle(totalCard); const tr = totalCard.getBoundingClientRect();
  out.totalCard = { w: Math.round(tr.width), h: Math.round(tr.height), pad: tcs.padding, radius: tcs.borderRadius, border: tcs.border };
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

echo "########## CLONE SIDE (the paired 1-row state — the added line item) ##########"
CENSUS_JS="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonetc93"
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
echo "rent card center: $POS"
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
echo "calculate button center: $CALC"
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
agent-browser mouse up >/dev/null 2>&1
sleep 3
# add the SAME line item the reference's Rent carries (Contents Insurance
# \$25 monthly active) through the real UI — a clone-side write (allowed)
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
# park the pointer FAR from the dialog before the census (the rest state)
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 2
echo "=== CLONE totalCard inner-text census (label + amount + basedOn + willUpdate + rows + card) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

# --- FULL cleanup: delete the line item, close, restore Rent's seed amount
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
EOF

echo ""
echo "=== seedcheck (env -u DATABASE_URL — the documented pollution discipline) ==="
cd "$(dirname "$0")/../.."
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs
echo "=== clone totalcard arbit v93 half done ==="
