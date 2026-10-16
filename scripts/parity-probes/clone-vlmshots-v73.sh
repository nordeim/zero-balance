#!/usr/bin/env bash
# clone-vlmshots-v73.sh — the v73 NEW-pair program, CLONE side: the LAST
# never-shot mobile 390x844 twins — the LOGIN page + the CALCULATOR
# dialog. Runs inside with-server.sh (the :3200 parity server).
# To pair against the reference's OWN Rent calculator (which carries 1
# line item, "Contents Insurance" $25.00 monthly active — the v45
# measurement note, re-measured by the v66 pair), the clone adds the
# SAME line item through the real UI (a CLONE-side write — allowed under
# the v46 read-only rule, which protects only the reference), screenshots
# the 1-row state, then FULLY RESTORES the fixture (delete the line item
# + restore Rent's $1850 seed amount through the edit flow + verify the
# $2,235.00 page total) — the v66 discipline, verbatim.
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm73

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm73"

# (1) The LOGIN page at mobile 390 — the fresh logged-out session.
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 2
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div')].find(d => d.querySelector && d.querySelector('input[type=email]'));
  return JSON.stringify({
    hasLoginCard: !!card,
    docSW: document.documentElement.scrollWidth,
    vw: window.innerWidth,
    title: document.title
  });
})()" 2>/dev/null | tail -1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot /tmp/vlm73/clone-login-mobile.png 2>/dev/null | tail -1

# (2) The CALCULATOR dialog at mobile 390 — login, hover the Rent card,
# click Calculate (the v66 flow at the mobile viewport).
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
# the mobile fold: the Rent card sits BELOW the fold in the 1-col grid at
# 390 (card center y > 844) — scroll it into view FIRST, then the hover.
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$1850'));
  if (!card) return 'ERR';
  card.scrollIntoView({ block: 'center' });
  return 'scrolled';
})()" 2>/dev/null | tail -1
sleep 1
POS=$(agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$1850'));
  if (!card) return 'ERR';
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1)
echo "rent card center: $POS"
POS=${POS//\"/}
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
})()" 2>/dev/null | tail -1)
echo "calculate button center: $CALC"
CALC=${CALC//\"/}
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3

# add the SAME line item the reference's Rent carries (Contents
# Insurance \$25 monthly active) through the real UI — a clone-side
# write (allowed)
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
agent-browser screenshot /tmp/vlm73/clone-calculator-mobile.png 2>/dev/null | tail -1

# census for the DOM arbitration (the clone's Radix dialog + geometry)
agent-browser eval "(async () => {
  const dlg = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!dlg) return 'no dialog';
  const r = dlg.getBoundingClientRect();
  return JSON.stringify({
    txt: dlg.innerText.replace(/\n/g,'|').slice(0, 300),
    rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) }
  });
})()" 2>/dev/null | tail -1

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
# restore Rent to the seed's \$1850 through the real edit flow
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

echo "clone v73 shots done (login-mobile + calculator-mobile)"
EOF
