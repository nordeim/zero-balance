#!/usr/bin/env bash
# nwjunction-clone-v100.sh — the CLONE half of the supplemental two-half
# census for the v100 pin's axes (the NETWORTH view's TABLIST->SECTION-ROW
# junction at 1280). READ-ONLY (login + passive navigation only — the v46
# rule). THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START.
# Runs inside with-server.sh (the :3200 parity server).
set -u
cd "$(dirname "$0")/../.."

NWJ_JS="(async () => {
  const out = { view: 'nw-junction-1280-v100', docSW: document.documentElement.scrollWidth, vw: window.innerWidth };
  // THE TABLIST (the Assets/Liabilities trigger row — role=tablist on both sides).
  const tablist = document.querySelector('[role="tablist"]');
  if (!tablist) return JSON.stringify({ err: 'no tablist' });
  const tl = tablist.getBoundingClientRect();
  const tcs = getComputedStyle(tablist);
  out.tablist = { w: Math.round(tl.width), h: Math.round(tl.height), bottom: Math.round(tl.bottom), template: tcs.gridTemplateColumns, maxW: tcs.maxWidth, pad: tcs.padding };
  // THE SECTION ROW (the v94 finder: the Assets h2 -> block -> row).
  const h2 = [...document.querySelectorAll('main h2')].find(h => (h.textContent || '').trim() === 'Assets');
  if (!h2) return JSON.stringify({ err: 'no h2' });
  const block = h2.parentElement;
  const row = block ? block.parentElement : null;
  if (!block || !row) return JSON.stringify({ err: 'no block/row' });
  const rr = row.getBoundingClientRect();
  const rcs = getComputedStyle(row);
  out.sectionRow = { top: Math.round(rr.top), h: Math.round(rr.height), w: Math.round(rr.width), display: rcs.display, justify: rcs.justifyContent };
  // THE JUNCTION: the tablist bottom -> section row top gap (the TabsContent's mt-6 — the never-pinned axis).
  out.junction = { gap: Math.round(rr.top - tl.bottom) };
  // The first type-group continuation (the v94 row-to-group rhythm re-measured in the junction context).
  const group = row.nextElementSibling;
  const g3 = group ? group.querySelector('h3') : null;
  out.groupH3 = g3 ? { fs: getComputedStyle(g3).fontSize, fw: getComputedStyle(g3).fontWeight, mb: getComputedStyle(g3).marginBottom } : null;
  out.rowToGroup = group ? { gap: Math.round(group.getBoundingClientRect().top - rr.bottom) } : null;
  return JSON.stringify(out);
})()"

NWJ_JS="$NWJ_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonenwj100"
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
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$NWJ_JS" 2>/dev/null | tail -1
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== clone nwjunction arbit v100 half done ==="
