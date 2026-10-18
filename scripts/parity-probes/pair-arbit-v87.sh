#!/usr/bin/env bash
# pair-arbit-v87.sh — the ONE-SHOT both-sides census for the v87 pin's
# family: the calculator CLOSE button's chrome beyond the v59 {36,36}
# (the radius 6px / the transparent bg / the 0px border-width — never
# pinned at ANY viewport; the v49/v53/v59 pins hold w/h only) + the
# LOGIN card's pad family (the outer container's 0px pad + the inner
# content pad — the v75 pin holds w/radius/bg, never the pad) + the
# LOGO img's own radius (the v75 pin holds w/h/alt, never the radius —
# the visual circle lives on the parent span). The v84/v85/v86 one-shot
# precedent: the pin's expected values are THIS census's own measured
# values, byte-identical on both sides at 1280x800.
# READ-ONLY on the reference (login + hover + dialog-open only — the
# v46 rule). Double-quoted-heredoc-safe: no dollar sequences in the
# census JS; no backticks; no attribute-value selectors (geometry +
# text-content filters only — the v78 rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CALC_CENSUS_JS="(async () => {
  const out = {};
  let panel = [...document.querySelectorAll('[role=dialog]')].find(d => (d.innerText||'').includes('Rent Calculator'));
  if (!panel) panel = [...document.querySelectorAll('div')].find(d => getComputedStyle(d).maxWidth === '768px' && d.getBoundingClientRect().width > 300);
  if (!panel) return JSON.stringify({ panel: 'not found' });
  // the close button: the FIRST 36x36-class button in the header (the
  // aria-label/text finders are NAME-dependent — the reference's own
  // button carries NO accessible name as of this cycle; geometry +
  // position find it on both sides: the header's leading large square)
  const btns = [...panel.querySelectorAll('button')];
  const close = btns.find(b => {
    const r = b.getBoundingClientRect();
    return Math.abs(r.width - 36) < 3 && Math.abs(r.height - 36) < 3 && r.top < panel.getBoundingClientRect().top + 80 && !(b.textContent||'').trim().match(/add/i);
  });
  if (close) {
    const s = getComputedStyle(close);
    const r = close.getBoundingClientRect();
    out.close = { w: Math.round(r.width), h: Math.round(r.height), radius: s.borderRadius, bg: s.backgroundColor, borderTopWidth: s.borderTopWidth, display: s.display };
  } else { out.close = 'not found'; }
  // the pillRow mb (the record — the v66 pin holds display/gap/fs/h)
  const h4 = [...panel.querySelectorAll('h4,h3,div,span')].filter(e => (e.textContent||'').trim() === 'Contents Insurance' && e.children.length === 0)[0];
  if (h4) {
    let row = h4;
    while (row && row !== panel) { const c = getComputedStyle(row); if (parseFloat(c.borderTopWidth) > 0 && c.backgroundColor === 'rgb(255, 255, 255)') break; row = row.parentElement; }
    if (row && row !== panel) {
      const pills = [...row.querySelectorAll('span')].filter(s => parseFloat(getComputedStyle(s).borderRadius) > 100 && s.getBoundingClientRect().width > 10);
      const pillRow = pills.length ? pills[0].parentElement : null;
      if (pillRow) out.pillRowMb = getComputedStyle(pillRow).marginBottom;
    }
  }
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

LOGIN_CENSUS_JS="(async () => {
  const out = { view: 'login' };
  const form = document.querySelector('form');
  if (!form) return JSON.stringify({ form: 'not found' });
  let card = form;
  while (card && card !== document.body) { const c = getComputedStyle(card); if (parseFloat(c.borderRadius) > 8 && c.backgroundColor !== 'rgba(0, 0, 0, 0)' && card.getBoundingClientRect().width > 300 && card.getBoundingClientRect().width < 700) break; card = card.parentElement; }
  if (card && card !== document.body) {
    const ccs = getComputedStyle(card);
    out.card = { w: Math.round(card.getBoundingClientRect().width), pad: ccs.padding, borderTopWidth: ccs.borderTopWidth };
    // the inner content pad (the direct child div holding the padding)
    const inner = [...card.children].find(ch => getComputedStyle(ch).padding && getComputedStyle(ch).padding !== '0px');
    if (inner) out.innerPad = getComputedStyle(inner).padding;
  } else { out.card = 'not found'; }
  const logo = document.querySelector('img');
  if (logo) {
    const s = getComputedStyle(logo);
    out.logo = { w: Math.round(logo.getBoundingClientRect().width), h: Math.round(logo.getBoundingClientRect().height), radius: s.borderRadius };
  }
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side: /login (1280) ==="
export AGENT_BROWSER_SESSION="refpair87"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$LOGIN_CENSUS_JS" 2>/dev/null | tail -1

echo "=== REFERENCE side: calculator (1280, read-only open) ==="
export AGENT_BROWSER_SESSION="refpair87calc"
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
  sleep 4
done
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
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 2
agent-browser eval "$CALC_CENSUS_JS" 2>/dev/null | tail -1

echo ""
echo "=== CLONE side: /login (1280) ==="
cd "$(dirname "$0")/../.."
CALC_CENSUS_JS="$CALC_CENSUS_JS" LOGIN_CENSUS_JS="$LOGIN_CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonepair87"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$LOGIN_CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side: calculator (1280, read-only open) ==="
export AGENT_BROWSER_SESSION="clonepair87calc"
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
POS=\$(agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\\\$1850'));
  if (!card) return 'ERR';
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
X=\$(echo "\$POS" | cut -d, -f1); Y=\$(echo "\$POS" | cut -d, -f2)
agent-browser mouse move "\$X" "\$Y" >/dev/null 2>&1
sleep 1
CALC=\$(agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent') && (c.innerText||'').includes('\\\$1850'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate\\\$/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
CX=\$(echo "\$CALC" | cut -d, -f1); CY=\$(echo "\$CALC" | cut -d, -f2)
agent-browser mouse move "\$CX" "\$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 2
agent-browser eval "$CALC_CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== pair arbit v87 done ==="
