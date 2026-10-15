#!/usr/bin/env bash
# arbit2-v62.sh — M2 follow-up: the mobile header subtitle finder. The h1's
# parent carries no <p> — the subtitle is another element shape. Find the
# element whose text ends with "net zero" near the page top, census it on
# both sides at 390x844. READ-ONLY.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

SUBTITLE_JS="(async () => {
  // walk every leaf-ish text node for the 'achieve net zero' tail
  const walker = document.createTreeWalker(document.querySelector('main') || document.body, NodeFilter.SHOW_TEXT);
  let node, hits = [];
  while ((node = walker.nextNode())) {
    const t = (node.textContent || '').trim();
    if (/net zero/i.test(t) && t.length < 120) hits.push(node.parentElement);
  }
  if (!hits.length) return 'no net-zero text found';
  // the subtitle is the one that is NOT a heading and not the hero card's
  // big label — take the first under the page header area
  const cands = hits.filter(el => el && el.getBoundingClientRect().height > 0 && el.children.length === 0);
  if (!cands.length) return JSON.stringify({ hits: hits.length, note: 'all containers' });
  const out = cands.slice(0, 4).map(p => {
    const r = p.getBoundingClientRect();
    const s = getComputedStyle(p);
    const range = document.createRange();
    range.selectNodeContents(p);
    return {
      tag: p.tagName, text: p.textContent.trim().slice(0, 80),
      w: Math.round(r.width), h: Math.round(r.height), top: Math.round(r.top),
      font: s.fontSize, weight: s.fontWeight, color: s.color, lh: s.lineHeight,
      lines: range.getClientRects().length,
      parentTag: p.parentElement ? p.parentElement.tagName + '.' + (p.parentElement.className || '').toString().slice(0, 40) : null,
      parentH: p.parentElement ? Math.round(p.parentElement.getBoundingClientRect().height) : null,
    };
  });
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (390) ==="
export AGENT_BROWSER_SESSION="refarbit62b"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser eval "$SUBTITLE_JS" 2>/dev/null | tail -1

echo "=== CLONE side (390) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbit62b"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval "$SUBTITLE_JS" 2>/dev/null | tail -1
EOF
echo "=== arbit2 v62 done ==="
