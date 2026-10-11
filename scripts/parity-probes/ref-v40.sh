#!/usr/bin/env bash
# v40: reference-side standing checks (34th) — the compact re-verification:
#   R1–R4 mobile navigation (the user's standing task focus), the data-drift
#   census (before + after), the SEO pair, the v39 sheet-structure census. The
#   v40 NEW surface (the dashboard Tab-order focus walk) is measured by
#   tabwalk-v36.sh + focus-census-v40.mjs + stat-card-chain-v40.mjs.
# Read-only discipline: no clicks that mutate data; the census runs before
# and after.
set -u
BASE="https://zero-balance-4885a8f3.base44.app"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="ref40"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'NO FORM — maybe already logged in';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4

echo "=== REF census (34th) — BEFORE probes ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref40 "$PB/census-v35.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF R1 (burger hit) at 390x844 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref40 "$PB/probe-r1-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF R2 (sheet opens, nav, traps — the reference bug) ==="
bash "$PB/run-probe.sh" ref40 "$PB/probe-r2-open-v34.mjs" 2>/dev/null | tail -1
bash "$PB/run-probe.sh" ref40 "$PB/probe-r2-nav-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF R3 (active nav on /) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref40 "$PB/probe-r3-v34.mjs" 2>/dev/null | tail -1

echo ""
echo "=== REF R4 (overflow census) ==="
bash "$PB/run-probe.sh" ref40 "$PB/probe-r4a-v34.mjs" 2>/dev/null | tail -1
agent-browser set viewport 1280 800 >/dev/null 2>&1

echo ""
echo "=== REF SEO pair ==="
agent-browser open "$BASE/robots.txt" >/dev/null 2>&1
sleep 2
agent-browser eval "document.body.innerText.slice(0,300)" 2>/dev/null | tail -1
agent-browser open "$BASE/sitemap.xml" >/dev/null 2>&1
sleep 2
agent-browser eval "document.body.innerText.replace(/\\s+/g,' ').slice(0,600)" 2>/dev/null | tail -1

echo ""
echo "=== REF census (34th) — AFTER probes (read-only check) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref40 "$PB/census-v35.mjs" 2>/dev/null | tail -1

echo ""
echo "=== SURFACE v40: reference mobile sheet-open structure (390x844) ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const burger = [...document.querySelectorAll('button')].find(b => {
    const r = b.getBoundingClientRect();
    return r.top < 80 && r.left < 60 && r.width < 60;
  });
  if (!burger) return 'NO BURGER';
  burger.click();
  await new Promise(r => setTimeout(r, 900));
  const fixed = [...document.querySelectorAll('div')].filter(d => {
    const c = (d.className || '').toString();
    const r = d.getBoundingClientRect();
    return c.includes('fixed') && r.width > 150 && r.height > 300;
  });
  const sheet = fixed[0];
  const nav = document.querySelector('nav');
  const sheetNav = sheet ? sheet.querySelector('nav') : null;
  const links = sheet ? [...sheet.querySelectorAll('a')].map(a => (a.textContent||'').trim().slice(0,18)) : [];
  const title = sheet ? [...sheet.querySelectorAll('*')].find(e =>
    (e.className||'').toString().includes('sr-only')) : null;
  return JSON.stringify({
    sheetFound: !!sheet,
    sheetRole: sheet ? sheet.getAttribute('role') : null,
    sheetNav: !!sheetNav,
    anyNav: !!nav,
    sheetTitle: title ? title.textContent.trim() : null,
    sheetLinks: links,
    bodyLocked: getComputedStyle(document.body).overflow === 'hidden',
    labelledby: sheet ? (sheet.getAttribute('aria-labelledby') || sheet.getAttribute('aria-label') || null) : null,
  });
})()" 2>/dev/null | tail -1
agent-browser set viewport 1280 800 >/dev/null 2>&1
