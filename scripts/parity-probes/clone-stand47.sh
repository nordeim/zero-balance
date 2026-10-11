#!/usr/bin/env bash
# 41st standing checks — clone side (R1-R4 + SEO pair) against :3200.
set -u
export AGENT_BROWSER_SESSION="clone47std"
BASE="http://localhost:3200"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
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

agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3

echo "=== R1: direct burger hit (native click at center — the toast viewport must NOT block) ==="
agent-browser click 'button[aria-label="Open menu"]' >/dev/null 2>&1 || true
sleep 1
R1=$(agent-browser eval "(() => { const links = [...document.querySelectorAll('a')].filter(a => a.offsetParent !== null && ['Dashboard','Income','Expenses','Savings','Net Worth'].includes(a.textContent.trim())); return JSON.stringify({ sheetLinks: links.length }); })()" 2>/dev/null | tail -1)
echo "R1: $R1"

echo "=== R2: sheet closes on navigation ==="
agent-browser eval "(() => { const link = [...document.querySelectorAll('a')].find(a => a.offsetParent !== null && a.textContent.trim() === 'Income'); if (link) { link.click(); return 'nav'; } return 'no link'; })()" >/dev/null 2>&1
sleep 3
R2=$(agent-browser eval "(() => { const links = [...document.querySelectorAll('a')].filter(a => a.offsetParent !== null && ['Dashboard','Income','Expenses','Savings','Net Worth'].includes(a.textContent.trim())); return JSON.stringify({ url: location.href, sheetLinksOpen: links.length }); })()" 2>/dev/null | tail -1)
echo "R2: $R2"

echo "=== R3: nav landmark + burger aria ==="
R3=$(agent-browser eval "(() => { const nav = document.querySelector('nav'); const burger = [...document.querySelectorAll('button')].find(b => (b.getAttribute('aria-label')||'').toLowerCase().includes('menu')); return JSON.stringify({ navLandmark: !!nav, navLinks: nav ? nav.querySelectorAll('a').length : 0, burgerAria: burger ? burger.getAttribute('aria-label') : null }); })()" 2>/dev/null | tail -1)
echo "R3: $R3"

echo "=== R4: zero horizontal overflow at 390 ==="
R4=$(agent-browser eval "(() => { const main = document.querySelector('main'); return JSON.stringify({ mainScrollWidth: main ? main.scrollWidth : null, docScrollWidth: document.documentElement.scrollWidth }); })()" 2>/dev/null | tail -1)
echo "R4: $R4"

echo "=== SEO pair on :3200 ==="
curl -s "$BASE/robots.txt" | head -3
curl -s -o /dev/null -w "sitemap.xml: %{http_code}\n" "$BASE/sitemap.xml"
