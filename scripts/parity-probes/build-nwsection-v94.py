#!/usr/bin/env python3
"""build-nwsection-v94.py — the supplemental two-half census for the v94
pin's own axes (the networth view's SECTION-HEADER row family at 1280),
BUILT TWO-HALF from the start (the v93 totalcard precedent): the census
JS block is embedded byte-identically across the reference half
(nwsection-arbit-v94.sh) and the clone half (nwsection-clone-v94.sh)."""
import hashlib

CENSUS_JS = r"""CENSUS_JS="(async () => {
  const out = { view: 'nw-section-1280-v94' };
  const h2 = [...document.querySelectorAll('main h2')].find(h => (h.textContent || '').trim() === 'Assets');
  if (!h2) return JSON.stringify({ err: 'no h2' });
  const block = h2.parentElement;
  const row = block ? block.parentElement : null;
  if (!block || !row) return JSON.stringify({ err: 'no block/row' });
  const rcs = getComputedStyle(row);
  const rr = row.getBoundingClientRect();
  out.row = { display: rcs.display, align: rcs.alignItems, justify: rcs.justifyContent, h: Math.round(rr.height), w: Math.round(rr.width) };
  const h2cs = getComputedStyle(h2);
  const h2r = h2.getBoundingClientRect();
  out.h2 = { fs: h2cs.fontSize, fw: h2cs.fontWeight, lh: h2cs.lineHeight, color: h2cs.color, mb: h2cs.marginBottom, h: Math.round(h2r.height) };
  const countP = [...block.children].find(c => c.tagName === 'P');
  if (countP) {
    const s = getComputedStyle(countP);
    out.countP = { fs: s.fontSize, fw: s.fontWeight, lh: s.lineHeight, color: s.color };
    out.countText = (countP.textContent || '').trim();
  }
  const br = block.getBoundingClientRect();
  out.block = { w: Math.round(br.width), h: Math.round(br.height) };
  const addBtn = [...row.querySelectorAll('button')].find(b => /Add Asset/i.test(b.textContent || ''));
  if (addBtn) {
    const s = getComputedStyle(addBtn);
    const r = addBtn.getBoundingClientRect();
    out.addBtn = { h: Math.round(r.height), w: Math.round(r.width), pad: s.padding, radius: s.borderRadius, fs: s.fontSize, fw: s.fontWeight, color: s.color, bg: (s.backgroundImage || '').replace(/\s+/g, ' ').slice(0, 90) };
    const icon = addBtn.querySelector('svg');
    out.addBtnIcon = icon ? { w: Math.round(icon.getBoundingClientRect().width), h: Math.round(icon.getBoundingClientRect().height) } : null;
  }
  const group = row.nextElementSibling;
  if (group) {
    const gcs = getComputedStyle(group);
    out.groupGap = { mt: gcs.marginTop, delta: Math.round(group.getBoundingClientRect().top - rr.bottom) };
    const g3 = group.querySelector('h3');
    if (g3) {
      const s = getComputedStyle(g3);
      out.groupH3 = { fs: s.fontSize, fw: s.fontWeight, lh: s.lineHeight, mb: s.marginBottom };
      out.groupH3Text = (g3.textContent || '').trim();
    }
  }
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()""" + '"'

REF_HALF = """#!/usr/bin/env bash
# nwsection-arbit-v94.sh — the ONE-SHOT census for the v94 pin's own
# axes, REFERENCE half (the v87..v93 supplemental precedent, BUILT
# TWO-HALF from the start): the NETWORTH view's SECTION-HEADER row
# family at desktop 1280 — the row's flex chrome, the "Assets" h2's
# typography (never pinned at ANY viewport), the count subtitle P's
# typography (visibility-only elsewhere), the Add Asset button's chrome
# on this row, the row-to-group rhythm. The reference's own populated
# Assets panel ("1 items · D25,000") — READ-ONLY (login + passive
# navigation only — the v46 rule). Heredoc-safe: no literal dollar
# sequences; no backticks.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

""" + CENSUS_JS + """

echo "########## REFERENCE SIDE (the populated Assets panel — read-only) ##########"
export AGENT_BROWSER_SESSION="refnwsec94"
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF networth section-header census at 1280 ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== ref nwsection v94 half done ==="
"""

CLONE_HALF = """#!/usr/bin/env bash
# nwsection-clone-v94.sh — the ONE-SHOT census for the v94 pin's own
# axes, CLONE half (the v87..v93 supplemental precedent, BUILT TWO-HALF
# from the start): the NETWORTH view's SECTION-HEADER row family at
# desktop 1280 — the same axes as the reference half, the census JS
# byte-identical (the md5 line-block contract). Runs inside with-server
# (the :3200 parity server); the clone's seeded Assets panel ("3 items ·
# D65,300") — READ-ONLY (no fixture writes; the v46 rule).
set -u
cd "$(dirname "$0")/../.."

""" + CENSUS_JS + """

echo "########## CLONE SIDE (the seeded Assets panel — read-only) ##########"
CENSUS_JS="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonenwsec94"
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
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== CLONE networth section-header census at 1280 ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF

echo ""
echo "=== seedcheck (env -u DATABASE_URL — the documented pollution discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs
echo "=== clone nwsection v94 half done ==="
"""

BASE = "scripts/parity-probes/"
open(BASE + "nwsection-arbit-v94.sh", "w").write(REF_HALF)
open(BASE + "nwsection-clone-v94.sh", "w").write(CLONE_HALF)

# The md5 line-block contract across the halves.
def census_md5(path):
    text = open(path).read()
    start = text.index('CENSUS_JS="(async () => {')
    end = text.index('})()"', start) + len('})()"')
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

rm, rn = census_md5(BASE + "nwsection-arbit-v94.sh")
cm, cn = census_md5(BASE + "nwsection-clone-v94.sh")
assert rm == cm, f"CENSUS MISMATCH: {rm} vs {cm}"
print(f"census JS md5 {rm} — {rn} lines — byte-identical across halves OK")
print("nwsection-arbit-v94.sh + nwsection-clone-v94.sh built")
