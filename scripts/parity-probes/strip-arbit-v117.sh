#!/usr/bin/env bash
# strip-arbit-v117.sh — the ONE-SHOT both-sides DOM census for the v117 pin
# candidate: the LOGIN CARD'S TOP ACCENT STRIP at desktop 1280x800 (the
# absolute h-1 slate-gradient bar at the card's top — the element every
# login census walked past: the v7 G2 pin holds its gradient COLORS via
# toContain only, the standing login census the card WRAPPER's chrome; the
# strip's geometry {position/top/left/right/h/w} is never pinned at ANY
# viewport in ANY spec).
# READ-ONLY (the logged-out /login surface — no session). The census JS is
# defined ONCE and eval'd on BOTH sides (byte-identical by construction).
# Double-quoted-heredoc-safe: no dollar sequences in the census JS; no
# backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

STRIP_JS="(async () => {
  const out = { view: 'login', docSW: document.documentElement.scrollWidth, vw: window.innerWidth };
  const form = document.querySelector('form');
  if (!form) return JSON.stringify({ form: 'not found' });
  // the card: walk UP from the form to the rounded container (the
  // standing login census's own finder — works on both sides)
  let card = form;
  while (card && card !== document.body) { const c = getComputedStyle(card); if (parseFloat(c.borderRadius) > 8 && c.backgroundColor !== 'rgba(0, 0, 0, 0)' && card.getBoundingClientRect().width > 300 && card.getBoundingClientRect().width < 700) break; card = card.parentElement; }
  if (!card || card === document.body) return JSON.stringify({ card: 'not found' });
  const cr = card.getBoundingClientRect();
  out.cardW = Math.round(cr.width);
  // the strip: the card's own child that is absolutely positioned, thin
  // (h <= 8), and pinned to the card's top (top === 0) — STRUCTURAL, the
  // class strings never trusted (the v72 class)
  const kids = [...card.children];
  const strip = kids.find(el => { const s = getComputedStyle(el); const r = el.getBoundingClientRect(); return s.position === 'absolute' && r.height <= 8 && Math.abs(r.top - cr.top) <= 1; });
  if (!strip) { out.strip = 'not found'; return JSON.stringify(out); }
  const s = getComputedStyle(strip);
  const r = strip.getBoundingClientRect();
  out.strip = {
    tag: strip.tagName,
    position: s.position,
    top: s.top, right: s.right, left: s.left, bottom: s.bottom,
    h: Math.round(r.height),
    w: Math.round(r.width),
    bgImage: s.backgroundImage,
    bgRepeat: s.backgroundRepeat,
    zIndex: s.zIndex,
  };
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280, /login — the logged-out surface) ==="
export AGENT_BROWSER_SESSION="refstrip117"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- strip census:"
agent-browser eval "$STRIP_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /login — the logged-out surface) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonestrip117"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- strip census:"
agent-browser eval "$STRIP_JS" 2>/dev/null | tail -1
EOF
echo "=== strip arbit v117 done ==="
