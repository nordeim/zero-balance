#!/usr/bin/env bash
# nav-arbit-v110.sh — the ONE-SHOT both-sides census for the v110 pin's
# own axes: the rail's NAV-BLOCK INTERIOR family at 1280 (the block BELOW
# the v104-pinned brand-block — the family the v110 savings-pair evidence
# walked past on every full-page shot).
# The never-pinned family (the coverage map: the session-5 pins hold the
# link BOX {h 32/pad 10px 12px/columnGap 12/fs 14/radius 8} on links[0]
# ONLY + the class-string hovers; the v8 G2a pin the inactive link COLOR;
# the v36 S3 bands the links' Y positions; the v104 pin the brand-block
# ABOVE; the v103 pin the user-footer BELOW; NEVER pinned at ANY viewport
# in ANY spec: the 'Navigation' section label's computed chrome {h/fs/fw/
# textTransform/letterSpacing/color/pad}, the UL's {flex/column/gap/w},
# the LI's {position/mb/h}, the nav ICON's computed {w/h} (the w-4 SUBSTRING
# never asserted; zero icon-w/h assertions across all 24 specs), the label
# SPAN's truncate family {overflow/textOverflow/whiteSpace}, and the
# ACTIVE rail link's computed chrome {bg image/color/fw} at desktop).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

NAV_CENSUS="(async () => {
  // the rail: the v103 fallback chain (the clone renders an aside; the
  // reference's rail is a DIV)
  const rail = document.querySelector('aside') || [...document.querySelectorAll('nav,aside,div')].find(d => {
    const r = d.getBoundingClientRect();
    return r.width > 180 && r.width < 320 && r.height > 700 && r.left === 0;
  });
  if (!rail) return JSON.stringify({ found: false, why: 'no rail' });
  // the nav block: the reference renders NO nav landmark (the documented
  // no-landmark bug) — walk STRUCTURALLY: the rail's ul with 5 anchor
  // children; the section label = the ul wrapper's previous element
  // sibling (the shadcn group-label row); fallback = the rail's only
  // childless uppercase div
  const ul = [...rail.querySelectorAll('ul')].find(u => {
    const r = u.getBoundingClientRect();
    return u.querySelectorAll('a').length >= 4 && r.width > 100 && r.height > 100;
  });
  if (!ul) return JSON.stringify({ found: false, why: 'no ul' });
  const wrap = ul.parentElement;
  let label = wrap ? wrap.previousElementSibling : null;
  if (!label || label.children.length > 0 || (label.textContent || '').trim().length === 0 || label.textContent.trim().length > 20) {
    label = [...rail.querySelectorAll('div')].find(d => {
      const cs2 = getComputedStyle(d);
      const r2 = d.getBoundingClientRect();
      return cs2.textTransform === 'uppercase' && !d.children.length && (d.textContent || '').trim().length > 0 && (d.textContent || '').trim().length <= 20 && r2.height > 0 && r2.height <= 40;
    }) || null;
  }
  const labelIcon = label ? label.querySelector('svg') : null;
  const labelFirst = label ? label.firstElementChild : null;
  const li = ul.firstElementChild;
  const link = li ? li.querySelector('a') : null;
  const span = link ? link.querySelector('span') : null;
  const icon = link ? link.querySelector('svg') : null;
  // the ACTIVE link: aria-current 'page' OR the gradient bg OR the /savings
  // text (the reference's own marker read live — no assumed markup)
  const activeLink = [...ul.querySelectorAll('a')].find(a => a.getAttribute('aria-current') === 'page')
    || [...ul.querySelectorAll('a')].find(a => {
      const g = getComputedStyle(a).backgroundImage;
      return g && g !== 'none' && g.includes('gradient');
    })
    || [...ul.querySelectorAll('a')].find(a => (a.textContent || '').trim() === 'Savings');
  const lcs = label ? getComputedStyle(label) : null;
  const ucs = getComputedStyle(ul);
  const lic = li ? getComputedStyle(li) : null;
  const kcs = link ? getComputedStyle(link) : null;
  const scs = span ? getComputedStyle(span) : null;
  const ics = icon ? getComputedStyle(icon) : null;
  const ir = icon ? icon.getBoundingClientRect() : null;
  const acs = activeLink ? getComputedStyle(activeLink) : null;
  const links = [...ul.querySelectorAll('a')];
  return JSON.stringify({
    docSW: document.documentElement.scrollWidth,
    label: label && lcs ? {
      text: (label.textContent || '').trim().slice(0, 16),
      h: Math.round(label.getBoundingClientRect().height),
      fs: lcs.fontSize, fw: lcs.fontWeight,
      transform: lcs.textTransform, spacing: lcs.letterSpacing,
      color: lcs.color, pad: lcs.padding, radius: lcs.borderRadius,
      display: lcs.display, align: lcs.alignItems,
      childCount: label.children.length,
      firstChildTag: labelFirst ? labelFirst.tagName : null,
      iconCount: label ? label.querySelectorAll('svg').length : null,
    } : null,
    ul: { display: ucs.display, dir: ucs.flexDirection, gap: ucs.rowGap, w: Math.round(ul.getBoundingClientRect().width), childCount: ul.children.length },
    li: li && lic ? { position: lic.position, mb: lic.marginBottom, h: Math.round(li.getBoundingClientRect().height) } : null,
    linkBox: link && kcs ? {
      text: (link.textContent || '').trim().slice(0, 12),
      h: Math.round(link.getBoundingClientRect().height),
      pad: kcs.padding, columnGap: kcs.columnGap,
      fs: kcs.fontSize, fw: kcs.fontWeight, radius: kcs.borderRadius,
      display: kcs.display, align: kcs.alignItems,
    } : null,
    icon: icon && ics && ir ? { w: Math.round(ir.width), h: Math.round(ir.height) } : null,
    span: span && scs ? { fs: scs.fontSize, overflow: scs.overflow, textOverflow: scs.textOverflow, whiteSpace: scs.whiteSpace } : null,
    active: activeLink && acs ? {
      text: (activeLink.textContent || '').trim().slice(0, 12),
      bg: acs.backgroundImage, color: acs.color, fw: acs.fontWeight,
      h: Math.round(activeLink.getBoundingClientRect().height),
    } : null,
    linkCount: links.length,
    iconCount: ul.querySelectorAll('a svg').length,
  });
})()"

echo "=== REFERENCE side (1280, /savings) ==="
export AGENT_BROWSER_SESSION="navref110"
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
echo "--- ref /savings nav block:"
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$NAV_CENSUS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /savings) ==="
cd "$(dirname "$0")/../.."
NAV_CENSUS_JS="$NAV_CENSUS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="navclone110"
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
echo "--- clone /savings nav block:"
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$NAV_CENSUS_JS" 2>/dev/null | tail -1
EOF

echo "=== nav arbit v110 done ==="
