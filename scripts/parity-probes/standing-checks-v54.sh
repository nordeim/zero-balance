#!/usr/bin/env bash
# standing-checks-v54.sh — the 53rd standing check, clone side (R1-R4 + SEO)
# via with-server on :3200. Read-only.
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clone54"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
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
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1

echo "=== R1: burger hit-test + sheet opens ==="
agent-browser eval "(async () => {
  const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('Toggle Sidebar'));
  if (!b) return 'no burger';
  const r = b.getBoundingClientRect();
  const hit = document.elementFromPoint(r.x + r.width/2, r.y + r.height/2);
  return JSON.stringify({ hitIsBurgerChild: b.contains(hit) });
})()" 2>/dev/null | tail -1
agent-browser eval "(async () => { const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('Toggle Sidebar')); b.click(); return 'clicked'; })()" 2>/dev/null | tail -1
sleep 2
agent-browser eval "(async () => {
  const sheet = [...document.querySelectorAll('div')].find(d => d.getAttribute('role') === 'dialog' && d.getBoundingClientRect().width === 288);
  return JSON.stringify({ sheetOpen: !!sheet });
})()" 2>/dev/null | tail -1

echo "=== R2: sheet closes on nav ==="
agent-browser eval "(async () => {
  const link = [...document.querySelectorAll('a')].filter(l => (l.getAttribute('href')||'') === '/income' && l.getBoundingClientRect().width > 0)[0];
  if (link) { link.click(); return 'clicked /income'; }
  return 'no link';
})()" 2>/dev/null | tail -1
sleep 3
agent-browser eval "(async () => {
  const sheet = [...document.querySelectorAll('div')].find(d => d.getAttribute('role') === 'dialog' && d.getBoundingClientRect().width === 288);
  const overlay = [...document.querySelectorAll('div')].find(d => getComputedStyle(d).backgroundColor === 'rgba(0, 0, 0, 0.8)' && d.getBoundingClientRect().width >= 300);
  return JSON.stringify({ url: location.pathname, sheetGone: !sheet, overlayGone: !overlay });
})()" 2>/dev/null | tail -1

echo "=== R3: nav landmark ==="
agent-browser eval "(() => JSON.stringify({ navLandmark: !!document.querySelector('nav') }))()" 2>/dev/null | tail -1

echo "=== R4: zero overflow at 390 (all views) ==="
for view in "/" "/income" "/savings" "/expenses" "/networth"; do
  agent-browser open "http://localhost:3200$view" >/dev/null 2>&1
  sleep 2
  agent-browser eval "(() => JSON.stringify({ view: '$view', docSW: document.documentElement.scrollWidth }))()" 2>/dev/null | tail -1
done

echo "=== SEO pair (clone) ==="
agent-browser open "http://localhost:3200/robots.txt" >/dev/null 2>&1
sleep 1
agent-browser eval "(() => document.body.innerText.slice(0,100).replace(/\n/g, ' | '))()" 2>/dev/null | tail -1
agent-browser open "http://localhost:3200/sitemap.xml" >/dev/null 2>&1
sleep 1
agent-browser eval "(() => document.body.innerText.slice(0,240).replace(/\n/g, ' | '))()" 2>/dev/null | tail -1
EOF
