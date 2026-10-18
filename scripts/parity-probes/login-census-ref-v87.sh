#!/usr/bin/env bash
# login-census-ref-v87.sh — the v87 arbitration's login follow-up: the
# reference /login census re-run (the arbit-v87.sh pass raced the cold
# session's page load — the form wasn't in the DOM at census time). The
# same LOGIN_CENSUS_JS axes as arbit-v87.sh, with the load RETRIED.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

LOGIN_CENSUS_JS="(async () => {
  const out = { view: 'login', docSW: document.documentElement.scrollWidth, vw: window.innerWidth, title: document.title };
  const form = document.querySelector('form');
  if (!form) return JSON.stringify({ form: 'not found' });
  let card = form;
  while (card && card !== document.body) { const c = getComputedStyle(card); if (parseFloat(c.borderRadius) > 8 && c.backgroundColor !== 'rgba(0, 0, 0, 0)' && card.getBoundingClientRect().width > 300 && card.getBoundingClientRect().width < 700) break; card = card.parentElement; }
  if (card && card !== document.body) {
    const ccs = getComputedStyle(card); const cr = card.getBoundingClientRect();
    out.card = { w: Math.round(cr.width), pad: ccs.padding, radius: ccs.borderRadius, border: ccs.borderTopWidth + ' ' + ccs.borderTopColor, bg: ccs.backgroundColor, shadow: ccs.boxShadow.slice(0,120) };
  } else { out.card = 'not found'; }
  const h1 = document.querySelector('h1');
  if (h1) { const s = getComputedStyle(h1); out.h1 = { text: (h1.textContent||'').trim().slice(0,24), fs: s.fontSize, fw: s.fontWeight, color: s.color, lh: s.lineHeight }; }
  const sub = h1 ? h1.parentElement.querySelector('p') : null;
  if (sub) { const s = getComputedStyle(sub); out.subtitle = { fs: s.fontSize, color: s.color, text: (sub.textContent||'').trim().slice(0,32) }; }
  const logo = document.querySelector('img');
  if (logo) { const lr = logo.getBoundingClientRect(); out.logo = { w: Math.round(lr.width), h: Math.round(lr.height), radius: getComputedStyle(logo).borderRadius, alt: (logo.getAttribute('alt')||'').slice(0,20) }; }
  const em = form.querySelector('input[type=email], input[name=email]');
  const pw = form.querySelector('input[type=password]');
  const inputCensus = (i) => { if (!i) return null; const s = getComputedStyle(i); const r = i.getBoundingClientRect(); return { h: Math.round(r.height), radius: s.borderRadius, border: s.borderTopWidth + ' ' + s.borderTopColor, fs: s.fontSize, ph: (i.placeholder||'').slice(0,20) }; };
  out.emailInput = inputCensus(em);
  out.pwInput = inputCensus(pw);
  const btn = [...form.querySelectorAll('button')].find(b => /sign in|log in/i.test(b.textContent));
  if (btn) { const s = getComputedStyle(btn); const r = btn.getBoundingClientRect(); out.signIn = { txt: (btn.textContent||'').trim(), w: Math.round(r.width), h: Math.round(r.height), radius: s.borderRadius, bg: s.backgroundColor, color: s.color, fs: s.fontSize, fw: s.fontWeight }; }
  const links = [...document.querySelectorAll('a')].filter(a => a.getBoundingClientRect().width > 0);
  out.links = links.slice(0,3).map(a => { const s = getComputedStyle(a); return { txt: (a.textContent||'').trim().slice(0,24), fs: s.fontSize, color: s.color, deco: s.textDecorationLine }; });
  out.hasGoogle = /google/i.test((document.querySelector('main')||document.body).innerText);
  out.hasORDivider = /(^|\n)\s*or\s*(\n|$)/i.test((document.querySelector('main')||document.body).innerText);
  return JSON.stringify(out);
})()"

export AGENT_BROWSER_SESSION="reflogin87b"
agent-browser set viewport 1280 800 >/dev/null 2>&1
for attempt in 1 2 3 4 5; do
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 5
  RESULT=$(agent-browser eval "$LOGIN_CENSUS_JS" 2>/dev/null | tail -1)
  echo "attempt $attempt: $RESULT"
  if ! echo "$RESULT" | grep -q "not found"; then break; fi
done
echo "=== ref login census follow-up done ==="
