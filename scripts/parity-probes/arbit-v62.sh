#!/usr/bin/env bash
# arbit-v62.sh — DOM arbitration for the two v62 VLM flags that are not
# already documented classes:
#   D4: the desktop donut labels (VLM: "labels absent on the reference")
#       — the v60 record says the reference DOES render them (the v9 G1b
#       measurement); re-verify live.
#   M2: the mobile header subtitle wrap (VLM: "the clone wraps to a third
#       line, the section taller") — potential REAL gap; census both sides.
# READ-ONLY.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

echo "=== REFERENCE side ==="
export AGENT_BROWSER_SESSION="refarbit62"
agent-browser open "$REF/login" >/dev/null 2>&1
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

# D4: the donut labels at 1280 — the recharts sector text nodes
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const svgs = [...document.querySelectorAll('svg')];
  const donut = svgs.find(s => (s.querySelectorAll('path[name]').length || s.querySelectorAll('recharts-sector').length) || /recharts-pie/.test(s.className.baseVal || ''));
  const texts = donut ? [...donut.querySelectorAll('text')].map(t => t.textContent.trim()).filter(Boolean) : [];
  const namedPaths = donut ? donut.querySelectorAll('path[name]').length : -1;
  return JSON.stringify({ donutFound: !!donut, labelCount: texts.length, labels: texts.slice(0, 8), namedPaths });
})()" 2>/dev/null | tail -1

# M2: the mobile header subtitle at 390 — text + geometry + line count
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const h1 = document.querySelector('h1');
  const block = h1 ? h1.parentElement : null;
  const p = block ? block.querySelector('p') : null;
  if (!p) return 'no subtitle';
  const r = p.getBoundingClientRect();
  const s = getComputedStyle(p);
  const range = document.createRange();
  range.selectNodeContents(p);
  const lines = range.getClientRects().length;
  return JSON.stringify({
    text: p.textContent.trim().slice(0, 90),
    w: Math.round(r.width), h: Math.round(r.height), top: Math.round(r.top),
    font: s.fontSize, weight: s.fontWeight, color: s.color,
    lh: s.lineHeight, ls: s.letterSpacing,
    lineCount: lines,
    blockH: block ? Math.round(block.getBoundingClientRect().height) : null,
  });
})()" 2>/dev/null | tail -1

echo "=== CLONE side ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonearbit62"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const svgs = [...document.querySelectorAll('svg')];
  const donut = svgs.find(s => (s.querySelectorAll('path[name]').length || s.querySelectorAll('recharts-sector').length) || /recharts-pie/.test(s.className.baseVal || ''));
  const texts = donut ? [...donut.querySelectorAll('text')].map(t => t.textContent.trim()).filter(Boolean) : [];
  const namedPaths = donut ? donut.querySelectorAll('path[name]').length : -1;
  return JSON.stringify({ donutFound: !!donut, labelCount: texts.length, labels: texts.slice(0, 8), namedPaths });
})()" 2>/dev/null | tail -1

agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const h1 = document.querySelector('h1');
  const block = h1 ? h1.parentElement : null;
  const p = block ? block.querySelector('p') : null;
  if (!p) return 'no subtitle';
  const r = p.getBoundingClientRect();
  const s = getComputedStyle(p);
  const range = document.createRange();
  range.selectNodeContents(p);
  const lines = range.getClientRects().length;
  return JSON.stringify({
    text: p.textContent.trim().slice(0, 90),
    w: Math.round(r.width), h: Math.round(r.height), top: Math.round(r.top),
    font: s.fontSize, weight: s.fontWeight, color: s.color,
    lh: s.lineHeight, ls: s.letterSpacing,
    lineCount: lines,
    blockH: block ? Math.round(block.getBoundingClientRect().height) : null,
  });
})()" 2>/dev/null | tail -1
EOF
echo "=== arbit v62 done ==="
