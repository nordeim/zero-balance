#!/usr/bin/env bash
# social-clone-v99.sh — the CLONE half of the supplemental two-half
# census for the v99 pin's axes (the login card's SOCIAL-LOGIN ROW at 1280:
# the OR divider + the Google button). READ-ONLY passive navigation only.
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START.
# Runs inside with-server.sh (the :3200 parity server).
set -u
cd "$(dirname "$0")/../.."

SOCIAL_JS="(async () => {
  const out = { view: 'login-social', docSW: document.documentElement.scrollWidth, vw: window.innerWidth };
  const form = document.querySelector('form');
  if (!form) return JSON.stringify({ err: 'no form' });
  let card = form;
  while (card && card !== document.body) { const c = getComputedStyle(card); if (parseFloat(c.borderRadius) > 8 && c.backgroundColor !== 'rgba(0, 0, 0, 0)' && card.getBoundingClientRect().width > 300 && card.getBoundingClientRect().width < 700) break; card = card.parentElement; }
  if (!card || card === document.body) return JSON.stringify({ err: 'no card' });
  // THE GOOGLE BUTTON (the card's only Google-texted button)
  const g = [...card.querySelectorAll('button')].find(b => /Continue with Google/i.test(b.textContent || ''));
  if (!g) return JSON.stringify({ err: 'no google button' });
  const gs = getComputedStyle(g); const gr = g.getBoundingClientRect();
  const svg = g.querySelector('svg');
  const sr = svg ? svg.getBoundingClientRect() : null;
  out.google = { w: Math.round(gr.width), h: Math.round(gr.height), radius: gs.borderRadius, fs: gs.fontSize, fw: gs.fontWeight, lh: gs.lineHeight, color: gs.color, bg: gs.backgroundColor, border: gs.borderTopWidth + ' ' + gs.borderTopColor, pad: gs.padding, gap: gs.columnGap, display: gs.display, svgW: sr ? Math.round(sr.width) : 0, svgH: sr ? Math.round(sr.height) : 0 };
  // THE SIGN IN BUTTON (the rhythm anchor above the social row)
  const si = [...form.querySelectorAll('button')].find(b => /sign in|log in/i.test(b.textContent));
  const siBottom = si ? Math.round(si.getBoundingClientRect().bottom) : null;
  // THE OR DIVIDER TEXT: any leaf element whose trimmed text is 'or'
  const orEl = [...card.querySelectorAll('span,p,div,h1,h2,h3,h4,button')].filter(e => e.children.length === 0).find(e => /^or$/i.test((e.textContent || '').trim()));
  if (!orEl) { out.orText = 'not found'; return JSON.stringify(out); }
  const os = getComputedStyle(orEl); const orr = orEl.getBoundingClientRect();
  out.orText = { fs: os.fontSize, fw: os.fontWeight, color: os.color, lh: os.lineHeight, tt: os.textTransform, ls: os.letterSpacing, pad: os.padding, bg: os.backgroundColor, h: Math.round(orr.height), w: Math.round(orr.width) };
  // THE RULE LINES: every element <= 2px tall, wider than 150px, inside the card
  const rules = [...card.querySelectorAll('*')].filter(e => {
    const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 150 && r.height > 0 && r.height <= 2 && s.backgroundColor !== 'rgba(0, 0, 0, 0)';
  }).map(e => { const s = getComputedStyle(e); const r = e.getBoundingClientRect(); return { tag: e.tagName, h: s.height, bg: s.backgroundColor, w: Math.round(r.width), y: Math.round(r.y) }; });
  out.rules = rules;
  // THE RHYTHM: signIn bottom -> google top -> or text center
  out.rhythm = { signInToGoogle: siBottom !== null ? Math.round(gr.top - siBottom) : null, googleToOr: Math.round((orr.y + orr.height / 2) - gr.bottom) };
  return JSON.stringify(out);
})()"

SOCIAL_JS="$SOCIAL_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonesocial99"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$SOCIAL_JS" 2>/dev/null | tail -1
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== clone social arbit v99 half done ==="
