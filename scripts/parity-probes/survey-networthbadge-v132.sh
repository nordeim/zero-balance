#!/usr/bin/env bash
# survey-networthbadge-v132.sh — the v132 candidate-survey probe (READ-ONLY,
# the v46 rule): read the REFERENCE's first networth asset card's badge
# structure live at 390x844 — enumerate the card's leaf spans/divs with
# computed chrome to identify the TYPE badge (the v29-era Badge-base DIV
# family) and its hover contract, so the census finder can be shaped
# TAG-AGNOSTIC and STATE-INDEPENDENT (the v107 lesson).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refsurvey132"
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
sleep 5

echo "=== REF: the first asset card census (leaf chrome enumeration) ==="
agent-browser eval '(async () => {
  // the asset card finder: the grouped card family — a white rounded card
  // whose text includes a dollar figure; the FIRST such card in the assets
  // section (below the tab bar)
  const cards = [...document.querySelectorAll("div")].filter((d) => {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return cs.backgroundColor === "rgb(255, 255, 255)" && r.width > 150 && r.width < 500
      && r.height > 80 && r.height < 300 && cs.borderRadius !== "0px"
      && (d.textContent || "").includes("$");
  });
  if (!cards.length) return JSON.stringify({err: "no cards", count: 0});
  const card = cards[0];
  card.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const cr = card.getBoundingClientRect();
  // the leaf spans/divs of the card — the badge candidates
  const leaves = [...card.querySelectorAll("span, div")].filter((s) => {
    const t = (s.textContent || "").trim();
    return t.length > 2 && t.length < 30 && s.children.length === 0;
  }).slice(0, 14).map((s) => {
    const cs = getComputedStyle(s);
    const r = s.getBoundingClientRect();
    return {
      tag: s.tagName, text: (s.textContent || "").trim().slice(0, 24),
      bg: cs.backgroundColor, color: cs.color, fs: cs.fontSize,
      radius: cs.borderRadius, disp: cs.display,
      tProp: cs.transitionProperty, tDur: cs.transitionDuration,
      w: Math.round(r.width), h: Math.round(r.height),
      cursor: cs.cursor,
    };
  });
  return JSON.stringify({cardW: Math.round(cr.width), cardH: Math.round(cr.height), leaves});
})()' 2>/dev/null | tail -1
echo "=== survey done ==="
