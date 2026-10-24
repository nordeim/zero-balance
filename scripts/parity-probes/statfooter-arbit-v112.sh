#!/usr/bin/env bash
# statfooter-arbit-v112.sh — the ONE-SHOT both-sides arbitration for the
# v112 networth + drill-down pair's three flags:
#   (a) the FAB claim (the VLM: "a black 'Edit with Base44' floating
#       action button... present in the reference, absent in the clone" —
#       the platform-chrome class; the v97/v103/v108/v109/v110 standing
#       disproof form: the FAB never renders in the app DOM on EITHER side
#       — it lives in the reference's platform iframe chrome);
#   (b) the stat-card FOOTER LEADER-LINE flag (the VLM: "a horizontal
#       dashed line extending to the trend icon in the clone, not present
#       in the reference" — never censused before: the footer row's
#       count-span + leader div + TrendingUp icon family, read live on
#       both sides);
#   (c) the statTitles re-read (the VLM's "Total Expense (singular)" —
#       the v106-documented VLM text-misread sub-form; the live DOM read
#       is the authority).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS (the v64 rule — amount leaves found via String.fromCharCode(36) where
# needed); no backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

FAB_JS="(async () => {
  const hits = [...document.querySelectorAll('body *')].filter(el => {
    const t = (el.textContent || '').trim();
    return t.length > 0 && t.length < 40 && /Base44/i.test(t) && el.children.length <= 2;
  });
  return JSON.stringify({ fabCount: hits.length, bodyHasBase44: /Base44/.test(document.body.textContent || '') });
})()"

STAT_JS="(async () => {
  const D = String.fromCharCode(36);
  const cards = [...document.querySelectorAll('h3')].filter(h => /Total (Income|Savings|Expenses)/.test((h.textContent || '').trim()))
    .map(h => h.closest('div[class*=rounded-2xl]'))
    .filter(Boolean);
  const out = cards.map(card => {
    const title = card.querySelector('h3');
    const footer = [...card.querySelectorAll('div')].find(d => {
      const cs = getComputedStyle(d);
      return cs.display === 'flex' && /item/.test((d.textContent || '')) && d.querySelector('svg');
    });
    if (!footer) return { title: (title.textContent || '').trim(), footer: 'no footer row' };
    const fcs = getComputedStyle(footer);
    const countSpan = [...footer.querySelectorAll('span')].find(s => /item/.test(s.textContent || ''));
    const leader = [...footer.querySelectorAll('div')].find(d => {
      const cs = getComputedStyle(d);
      return cs.flex === '1 1 0%' || (d.className && /flex-1/.test(d.className) || d.getAttribute && (d.getAttribute('aria-hidden') === 'true' && cs.height.replace('px','') < 3));
    });
    const icon = footer.querySelector('svg');
    const lcs = leader ? getComputedStyle(leader) : null;
    const lr = leader ? leader.getBoundingClientRect() : null;
    const ics = icon ? getComputedStyle(icon) : null;
    const ir = icon ? icon.getBoundingClientRect() : null;
    return {
      title: (title.textContent || '').trim(),
      footer: {
        display: fcs.display, alignItems: fcs.alignItems, gap: fcs.gap,
        h: Math.round(footer.getBoundingClientRect().height),
        countText: countSpan ? (countSpan.textContent || '').trim() : null,
        countFs: countSpan ? getComputedStyle(countSpan).fontSize : null,
        countColor: countSpan ? getComputedStyle(countSpan).color : null,
        leader: lcs ? {
          h: Math.round(lr.height), bg: lcs.backgroundColor,
          borderTopStyle: lcs.borderTopStyle, borderTopW: lcs.borderTopWidth,
          w: Math.round(lr.width), flex: lcs.flex,
        } : 'no leader',
        icon: ics ? { w: Math.round(ir.width), h: Math.round(ir.height), color: ics.color } : 'no icon',
      },
    };
  });
  return JSON.stringify({ docSW: window.innerWidth, statCardCount: out.length, statTitles: out.map(o => o.title), cards: out });
})()"

echo "=== REFERENCE side (1280, /networth FAB + / stat-footer) ==="
export AGENT_BROWSER_SESSION="refsf112"
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
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census (ref, /networth):"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- stat-footer + titles census (ref, /):"
agent-browser eval "$STAT_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /networth FAB + / stat-footer) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonesf112"
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
echo "--- FAB census (clone, /networth):"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- stat-footer + titles census (clone, /):"
agent-browser eval "$STAT_JS" 2>/dev/null | tail -1
EOF
echo "=== statfooter arbit v112 done ==="
