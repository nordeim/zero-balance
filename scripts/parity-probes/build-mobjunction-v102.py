#!/usr/bin/env python3
"""Build mobjunction-arbit-v102.sh + mobjunction-clone-v102.sh — the
supplemental two-half census for the v102 pin's own axes (the NETWORTH
view's MOBILE junctions at 390: the summary card -> tablist gap [the
card's mb-8] + the tablist -> section-row gap [the TabsContent's mt-6]),
BUILT TWO-HALF FROM THE START (the v92..v101 lesson, the v94 nwsection +
v96 headrow + v97 listbox + v98 menu + v99 social + v100 nwjunction +
v101 spending precedents). The census JS block is extracted ONCE from
this builder and embedded byte-identically in both halves (the md5
line-block contract).

The F4 coverage-map finding this census serves: the v41 F2 pin (640)
walks the UPPER rhythm only (headerToCard 32 + cardToTablist 32 — at
640); the v69 F3 pin (390) walks the header row -> card gap only; the
v53 F1 pin (390) the tablist's own chrome; the v94 F4 pin (1280) the
section row's chrome + the row-to-group rhythm; the v100 F4 pin (1280)
the tablist->section junction — but the MOBILE junctions at 390 (the
card->tablist gap + the tablist->section gap) are NEVER pinned at ANY
viewport in ANY spec (zero specs assert any cardToTablist or
tablistToSection value at 390; the only cardToTablist assertion in the
suite is the v41 F2 pin's own at 640; the only junction assertion the
v100 pin's own at 1280). Both halves READ-ONLY (login + passive
navigation only — the v46 rule)."""
import hashlib, re

# The census JS — shared byte-identically across both halves.
# Heredoc-safe: no literal dollar sequences; no backticks.
# The LIABILITIES pass clicks the tab via the DOM .click() method — the
# parked pointer stays at (5,5) (no hover-revealed chrome mid-flight).
CENSUS_JS = """MJ_JS="(async () => {
  const out = { view: 'nw-junction-390-v102', docSW: document.documentElement.scrollWidth, vw: window.innerWidth };
  // THE SUMMARY CARD (the NW_CENSUS gradient-card finder, proven on both sides).
  const cards = [...document.querySelectorAll('main div, div')].filter(d => {
    const s = getComputedStyle(d);
    return d.getBoundingClientRect().height > 100 && d.getBoundingClientRect().width > 200
      && s.backgroundImage && s.backgroundImage.includes('linear-gradient');
  });
  const card = cards.find(c => c.getBoundingClientRect().width < 500) || cards[0];
  if (!card) return JSON.stringify({ err: 'no summary card' });
  const cr = card.getBoundingClientRect();
  out.card = { w: Math.round(cr.width), h: Math.round(cr.height), bottom: Math.round(cr.bottom) };
  // THE TABLIST (the Assets/Liabilities trigger row — role=tablist on both sides).
  const tablist = document.querySelector('[role=\"tablist\"]');
  if (!tablist) return JSON.stringify({ err: 'no tablist' });
  const tl = tablist.getBoundingClientRect();
  const tcs = getComputedStyle(tablist);
  out.tablist = { w: Math.round(tl.width), h: Math.round(tl.height), top: Math.round(tl.top), bottom: Math.round(tl.bottom), template: tcs.gridTemplateColumns, pad: tcs.padding };
  // THE JUNCTION 1: the summary card bottom -> tablist top gap (the card's mb-8 — never pinned at 390).
  out.cardToTablist = { gap: Math.round(tl.top - cr.bottom) };
  // THE SECTION ROW (the v94 finder: the Assets h2 -> block -> row).
  const h2 = [...document.querySelectorAll('main h2')].find(h => (h.textContent || '').trim() === 'Assets');
  if (!h2) return JSON.stringify({ err: 'no h2' });
  const block = h2.parentElement;
  const row = block ? block.parentElement : null;
  if (!block || !row) return JSON.stringify({ err: 'no block/row' });
  const rr = row.getBoundingClientRect();
  const rcs = getComputedStyle(row);
  out.sectionRow = { top: Math.round(rr.top), h: Math.round(rr.height), w: Math.round(rr.width), display: rcs.display, justify: rcs.justifyContent };
  // THE JUNCTION 2: the tablist bottom -> section row top gap (the ASSETS TabsContent's mt-6 — pinned at 1280 only, never at 390).
  out.tablistToSection = { gap: Math.round(rr.top - tl.bottom) };
  // THE LIABILITIES PASS: switch tabs with the FULL pointer event sequence (the reference's Radix-style trigger ignores a bare DOM click — the pointerdown family is load-bearing; the clone responds to both), settle, measure the SECOND panel's own junction (its own mt-6 — never pinned at ANY viewport in ANY spec).
  const trig = [...document.querySelectorAll('button[role=\"tab\"]')].find(b => (b.textContent || '').includes('Liabilities'));
  if (!trig) return JSON.stringify(Object.assign(out, { err: 'no liabilities trigger' }));
  const fire = (type) => trig.dispatchEvent(new PointerEvent(type, { bubbles: true, cancelable: true, pointerId: 1 }));
  fire('pointerdown'); trig.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true }));
  fire('pointerup'); trig.dispatchEvent(new MouseEvent('mouseup', { bubbles: true, cancelable: true }));
  trig.click();
  await new Promise(r => setTimeout(r, 900));
  const h2b = [...document.querySelectorAll('main h2')].find(h => (h.textContent || '').trim() === 'Liabilities');
  if (!h2b) return JSON.stringify(Object.assign(out, { err: 'no liabilities h2 after click' }));
  const blockB = h2b.parentElement;
  const rowB = blockB ? blockB.parentElement : null;
  if (!blockB || !rowB) return JSON.stringify(Object.assign(out, { err: 'no liabilities block/row' }));
  const rrb = rowB.getBoundingClientRect();
  const rcsb = getComputedStyle(rowB);
  out.liabSectionRow = { top: Math.round(rrb.top), h: Math.round(rrb.height), w: Math.round(rrb.width), display: rcsb.display, justify: rcsb.justifyContent };
  // THE JUNCTION 3: the tablist bottom -> the LIABILITIES section row top gap (the liabilities TabsContent's own mt-6 — the never-pinned axis).
  out.liabJunction = { gap: Math.round(rrb.top - tl.bottom) };
  out.docSWAfter = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"
"""

REF_HALF = """#!/usr/bin/env bash
# mobjunction-arbit-v102.sh — the REFERENCE half of the supplemental
# two-half census for the v102 pin's axes (the NETWORTH view's MOBILE
# junctions at 390: the card->tablist gap + the tablist->section gap).
# READ-ONLY (login + passive navigation only — the v46 rule). THE
# TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v101 lesson).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

""" + CENSUS_JS + """
export AGENT_BROWSER_SESSION="refmj102"
agent-browser set viewport 390 844 >/dev/null 2>&1
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
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$MJ_JS" 2>/dev/null | tail -1
echo "=== ref mobjunction arbit v102 half done ==="
"""

CLONE_HALF = """#!/usr/bin/env bash
# mobjunction-clone-v102.sh — the CLONE half of the supplemental two-half
# census for the v102 pin's axes (the NETWORTH view's MOBILE junctions at
# 390: the card->tablist gap + the tablist->section gap). READ-ONLY
# (login + passive navigation only — the v46 rule). THE TWO-HALF
# CONTROLLED FORM, BUILT FROM THE START. Runs inside with-server.sh (the
# :3200 parity server).
set -u
cd "$(dirname "$0")/../.."

""" + CENSUS_JS + """
MJ_JS="$MJ_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonemj102"
agent-browser set viewport 390 844 >/dev/null 2>&1
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
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$MJ_JS" 2>/dev/null | tail -1
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== clone mobjunction arbit v102 half done ==="
"""

open("scripts/parity-probes/mobjunction-arbit-v102.sh", "w").write(REF_HALF)
open("scripts/parity-probes/mobjunction-clone-v102.sh", "w").write(CLONE_HALF)

# The md5 line-block contract: the census JS byte-identical across halves.
def block_md5(path, start_marker, end_marker):
    text = open(path).read()
    start = text.index(start_marker)
    end = text.index(end_marker, start) + len(end_marker)
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

rm, rn = block_md5("scripts/parity-probes/mobjunction-arbit-v102.sh",
                   'MJ_JS="(async () => {', '})()"')
cm, cn = block_md5("scripts/parity-probes/mobjunction-clone-v102.sh",
                   'MJ_JS="(async () => {', '})()"')
assert rm == cm, f"CENSUS BLOCK MISMATCH: {rm} vs {cm}"
print(f"block MJ_JS md5 {rm} — {rn} lines — byte-identical across halves OK")

# The doubled-brace spot check (the v95 template-brace lesson).
for path in ("scripts/parity-probes/mobjunction-arbit-v102.sh",
             "scripts/parity-probes/mobjunction-clone-v102.sh"):
    text = open(path).read()
    start = text.index('MJ_JS="(async () => {')
    end = text.index('})()"', start)
    body = text[start:end]
    dbl = re.findall(r"\{\{|\}\}", body)
    if dbl:
        raise SystemExit(f"DOUBLED BRACES in {path}: {len(dbl)} found")
    print(f"doubled-brace spot check {path}: clean")
