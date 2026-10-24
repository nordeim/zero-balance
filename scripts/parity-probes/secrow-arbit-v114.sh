#!/usr/bin/env bash
# secrow-arbit-v114.sh — the ONE-SHOT both-sides DOM census for the v114
# F4 candidate: the NETWORTH section-row INTERIOR family at 390 (the v94
# pin's never-pinned mobile twin — the family every mobile junction census
# walked past on its way to the junction arithmetic). The axes:
#   the row's own flex chrome {display/align/justify/h} (the v102 pin holds
#   display/justify/h for the junction context — the ALIGN axis never
#   pinned), the h2 "Assets" typography {fs/fw/lh/color/mb/h}, the count
#   P's chrome {fs/fw/lh/color}, the left block's height, the Add Asset
#   button's full chrome {h/w/pad/radius/fs/fw/color/bg/icon}, the
#   row-to-group rhythm, and the group h3's chrome.
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors.
# The pin's axes stay DATA-INDEPENDENT: the h2 "Assets" a fixed string; the
# count P pinned by its CHROME (the text data-coupled, never pinned); the
# block's WIDTH excluded (the v82 labelBlock convention); the addBtn's
# x/y position arithmetic unpinned (the v107 xInRow discipline).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

SECROW_JS="(async () => {
  const h2 = [...document.querySelectorAll('main h2')].find(h => (h.textContent || '').trim() === 'Assets');
  if (!h2) return JSON.stringify({ secrow: 'no Assets h2' });
  const block = h2.parentElement;
  const row = block ? block.parentElement : null;
  if (!block || !row) return JSON.stringify({ secrow: 'no block/row' });
  const rcs = getComputedStyle(row);
  const rr = row.getBoundingClientRect();
  const h2cs = getComputedStyle(h2);
  const h2r = h2.getBoundingClientRect();
  const countP = [...block.children].find(c => c.tagName === 'P');
  const pcs = countP ? getComputedStyle(countP) : null;
  const br = block.getBoundingClientRect();
  const addBtn = [...row.querySelectorAll('button')].find(b => /Add Asset/i.test(b.textContent || ''));
  const btn = addBtn ? (() => {
    const s = getComputedStyle(addBtn);
    const r = addBtn.getBoundingClientRect();
    const icon = addBtn.querySelector('svg');
    return {
      h: Math.round(r.height), w: Math.round(r.width),
      pad: s.padding, radius: s.borderRadius,
      fs: s.fontSize, fw: s.fontWeight, color: s.color,
      bg: (s.backgroundImage || '').replace(/\\s+/g, ' ').slice(0, 90),
      icon: icon ? { w: Math.round(icon.getBoundingClientRect().width), h: Math.round(icon.getBoundingClientRect().height) } : null
    };
  })() : null;
  const group = row.nextElementSibling;
  const g3 = group ? group.querySelector('h3') : null;
  const g3cs = g3 ? getComputedStyle(g3) : null;
  return JSON.stringify({
    row: { display: rcs.display, align: rcs.alignItems, justify: rcs.justifyContent, h: Math.round(rr.height) },
    h2: { fs: h2cs.fontSize, fw: h2cs.fontWeight, lh: h2cs.lineHeight, color: h2cs.color, mb: h2cs.marginBottom, h: Math.round(h2r.height) },
    countP: pcs ? { fs: pcs.fontSize, fw: pcs.fontWeight, lh: pcs.lineHeight, color: pcs.color } : null,
    block: { h: Math.round(br.height) },
    addBtn: btn,
    rowToGroup: group ? { gap: Math.round(group.getBoundingClientRect().top - rr.bottom) } : null,
    groupH3: g3cs ? { fs: g3cs.fontSize, fw: g3cs.fontWeight, lh: g3cs.lineHeight, mb: g3cs.marginBottom } : null,
    docSW: document.documentElement.scrollWidth
  });
})()"

echo "=== REFERENCE side (390, /networth) ==="
export AGENT_BROWSER_SESSION="refsecrow114"
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
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$SECROW_JS" 2>/dev/null | tail -1

echo "=== CLONE side (390, /networth) ==="
cd "$(dirname "$0")/../.."
SECROW_JS="$SECROW_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonesecrow114"
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
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$SECROW_JS" 2>/dev/null | tail -1
EOF
echo "=== secrow arbit v114 done ==="
