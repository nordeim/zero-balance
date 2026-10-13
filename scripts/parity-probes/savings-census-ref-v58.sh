#!/usr/bin/env bash
# savings-census-ref-v58.sh — the v58 savings-view DOM arbitration census,
# REFERENCE side (the v43 rule: every VLM flag is DOM-verified before it
# counts) + the pin's measurement source. The flags to arbitrate:
# (1) the savings card's footer content (the reference's savings item
# carries NO payment method — the footer should render ONE child, the
# date alone; the footer row's CHROME must be byte-identical to the
# clone's); (2) the badge family (the reference's savings item is
# classified "need" [red] vs the clone's "savings" [green] — the color
# maps are the documented data class; the badge-row chrome + the badge
# geometry must be byte-identical). Also censused: the grid template +
# the card chrome. READ-ONLY (the v46 rule).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

CENSUS='(async () => {
  const out = {};
  const grid = [...document.querySelectorAll("div")].find(
    (d) => typeof d.className === "string" && /grid-cols-3/.test(d.className) && d.children.length > 0
  );
  if (!grid) return JSON.stringify({ grid: "not found" });
  const gcs = getComputedStyle(grid);
  out.grid = {
    template: gcs.gridTemplateColumns,
    gap: gcs.gap,
    w: Math.round(grid.getBoundingClientRect().width),
    childCount: grid.children.length,
  };
  const card = grid.children[0];
  // the footer: the LAST space-between flex row in the card
  const flexRows = [...card.querySelectorAll("div")].filter((d) => {
    const s = getComputedStyle(d);
    return s.display === "flex" && s.justifyContent === "space-between" && d.children.length >= 1 && !d.querySelector("h4") && d.getBoundingClientRect().height < 40;
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
        return {
          tag: c.tagName,
          text: (c.textContent || "").trim().slice(0, 24),
          display: cs.display,
          gap: cs.gap,
          fs: cs.fontSize,
          color: cs.color,
          iconW: c.querySelector("svg") ? Math.round(c.querySelector("svg").getBoundingClientRect().width) : null,
          iconH: c.querySelector("svg") ? Math.round(c.querySelector("svg").getBoundingClientRect().height) : null,
          iconColor: c.querySelector("svg") ? getComputedStyle(c.querySelector("svg")).color : null,
        };
      }),
    };
  }
  // the badge row: the card DIRECT child carrying flex-wrap
  const row = [...card.children].find((c) => /flex-wrap/.test((c.className || "").toString()));
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
      return {
        text: (c.textContent || "").trim().slice(0, 16),
        display: cs.display,
        alignItems: cs.alignItems,
        radius: cs.borderRadius,
        pad: cs.padding,
        border: cs.borderTopWidth + " " + cs.borderTopStyle + " " + cs.borderTopColor,
        bg: cs.backgroundColor,
        fs: cs.fontSize,
        fw: cs.fontWeight,
        h: Math.round(c.getBoundingClientRect().height),
        gap: cs.gap,
        iconW: c.querySelector("svg") ? Math.round(c.querySelector("svg").getBoundingClientRect().width) : null,
        iconH: c.querySelector("svg") ? Math.round(c.querySelector("svg").getBoundingClientRect().height) : null,
      };
    });
  }
  const ccs = getComputedStyle(card);
  out.card = {
    w: Math.round(card.getBoundingClientRect().width),
    pad: ccs.padding,
    radius: ccs.borderRadius,
    border: ccs.borderTopWidth + " " + ccs.borderTopStyle + " " + ccs.borderTopColor,
    bg: ccs.backgroundColor,
  };
  return JSON.stringify(out);
})()'

export AGENT_BROWSER_SESSION="refsv58"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 4
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

echo "=== REF /savings census (grid + card + footer + badges) ==="
agent-browser open "$BASE/savings" >/dev/null 2>&1
sleep 3
agent-browser eval "$CENSUS" 2>/dev/null | tail -1

echo "=== ref savings census v58 done ==="
