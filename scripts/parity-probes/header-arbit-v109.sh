#!/usr/bin/env bash
# header-arbit-v109.sh — the ONE-SHOT both-sides census for the v109 pin's
# own axes: the ITEMS views' DESKTOP 1280 page-header row INTERIOR family
# (the income + expenses variants — the family the v65 pin holds on the
# SAVINGS variant only; the v92 family-extension pattern).
# The never-pinned family (the coverage map: the v65 pin holds the row +
# chip + h1 + subtitle + Add button on /savings at 1280; the v52 pin the
# MOBILE 390 stacked state on /income; the tokens G2 pin the Add button's
# 16px icon + shadow layers on /income; NEVER pinned at ANY viewport: the
# header row's computed chrome on the INCOME/EXPENSES variants at 1280,
# the LEFT BLOCK's interior [flex/center/gap 12 — the chip-to-title
# junction, never pinned on ANY variant], the chip icon's computed chrome,
# the h1's lh at 1280 on income/expenses, the subtitle chrome at 1280 on
# income/expenses, and the Add button's full chrome [w/h/radius/pad/fs/fw/
# color/bg] on income/expenses at 1280).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

HDR_CENSUS="(async () => {
  // the Add button: the topmost main button whose text starts with 'Add'
  // (the v65 finder form — the header row walks UP from it to the container
  // that also holds the visible h1)
  const addBtn = [...document.querySelectorAll('main button')].find((b) =>
    (b.textContent || '').trim().startsWith('Add') && b.getBoundingClientRect().top < 200);
  if (!addBtn) return JSON.stringify({ found: false, why: 'no add button' });
  let row = null;
  let cur = addBtn.parentElement;
  for (let i = 0; i < 6 && cur; i++) {
    if (cur.querySelector('h1') && cur !== addBtn) { row = cur; break; }
    cur = cur.parentElement;
  }
  if (!row) return JSON.stringify({ found: false, why: 'no header row' });
  const rcs = getComputedStyle(row);
  const rr = row.getBoundingClientRect();
  // the left block: the row's first element child (the chip + title stack)
  const left = row.firstElementChild;
  const lcs = left ? getComputedStyle(left) : null;
  const lr = left ? left.getBoundingClientRect() : null;
  // the chip: the left block's first element child (the 48x48 gradient tile)
  const chip = left ? left.firstElementChild : null;
  const ccs = chip ? getComputedStyle(chip) : null;
  const cr = chip ? chip.getBoundingClientRect() : null;
  const chipIcon = chip ? chip.querySelector('svg') : null;
  const cic = chipIcon ? getComputedStyle(chipIcon) : null;
  const cir = chipIcon ? chipIcon.getBoundingClientRect() : null;
  // the h1: the row's visible h1 (the reference carries a hidden zero-size
  // app-shell h1 first in the DOM — the v65 lesson: filter to the VISIBLE one)
  const h1 = [...row.querySelectorAll('h1')].find((h) => h.getBoundingClientRect().height > 0);
  const h1cs = h1 ? getComputedStyle(h1) : null;
  // the subtitle P: the h1's sibling P inside the title block
  const titleBlock = h1 ? h1.parentElement : null;
  const sub = titleBlock ? titleBlock.querySelector('p') : null;
  const scs = sub ? getComputedStyle(sub) : null;
  // the Add button's own chrome + its plus icon
  const abcs = getComputedStyle(addBtn);
  const abr = addBtn.getBoundingClientRect();
  const plusIcon = addBtn.querySelector('svg');
  const pic = plusIcon ? getComputedStyle(plusIcon) : null;
  const pir = plusIcon ? plusIcon.getBoundingClientRect() : null;
  return JSON.stringify({
    docSW: document.documentElement.scrollWidth,
    row: { display: rcs.display, justify: rcs.justifyContent, align: rcs.alignItems, gap: rcs.columnGap, mb: rcs.marginBottom, h: Math.round(rr.height), childCount: row.children.length },
    left: lcs ? { display: lcs.display, align: lcs.alignItems, gap: lcs.columnGap, h: Math.round(lr.height), childCount: left.children.length } : null,
    chip: ccs ? { w: Math.round(cr.width), h: Math.round(cr.height), radius: ccs.borderRadius, bg: ccs.backgroundImage } : null,
    chipIcon: cic ? { w: Math.round(cir.width), h: Math.round(cir.height), color: cic.color } : null,
    h1: h1cs ? { fs: h1cs.fontSize, fw: h1cs.fontWeight, lh: h1cs.lineHeight, color: h1cs.color } : null,
    subtitle: scs ? { fs: scs.fontSize, fw: scs.fontWeight, color: scs.color } : null,
    addBtn: { text: (addBtn.textContent || '').trim().slice(0, 20), w: Math.round(abr.width), h: Math.round(abr.height), radius: abcs.borderRadius, pad: abcs.padding, fs: abcs.fontSize, fw: abcs.fontWeight, color: abcs.color, bg: abcs.backgroundImage },
    addIcon: pic ? { w: Math.round(pir.width), h: Math.round(pir.height), mr: pic.marginRight } : null,
  });
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="hdrref109"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {
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
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
echo "--- ref /income:"
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$HDR_CENSUS" 2>/dev/null | tail -1
echo "--- ref /expenses:"
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$HDR_CENSUS" 2>/dev/null | tail -1

echo "=== CLONE side (1280) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="hdrclone109"
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
echo "--- clone /income:"
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$HDR_CENSUS" 2>/dev/null | tail -1
echo "--- clone /expenses:"
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$HDR_CENSUS" 2>/dev/null | tail -1
EOF
echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== header arbit v109 done ==="
