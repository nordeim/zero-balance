#!/usr/bin/env bash
# arbit-v70.sh — the v70 pair's flags, DOM-arbitrated per the v43 rule:
#   PAIR 1 flags (the income view):
#   (1) the sidebar avatar letter "U" vs "D" — the expected user-identity
#       class (the CHROME — size/geometry/color — must be byte-identical)
#   (2) the card grid layout (1 card vs 2 side-by-side) — the expected
#       seed-count data class (the grid AXES must be byte-identical, the
#       v45/v64 grid-census class re-measured live)
#   PAIR 2 flags (the expenses view):
#   (1) the card footer content (the payment-method chips) — the expected
#       v57 DATA-CONDITIONAL class (chrome byte-identical, chips data)
#   (2) the badge arrangement (the Recurring superset wrap) — the v57
#       wrap data class (chrome byte-identical, wrap arithmetic)
#   (3) the sidebar avatar — the user-identity class (again)
# Also scans the never-pinned candidate: the EXPENSES view's FILTER CARD
# at desktop 1280 (the v38 S2 pin covered /savings, the v64 pin /income,
# the v52 F3 pin the expenses card's MOBILE 390 state only; the expenses
# desktop variant — the 4-track grid with the search NOT spanning, the
# 4 children incl. the 3 comboboxes — was never censused).
# Census BOTH sides at 1280x800. READ-ONLY.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const out = {};
  // the sidebar avatar (the flagged surface): the CHROME must match;
  // the initial is the user-identity class
  const rail = document.querySelector('aside') || [...document.querySelectorAll('nav,aside,div')].find(d => {
    const r = d.getBoundingClientRect();
    return r.width > 180 && r.width < 320 && r.height > 700 && r.left === 0;
  });
  if (rail) {
    const avatar = rail.querySelector('[class*=avatar i], [class*=rounded-full]') || rail.querySelector('div[class*=bg-]');
    if (avatar) {
      const acs = getComputedStyle(avatar);
      const ar = avatar.getBoundingClientRect();
      out.avatar = {
        w: Math.round(ar.width),
        h: Math.round(ar.height),
        radius: acs.borderRadius,
        fs: acs.fontSize,
        fw: acs.fontWeight,
        color: acs.color,
        bg: acs.backgroundColor,
        text: (avatar.textContent || '').trim().slice(0, 4),
      };
    }
  }
  // the item grid
  const grid = [...document.querySelectorAll('div')].find(
    (d) => typeof d.className === 'string' && d.className.includes('grid-cols-3'),
  );
  if (grid) {
    const gcs = getComputedStyle(grid);
    out.grid = {
      w: Math.round(grid.getBoundingClientRect().width),
      gap: gcs.gap,
      childCount: grid.children.length,
      template: gcs.gridTemplateColumns,
    };
    const card = grid.children[0];
    const ccs = getComputedStyle(card);
    out.card = {
      w: Math.round(card.getBoundingClientRect().width),
      h: Math.round(card.getBoundingClientRect().height),
      pad: ccs.padding,
      radius: ccs.borderRadius,
      border: ccs.borderTopColor,
    };
    const footer = card.children[card.children.length - 1];
    const fcs = getComputedStyle(footer);
    out.footer = {
      display: fcs.display,
      justify: fcs.justifyContent,
      fs: fcs.fontSize,
      color: fcs.color,
      h: Math.round(footer.getBoundingClientRect().height),
      childCount: footer.children.length,
      children: [...footer.children].map((el) => {
        const cs = getComputedStyle(el);
        const icon = el.querySelector('svg');
        return {
          display: cs.display,
          gap: cs.gap,
          text: (el.textContent || '').trim().slice(0, 20),
          iconW: icon ? Math.round(icon.getBoundingClientRect().width) : null,
          iconH: icon ? Math.round(icon.getBoundingClientRect().height) : null,
        };
      }),
    };
    const badgeRow = [...card.children].find(
      (c) => typeof c.className === 'string' && /flex-wrap/.test(c.className),
    );
    if (badgeRow) {
      const bcs = getComputedStyle(badgeRow);
      out.badgeRow = {
        display: bcs.display,
        wrap: bcs.flexWrap,
        gap: bcs.gap,
        mb: bcs.marginBottom,
        h: Math.round(badgeRow.getBoundingClientRect().height),
        badgeCount: badgeRow.children.length,
        texts: [...badgeRow.children].map((b) => (b.textContent || '').trim()),
      };
      const b0 = badgeRow.children[0];
      const b0cs = getComputedStyle(b0);
      out.badge0 = {
        display: b0cs.display,
        radius: b0cs.borderRadius,
        pad: b0cs.padding,
        fs: b0cs.fontSize,
        fw: b0cs.fontWeight,
        h: Math.round(b0.getBoundingClientRect().height),
      };
    }
  }
  // the filter card: the white rounded-2xl card wrapping the search input
  const search = document.querySelector('input[placeholder*=\"search\" i], input[placeholder*=\"Search\" i], input[type=\"search\"], input[placeholder*=\"item\" i]');
  const filterCard = search ? search.closest('div.rounded-2xl') : null;
  if (search && filterCard) {
    const fcs = getComputedStyle(filterCard);
    const srcs = getComputedStyle(search);
    const inner = [...filterCard.children].find(
      (c) => getComputedStyle(c).display === 'grid',
    );
    const ics = inner ? getComputedStyle(inner) : null;
    out.filterCard = {
      w: Math.round(filterCard.getBoundingClientRect().width),
      h: Math.round(filterCard.getBoundingClientRect().height),
      pad: fcs.padding,
      radius: fcs.borderRadius,
      bg: fcs.backgroundColor,
      border: fcs.borderTopColor,
      mb: fcs.marginBottom,
      searchW: Math.round(search.getBoundingClientRect().width),
      searchH: Math.round(search.getBoundingClientRect().height),
      searchPad: srcs.padding,
      searchRadius: srcs.borderRadius,
      searchBorder: srcs.borderTopColor,
      innerCols: ics ? ics.gridTemplateColumns : null,
      innerGap: ics ? ics.gap : null,
      innerChildCount: inner ? inner.children.length : null,
      comboboxes: inner
        ? [...inner.querySelectorAll('[role=\"combobox\"]')].map((c) => {
            const r = c.getBoundingClientRect();
            const cs = getComputedStyle(c);
            return {
              w: Math.round(r.width),
              h: Math.round(r.height),
              fs: cs.fontSize,
              text: (c.textContent || '').trim().slice(0, 22),
            };
          })
        : [],
    };
  }
  // the page header row
  const h1 = document.querySelector('h1');
  if (h1) {
    const header = h1.closest('div');
    const hcs = getComputedStyle(header);
    out.header = {
      display: hcs.display,
      justify: hcs.justifyContent,
      align: hcs.alignItems,
      gap: hcs.gap,
      mb: hcs.marginBottom,
      h: Math.round(header.getBoundingClientRect().height),
      h1Fs: getComputedStyle(h1).fontSize,
      h1Fw: getComputedStyle(h1).fontWeight,
    };
  }
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="refarbv70"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
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
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
echo "--- ref expenses ---"
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- ref income ---"
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbv70"
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
echo "--- clone expenses ---"
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- clone income ---"
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== arbit v70 done ==="
