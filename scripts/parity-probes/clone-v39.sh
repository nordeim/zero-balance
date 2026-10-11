#!/usr/bin/env bash
# v39: clone-side standing checks (33rd) — the compact mirror of
# ref-v39.sh: R1–R4 mobile navigation, the census, the SEO pair, plus the
# v39 NEW surface's structural census: the MOBILE sheet-open a11y
# structure (the nav landmark + the DialogTitle + the named burger — the
# superset the reference lacks: its sheet has NO nav, NO title).
# Runs INSIDE with-server.sh (the :3200 parity server).
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone39"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 3

echo "=== CLONE census (33rd) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone39 "$PB/census-v35.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R1 (burger hit) at 390x844 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone39 "$PB/probe-r1-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R2 (sheet opens, nav, closes — the superset) ==="
bash "$PB/run-probe.sh" clone39 "$PB/probe-r2-open-v34.mjs" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" clone39 "$PB/probe-r2-nav-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R3 (active nav on /) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone39 "$PB/probe-r3-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE R4 (overflow census) ==="
bash "$PB/run-probe.sh" clone39 "$PB/probe-r4a-v34.mjs" 2>/dev/null | tail -1
agent-browser set viewport 1280 800 >/dev/null 2>&1

echo ""
echo "=== CLONE SEO pair ==="
agent-browser open "$BASE/robots.txt" >/dev/null 2>&1
sleep 2
agent-browser eval "document.body.innerText.slice(0,300)" 2>/dev/null | tail -1
agent-browser open "$BASE/sitemap.xml" >/dev/null 2>&1
sleep 2
agent-browser eval "document.body.innerText.replace(/\\s+/g,' ').slice(0,600)" 2>/dev/null | tail -1

echo ""
echo "=== SURFACE v39: mobile sheet-open a11y structure (390x844) ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  // open the sheet via the named burger
  const burger = [...document.querySelectorAll('button')].find(b =>
    (b.getAttribute('aria-label') || '').includes('Toggle Sidebar') ||
    !!b.querySelector('.sr-only'));
  if (!burger) return 'NO BURGER';
  burger.click();
  await new Promise(r => setTimeout(r, 900));
  // the sheet content: Radix DialogContent with data-state=open (portal,
  // end of body — query the LAST one, not the first)
  const openEls = [...document.querySelectorAll('[data-state=open]')];
  const sheet = openEls.reverse().find(e => e.querySelector('nav'));
  // The sheet's OWN nav (NOT document.querySelector('nav') — that finds the
  // display:none desktop rail first in DOM order; the sheet's portal is at
  // the end of body).
  const nav = sheet ? sheet.querySelector('nav') : null;
  const inSheet = !!nav;
  const title = sheet ? (sheet.querySelector('[id]') && [...sheet.querySelectorAll('*')].find(e =>
    (e.className||'').toString().includes('sr-only') && e.textContent.trim())) : null;
  const links = sheet ? [...sheet.querySelectorAll('a')].map(a => (a.textContent||'').trim().slice(0,18)) : [];
  const bodyLock = getComputedStyle(document.body).overflow;
  return JSON.stringify({
    burgerNamed: !!(burger.getAttribute('aria-label') || burger.querySelector('.sr-only')),
    sheetFound: !!sheet,
    sheetRole: sheet ? sheet.getAttribute('role') : null,
    navInSheet: inSheet,
    navAriaLabel: nav ? nav.getAttribute('aria-label') : null,
    sheetTitle: title ? title.textContent.trim() : null,
    sheetLinks: links,
    bodyLocked: bodyLock === 'hidden',
    dialogLabelled: sheet ? (sheet.getAttribute('aria-labelledby') || sheet.getAttribute('aria-label') || null) : 'NO SHEET',
  });
})()" 2>/dev/null | tail -1
agent-browser set viewport 1280 800 >/dev/null 2>&1
