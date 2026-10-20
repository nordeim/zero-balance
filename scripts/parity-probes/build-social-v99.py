#!/usr/bin/env python3
"""Build social-arbit-v99.sh + social-clone-v99.sh — the supplemental
two-half census for the v99 pin's own axes (the login card's SOCIAL-LOGIN
ROW at 1280: the OR divider's text + rule chrome + the Google button's
geometry/typography + the row's vertical rhythm), BUILT TWO-HALF FROM THE
START (the v92..v98 lesson, the v96 headrow + v97 listbox + v98 menu
precedents). The census JS block is extracted ONCE from this builder and
embedded byte-identically in both halves (the md5 line-block contract).

The F4 coverage-map finding this census serves: the v75 F4 pin walked the
card/h1/subtitle/inputs/signIn/logo; the v7 G3 pin holds the Google
button's COLORS and the v45 F4 pin its HOVER shadow; the auth.spec pins
hold the OR divider's PRESENCE per state — but the OR divider's computed
chrome (text typography + rule line + wrapper rhythm) and the Google
button's GEOMETRY/typography (w/h/radius/fs/lh/svg) are NEVER pinned at
ANY viewport in ANY spec. The logged-out /login surface needs no auth on
either side — the census is passive navigation only (the v46 rule holds
trivially)."""
import hashlib, re

# The census JS — shared byte-identically across both halves.
CENSUS_JS = """SOCIAL_JS="(async () => {
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
"""

REF_HALF = """#!/usr/bin/env bash
# social-arbit-v99.sh — the REFERENCE half of the supplemental two-half
# census for the v99 pin's axes (the login card's SOCIAL-LOGIN ROW at 1280:
# the OR divider + the Google button). READ-ONLY passive navigation only
# (the logged-out /login surface — no session, no clicks). THE TWO-HALF
# CONTROLLED FORM, BUILT FROM THE START (the v92..v98 lesson).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

""" + CENSUS_JS + """
export AGENT_BROWSER_SESSION="refsocial99"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$SOCIAL_JS" 2>/dev/null | tail -1
echo "=== ref social arbit v99 half done ==="
"""

CLONE_HALF = """#!/usr/bin/env bash
# social-clone-v99.sh — the CLONE half of the supplemental two-half
# census for the v99 pin's axes (the login card's SOCIAL-LOGIN ROW at 1280:
# the OR divider + the Google button). READ-ONLY passive navigation only.
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START.
# Runs inside with-server.sh (the :3200 parity server).
set -u
cd "$(dirname "$0")/../.."

""" + CENSUS_JS + """
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
"""

open("scripts/parity-probes/social-arbit-v99.sh", "w").write(REF_HALF)
open("scripts/parity-probes/social-clone-v99.sh", "w").write(CLONE_HALF)

# The md5 line-block contract: the census JS byte-identical across halves.
def block_md5(path, start_marker, end_marker):
    text = open(path).read()
    start = text.index(start_marker)
    end = text.index(end_marker, start) + len(end_marker)
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

rm, rn = block_md5("scripts/parity-probes/social-arbit-v99.sh",
                   'SOCIAL_JS="(async () => {', '})()"')
cm, cn = block_md5("scripts/parity-probes/social-clone-v99.sh",
                   'SOCIAL_JS="(async () => {', '})()"')
assert rm == cm, f"CENSUS BLOCK MISMATCH: {rm} vs {cm}"
print(f"block SOCIAL_JS md5 {rm} — {rn} lines — byte-identical across halves OK")

# The doubled-brace spot check (the v95 template-brace lesson).
for path in ("scripts/parity-probes/social-arbit-v99.sh",
             "scripts/parity-probes/social-clone-v99.sh"):
    text = open(path).read()
    start = text.index('SOCIAL_JS="(async () => {')
    end = text.index('})()"', start)
    body = text[start:end]
    dbl = re.findall(r"\{\{|\}\}", body)
    if dbl:
        raise SystemExit(f"DOUBLED BRACES in {path}: {len(dbl)} found")
    print(f"doubled-brace spot check {path}: clean")
print("halves written")
