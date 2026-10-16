#!/usr/bin/env bash
# arbit-v73.sh — the v73 NEW-pair program's flags, DOM-arbitrated per the
# v43 rule, at MOBILE 390x844 on BOTH sides. The calculator mobile twin's
# flags:
#   (1) "the clone's scrim appears lighter/more transparent than the
#       reference's" — the SCRIM census (bg color, opacity,
#       backdropFilter, geometry) on BOTH sides. NOTE the v72 structural
#       lesson: the reference's scrim WRAPS the panel (one fixed overlay
#       carrying the text) while the clone's Radix scrim is a SIBLING of
#       the panel — the census must therefore collect EVERY fixed z>=50
#       full-viewport candidate and report each one's chrome.
#   (2) the "Will update category total" span (shown on the clone, absent
#       on the reference) — the v66 DATA-CONDITIONAL class re-verified:
#       the span renders while total !== item.amount; the reference's own
#       Rent is natively 25.00 and its single line item sums to 25.00 ->
#       HIDDEN; the clone's modal snapshot carries the opened-at parent
#       1850 against the recalculated 25.00 -> SHOWN. The census measures
#       the span's presence + chrome where present.
#   Plus the full PANEL + header + summary-block + row census (the
#   never-measured calculator geometry at 390: the panel x/y/w/h/radius/
#   shadow, the 40x40 gradient chip, the 36x36 X close, the #fff7f5
#   summary block, the row inventory) — the pin candidate's expected
#   values.
# READ-ONLY on the reference (login + passive navigation + hover +
# dialog-open only); the clone's census rides the v66/v73 fixture
# discipline (add the Contents Insurance line item -> census -> delete ->
# restore Rent's 1850 -> verify the page total).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CALC_CENSUS_JS="(async () => {
  const out = { view: location.pathname, docSW: document.documentElement.scrollWidth, vw: window.innerWidth };

  // every fixed z>=50 full-viewport candidate (the scrim family — the
  // reference's wrapper-scrim AND the clone's sibling overlay both match)
  out.scrims = [...document.querySelectorAll('div')].filter(d => {
    const s = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return s.position === 'fixed' && parseInt(s.zIndex || '0') >= 50 &&
      r.width >= 380 && r.height >= 800 &&
      s.backgroundColor && s.backgroundColor !== 'rgba(0, 0, 0, 0)';
  }).map(d => {
    const s = getComputedStyle(d);
    return {
      bg: s.backgroundColor, opacity: s.opacity,
      blur: s.backdropFilter || s.webkitBackdropFilter || '',
      hasText: (d.textContent || '').trim().length > 10,
      w: Math.round(d.getBoundingClientRect().width),
      h: Math.round(d.getBoundingClientRect().height)
    };
  });

  // the dialog root: fixed z>=50 whose text includes the calculator title
  const root = [...document.querySelectorAll('div')].find(d => {
    const s = getComputedStyle(d);
    return s.position === 'fixed' && parseInt(s.zIndex || '0') >= 50 &&
      (d.textContent || '').includes('Rent Calculator') &&
      d.getBoundingClientRect().width > 300 && d.getBoundingClientRect().height > 150;
  });
  if (!root) return JSON.stringify({ err: 'no calculator dialog open' });
  const rootS = getComputedStyle(root);

  // the panel: the root itself if it is the white rounded surface (the
  // clone's Radix panel), else the white rounded descendant (the
  // reference's inner panel inside its wrapper-scrim)
  let panel = null;
  if (rootS.backgroundColor === 'rgb(255, 255, 255)' && parseFloat(rootS.borderRadius) >= 8) {
    panel = root;
  } else {
    for (const ch of root.querySelectorAll('div')) {
      const s = getComputedStyle(ch);
      const r = ch.getBoundingClientRect();
      if (s.backgroundColor === 'rgb(255, 255, 255)' && parseFloat(s.borderRadius) >= 8 &&
        r.width >= 300 && r.height >= 200) { panel = ch; break; }
    }
  }
  if (!panel) panel = root;
  const ps = getComputedStyle(panel);
  const pr = panel.getBoundingClientRect();
  out.panel = {
    x: Math.round(pr.x), y: Math.round(pr.y), w: Math.round(pr.width), h: Math.round(pr.height),
    maxW: ps.maxWidth, maxH: ps.maxHeight, radius: ps.borderRadius,
    bg: ps.backgroundColor, border: ps.borderTopWidth + ' ' + ps.borderTopStyle + ' ' + ps.borderTopColor,
    shadow: ps.boxShadow.slice(0, 80), overflow: ps.overflow, pos: ps.position
  };

  // the header row: the panel's first border-b child (the chip + title
  // + X close live inside)
  let header = null;
  for (const ch of panel.querySelectorAll('div')) {
    const s = getComputedStyle(ch);
    if (s.borderBottomWidth !== '0px' && ch.querySelector('button')) { header = ch; break; }
  }
  if (header) {
    const hs = getComputedStyle(header);
    out.header = {
      h: Math.round(header.getBoundingClientRect().height),
      pad: hs.padding, display: hs.display,
      borderB: hs.borderBottomWidth + ' ' + hs.borderBottomStyle + ' ' + hs.borderBottomColor
    };
    // the gradient chip: the header's first sized rounded square
    const chip = [...header.querySelectorAll('div')].find(d => {
      const r = d.getBoundingClientRect();
      return r.width >= 36 && r.width <= 44 && Math.abs(r.width - r.height) <= 1;
    });
    if (chip) {
      const cs = getComputedStyle(chip);
      out.chip = { w: Math.round(chip.getBoundingClientRect().width), h: Math.round(chip.getBoundingClientRect().height), radius: cs.borderRadius, bg: cs.backgroundImage.slice(0, 90) || cs.backgroundColor };
    }
    // the X close: the header's last button
    const closeBtn = [...header.querySelectorAll('button')].pop();
    if (closeBtn) {
      const cbs = getComputedStyle(closeBtn);
      const cbr = closeBtn.getBoundingClientRect();
      out.closeBtn = {
        w: Math.round(cbr.width), h: Math.round(cbr.height), radius: cbs.borderRadius,
        border: cbs.borderTopWidth + ' ' + cbs.borderTopStyle, bg: cbs.backgroundColor,
        boxShadow: cbs.boxShadow.slice(0, 50), outline: cbs.outlineWidth + ' ' + cbs.outlineStyle,
        color: cbs.color
      };
    }
  }

  // the title + description leaves
  const title = [...panel.querySelectorAll('*')].find(e => e.children.length === 0 && (e.textContent || '').trim() === 'Rent Calculator');
  if (title) {
    const ts = getComputedStyle(title);
    out.title = { fs: ts.fontSize, fw: ts.fontWeight, lh: ts.lineHeight, color: ts.color, mb: ts.marginBottom };
  }
  const desc = [...panel.querySelectorAll('*')].find(e => e.children.length === 0 && /Break down your rent/i.test(e.textContent || ''));
  if (desc) {
    const ds = getComputedStyle(desc);
    out.desc = { fs: ds.fontSize, color: ds.color, lh: ds.lineHeight };
  }

  // the Total Calculated summary block: the tinted rounded block
  let summary = null;
  for (const ch of panel.querySelectorAll('div')) {
    const s = getComputedStyle(ch);
    if (s.backgroundColor === 'rgb(255, 247, 245)') { summary = ch; break; }
  }
  if (summary) {
    const ss = getComputedStyle(summary);
    const sr = summary.getBoundingClientRect();
    out.summary = {
      bg: ss.backgroundColor, border: ss.borderTopWidth + ' ' + ss.borderTopColor,
      radius: ss.borderRadius, pad: ss.padding,
      w: Math.round(sr.width), h: Math.round(sr.height), mb: ss.marginBottom
    };
    const amt = [...summary.querySelectorAll('*')].find(e => e.children.length === 0 && /25\.00/.test(e.textContent || ''));
    if (amt) {
      const as = getComputedStyle(amt);
      out.summaryAmount = { fs: as.fontSize, fw: as.fontWeight, color: as.color, lh: as.lineHeight };
    }
  }

  // the will-update span (the DATA-CONDITIONAL class)
  const willUpdate = [...panel.querySelectorAll('*')].find(e => e.children.length === 0 && /Will update category total/i.test(e.textContent || ''));
  out.willUpdateSpan = willUpdate ? (() => { const ws = getComputedStyle(willUpdate); return { present: true, fs: ws.fontSize, color: ws.color, fw: ws.fontWeight }; })() : { present: false };

  // the line-item row inventory
  const rowName = [...panel.querySelectorAll('*')].find(e => e.children.length === 0 && /Contents Insurance/.test(e.textContent || ''));
  if (rowName) {
    let row = rowName.parentElement;
    while (row && row !== panel && (getComputedStyle(row).borderRadius === '0px' || !row.querySelector('button'))) row = row.parentElement;
    if (row && row !== panel) {
      const rs = getComputedStyle(row);
      const rr = row.getBoundingClientRect();
      out.row = {
        h: Math.round(rr.height), w: Math.round(rr.width), pad: rs.padding,
        radius: rs.borderRadius, bg: rs.backgroundColor,
        border: rs.borderTopWidth + ' ' + rs.borderTopColor,
        btns: [...row.querySelectorAll('button')].map(b => {
          const bs = getComputedStyle(b);
          return { w: Math.round(b.getBoundingClientRect().width), opacity: bs.opacity, aria: b.getAttribute('aria-label') || b.textContent.trim().slice(0, 24) };
        })
      };
    }
  }

  // the Add Item button
  const addBtn = [...panel.querySelectorAll('button')].find(b => /Add Item/i.test(b.textContent || ''));
  if (addBtn) {
    const abs = getComputedStyle(addBtn);
    out.addBtn = { w: Math.round(addBtn.getBoundingClientRect().width), h: Math.round(addBtn.getBoundingClientRect().height), fs: abs.fontSize, fw: abs.fontWeight, radius: abs.borderRadius, color: abs.color };
  }

  // the based-on line
  const basedOn = [...panel.querySelectorAll('*')].find(e => e.children.length === 0 && /Based on 1 item/i.test(e.textContent || ''));
  if (basedOn) {
    const bs = getComputedStyle(basedOn);
    out.basedOn = { fs: bs.fontSize, color: bs.color };
  }

  return JSON.stringify(out);
})()"

echo "########## REFERENCE SIDE ##########"
export AGENT_BROWSER_SESSION="refarbit73"
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
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
# the mobile fold: scroll the Rent card into view, then the real-mouse
# hover + Calculate click (the v73 probe's fixed flow)
agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
  if (!card) return 'ERR';
  card.scrollIntoView({ block: 'center' });
  return 'scrolled';
})()" 2>/dev/null | tail -1
sleep 1
POS=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\$25'));
  if (!card) return 'ERR';
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1)
POS=${POS//\"/}
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
})()" 2>/dev/null | tail -1)
CALC=${CALC//\"/}
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF calculator dialog at 390 ==="
agent-browser eval "$CALC_CENSUS_JS" 2>/dev/null | tail -1

echo ""
echo "########## CLONE SIDE ##########"
cd "$(dirname "$0")/../.."
CALC_CENSUS_JS="$CALC_CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonearbit73"
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
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
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
CALC=${CALC//\"/}
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3

# the fixture: add the reference's own line item (Contents Insurance
# \$25 monthly active) through the real UI — the v66/v73 discipline
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
sleep 1
echo "=== CLONE calculator dialog at 390 ==="
agent-browser eval "$CALC_CENSUS_JS" 2>/dev/null | tail -1

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

echo "=== arbit-v73 done ==="
EOF
