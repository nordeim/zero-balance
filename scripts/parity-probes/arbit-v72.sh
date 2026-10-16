#!/usr/bin/env bash
# arbit-v72.sh — the v72 NEW-pair program's flags, DOM-arbitrated per the
# v43 rule, at MOBILE 390x844 on BOTH sides:
#   PAIR 1/2 (the details sheets) flags:
#   (1) "the X close button has a visible square border in the clone" —
#       the close-button chrome census (border/outline/box-shadow/bg/
#       radius/size + the svg) on BOTH sides
#   (2) "the reference is cropped just below Status; the clone reveals
#       Created/Last Updated rows" — the sheet-surface geometry census
#       (y/h/bottom/maxH/overflow + the full DOM row inventory incl. the
#       meta footer) on BOTH sides
#   (3) the payment-method row (the clone's seeded Rent carries one) —
#       the v52 optional-field DATA-CONDITIONAL class
#   (4) the Base44 FAB — platform chrome (excluded by rule)
#   PAIR 3 (the drill-down EXPANDED mobile twin) flags:
#   (5) "2 vs 3 child rows in the expanded category" — the drill-down
#       row census (count/texts/chrome) on BOTH sides (the seed-data
#       class expected: the reference's 1 income item vs the clone's 2)
#   (6) the pie percentages / legend / summary values — DATA classes
# READ-ONLY on the reference (login + passive navigation + view-state
# clicks only); the clone's no-sub census rides the v71 F4 fixture
# discipline (create → census → delete → header restored).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

SHEET_CENSUS_JS="(async () => {
  const out = { view: location.pathname, docSW: document.documentElement.scrollWidth };
  // the sheet root: fixed z>=50 whose text starts with the sheet title
  const root = [...document.querySelectorAll('div')].find(d => {
    const s = getComputedStyle(d);
    return s.position === 'fixed' && parseInt(s.zIndex || '0') >= 50 && (d.textContent || '').trim().startsWith('Budget Item Details');
  });
  if (!root) return JSON.stringify({ err: 'no sheet open' });
  // the scrim: fixed full-viewport, non-transparent bg
  out.scrim = [...document.querySelectorAll('div')].filter(d => {
    const s = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return s.position === 'fixed' && r.width >= 380 && r.height >= 800 && s.backgroundColor && s.backgroundColor !== 'rgba(0, 0, 0, 0)' && (d.textContent || '').trim().startsWith('Budget Item Details');
  }).map(d => {
    const s = getComputedStyle(d);
    return { bg: s.backgroundColor, blur: s.backdropFilter, w: Math.round(d.getBoundingClientRect().width), h: Math.round(d.getBoundingClientRect().height) };
  });
  // the surface: the white rounded descendant (the sheet panel)
  let surface = null;
  for (const ch of root.querySelectorAll('div')) {
    const s = getComputedStyle(ch);
    const r = ch.getBoundingClientRect();
    if (s.backgroundColor === 'rgb(255, 255, 255)' && parseFloat(s.borderRadius) >= 10 && r.width >= 300 && r.width <= 400 && r.height >= 150) { surface = ch; break; }
  }
  if (!surface) surface = root;
  const scs = getComputedStyle(surface);
  const sr = surface.getBoundingClientRect();
  out.surface = {
    cls: (surface.className || '').toString().slice(0, 70),
    x: Math.round(sr.x), y: Math.round(sr.y), w: Math.round(sr.width), h: Math.round(sr.height), bottom: Math.round(sr.bottom),
    maxH: scs.maxHeight, overflow: scs.overflow, radius: scs.borderRadius,
    pos: scs.position, shadow: scs.boxShadow.slice(0, 60),
  };
  // the title leaf + the header row (the title's ancestor containing a button)
  const titleEl = [...surface.querySelectorAll('*')].find(e => e.children.length === 0 && (e.textContent || '').trim() === 'Budget Item Details');
  let header = titleEl ? titleEl.parentElement : null;
  while (header && header !== surface.parentElement && !header.querySelector('button')) header = header.parentElement;
  if (header) {
    const hcs = getComputedStyle(header);
    out.header = {
      h: Math.round(header.getBoundingClientRect().height), pos: hcs.position,
      display: hcs.display, pad: hcs.padding, borderB: hcs.borderBottomWidth + ' ' + hcs.borderBottomStyle + ' ' + hcs.borderBottomColor,
    };
    // the close button: the header's last button (top-right)
    const closeBtn = [...header.querySelectorAll('button')].pop();
    if (closeBtn) {
      const cbs = getComputedStyle(closeBtn);
      const br = closeBtn.getBoundingClientRect();
      const svg = closeBtn.querySelector('svg');
      out.closeBtn = {
        w: Math.round(br.width), h: Math.round(br.height), display: cbs.display,
        radius: cbs.borderRadius,
        border: cbs.borderTopWidth + ' ' + cbs.borderTopStyle + ' ' + cbs.borderTopColor,
        bg: cbs.backgroundColor, boxShadow: cbs.boxShadow.slice(0, 60),
        outline: cbs.outlineWidth + ' ' + cbs.outlineStyle,
        color: cbs.color,
        svgW: svg ? Math.round(svg.getBoundingClientRect().width) : null,
        svgStroke: svg ? getComputedStyle(svg).stroke : null,
        text: (closeBtn.textContent || '').trim().slice(0, 20),
      };
    }
  }
  // the summary text blocks (leaf elements fs >= 18: the name 24 / the
  // subtitle 18 / the amount 36)
  out.textBlocks = [...surface.querySelectorAll('p,h1,h2,h3,h4,span')].filter(e => {
    if (e.children.length > 0) return false;
    const fs = parseFloat(getComputedStyle(e).fontSize);
    return fs >= 18 && (e.textContent || '').trim().length > 0;
  }).map(e => {
    const s = getComputedStyle(e);
    return { tag: e.tagName, text: (e.textContent || '').trim().slice(0, 24), fs: s.fontSize, fw: s.fontWeight, color: s.color, lh: s.lineHeight, h: Math.round(e.getBoundingClientRect().height), mt: s.marginTop, mb: s.marginBottom };
  });
  // the summary pill badges (uppercase short text, rounded)
  out.pills = [...surface.querySelectorAll('span')].filter(sp => {
    const t = (sp.textContent || '').trim();
    const s = getComputedStyle(sp);
    const r = sp.getBoundingClientRect();
    return t.length > 2 && t.length < 20 && t === t.toUpperCase() && r.height >= 20 && r.height <= 34 && s.borderRadius !== '0px' && sp.children.length === 0;
  }).map(sp => {
    const s = getComputedStyle(sp);
    const r = sp.getBoundingClientRect();
    return { text: (sp.textContent || '').trim(), h: Math.round(r.height), w: Math.round(r.width), pad: s.padding, radius: s.borderRadius, fs: s.fontSize, fw: s.fontWeight, bg: s.backgroundColor, color: s.color, border: s.borderTopColor };
  });
  // the fact rows + the meta footer (the full DOM inventory)
  const labels = ['Date', 'Frequency', 'Recurring', 'Payment Method', 'Status', 'Created', 'Last Updated'];
  out.factRows = labels.map(lb => {
    const el = [...surface.querySelectorAll('p,span')].find(e => e.children.length === 0 && (e.textContent || '').trim() === lb);
    if (!el) return { label: lb, present: false };
    let row = el;
    while (row && row !== surface && row.children.length < 2) row = row.parentElement;
    const rs = row ? getComputedStyle(row) : null;
    return { label: lb, present: true, rowH: row ? Math.round(row.getBoundingClientRect().height) : null, labelFs: getComputedStyle(el).fontSize, labelColor: getComputedStyle(el).color, rowText: row ? (row.textContent || '').trim().slice(0, 44) : '' };
  });
  return JSON.stringify(out);
})()"

DRILL_CENSUS_JS="(async () => {
  const out = { view: location.pathname, docSW: document.documentElement.scrollWidth };
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent || '').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return JSON.stringify({ err: 'no breakdown card' });
  // the expanded category's child rows: the rows nested under the open
  // category (the container following the expanded row's content)
  const rows = [...card.querySelectorAll('button')].filter(b => b.offsetParent !== null);
  out.buttonCount = rows.length;
  out.buttons = rows.slice(0, 10).map(b => {
    const s = getComputedStyle(b);
    const r = b.getBoundingClientRect();
    return { text: (b.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40), h: Math.round(r.height), w: Math.round(r.width), fs: s.fontSize, fw: s.fontWeight, pad: s.padding, borderB: s.borderBottomWidth + ' ' + s.borderBottomColor, radius: s.borderRadius };
  });
  // the expanded child-row family: divs between the category button and
  // the next category (indent census)
  const catBtn = rows.find(b => /\\\$/.test(b.textContent || '') && !/Total|Net Balance/i.test(b.textContent || ''));
  if (catBtn) {
    let container = catBtn.parentElement;
    while (container && container !== card && container.querySelectorAll('button').length < 2) container = container.parentElement;
    const cr = container ? container.getBoundingClientRect() : null;
    out.expandedContainer = container ? { h: Math.round(cr.height), childCount: container.children.length, pl: getComputedStyle(container).paddingLeft, ml: getComputedStyle(container).marginLeft } : null;
  }
  out.footerText = (card.textContent || '').match(/\d+ categor(y|ies)/) ? (card.textContent || '').match(/\d+ categor(y|ies)/)[0] : 'no footer match';
  return JSON.stringify(out);
})()"

open_sheet_and_census () {
  local URL="$1" NAME="$2" TAG="$3"
  agent-browser open "$URL" >/dev/null 2>&1
  sleep 4
  agent-browser eval "(async () => {
    const h4 = [...document.querySelectorAll('h4')].find(h => (h.textContent||'').trim() === '$NAME');
    const card = h4 ? h4.closest('div.rounded-xl') : null;
    if (!card) return 'no card $NAME';
    card.click();
    return 'clicked $NAME';
  })()" 2>/dev/null | tail -1
  sleep 2
  echo "=== $TAG sheet ($NAME) at 390 ==="
  agent-browser eval "$SHEET_CENSUS_JS" 2>/dev/null | tail -1
}

echo "########## REFERENCE SIDE ##########"
export AGENT_BROWSER_SESSION="refarbit72"
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
  if echo "$RESULT" | grep -q "submitted"; then echo "login ok"; break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
open_sheet_and_census "$REF/expenses" "Rent" "REF with-sub"
open_sheet_and_census "$REF/expenses" "Miscellaneous" "REF no-sub"

# the drill-down EXPANDED census (view-state clicks only)
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  const sec = card ? [...card.querySelectorAll('button')].find(b => /Total Income/i.test(b.textContent||'')) : null;
  if (sec) { sec.click(); return 'section clicked'; }
  return 'no section';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  const cat = card ? [...card.querySelectorAll('button')].find(b => b.offsetParent !== null && /\\\$/.test(b.textContent||'') && !/Total|Net Balance/i.test(b.textContent||'')) : null;
  if (cat) { cat.click(); return 'category clicked'; }
  return 'no category';
})()" 2>/dev/null | tail -1
sleep 1
echo "=== REF drill-down expanded at 390 ==="
agent-browser eval "$DRILL_CENSUS_JS" 2>/dev/null | tail -1

echo ""
echo "########## CLONE SIDE ##########"
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbit72"
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

# the seeded Rent sheet (with-sub)
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
echo "=== CLONE with-sub sheet (Rent) at 390 ==="
agent-browser eval "$SHEET_CENSUS_JS" 2>/dev/null | tail -1

# the no-sub fixture sheet (the v71 F4 discipline: create → census → delete)
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
agent-browser eval "(async () => {
  const h4 = [...document.querySelectorAll('h4')].find(h => (h.textContent||'').trim() === 'Probe NoSub');
  const card = h4 ? h4.closest('div.rounded-xl') : null;
  if (!card) return 'no probe card';
  card.click();
  return 'probe clicked';
})()" 2>/dev/null | tail -1
sleep 2
echo "=== CLONE no-sub sheet (Probe NoSub) at 390 ==="
agent-browser eval "$SHEET_CENSUS_JS" 2>/dev/null | tail -1

# cleanup (the FIXED flow: the Edit dialog identified by the Category
# INPUT VALUE, not textContent)
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
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

# the drill-down EXPANDED census
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  const sec = card ? [...card.querySelectorAll('button')].find(b => /Total Income/i.test(b.textContent||'')) : null;
  if (sec) { sec.click(); return 'section clicked'; }
  return 'no section';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  const cat = card ? [...card.querySelectorAll('button')].find(b => b.offsetParent !== null && /\\\$/.test(b.textContent||'') && !/Total|Net Balance/i.test(b.textContent||'')) : null;
  if (cat) { cat.click(); return 'category clicked'; }
  return 'no category';
})()" 2>/dev/null | tail -1
sleep 1
echo "=== CLONE drill-down expanded at 390 ==="
agent-browser eval "$DRILL_CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== arbit-v72 done ==="
