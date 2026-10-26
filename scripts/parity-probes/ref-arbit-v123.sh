#!/usr/bin/env bash
# arbit-v123.sh — the v123 re-run pair's flags, DOM-arbitrated per the v43
# rule, at DESKTOP 1280x800 on BOTH sides (the v117-era pair's fresh sweep —
# the calculator dialog + the login view, last re-shot v117; the pair's
# TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123]). The censuses:
#   (1) the CALCULATOR dialog census — the panel + totalCard + row + the
#       name h4 + the pill row + the amount + the hover actions (the v66
#       axes, a drift re-check) PLUS the header family (title + desc +
#       close) and the Add Item button (the axes the VLM flags touch).
#   (2) the LOGIN view census — the card chrome + the h1/subtitle + the
#       input pair + the Sign in button + the mode links + the brand logo.
# READ-ONLY on the reference (login + hover + dialog-open only — the v46
# rule). The clone side adds the matching "Contents Insurance" $25 line
# item through the real UI (a clone-side write — allowed) then FULLY
# restores the fixture (delete + restore Rent's $1850 + verify the
# $2235.00 page total). The v73 heredoc lesson: the QUOTED <<'EOF' with
# the env-injected censuses; no literal dollar sequences in the census JS
# (the v64 rule — the amount leaf is found via String.fromCharCode(36)).
set -u
REF="https://zero-balance-4885a8f3.base44.app"


# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v122 lesson):
# the combined arbit form's clone half is the chromium resource-exhaustion
# risk (the v89/v91-documented symptom class), so the census runs as two
# independent halves from the start; the census JS blocks are byte-identical
# across the halves (the md5 line-block contract).

CALC_CENSUS_JS="(async () => {
  const out = {};
  // the panel: the clone's Radix dialog first, the reference's plain
  // fixed div (maxWidth 768px) as the fallback — one finder, both sides.
  let panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!panel) panel = [...document.querySelectorAll('div')].find(d => getComputedStyle(d).maxWidth === '768px' && d.getBoundingClientRect().width > 300);
  if (!panel) return JSON.stringify({ panel: 'not found' });
  const cs = getComputedStyle(panel);
  const r = panel.getBoundingClientRect();
  out.panel = { w: Math.round(r.width), h: Math.round(r.height), radius: cs.borderRadius, maxW: cs.maxWidth, bg: cs.backgroundColor, shadow: cs.boxShadow.slice(0,130) };

  // the scrim sibling (the reference's scrim WRAPS the panel; the clone's
  // is a sibling — the v72 structural class; the rendered chrome is the
  // axis, never the DOM shape)
  let scrim = null;
  if (panel.parentElement && getComputedStyle(panel.parentElement).backdropFilter && getComputedStyle(panel.parentElement).backdropFilter !== 'none') scrim = panel.parentElement;
  if (!scrim) { const fixed = [...document.querySelectorAll('div')].filter(d => { const s = getComputedStyle(d); return s.position === 'fixed' && s.backdropFilter && s.backdropFilter !== 'none' && d.getBoundingClientRect().width > 300; }); scrim = fixed[fixed.length-1] || null; }
  if (scrim) { const scs = getComputedStyle(scrim); const sr = scrim.getBoundingClientRect(); out.scrim = { bg: scs.backgroundColor, blur: scs.backdropFilter, w: Math.round(sr.width), h: Math.round(sr.height) }; }

  // the header family: the title + the description + the close button
  const title = [...panel.querySelectorAll('h2,h3,h1,div,span')].filter(e => (e.textContent||'').trim() === 'Rent Calculator' && e.children.length === 0)[0];
  if (title) { const s = getComputedStyle(title); out.title = { fs: s.fontSize, fw: s.fontWeight, color: s.color, lh: s.lineHeight }; }
  const desc = [...panel.querySelectorAll('p,div,span')].filter(e => /Break down your rent into individual items/i.test((e.textContent||'').trim()) && e.children.length === 0)[0];
  if (desc) { const s = getComputedStyle(desc); out.desc = { fs: s.fontSize, color: s.color, lh: s.lineHeight }; }
  const closeBtn = [...panel.querySelectorAll('button')].find(b => /close/i.test(b.getAttribute('aria-label')||'') || /^[×x]$/i.test((b.textContent||'').trim()));
  if (closeBtn) { const s = getComputedStyle(closeBtn); const br = closeBtn.getBoundingClientRect(); out.close = { w: Math.round(br.width), h: Math.round(br.height), radius: s.borderRadius, bg: s.backgroundColor, border: s.borderTopWidth + ' ' + s.borderTopColor }; }

  // the Total Calculated card + the will-update span
  const totalCard = [...panel.querySelectorAll('div')].find(d => getComputedStyle(d).backgroundColor === 'rgb(255, 247, 245)');
  if (totalCard) { const tcs = getComputedStyle(totalCard); const tr = totalCard.getBoundingClientRect(); out.totalCard = { w: Math.round(tr.width), h: Math.round(tr.height), pad: tcs.padding, radius: tcs.borderRadius, border: tcs.border, hasWillUpdateSpan: (totalCard.innerText||'').includes('Will update category total') }; }

  // the line-item row (walk UP from the name leaf)
  const h4 = [...panel.querySelectorAll('h4,h3,div,span')].filter(e => (e.textContent||'').trim() === 'Contents Insurance' && e.children.length === 0)[0];
  if (h4) {
    const h4cs = getComputedStyle(h4);
    out.nameH4 = { fs: h4cs.fontSize, fw: h4cs.fontWeight, color: h4cs.color, h: Math.round(h4.getBoundingClientRect().height), mb: h4cs.marginBottom };
    let row = h4;
    while (row && row !== panel) { const c = getComputedStyle(row); if (parseFloat(c.borderTopWidth) > 0 && c.backgroundColor === 'rgb(255, 255, 255)') break; row = row.parentElement; }
    if (row && row !== panel) {
      const rowCs = getComputedStyle(row); const rowR = row.getBoundingClientRect();
      out.row = { w: Math.round(rowR.width), h: Math.round(rowR.height), pad: rowCs.padding, radius: rowCs.borderRadius, borderTop: rowCs.borderTop, bg: rowCs.backgroundColor };
      const pills = [...row.querySelectorAll('span')].filter(s => parseFloat(getComputedStyle(s).borderRadius) > 100 && s.getBoundingClientRect().width > 10);
      const pillRow = pills.length ? pills[0].parentElement : null;
      if (pillRow) { const prcs = getComputedStyle(pillRow); out.pillRow = { display: prcs.display, gap: prcs.gap, fs: prcs.fontSize, h: Math.round(pillRow.getBoundingClientRect().height), mb: prcs.marginBottom }; }
      if (pills[0]) { const p1 = getComputedStyle(pills[0]); const p1R = pills[0].getBoundingClientRect(); out.pill1 = { h: Math.round(p1R.height), w: Math.round(p1R.width), pad: p1.padding, radius: p1.borderRadius, fs: p1.fontSize, fw: p1.fontWeight }; }
      const D = String.fromCharCode(36);
      const amountP = [...row.querySelectorAll('p,span,div')].filter(e => e.children.length === 0 && (e.textContent||'').trim().startsWith(D)).sort((a,b) => parseFloat(getComputedStyle(b).fontSize) - parseFloat(getComputedStyle(a).fontSize))[0];
      if (amountP) { const apcs = getComputedStyle(amountP); out.amountP = { fs: apcs.fontSize, fw: apcs.fontWeight, color: apcs.color, h: Math.round(amountP.getBoundingClientRect().height) }; }
      let actions = null;
      for (const d of row.querySelectorAll('div')) { const c = getComputedStyle(d); if (c.display === 'flex' && d.querySelectorAll('button').length >= 1 && (c.opacity === '0' || c.opacity === '1') && c.transitionProperty.includes('opacity')) { actions = d; break; } }
      out.actionsAtRest = actions ? { opacity: getComputedStyle(actions).opacity, btnCount: actions.querySelectorAll('button').length } : 'not found';
    } else { out.row = 'not found'; }
  } else { out.nameH4 = 'not found'; }

  // the Add Item button (the orange-gradient CTA)
  const addBtn = [...panel.querySelectorAll('button')].find(b => /^add item$/i.test((b.textContent||'').trim()));
  if (addBtn) { const s = getComputedStyle(addBtn); const br = addBtn.getBoundingClientRect(); out.addBtn = { w: Math.round(br.width), h: Math.round(br.height), radius: s.borderRadius, fs: s.fontSize, fw: s.fontWeight, color: s.color }; }

  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

LOGIN_CENSUS_JS="(async () => {
  const out = { view: 'login', docSW: document.documentElement.scrollWidth, vw: window.innerWidth, title: document.title };
  const form = document.querySelector('form');
  if (!form) return JSON.stringify({ form: 'not found' });
  // the card: walk UP from the form to the rounded container
  let card = form;
  while (card && card !== document.body) { const c = getComputedStyle(card); if (parseFloat(c.borderRadius) > 8 && c.backgroundColor !== 'rgba(0, 0, 0, 0)' && card.getBoundingClientRect().width > 300 && card.getBoundingClientRect().width < 700) break; card = card.parentElement; }
  if (card && card !== document.body) {
    const ccs = getComputedStyle(card); const cr = card.getBoundingClientRect();
    out.card = { w: Math.round(cr.width), pad: ccs.padding, radius: ccs.borderRadius, border: ccs.borderTopWidth + ' ' + ccs.borderTopColor, bg: ccs.backgroundColor, shadow: ccs.boxShadow.slice(0,120) };
  } else { out.card = 'not found'; }
  // the h1 + subtitle
  const h1 = document.querySelector('h1');
  if (h1) { const s = getComputedStyle(h1); out.h1 = { text: (h1.textContent||'').trim().slice(0,24), fs: s.fontSize, fw: s.fontWeight, color: s.color, lh: s.lineHeight }; }
  const sub = h1 ? h1.parentElement.querySelector('p') : null;
  if (sub) { const s = getComputedStyle(sub); out.subtitle = { fs: s.fontSize, color: s.color, text: (sub.textContent||'').trim().slice(0,32) }; }
  // the brand logo image
  const logo = document.querySelector('img');
  if (logo) { const lr = logo.getBoundingClientRect(); out.logo = { w: Math.round(lr.width), h: Math.round(lr.height), radius: getComputedStyle(logo).borderRadius, alt: (logo.getAttribute('alt')||'').slice(0,20) }; }
  // the input pair
  const em = form.querySelector('input[type=email], input[name=email]');
  const pw = form.querySelector('input[type=password]');
  const inputCensus = (i) => { if (!i) return null; const s = getComputedStyle(i); const r = i.getBoundingClientRect(); return { h: Math.round(r.height), radius: s.borderRadius, border: s.borderTopWidth + ' ' + s.borderTopColor, fs: s.fontSize, ph: (i.placeholder||'').slice(0,20) }; };
  out.emailInput = inputCensus(em);
  out.pwInput = inputCensus(pw);
  // the Sign in button
  const btn = [...form.querySelectorAll('button')].find(b => /sign in|log in/i.test(b.textContent));
  if (btn) { const s = getComputedStyle(btn); const r = btn.getBoundingClientRect(); out.signIn = { txt: (btn.textContent||'').trim(), w: Math.round(r.width), h: Math.round(r.height), radius: s.borderRadius, bg: s.backgroundColor, color: s.color, fs: s.fontSize, fw: s.fontWeight }; }
  // the mode links
  const links = [...document.querySelectorAll('a')].filter(a => a.getBoundingClientRect().width > 0);
  out.links = links.slice(0,3).map(a => { const s = getComputedStyle(a); return { txt: (a.textContent||'').trim().slice(0,24), fs: s.fontSize, color: s.color, deco: s.textDecorationLine }; });
  // the Google + OR block (the sign-in state's parity family)
  out.hasGoogle = /google/i.test((document.querySelector('main')||document.body).innerText);
  out.hasORDivider = /(^|\n)\s*or\s*(\n|$)/i.test((document.querySelector('main')||document.body).innerText);
  return JSON.stringify(out);
})()"

########## REFERENCE SIDE (the half) ##########
export AGENT_BROWSER_SESSION="reflogin123arbit"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF /login census (card + h1 + inputs + button + links + brand) ==="
agent-browser eval "$LOGIN_CENSUS_JS" 2>/dev/null | tail -1

export AGENT_BROWSER_SESSION="refcalc123arbit"
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
  echo "ref login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4

# the Rent card finder RETRIES — the fresh-login first fetch can be slow
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
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
# park the pointer FAR from the dialog before the census (the rest state)
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 2
echo "=== REF calculator census (panel + scrim + header + totalCard + row + pills + amount + actions + addBtn) ==="
agent-browser eval "$CALC_CENSUS_JS" 2>/dev/null | tail -1
echo "=== ref arbit v123 half done ==="
