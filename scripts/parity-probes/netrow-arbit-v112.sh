#!/usr/bin/env bash
# netrow-arbit-v112.sh — the ONE-SHOT both-sides arbitration census for the
# v112 F4 candidate: the NET ZERO BREAKDOWN card's NET-BALANCE FOOTER ROW
# INTERIOR at 1280 (the collapsed card — the row renders without any
# clicks, the v46 read-only rule holds). The never-pinned family (the
# coverage map: the v5-era 'Net Balance renders positive' test pins the
# AMOUNT color + the icon's existence only; the v42 F1 band census the
# divider's EXISTENCE + the band texts; the v43 F3/v44 F2b/v60 F2/v76 F4
# censuses the section/category/sub/item rows + the income-section chip —
# NEVER the net-balance row's own interior): the border-t wrapper + the
# row's flex chrome + the left block + the icon chip + the chip icon's
# glyph + the label typography + the value typography + the junction.
# Both sides POSITIVE balances (ref +$3,475.00 / clone +$2,065.00) — the
# sign-conditional color family lands orangeLight on BOTH.
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS (the v64 rule); no backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const D = String.fromCharCode(36);
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(
    (e) => (e.textContent || '').trim() === 'Net Zero Breakdown' && e.children.length === 0
  );
  if (!leaf) return 'no breakdown card';
  const card = leaf.closest('div[class*=rounded-2xl]');
  if (!card) return 'no card';
  const label = [...card.querySelectorAll('span')].find(
    (s) => (s.textContent || '').trim() === 'Net Balance' && s.children.length === 0
  );
  if (!label) return 'no net label';
  // The value: the signed money leaf in the card's footer zone — the LAST
  // money-like childless span in DOM order (the net row sits after every
  // section button; the section rows carry no bare money span — their
  // totals live inside BUTTON text).
  const moneyRe = new RegExp('^[-+]\\\\' + D + '[\\\\d,]+(\\\\.\\\\d+)?$');
  const moneyLeaves = [...card.querySelectorAll('span,p,div')].filter(
    (s) => s.children.length === 0 && moneyRe.test((s.textContent || '').trim())
  );
  const value = moneyLeaves.length ? moneyLeaves[moneyLeaves.length - 1] : null;
  if (!value) return 'no value leaf';
  // The row: the flex ancestor of the label that ALSO contains the value
  // (structural — never by class alone; the ref's left block may itself be
  // a flex div that would otherwise shadow the row).
  let row = label.parentElement;
  while (row && row !== card) {
    if (row.contains(value) && getComputedStyle(row).display === 'flex') break;
    row = row.parentElement;
  }
  if (!row || row === card) return 'no row';
  const leftBlock = label.parentElement;
  const chip = leftBlock.querySelector('span.rounded-lg, div.rounded-lg');
  const icon = chip ? chip.querySelector('svg') : null;
  const wrapper = row.parentElement;
  const wcs = wrapper ? getComputedStyle(wrapper) : null;
  const rcs = getComputedStyle(row);
  const rr = row.getBoundingClientRect();
  const lcs = getComputedStyle(leftBlock);
  const ccs = chip ? getComputedStyle(chip) : null;
  const cr = chip ? chip.getBoundingClientRect() : null;
  const ics = icon ? getComputedStyle(icon) : null;
  const ir = icon ? icon.getBoundingClientRect() : null;
  const lbcs = getComputedStyle(label);
  const lr = label.getBoundingClientRect();
  const vcs = value ? getComputedStyle(value) : null;
  const chipCy = cr ? Math.round(cr.top + cr.height / 2) : null;
  const rowCy = Math.round(rr.top + rr.height / 2);
  const labelCy = Math.round(lr.top + lr.height / 2);
  return JSON.stringify({
    docSW: window.innerWidth,
    row: { display: rcs.display, align: rcs.alignItems, justify: rcs.justifyContent, h: Math.round(rr.height), w: Math.round(rr.width) },
    leftBlock: { display: lcs.display, align: lcs.alignItems, gap: lcs.gap, h: Math.round(leftBlock.getBoundingClientRect().height) },
    chip: ccs ? { w: Math.round(cr.width), h: Math.round(cr.height), radius: ccs.borderRadius, bg: ccs.backgroundColor } : 'no chip',
    icon: ics ? {
      w: Math.round(ir.width), h: Math.round(ir.height), color: ics.color,
      glyphSig: (icon.innerHTML || '').replace(/\s+/g, ' ').slice(0, 110),
      viewBox: icon.getAttribute('viewBox'),
    } : 'no icon',
    label: { text: (label.textContent || '').trim(), fs: lbcs.fontSize, fw: lbcs.fontWeight, color: lbcs.color, h: Math.round(lr.height) },
    value: vcs ? { fs: vcs.fontSize, fw: vcs.fontWeight, color: vcs.color, h: Math.round(value.getBoundingClientRect().height) } : 'no value',
    wrapper: wcs ? { mt: wcs.marginTop, pt: wcs.paddingTop, borderTopW: wcs.borderTopWidth, borderTopC: wcs.borderTopColor } : 'no wrapper',
    junction: { chipCy: chipCy, rowCy: rowCy, labelCy: labelCy, chipToRowCenter: chipCy !== null ? Math.abs(chipCy - rowCy) : null, labelToRowCenter: Math.abs(labelCy - rowCy) },
  });
})()"

echo "=== REFERENCE side (1280, /dashboard collapsed card) ==="
export AGENT_BROWSER_SESSION="refnr112"
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
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- net-row census:"
CENSUS="$CENSUS_JS" agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /dashboard collapsed card) ==="
cd "$(dirname "$0")/../.."
CENSUS_EXPORT="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export CENSUS_JS="$CENSUS_EXPORT"
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
agent-browser open "http://localhost:3200/dashboard" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- net-row census:"
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== netrow arbit v112 done ==="
