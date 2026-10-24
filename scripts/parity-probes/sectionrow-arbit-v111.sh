#!/usr/bin/env bash
# sectionrow-arbit-v111.sh — the ONE-SHOT both-sides census for the v111
# pin's own axes: the calculator dialog's LINE-ITEMS SECTION HEADER ROW
# family at 1280 (the family the v105-era pair's censuses walked past on
# every dialog shot: the CALC_CENSUS_JS blocks hold the panel + scrim +
# the DIALOG header (title/desc/close) + totalCard + the row + pills +
# addBtn — NEVER the section row between the totalCard and the items).
# The never-pinned family (the coverage map across all 24 specs): the v45
# F2a pin holds the line-item ROW census; the v59 pin the panel; the v66
# pin the height family {row/nameH4/pillRow/pill1/amountP/totalCard}; the
# v73 pin the scrim + summary at 390; the v81 pin the dialog header
# (title/desc/close) + addBtn + scrim at 1280; the v87 pin the
# close-button; the v93 pin the totalCard inner text; the v5 dialog-button
# pin the addBtn's gradient family — NEVER pinned at ANY viewport in ANY
# spec: the SECTION ROW's flex chrome {display/align/justify/mb/h/childCount},
# the 'Line Items' h3's computed chrome {fs/fw/color/lh/h/margin}, and the
# row's junction geometry. The addBtn is walked as CONTEXT ONLY (the v81
# pin already holds its {w/h/radius/fs/fw/color}).
# READ-ONLY: login + hover + dialog-open only — no form saves, no data
# mutations (the v46 incident rule). The parked pointer at (5,5) after the
# click. Double-quoted-heredoc-safe: no raw dollar sequences in the census
# JS; no backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

SECTION_CENSUS="(async () => {
  const out = {};
  // the panel: the clone's Radix dialog first, the reference's plain
  // fixed div (maxWidth 768px) as the fallback — the v45 finder form.
  let panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!panel) panel = [...document.querySelectorAll('div')].find(d => getComputedStyle(d).maxWidth === '768px' && d.getBoundingClientRect().width > 300);
  if (!panel) return JSON.stringify({ found: false, why: 'no panel' });
  // the section h3: exact-text 'Line Items', childless (the title-finder
  // form — never by tag alone; the reference's markup may differ)
  const h3 = [...panel.querySelectorAll('h1,h2,h3,h4,div,span,p')].filter(e => (e.textContent||'').trim() === 'Line Items' && e.children.length === 0)[0];
  if (!h3) return JSON.stringify({ found: false, why: 'no section h3' });
  // the section row: the h3's nearest flex ancestor that contains the
  // Add Item button (the rendered chrome is the axis, never the DOM
  // shape — the v72 structural class)
  let row = h3.parentElement;
  for (let i = 0; i < 6 && row; i++) {
    const s = getComputedStyle(row);
    const hasAdd = [...row.querySelectorAll('button')].some(b => /Add Item/i.test(b.textContent || ''));
    if (s.display === 'flex' && hasAdd) break;
    row = row.parentElement;
  }
  if (!row) return JSON.stringify({ found: false, why: 'no section row' });
  const rcs = getComputedStyle(row);
  const rr = row.getBoundingClientRect();
  out.row = {
    display: rcs.display, align: rcs.alignItems, justify: rcs.justifyContent,
    mb: rcs.marginBottom, mt: rcs.marginTop,
    h: Math.round(rr.height), w: Math.round(rr.width),
    childCount: row.children.length,
  };
  const hcs = getComputedStyle(h3);
  const hr = h3.getBoundingClientRect();
  out.sectionH3 = {
    text: (h3.textContent || '').trim().slice(0, 16),
    tag: h3.tagName,
    fs: hcs.fontSize, fw: hcs.fontWeight, color: hcs.color,
    lh: hcs.lineHeight, h: Math.round(hr.height),
    margin: hcs.margin,
  };
  // the addBtn as CONTEXT ONLY (the v81 pin holds its full chrome)
  const addBtn = [...row.querySelectorAll('button')].find(b => /Add Item/i.test(b.textContent || ''));
  if (addBtn) {
    const ar = addBtn.getBoundingClientRect();
    out.addBtnCtx = { w: Math.round(ar.width), h: Math.round(ar.height), text: (addBtn.textContent||'').trim().slice(0, 12) };
  }
  // the junction: the h3's y-center vs the row's y-center (the
  // items-center alignment, read live)
  out.junction = {
    h3CenterY: Math.round(hr.y + hr.height / 2),
    rowCenterY: Math.round(rr.y + rr.height / 2),
  };
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280, calculator dialog) ==="
export AGENT_BROWSER_SESSION="secref111"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
POS=""
for attempt in 1 2 3 4 5; do
  POS=$(agent-browser eval "(async () => {
    const main = document.querySelector('main')||document.body;
    const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
    if (!card) return 'ERR';
    const r = card.getBoundingClientRect();
    return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
  })()" 2>/dev/null | tail -1 | tr -d '"')
  if [ "$POS" != "ERR" ] && [ -n "$POS" ]; then break; fi
  echo "rent card not ready (attempt $attempt), waiting..."
  sleep 4
done
echo "rent card center: $POS"
X=$(echo "$POS" | cut -d, -f1); Y=$(echo "$POS" | cut -d, -f2)
agent-browser mouse move "$X" "$Y" >/dev/null 2>&1
sleep 1
CALC=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate\$/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
echo "calculate button center: $CALC"
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
# the vlm-shots click form: move to the button center FIRST (the hover
# state holds), then mouse down/up — the bare click command can drop the
# hover-revealed button before the press lands
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- REF section-row census ---"
agent-browser eval "$SECTION_CENSUS" 2>/dev/null | tail -1

echo ""
echo "=== CLONE side (1280, calculator dialog, :3200) ==="
SECTION_CENSUS_JS="$SECTION_CENSUS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="secclone111"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
CLONE_LOGIN="(async () => {
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
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$CLONE_LOGIN" 2>/dev/null | tail -1)
  echo "clone login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
  sleep 3
done
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
CPOS=""
for attempt in 1 2 3 4 5; do
  CPOS=$(agent-browser eval "(async () => {
    const main = document.querySelector('main')||document.body;
    const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('1850'));
    if (!card) return 'ERR';
    const r = card.getBoundingClientRect();
    return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
  })()" 2>/dev/null | tail -1 | tr -d '"')
  if [ "$CPOS" != "ERR" ] && [ -n "$CPOS" ]; then break; fi
  echo "clone rent card not ready (attempt $attempt), waiting..."
  sleep 4
done
echo "clone rent card center: $CPOS"
CXX=$(echo "$CPOS" | cut -d, -f1); CYY=$(echo "$CPOS" | cut -d, -f2)
agent-browser mouse move "$CXX" "$CYY" >/dev/null 2>&1
sleep 1
CCALC=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('1850'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate\$/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
echo "clone calculate button center: $CCALC"
CCX=$(echo "$CCALC" | cut -d, -f1); CCY=$(echo "$CCALC" | cut -d, -f2)
agent-browser mouse move "$CCX" "$CCY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- CLONE section-row census ---"
agent-browser eval "$SECTION_CENSUS_JS" 2>/dev/null | tail -1
echo "=== sectionrow arbit v111 done ==="
EOF
echo "=== seedcheck (env -u DATABASE_URL — the documented pollution discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs
