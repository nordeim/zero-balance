#!/usr/bin/env bash
# cardheight-arbit-v117.sh — locate the 4px login-card height delta (ref
# card 746 vs clone 742 at 1280, found by strip-arbit-v117.sh's bottom
# axis). Measures the card + its major content blocks' heights on BOTH
# sides. READ-ONLY (the logged-out /login surface).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

H_JS="(async () => {
  const out = { view: 'login', docSW: document.documentElement.scrollWidth, vw: window.innerWidth };
  const form = document.querySelector('form');
  if (!form) return JSON.stringify({ form: 'not found' });
  let card = form;
  while (card && card !== document.body) { const c = getComputedStyle(card); if (parseFloat(c.borderRadius) > 8 && c.backgroundColor !== 'rgba(0, 0, 0, 0)' && card.getBoundingClientRect().width > 300 && card.getBoundingClientRect().width < 700) break; card = card.parentElement; }
  if (!card || card === document.body) return JSON.stringify({ card: 'not found' });
  const cr = card.getBoundingClientRect();
  out.cardH = Math.round(cr.height);
  out.cardPad = getComputedStyle(card).padding;
  // the inner padding wrapper (the card's non-absolute child)
  const inner = [...card.children].find(el => getComputedStyle(el).position !== 'absolute');
  if (inner) { const ir = inner.getBoundingClientRect(); const is = getComputedStyle(inner); out.inner = { h: Math.round(ir.height), pad: is.padding, display: is.display }; }
  // the direct children of inner, with heights
  if (inner) {
    out.innerKids = [...inner.children].map(el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return { tag: el.tagName, txt: (el.textContent || '').trim().slice(0, 18), h: Math.round(r.height), y: Math.round(r.top - ir.top), mt: s.marginTop, mb: s.marginBottom }; });
  }
  // the form's own kids (inputs/button/rows)
  out.formKids = [...form.children].map(el => { const r = el.getBoundingClientRect(); return { tag: el.tagName, txt: (el.textContent || '').trim().slice(0, 16), h: Math.round(r.height) }; });
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280, /login) ==="
export AGENT_BROWSER_SESSION="refh117"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- card-height census:"
agent-browser eval "$H_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /login) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="cloneh117"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- card-height census:"
agent-browser eval "$H_JS" 2>/dev/null | tail -1
EOF
echo "=== cardheight arbit v117 done ==="
