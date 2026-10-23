#!/usr/bin/env bash
# capture-dev-shots-v106.sh — the DEV-SERVER screenshot set for the v106
# cycle: boots `npm run dev` (http://localhost:3000), signs the demo user
# in, and captures the remediated codebase as served by the dev server
# into docs/screenshots/dev/ (the 16-shot parity catalog in
# docs/screenshots/ stays untouched — the subfolder keeps the byte-compare
# discipline intact). One invocation: the server and the captures share
# one process tree (the sandbox reaps background processes between shell
# invocations).
set -u
cd "$(dirname "$0")/../.."

mkdir -p docs/screenshots/dev
npm run dev > /tmp/dev-server-v106.log 2>&1 &
DEV_PID=$!
trap 'kill $DEV_PID 2>/dev/null; pkill -f "next dev" 2>/dev/null' EXIT

# wait for the dev server
for i in $(seq 1 60); do
  if curl -s -o /dev/null http://localhost:3000/api/health; then break; fi
  sleep 1
done
sleep 2

export AGENT_BROWSER_SESSION="devshots106"
agent-browser open "http://localhost:3000/login" >/dev/null 2>&1
sleep 5
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
sleep 5

# desktop 1280x800: the dashboard (the remediated codebase's home)
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot docs/screenshots/dev/dev-dashboard-1280.png 2>/dev/null | tail -1

# desktop: the networth view (the v106 pin's surface)
agent-browser open "http://localhost:3000/networth" >/dev/null 2>&1
sleep 5
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot docs/screenshots/dev/dev-networth-1280.png 2>/dev/null | tail -1

# mobile 390x844: the mobile menu OPEN (the superset fixes' surface — the
# user-requested mobile-navigation verification)
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3000/" >/dev/null 2>&1
sleep 5
agent-browser eval "(async () => {
  const b = [...document.querySelectorAll('button')].find(x => (x.textContent||'').includes('Toggle Sidebar'));
  if (b) { b.click(); return 'burger clicked'; }
  return 'no burger';
})()" 2>/dev/null | tail -1
sleep 2
agent-browser screenshot docs/screenshots/dev/dev-mobile-menu-open-390.png 2>/dev/null | tail -1

# mobile: the dashboard with the menu closed
agent-browser eval "(async () => {
  const link = [...document.querySelectorAll('a')].filter(l => (l.getAttribute('href')||'') === '/income' && l.getBoundingClientRect().width > 0)[0];
  if (link) { link.click(); return 'nav link clicked — sheet closes (superset fix #2)'; }
  return 'no link';
})()" 2>/dev/null | tail -1
sleep 3
agent-browser screenshot docs/screenshots/dev/dev-mobile-income-390.png 2>/dev/null | tail -1

agent-browser eval "(() => JSON.stringify({ url: location.pathname, docSW: document.documentElement.scrollWidth, navLandmark: !!document.querySelector('nav') }))()" 2>/dev/null | tail -1

echo "dev shots done"
