#!/usr/bin/env bash
# topbar-arbit-v108.sh — the ONE-SHOT both-sides census for the v108 pin's
# own axes: the MOBILE TOPBAR's interior junction family at 390x844 (the
# dashboard surface — the app-shell chrome shared by both mobile twins).
# The never-pinned family (the coverage map: the v7 G5 pin holds the
# burger's 28x28 box + the 16px icon color; the mobile-layout pin the
# topbar's box GEOMETRY [h <= 65, x 0, full width] + the icon CLASS + the
# brand CLASS; NEVER pinned at ANY viewport: the header's own chrome
# [pad 24/16, border-b 1px rgb(229,231,227), bg white], the row's flex
# chrome [flex/center/gap 16], the burger's POSITION [the px-6/py-4
# rhythm], and the brand h1's COMPUTED chrome [fs 20px/fw 700/
# forestDark] — the class-only assertions never pin the computed values).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

TB_CENSUS="(async () => {
  // the burger: the panel-left toggle (the v7 G5 finder — the panel-left
  // class is the reference's own glyph, byte-identical both sides per this
  // cycle's base44-fab-arbit-v108.sh)
  const btn = [...document.querySelectorAll('button')].find((b) =>
    (b.querySelector('svg') ? b.querySelector('svg').getAttribute('class') : '').includes('panel-left'));
  if (!btn) return JSON.stringify({ found: false });
  const header = btn.closest('header');
  if (!header) return JSON.stringify({ found: true, headerFound: false });
  const row = header.firstElementChild;
  const hr = header.getBoundingClientRect();
  const hcs = getComputedStyle(header);
  const rcs = row ? getComputedStyle(row) : null;
  const rr = row ? row.getBoundingClientRect() : null;
  const br = btn.getBoundingClientRect();
  const bcs = getComputedStyle(btn);
  const icon = btn.querySelector('svg');
  const ics = icon ? getComputedStyle(icon) : null;
  const irr = icon ? icon.getBoundingClientRect() : null;
  const brand = row ? row.lastElementChild : null;
  const bc = brand ? getComputedStyle(brand) : null;
  return JSON.stringify({
    docSW: document.documentElement.scrollWidth,
    header: { w: Math.round(hr.width), h: Math.round(hr.height), padX: hcs.paddingLeft, padY: hcs.paddingTop, borderBW: hcs.borderBottomWidth, borderBColor: hcs.borderBottomColor, bg: hcs.backgroundColor },
    row: rcs ? { display: rcs.display, align: rcs.alignItems, gap: rcs.columnGap, h: Math.round(rr.height), childCount: row.children.length } : null,
    burger: { x: Math.round(br.x), y: Math.round(br.y), w: Math.round(br.width), h: Math.round(br.height), radius: bcs.borderRadius },
    icon: ics ? { w: Math.round(irr.width), h: Math.round(irr.height), color: ics.color } : null,
    brand: bc ? { text: (brand.textContent || '').trim(), fs: bc.fontSize, fw: bc.fontWeight, lh: bc.lineHeight, color: bc.color } : null,
  });
})()"

echo "=== REFERENCE side (390, /) ==="
export AGENT_BROWSER_SESSION="tbarref108"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$TB_CENSUS" 2>/dev/null | tail -1

echo "=== CLONE side (390, /) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="tbarclone108"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$TB_CENSUS" 2>/dev/null | tail -1
EOF
echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== topbar arbit v108 done ==="
