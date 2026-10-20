#!/usr/bin/env python3
"""Build spending-arbit-v101.sh + spending-clone-v101.sh — the supplemental
two-half census for the v101 pin's own axes (the DASHBOARD's
spending+guidelines 2-COL ROW at 1280: the row's own grid chrome — the
lg:grid-cols-2 template/column-gap/width — plus the LEFT column's
Spending Breakdown card's box chrome + header block + body-pad contract),
BUILT TWO-HALF FROM THE START (the v92..v100 lesson, the v94 nwsection +
v96 headrow + v97 listbox + v98 menu + v99 social + v100 nwjunction
precedents). The census JS block is extracted ONCE from this builder and
embedded byte-identically in both halves (the md5 line-block contract).

The F4 coverage-map finding this census serves: the v61 F2 pin walks the
row ONLY for rowH 656 (the stretch contract) + the guidelines card's own
box; the v77 pin the guidelines card's interior text; the v83 F4 pin the
card-level cross-row gap — but the ROW'S OWN GRID CHROME (the
"468px 468px" template, the 24px column gap, the 960 width, the two
children's widths) and the SPENDING CARD'S OWN BOX + HEADER (the card
radius/border/bg/shadow, the title's typography, the subtitle's chrome,
the title->subtitle rhythm, the body's pt-0 contract) are NEVER pinned at
ANY viewport in ANY spec (grep-verified: zero "468px 468px" matches, zero
spending-card radius/border assertions, the subtitle only
visibility-asserted). Both halves READ-ONLY (login + passive navigation
only — the v46 rule)."""
import hashlib, re

# The census JS — shared byte-identically across both halves.
# Heredoc-safe: no literal dollar sequences; no backticks.
CENSUS_JS = """SPEND_JS="(async () => {
  const out = { view: 'spending-row-1280-v101', docSW: document.documentElement.scrollWidth, vw: window.innerWidth };
  // THE SPENDING CARD (the leaf title -> the bordered card walk — the v61
  // F2 pattern: shadow + radius + a <p> descendant).
  const title = [...document.querySelectorAll('h1,h2,h3,h4,div,span,p')].find(
    (e) => (e.textContent || '').trim() === 'Spending Breakdown' && e.children.length === 0
  );
  if (!title) return JSON.stringify({ err: 'no title' });
  let card = title;
  while (card.parentElement) {
    const cs = getComputedStyle(card);
    if (cs.boxShadow !== 'none' && cs.borderRadius !== '0px' && card.querySelector('p')) break;
    card = card.parentElement;
  }
  const csC = getComputedStyle(card);
  const rC = card.getBoundingClientRect();
  out.card = { w: Math.round(rC.width), h: Math.round(rC.height), radius: csC.borderRadius, border: csC.borderTopColor, bg: csC.backgroundColor, shadow: csC.boxShadow };
  // THE HEADER BLOCK (the title's parent) + the subtitle.
  const header = title.parentElement;
  const csH = getComputedStyle(header);
  const rT = title.getBoundingClientRect();
  const subtitle = header ? header.querySelector('p') : null;
  const rS = subtitle ? subtitle.getBoundingClientRect() : null;
  out.header = { pad: csH.padding };
  out.title = { fs: getComputedStyle(title).fontSize, fw: getComputedStyle(title).fontWeight, color: getComputedStyle(title).color, lh: getComputedStyle(title).lineHeight, tracking: getComputedStyle(title).letterSpacing };
  out.subtitle = subtitle && rS ? { text: (subtitle.textContent || '').trim(), fs: getComputedStyle(subtitle).fontSize, fw: getComputedStyle(subtitle).fontWeight, color: getComputedStyle(subtitle).color, lh: getComputedStyle(subtitle).lineHeight, top: Math.round(rS.top - rT.bottom) } : null;
  // THE BODY (the card's non-header child — the p-6 pt-0 contract).
  const body = [...card.children].find((c) => c !== header);
  out.body = body ? { pad: getComputedStyle(body).padding } : null;
  // THE ROW (the ancestor 2-col grid — the v61 F2 walk).
  let row = card.parentElement;
  while (row) {
    const cls = (row.className || '').toString();
    if (/grid-cols-2/.test(cls) && row.children.length === 2) break;
    row = row.parentElement;
  }
  if (!row) return JSON.stringify({ err: 'no row' });
  const csR = getComputedStyle(row);
  const rR = row.getBoundingClientRect();
  out.row = { display: csR.display, template: csR.gridTemplateColumns, colGap: csR.columnGap, w: Math.round(rR.width), h: Math.round(rR.height) };
  // THE TWO CHILDREN (the spending card + the guidelines wrapper).
  const kids = [...row.children].map((k) => {
    const kr = k.getBoundingClientRect();
    return { w: Math.round(kr.width), h: Math.round(kr.height), display: getComputedStyle(k).display };
  });
  out.children = kids;
  return JSON.stringify(out);
})()"
"""

REF_HALF = """#!/usr/bin/env bash
# spending-arbit-v101.sh — the REFERENCE half of the supplemental two-half
# census for the v101 pin's axes (the DASHBOARD's spending+guidelines
# 2-col row's grid chrome + the Spending Breakdown card's box/header at
# 1280). READ-ONLY (login + passive navigation only — the v46 rule). THE
# TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v100 lesson).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

""" + CENSUS_JS + """
export AGENT_BROWSER_SESSION="refspend101"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$SPEND_JS" 2>/dev/null | tail -1
echo "=== ref spending arbit v101 half done ==="
"""

CLONE_HALF = """#!/usr/bin/env bash
# spending-clone-v101.sh — the CLONE half of the supplemental two-half
# census for the v101 pin's axes (the DASHBOARD's spending+guidelines
# 2-col row's grid chrome + the Spending Breakdown card's box/header at
# 1280). READ-ONLY (login + passive navigation only — the v46 rule). THE
# TWO-HALF CONTROLLED FORM, BUILT FROM THE START.
# Runs inside with-server.sh (the :3200 parity server).
set -u
cd "$(dirname "$0")/../.."

""" + CENSUS_JS + """
SPEND_JS="$SPEND_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonespend101"
agent-browser set viewport 1280 800 >/dev/null 2>&1
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$SPEND_JS" 2>/dev/null | tail -1
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== clone spending arbit v101 half done ==="
"""

open("scripts/parity-probes/spending-arbit-v101.sh", "w").write(REF_HALF)
open("scripts/parity-probes/spending-clone-v101.sh", "w").write(CLONE_HALF)

# The md5 line-block contract: the census JS byte-identical across halves.
def block_md5(path, start_marker, end_marker):
    text = open(path).read()
    start = text.index(start_marker)
    end = text.index(end_marker, start) + len(end_marker)
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

rm, rn = block_md5("scripts/parity-probes/spending-arbit-v101.sh",
                   'SPEND_JS="(async () => {', '})()"')
cm, cn = block_md5("scripts/parity-probes/spending-clone-v101.sh",
                   'SPEND_JS="(async () => {', '})()"')
assert rm == cm, f"CENSUS BLOCK MISMATCH: {rm} vs {cm}"
print(f"block SPEND_JS md5 {rm} — {rn} lines — byte-identical across halves OK")

# The doubled-brace spot check (the v95 template-brace lesson).
for path in ("scripts/parity-probes/spending-arbit-v101.sh",
             "scripts/parity-probes/spending-clone-v101.sh"):
    text = open(path).read()
    start = text.index('SPEND_JS="(async () => {')
    end = text.index('})()"', start)
    body = text[start:end]
    dbl = re.findall(r"\{\{|\}\}", body)
    if dbl:
        raise SystemExit(f"DOUBLED BRACES in {path}: {len(dbl)} found")
    print(f"doubled-brace spot check {path}: clean")
