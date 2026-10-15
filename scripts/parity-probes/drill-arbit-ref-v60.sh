#!/usr/bin/env bash
# drill-arbit-ref-v60.sh — the v60 PAIR 2 flags' DOM arbitration, REFERENCE
# side (the v43 rule: every VLM flag is DOM-verified before it counts).
# The five flags: (1) the nav highlight [the v56-arbitrated root-URL
# active-nav gap], (2) the avatar [the user-identity class], (3) the Base44
# badge [the platform-chrome class], (4) the hero progress-bar fill [the
# pct x 568 data class — v56-arbitrated], (5) the DONUT PERCENTAGE LABELS
# [NEW — the vLM claims the reference shows none; the v9 G1b measurement
# says both render labels with labelLineCount 0]. This census re-confirms
# all five live. READ-ONLY (the v46 rule).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

ARBIT='(async () => {
  const out = { view: "drill-arbit-ref-1280" };
  // (1) the nav highlight at the root URL (the v56 class): the computed
  // bg of the Dashboard nav link — the reference shows NONE at /.
  const links = [...document.querySelectorAll("a")];
  const dash = links.find((l) => /dashboard/i.test((l.textContent || "")) && l.getBoundingClientRect().height > 0 && l.getBoundingClientRect().left < 300);
  if (dash) {
    const s = getComputedStyle(dash);
    out.navHighlight = { bg: s.backgroundColor, color: s.color, radius: s.borderRadius, fw: s.fontWeight };
  }
  // (2) the avatar letter
  const avatar = [...document.querySelectorAll("div,span")].find((d) => {
    const r = d.getBoundingClientRect();
    const c = getComputedStyle(d);
    return !d.children.length && r.width > 24 && r.width < 60 && c.borderRadius === "9999px" && /^[A-Z]$/.test((d.textContent || "").trim());
  });
  out.avatarLetter = avatar ? (avatar.textContent || "").trim() : null;
  // (3) the Base44 badge (platform chrome)
  out.base44Badge = /base44/i.test(document.body.textContent || "");
  // (4) the hero progress fill: the track + the fill width (the pct data class)
  const track = [...document.querySelectorAll("div")].find((d) => {
    const r = d.getBoundingClientRect();
    const c = getComputedStyle(d);
    return !d.children.length && r.width > 400 && r.height >= 10 && r.height <= 16 && c.borderRadius === "9999px" && /rgba/.test(c.backgroundColor);
  });
  if (track) {
    const fill = track.parentElement && [...track.parentElement.querySelectorAll("div")].find((d) => d !== track && d.getBoundingClientRect().height >= 8 && getComputedStyle(d).borderRadius === "9999px");
    const tr = track.getBoundingClientRect();
    out.progress = {
      trackW: Math.round(tr.width), trackH: Math.round(tr.height),
      trackBg: getComputedStyle(track).backgroundColor,
      fillW: fill ? Math.round(fill.getBoundingClientRect().width) : null,
      fillBg: fill ? getComputedStyle(fill).backgroundImage.slice(0, 60) : null,
    };
  }
  // (5) the DONUT PERCENTAGE LABELS — the recharts pie label text nodes
  const pieSvgs = [...document.querySelectorAll("svg")].filter((s) => s.querySelector("[class*=recharts-pie-sector], [class*=recharts-pie-label]"));
  out.pieSvgCount = pieSvgs.length;
  if (pieSvgs.length) {
    const svg = pieSvgs[0];
    const labels = [...svg.querySelectorAll("[class*=recharts-pie-label]")].filter((e) => !/line/i.test(e.getAttribute("class") || ""));
    const labelLines = [...svg.querySelectorAll("[class*=recharts-pie-label-line]")];
    out.donutLabels = {
      count: labels.length,
      texts: labels.map((e) => (e.textContent || "").trim()).slice(0, 6),
      labelLineCount: labelLines.length,
      labelFs: labels.length ? getComputedStyle(labels[0]).fontSize : null,
      labelFill: labels.length ? getComputedStyle(labels[0]).fill : null,
      sectors: [...svg.querySelectorAll("[class*=recharts-pie-sector]")].length,
    };
  }
  return JSON.stringify(out);
})()'

export AGENT_BROWSER_SESSION="refar60"
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

echo "=== REF drill-down arbitration census at 1280 ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 4
agent-browser eval "$ARBIT" 2>/dev/null | tail -1

echo "=== ref drill arbit v60 done ==="
