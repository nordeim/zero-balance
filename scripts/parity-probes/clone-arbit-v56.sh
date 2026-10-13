#!/usr/bin/env bash
# clone-arbit-v56.sh — the v56 DOM arbitration, CLONE side (companion to
# vlm-arbit-v56.sh). Runs inside with-server.sh on :3200.
set -u
cd "$(dirname "$0")/../.."

NAVPROBE='(async () => {
  const links = [...document.querySelectorAll("a")];
  const probe = {};
  for (const view of ["dashboard", "networth"]) {
    const l = links.find(a => (a.getAttribute("href") || "").toLowerCase().includes(view) && a.getBoundingClientRect().width > 0);
    if (!l) { probe[view] = "no link"; continue; }
    const s = getComputedStyle(l);
    probe[view] = { bg: s.backgroundColor, bgImage: s.backgroundImage.slice(0, 60), color: s.color, weight: s.fontWeight };
  }
  return JSON.stringify(probe);
})()'

PROGRESSPROBE='(async () => {
  const bars = [...document.querySelectorAll("div")].filter(d => {
    const s = getComputedStyle(d);
    return /rgb/.test(s.backgroundColor) && s.backgroundColor !== "rgba(0, 0, 0, 0)" && d.getBoundingClientRect().width > 40 && d.getBoundingClientRect().height >= 4 && d.getBoundingClientRect().height <= 16;
  });
  const samples = bars.map(b => ({ w: Math.round(b.getBoundingClientRect().width), h: Math.round(b.getBoundingClientRect().height), bg: getComputedStyle(b).backgroundColor }));
  const pct = (document.body.textContent || "").match(/([0-9.]+)%/);
  return JSON.stringify({ barSamples: samples.slice(0, 6), firstPct: pct ? pct[1] : null });
})()'

bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbit56"
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

echo "--- clone / (root): nav + progress ---"
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval '$NAVPROBE' 2>/dev/null | tail -1
agent-browser eval '$PROGRESSPROBE' 2>/dev/null | tail -1

echo "--- clone /networth: nav ---"
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser eval '$NAVPROBE' 2>/dev/null | tail -1
echo "=== clone arbitration done ==="
EOF
