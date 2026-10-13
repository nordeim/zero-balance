#!/usr/bin/env bash
# vlm-arbit-v56.sh — the v56 VLM-pair DOM arbitration (the v43 rule: every
# flag is DOM-verified before it counts). The PAIR 1 flags to arbitrate:
# (1) the nav "Dashboard" highlight — the clone highlights, the reference
#     does not AT ROOT (the documented root-URL active-nav gap, a reference
#     bug the clone deliberately fixes — superset class). Probe: the nav
#     link's computed style at / AND at /networth on both sites (the
#     non-root view must highlight on BOTH — proving the clone's rail
#     matches the reference's rail wherever the reference works).
# (2) the hero progress bar width — verify it is data-driven (width ∝ the
#     allocation % each site computes), not a style drift.
# NOTE: the reference has NO <nav> landmark (its own documented bug) — the
# link finder must scan ALL anchors, not nav-scoped selectors.
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

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

echo "=== REFERENCE side ==="
export AGENT_BROWSER_SESSION="refarbit56"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
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
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1

echo "--- ref / (root): nav + progress ---"
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 4
agent-browser eval "$NAVPROBE" 2>/dev/null | tail -1
agent-browser eval "$PROGRESSPROBE" 2>/dev/null | tail -1

echo "--- ref /networth: nav ---"
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 4
agent-browser eval "$NAVPROBE" 2>/dev/null | tail -1
echo "=== ref arbitration done ==="
