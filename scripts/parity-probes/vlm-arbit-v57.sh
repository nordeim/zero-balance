#!/usr/bin/env bash
# vlm-arbit-v57.sh — the v57 VLM-pair DOM arbitration (the v43 rule: every
# flag is DOM-verified before it counts) + the pin's measurement source.
# The flags to arbitrate: (1) the expense card footer content (the payment
# chips are DATA-CONDITIONAL — the footer row's chrome must be
# byte-identical); (2) the badge wrap (the clone's Recurring superset badge
# wraps the row — the row's chrome must be byte-identical). Also censused:
# the grid templates + the card chrome on both views.
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

echo "=== REFERENCE /income census ==="
export AGENT_BROWSER_SESSION="refarbit57"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
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
agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3
agent-browser eval "$CENSUS" 2>/dev/null | tail -1
echo "=== REFERENCE /expenses census ==="
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "$CENSUS" 2>/dev/null | tail -1
echo "=== ref arbit v57 done ==="
