#!/usr/bin/env bash
# hero-desk-v56.sh — the desktop 1280x800 hero-card census on BOTH sides
# (the v56 pin's measurement source). PAIR-1 surface: the NET ZERO GOAL
# card's desktop geometry + the progress track (the v56 arbitration's
# byte-identical finding: w 568 h 12 rgba(255,255,255,0.1)) + the fill +
# the stat-row icon tiles (the glyph-swap chrome). READ-ONLY both sides.
set -u
BASE="${1:-https://zero-balance-4885a8f3.base44.app}"
SESS="${2:-refhero56}"
PORTSIDE="${3:-ref}"

CENSUS='(async () => {
  const h3 = [...document.querySelectorAll("h3")].find(h => (h.textContent || "").trim() === "NET ZERO GOAL");
  if (!h3) return "no hero";
  let card = h3.parentElement;
  for (let i = 0; i < 12 && card; i++) {
    const cs = getComputedStyle(card);
    const r = card.getBoundingClientRect();
    if (r.width > 500 && r.height > 250 && cs.borderRadius !== "0px" && cs.boxShadow !== "none") break;
    card = card.parentElement;
  }
  if (!card) return "no card";
  const csC = getComputedStyle(card);
  const rC = card.getBoundingClientRect();
  const grid = (card.parentElement).parentElement;
  const csG = getComputedStyle(grid);
  const siblings = [...grid.children].map(c => ({ w: Math.round(c.getBoundingClientRect().width), h: Math.round(c.getBoundingClientRect().height), y: Math.round(c.getBoundingClientRect().y) }));
  // the progress track: the rounded bar 10-16 tall
  const track = [...card.querySelectorAll("div")].find(d => {
    const r = d.getBoundingClientRect();
    const cs = getComputedStyle(d);
    return r.height >= 10 && r.height <= 16 && cs.borderRadius === "9999px" && r.width > 200;
  });
  const fill = track && track.firstElementChild ? track.firstElementChild : null;
  const fillW = fill ? Math.round(fill.getBoundingClientRect().width) : null;
  // the pct label
  const pct = [...card.querySelectorAll("span, p")].find(s => /^[0-9.]+%$/.test((s.textContent || "").trim()));
  // the stat rows: the 48px icon tiles (the glyph-swap chrome)
  const tiles = [...card.closest("main") ? card.closest("main").querySelectorAll("div") : []].filter(d => {
    const r = d.getBoundingClientRect();
    return Math.abs(r.width - 48) < 2 && Math.abs(r.height - 48) < 2;
  }).slice(0, 3).map(d => {
    const svg = d.querySelector("svg");
    return { w: Math.round(d.getBoundingClientRect().width), h: Math.round(d.getBoundingClientRect().height), svg: svg ? { w: svg.getBoundingClientRect().width, h: svg.getBoundingClientRect().height } : null };
  });
  return JSON.stringify({
    heroGrid: { cols: csG.gridTemplateColumns, gap: csG.gap, children: siblings.length, siblings },
    card: { w: Math.round(rC.width), h: Math.round(rC.height), radius: csC.borderRadius, pad: csC.padding, bg: csC.backgroundImage.slice(0, 70), shadow: csC.boxShadow.slice(0, 60) },
    track: track ? { w: Math.round(track.getBoundingClientRect().width), h: Math.round(track.getBoundingClientRect().height), bg: getComputedStyle(track).backgroundColor, radius: getComputedStyle(track).borderRadius } : null,
    fill: fill ? { w: fillW, bg: getComputedStyle(fill).backgroundImage.slice(0, 70), radius: getComputedStyle(fill).borderRadius } : null,
    pct: pct ? (pct.textContent || "").trim() : null,
    tiles
  });
})()'

export AGENT_BROWSER_SESSION="$SESS"
if [ "$PORTSIDE" = "ref" ]; then
  agent-browser open "$BASE/login" >/dev/null 2>&1
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
else
  agent-browser open "$BASE/login" >/dev/null 2>&1
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
fi
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 4
echo "=== $PORTSIDE hero census at 1280x800 ==="
agent-browser eval "$CENSUS" 2>/dev/null | tail -1
echo "=== $PORTSIDE done ==="
