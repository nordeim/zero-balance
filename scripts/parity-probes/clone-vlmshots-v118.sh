#!/usr/bin/env bash
# clone-vlmshots-v118.sh — the v118 VLM pair, CLONE side: a fresh re-run of the
# v112-era pair (the re-run cadence's rotation — the pair's NINTH re-run
# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118], last re-shot v112, the FORTY-FIRST consecutive
# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the
# NETWORTH view and (2) the DASHBOARD's drill-down EXPANDED state. Runs inside
# with-server.sh (the :3200 parity server). The v56 lesson: split the shots
# into per-view invocations when the 240s timeout bites.
set -u
cd "$(dirname "$0")/../.."
mkdir -p /tmp/vlm118

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonevlm118"
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

# PAIR 1: the networth view at desktop 1280 — full page.
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm118/clone-networth.png 2>/dev/null | tail -1

# PAIR 2: the dashboard's drill-down EXPANDED state at desktop 1280.
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const sec = [...card.querySelectorAll('button')].find(b => /Total Income/i.test(b.textContent||''));
  if (!sec) return 'no section';
  sec.click();
  return 'section clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const cat = [...card.querySelectorAll('button')].find(b => b.offsetParent !== null && /\\\$/.test(b.textContent||'') && !/Total|Net Balance/i.test(b.textContent||''));
  if (!cat) return 'no category';
  cat.click();
  return 'category clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser screenshot --full /tmp/vlm118/clone-drilldown.png 2>/dev/null | tail -1

echo "clone shots done"
EOF
