#!/usr/bin/env bash
# arbit-v133.sh — the v133 re-run pair's both-sides DOM census (the v75
# convention: the census runs REGARDLESS of the VLM verdict — it documents
# the drift state and measures the pin's axes). The v79 census axes
# (themselves the v70 census re-measured), re-measured on BOTH sides at
# desktop 1280x800 on BOTH items views — the TWELFTH re-run of the pair
# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133]:
#   the sidebar AVATAR chrome (the v70b axes: 36x36 / radius 9999px /
#   14px-600 / white / rgb(143,188,63) — the identity text the only delta)
#   the item GRID + the FIRST CARD (w AND h — the height the v70b lesson
#   decomposed: the natural income 200 vs the superset-wrap 230) + the
#   titleRow + the AMOUNT leaf (text-2xl font-bold — never pinned at 1280)
#   the FOOTER row + the BADGE row + badge0 (the v57 axes re-measured)
#   the FILTER CARD on both views (the v64/v70 axes re-measured) + the
#   page HEADER row (the v65 axes re-measured) + the docSW guard.
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors (geometry + text-content
# filters only).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const out = { url: location.pathname };
  // the sidebar avatar (the v70b finder: a small round 1-2 char element
  // in the rail — geometry + content filters only)
  const rail = document.querySelector('aside') || [...document.querySelectorAll('nav,aside,div')].find(d => {
    const r = d.getBoundingClientRect();
    return r.width > 180 && r.width < 320 && r.height > 700 && r.left === 0;
  });
  if (rail) {
    const avatar = [...rail.querySelectorAll('div,span,button')].find(el => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      const t = (el.textContent || '').trim();
      return r.width >= 30 && r.width <= 45 && Math.abs(r.width - r.height) < 3
        && parseFloat(cs.borderRadius) > 100 && t.length >= 1 && t.length <= 2;
    });
    if (avatar) {
      const acs = getComputedStyle(avatar);
      out.avatar = {
        w: Math.round(avatar.getBoundingClientRect().width),
        h: Math.round(avatar.getBoundingClientRect().height),
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
    // the titleRow: the dot + the h4 category title
    const title = [...card.querySelectorAll('h1,h2,h3,h4')][0];
    if (title) {
      const dot = [...(title.parentElement || card).querySelectorAll('div,span')].find((d) => {
        const cs = getComputedStyle(d);
        const r = d.getBoundingClientRect();
        return !d.children.length && r.width > 0 && r.width <= 12 && cs.backgroundColor !== 'rgba(0, 0, 0, 0)';
      });
      out.titleRow = {
        gap: getComputedStyle(title.parentElement).gap,
        dotW: dot ? Math.round(dot.getBoundingClientRect().width) : null,
        dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
        font: getComputedStyle(title).fontSize,
        weight: getComputedStyle(title).fontWeight,
      };
    }
    // the AMOUNT leaf: the largest-font P in the card (text-2xl font-bold)
    const amount = [...card.querySelectorAll('p')].find(
      (p) => parseFloat(getComputedStyle(p).fontSize) >= 20,
    );
    if (amount) {
      const acs = getComputedStyle(amount);
      out.amount = {
        fs: acs.fontSize,
        fw: acs.fontWeight,
        color: acs.color,
        lh: acs.lineHeight,
        h: Math.round(amount.getBoundingClientRect().height),
        text: (amount.textContent || '').trim().slice(0, 14),
      };
    }
    // the footer row: the LAST direct child
    const footer = card.children[card.children.length - 1];
    if (footer) {
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
    }
    // the badge row: the flex-wrap direct child
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
  // the filter card: the wide input's rounded-2xl ancestor
  const search = [...document.querySelectorAll('input')].find(
    (i) => i.getBoundingClientRect().width > 100,
  );
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
        ? [...inner.querySelectorAll('[role=combobox]')].map((c) => {
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
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="refarbit133"
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
echo "--- ref income ---"
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- ref expenses ---"
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbit133"
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
echo "--- clone income ---"
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- clone expenses ---"
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== arbit v133 done ==="
