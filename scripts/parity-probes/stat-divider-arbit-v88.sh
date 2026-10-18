#!/usr/bin/env bash
# stat-divider-arbit-v88.sh — the dedicated one-shot both-sides arbitration
# for the v88 VLM's NEW drill-down flag: "the faint horizontal divider lines
# above the item counts in the three middle stat cards are present in the
# CLONE but missing in the REFERENCE". The census measures the stat cards'
# COUNT-ROW divider chrome (the h-px flex-1 line between the "N items" text
# and the trend icon) on BOTH sides at 1280x800 — the v87 close-arbit
# precedent (a dedicated inventory probe for a single new flag; the v87
# name-independent-finder lesson: geometry + text-content filters only, no
# accessible-name selectors). READ-ONLY on both sides (the v46 rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

ARBIT='(async () => {
  const out = { view: "stat-divider-arbit-1280-v88" };
  // The three dashboard stat cards: rounded cards containing a "Total X" h3.
  const cards = [...document.querySelectorAll("div")].filter((d) => {
    if (!d.className || typeof d.className !== "string") return false;
    if (!d.className.includes("rounded-2xl")) return false;
    const h3s = [...d.querySelectorAll("h3")];
    const hasTitle = h3s.some((h) => /^Total (Income|Savings|Expenses)/i.test((h.textContent || "").trim()));
    const r = d.getBoundingClientRect();
    return hasTitle && r.width > 200 && r.width < 500 && r.height > 150 && d.querySelectorAll("svg").length > 0;
  });
  out.statCardCount = cards.length;
  out.cards = cards.slice(0, 3).map((card) => {
    const title = ([...card.querySelectorAll("h3")].find((h) => /^Total /i.test((h.textContent || "").trim())) || {}).textContent;
    // The count row: the flex row containing the "N items" text leaf.
    const itemsText = [...card.querySelectorAll("span, p")].find((e) => /^\d+ items?$/.test((e.textContent || "").trim()) && e.children.length === 0);
    if (!itemsText) return { title, err: "no items text" };
    const row = itemsText.closest("div.flex") || itemsText.parentElement;
    const rr = row.getBoundingClientRect();
    const rcs = getComputedStyle(row);
    // The divider: the 1px-high flex-1 line in the row (geometry finder —
    // never a class or name selector; the reference may or may not render it).
    const kids = [...row.children];
    const divider = kids.find((k) => {
      const kr = k.getBoundingClientRect();
      return Math.round(kr.height) <= 1 && kr.width > 20;
    });
    // The trend icon: the 16x16 svg in the row.
    const icon = kids.find((k) => k.tagName === "svg" || (k.querySelector && k.querySelector("svg")));
    const iconSvg = row.querySelector("svg");
    const dcs = divider ? getComputedStyle(divider) : null;
    const dr = divider ? divider.getBoundingClientRect() : null;
    return {
      title,
      row: {
        h: Math.round(rr.height), w: Math.round(rr.width),
        display: rcs.display, gap: rcs.gap, alignItems: rcs.alignItems,
        fs: rcs.fontSize, color: rcs.color,
      },
      itemsText: (itemsText.textContent || "").trim(),
      divider: divider ? {
        tag: divider.tagName, h: Math.round(dr.height), w: Math.round(dr.width),
        bg: dcs.backgroundColor, flexGrow: dcs.flexGrow,
      } : null,
      trendIcon: iconSvg ? {
        w: Math.round(iconSvg.getBoundingClientRect().width),
        h: Math.round(iconSvg.getBoundingClientRect().height),
        color: getComputedStyle(iconSvg).color,
      } : null,
      rowChildTags: kids.map((k) => k.tagName),
    };
  });
  return JSON.stringify(out);
})()'

# ---------- REFERENCE side ----------
export AGENT_BROWSER_SESSION="refdiv88"
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
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF stat-card count-row divider census at 1280 ==="
agent-browser eval "$ARBIT" 2>/dev/null | tail -1

# ---------- CLONE side (inside with-server, census env-injected) ----------
ARBIT="$ARBIT" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonediv88"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== CLONE stat-card count-row divider census at 1280 ==="
agent-browser eval "$ARBIT" 2>/dev/null | tail -1
EOF
echo "=== stat-divider arbit v88 done ==="
