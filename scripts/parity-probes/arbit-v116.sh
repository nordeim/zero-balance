#!/usr/bin/env bash
# arbit-v116.sh — the v116 re-run pair's flags, DOM-arbitrated per the v43
# rule, at DESKTOP 1280x800 on BOTH sides (the savings view full-page —
# the v110-era savings pair's NINTH re-run, last re-shot v110 — now the
# oldest remaining candidate [v110 < v111 < v112 < v113 < v114 < v115]).
# The census: the v74/v80 axes (header + grid + card + title + amount +
# footer + badges + docSW) PLUS the v80 titleRow geometry (the h4's
# parent row + the category dot — the 1280 state of the v51/v54
# 390-only family, first census'd at desktop in v80, re-verified here). The VLM flags to
# arbitrate:
#   (1) "Card Grid Alignment" — the reference's single card vs the clone's
#       two cards in "a 2-column grid": the GRID census (display,
#       grid-template-columns, gap, w, childCount) + the CARD chrome (w,
#       pad, radius, border, bg) must be byte-identical; the child count
#       is the seed-data class (the reference's 1-item seed vs the
#       clone's 2-item dev seed).
#   (2) "Card Footer Content" — the clone's account-type label
#       ("Brokerage"/"Bank Account" + icon) absent on the reference: the
#       v58 DATA-CONDITIONAL footer class re-verified — the footer row's
#       chrome (flex justify-between 12px rgb(107,114,128) h 16; each
#       span flex gap 4px with the 12x12 gray icon) byte-identical; the
#       reference's own savings item carries NO paymentMethod so its
#       footer renders ONE child (the date alone) while the clone's carry
#       paymentMethods (the same two-child structure the reference's own
#       income card renders) — the v57 conditional-footer contract.
#   (3) the badge family — the reference's "need" (red) vs the clone's
#       "savings" (green): the classification VALUE is the data class;
#       the badge-row + per-badge chrome must be byte-identical; the
#       color maps are locked by badge-colors.spec.ts.
#   Plus the header row + the filter card census (drift re-checks) and
#   the docSW overflow check.
# READ-ONLY on BOTH sides (login + passive navigation only — the v46
# rule). The v73 heredoc lesson: the QUOTED <<'EOF' with the
# env-injected census; no literal dollar sequences in the census JS.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

SV_CENSUS_JS="(async () => {
  const out = { view: location.pathname, docSW: document.documentElement.scrollWidth, vw: window.innerWidth };

  // the page header row: the h1 + subtitle + the Add button (the v65
  // F3-pinned axes — a drift re-check, not a re-pin)
  const h1 = document.querySelector('h1');
  if (h1) {
    const s = getComputedStyle(h1);
    out.h1 = { text: (h1.textContent || '').trim().slice(0, 20), fs: s.fontSize, fw: s.fontWeight, color: s.color };
  }
  const sub = h1 ? h1.parentElement.querySelector('p') : null;
  if (sub) {
    const s = getComputedStyle(sub);
    out.subtitle = { fs: s.fontSize, color: s.color, text: (sub.textContent || '').trim().slice(0, 24) };
  }
  const addBtn = [...document.querySelectorAll('button')].find(b => /add savings goal/i.test(b.textContent || ''));
  if (addBtn) {
    const s = getComputedStyle(addBtn);
    const r = addBtn.getBoundingClientRect();
    out.addBtn = { w: Math.round(r.width), h: Math.round(r.height), radius: s.borderRadius, fs: s.fontSize, fw: s.fontWeight, color: s.color };
  }

  // the grid: the v58 axes (template, gap, w, childCount)
  const grid = [...document.querySelectorAll('div')].find(
    (d) => typeof d.className === 'string' && /grid-cols-3/.test(d.className) && d.children.length > 0
  );
  if (!grid) { out.grid = 'not found'; return JSON.stringify(out); }
  const gcs = getComputedStyle(grid);
  out.grid = {
    display: gcs.display,
    template: gcs.gridTemplateColumns,
    gap: gcs.gap,
    w: Math.round(grid.getBoundingClientRect().width),
    childCount: grid.children.length,
  };

  // the first card's chrome
  const card = grid.children[0];
  const ccs = getComputedStyle(card);
  out.card = {
    w: Math.round(card.getBoundingClientRect().width),
    h: Math.round(card.getBoundingClientRect().height),
    pad: ccs.padding,
    radius: ccs.borderRadius,
    border: ccs.borderTopWidth + ' ' + ccs.borderTopStyle + ' ' + ccs.borderTopColor,
    bg: ccs.backgroundColor,
  };

  // the card's title + amount (the interior text blocks). The amount is
  // the text-2xl p (formatMoney's dollar-prefixed string — matched by
  // CLASS, not text: no literal dollar in the census JS, the v64 rule).
  const h4 = card.querySelector('h4');
  if (h4) {
    const s = getComputedStyle(h4);
    out.cardTitle = { fs: s.fontSize, fw: s.fontWeight, color: s.color, lh: s.lineHeight };
  }
  // the TITLE ROW — the h4's direct parent (the dot + title line — the
  // v98-era pin candidate: the 1280 state of the v51/v54 390-only family,
  // never census'd at desktop)
  if (h4 && h4.parentElement && h4.parentElement !== card) {
    const row = h4.parentElement;
    const rs = getComputedStyle(row);
    const dot = [...row.querySelectorAll('div,span')].find((d) => {
      const b = d.getBoundingClientRect();
      return b.width > 0 && b.width <= 12 && b.height > 0 && b.height <= 12;
    });
    out.titleRow = {
      display: rs.display,
      gap: rs.gap,
      alignItems: rs.alignItems,
      h: Math.round(row.getBoundingClientRect().height),
      dotW: dot ? Math.round(dot.getBoundingClientRect().width) : null,
      dotH: dot ? Math.round(dot.getBoundingClientRect().height) : null,
      dotRadius: dot ? getComputedStyle(dot).borderRadius : null,
      dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
    };
  }
  const amtP = [...card.querySelectorAll('p')].find(p => typeof p.className === 'string' && /text-2xl/.test(p.className));
  if (amtP) {
    const s = getComputedStyle(amtP);
    out.cardAmount = { fs: s.fontSize, fw: s.fontWeight, lh: s.lineHeight, color: s.color };
  }

  // the footer: the LAST space-between flex row in the card (the v58
  // detection — the DATA-CONDITIONAL axis)
  const flexRows = [...card.querySelectorAll('div')].filter((d) => {
    const s = getComputedStyle(d);
    return s.display === 'flex' && s.justifyContent === 'space-between' && d.children.length >= 1 && !d.querySelector('h4') && d.getBoundingClientRect().height < 40;
  });
  const footer = flexRows[flexRows.length - 1];
  if (footer) {
    const fs = getComputedStyle(footer);
    out.footer = {
      display: fs.display,
      justify: fs.justifyContent,
      fs: fs.fontSize,
      color: fs.color,
      h: Math.round(footer.getBoundingClientRect().height),
      childCount: footer.children.length,
      children: [...footer.children].map((c) => {
        const cs = getComputedStyle(c);
        const svg = c.querySelector('svg');
        return {
          tag: c.tagName,
          text: (c.textContent || '').trim().slice(0, 24),
          display: cs.display,
          gap: cs.gap,
          fs: cs.fontSize,
          color: cs.color,
          iconW: svg ? Math.round(svg.getBoundingClientRect().width) : null,
          iconH: svg ? Math.round(svg.getBoundingClientRect().height) : null,
          iconColor: svg ? getComputedStyle(svg).color : null,
        };
      }),
    };
  }

  // the badge row: the card DIRECT child carrying flex-wrap (the v58
  // detection — the classification-color axis)
  const row = [...card.children].find((c) => /flex-wrap/.test((c.className || '').toString()));
  if (row) {
    const s = getComputedStyle(row);
    out.badgeRow = {
      display: s.display,
      wrap: s.flexWrap,
      gap: s.gap,
      mb: s.marginBottom,
      h: Math.round(row.getBoundingClientRect().height),
      n: row.children.length,
    };
    out.badges = [...row.children].map((c) => {
      const cs = getComputedStyle(c);
      const svg = c.querySelector('svg');
      return {
        text: (c.textContent || '').trim().slice(0, 16),
        display: cs.display,
        alignItems: cs.alignItems,
        radius: cs.borderRadius,
        pad: cs.padding,
        border: cs.borderTopWidth + ' ' + cs.borderTopStyle + ' ' + cs.borderTopColor,
        bg: cs.backgroundColor,
        color: cs.color,
        fs: cs.fontSize,
        fw: cs.fontWeight,
        h: Math.round(c.getBoundingClientRect().height),
        gap: cs.gap,
        iconW: svg ? Math.round(svg.getBoundingClientRect().width) : null,
        iconH: svg ? Math.round(svg.getBoundingClientRect().height) : null,
      };
    });
  }
  return JSON.stringify(out);
})()"

########## REFERENCE SIDE ##########
export AGENT_BROWSER_SESSION="refarbit116"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "(async () => {
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
})()" 2>/dev/null | tail -1)
  echo "ref login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF /savings census (header + grid + card + footer + badges) ==="
agent-browser eval "$SV_CENSUS_JS" 2>/dev/null | tail -1

echo ""
echo "########## CLONE SIDE ##########"
cd "$(dirname "$0")/../.."
SV_CENSUS_JS="$SV_CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonearbit116"
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
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== CLONE /savings census (header + grid + card + footer + badges) ==="
agent-browser eval "$SV_CENSUS_JS" 2>/dev/null | tail -1
EOF

echo ""
echo "=== seedcheck (env -u DATABASE_URL — the documented pollution discipline) ==="
cd "$(dirname "$0")/../.."
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs
echo "=== arbit v116 done ==="
