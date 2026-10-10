#!/usr/bin/env bash
# v33: clone-side mobile-nav R1-R4 standing check (27th) — burger hit test,
# sheet behavior, per-route overflow, at 390x844. Runs INSIDE with-server.sh.
# Usage: bash scripts/parity-probes/with-server.sh bash scripts/parity-probes/clone-mobile-nav-v33.sh
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes

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
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3

echo "=== CLONE R1 (burger hit) ==="
bash "$PB/run-probe.sh" default "$PB/probe-r1-v31.mjs" 2>/dev/null
echo ""
echo "=== CLONE R2 (sheet closes after nav — superset fix #2) ==="
agent-browser eval "const b=[...document.querySelectorAll('button')].find(b=>{const r=b.getBoundingClientRect();return r.width>20&&r.width<45&&r.top<60&&b.querySelector('svg')}); b?.click(); 'opened:'+(!!b)" >/dev/null 2>&1
sleep 1.5
bash "$PB/run-probe.sh" default "$PB/probe-r2-ref-v32.mjs" 2>/dev/null
echo ""
agent-browser eval "[...document.querySelectorAll('div.fixed a, aside a')].find(a=>/income/i.test(a.textContent))?.click(); 'nav'" >/dev/null 2>&1
sleep 2
bash "$PB/run-probe.sh" default "$PB/probe-r2-ref-v32.mjs" 2>/dev/null
echo ""
echo "=== CLONE R3 (active nav + landmark on /) ==="
agent-browser eval "const x=document.querySelector('button[aria-label*=close i], [data-state=open] button'); 'landmark:'+(!!document.querySelector('nav'))" >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 2.5
agent-browser eval "JSON.stringify({path:location.pathname, navLandmark:!!document.querySelector('nav'), activeLinks:[...document.querySelectorAll('nav a')].filter(a=>{const bg=getComputedStyle(a).backgroundColor;return bg!=='rgba(0, 0, 0, 0)'||/text-gray-900|bg-gray-100/.test(a.className)}).map(a=>a.textContent.trim().slice(0,20))})" 2>/dev/null
echo ""
echo "=== CLONE R4 (per-route overflow) ==="
for p in / /dashboard /income /expenses /savings /networth; do
  agent-browser open "$BASE$p" >/dev/null 2>&1
  sleep 2.5
  echo -n "$p → "
  agent-browser eval "document.documentElement.scrollWidth" 2>/dev/null
done
echo "DONE"
