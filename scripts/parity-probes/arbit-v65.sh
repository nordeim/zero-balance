#!/usr/bin/env bash
# arbit-v65.sh — the v65 pair's flags, DOM-arbitrated per the v43 rule:
#   (1) the sidebar avatar color + initial — the expected user-identity
#       class (the reference's account vs the clone's demo user; the
#       CHROME — size/geometry — must still be byte-identical)
#   (2) the card grid layout (1 card vs 2 side-by-side) — the expected
#       seed-count data class (the grid AXES must be byte-identical —
#       the v45 grid-census class re-measured live)
#   (3) the goal-card footer content + badges — the v57 DATA-CONDITIONAL
#       classes (chrome byte-identical; the reference's 1 item carries
#       no paymentMethod so its footer renders the date alone)
# Also scans the never-pinned candidate: the PAGE-HEADER ROW at desktop
# 1280 (the chip + h1 + count subtitle + Add Savings button — the v42
# census covered the MID-640 stacked state only; the 1280 row's computed
# geometry was never measured; the early-era tests pin class strings).
# Census BOTH sides at 1280x800. READ-ONLY.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const out = {};
  // the sidebar avatar (the flagged surface): the CHROME must match;
  // the color + initial are the user-identity class
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
        text: (avatar.textContent || '').trim().slice(0, 2),
        bottom: Math.round(ar.bottom),
        left: Math.round(ar.left),
      };
    }
  }
  // the item grid (the flagged layout): the AXES must be byte-identical
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
    // the footer row: the LAST direct child (the date + payment row)
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
    // the badge row: the DIRECT child with flex-wrap (the v57 lesson)
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
  // the page-header row at 1280 — the never-census'd family: the chip +
  // h1 + count subtitle + Add button, computed geometry. NOTE: the
  // reference carries a HIDDEN zero-size h1 'ZeroBalance' FIRST in the
  // DOM (its own SEO pattern) — grab the VISIBLE h1 (non-zero geometry).
  const h1 = [...document.querySelectorAll('h1')].find(
    (h) => h.getBoundingClientRect().width > 0,
  );
  if (h1) {
    // the header row: walk UP from the Add button to the container that
    // also holds the visible h1 (the justify-between row at 1280)
    const addBtn = [...document.querySelectorAll('button')].find(
      (b) => (b.textContent || '').includes('Add') && b.getBoundingClientRect().width > 0,
    );
    let row = null;
    if (addBtn) {
      let cur = addBtn.parentElement;
      for (let i = 0; i < 6 && cur; i++) {
        if (cur.contains(h1) && cur !== h1) { row = cur; break; }
        cur = cur.parentElement;
      }
    }
    if (row) {
      const rcs = getComputedStyle(row);
      out.headerRow = {
        display: rcs.display,
        justify: rcs.justifyContent,
        align: rcs.alignItems,
        gap: rcs.gap,
        mb: rcs.marginBottom,
        h: Math.round(row.getBoundingClientRect().height),
      };
      // the chip block: the h-12 gradient square holding the view icon
      const chip = row.querySelector('div.h-12, [class*=h-12]');
      if (chip) {
        const chcs = getComputedStyle(chip);
        out.chip = {
          w: Math.round(chip.getBoundingClientRect().width),
          h: Math.round(chip.getBoundingClientRect().height),
          radius: chcs.borderRadius,
          bg: chcs.backgroundImage.slice(0, 80),
        };
        const chipIcon = chip.querySelector('svg');
        if (chipIcon) {
          out.chipIcon = {
            w: Math.round(chipIcon.getBoundingClientRect().width),
            h: Math.round(chipIcon.getBoundingClientRect().height),
            color: getComputedStyle(chipIcon).color,
          };
        }
      }
      // the h1 + its font
      const h1cs = getComputedStyle(h1);
      out.h1 = {
        fs: h1cs.fontSize,
        fw: h1cs.fontWeight,
        lh: h1cs.lineHeight,
        color: h1cs.color,
      };
      // the count subtitle: the sibling P of the h1 (the item-count line)
      const sub = h1.parentElement.querySelector('p');
      if (sub) {
        const scs = getComputedStyle(sub);
        out.subtitle = {
          fs: scs.fontSize,
          color: scs.color,
          fw: scs.fontWeight,
          text: (sub.textContent || '').trim().slice(0, 24),
        };
      }
      // the Add button (the gradient 'Add Savings' / 'Add Savings Goal')
      const btn = [...row.querySelectorAll('button')].find(
        (b) => (b.textContent || '').includes('Add'),
      );
      if (btn) {
        const btcs = getComputedStyle(btn);
        out.addButton = {
          text: (btn.textContent || '').trim().slice(0, 20),
          w: Math.round(btn.getBoundingClientRect().width),
          h: Math.round(btn.getBoundingClientRect().height),
          radius: btcs.borderRadius,
          pad: btcs.padding,
          fs: btcs.fontSize,
          fw: btcs.fontWeight,
          color: btcs.color,
          bg: btcs.backgroundImage.slice(0, 80),
          shadow: btcs.boxShadow.slice(0, 80),
        };
        const btnIcon = btn.querySelector('svg');
        if (btnIcon) {
          out.addButtonIcon = {
            w: Math.round(btnIcon.getBoundingClientRect().width),
            h: Math.round(btnIcon.getBoundingClientRect().height),
          };
        }
      }
    }
  }
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280, savings) ==="
export AGENT_BROWSER_SESSION="refarbv65"
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
echo "--- ref savings ---"
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, savings) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbv65"
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
echo "--- clone savings ---"
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== arbit v65 done ==="
