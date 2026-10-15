#!/usr/bin/env bash
# drill-itemdump-ref-v60.sh — the v60 drill census's ONE divergent axis
# arbitrated: the reference's sub-area row structure under the first
# category (the item row measured h 16 / pad 0 vs the clone's h 24 /
# pad 4px 8px — the v43 probe measured both byte-identical at 640).
# This dump lists EVERY row's class/text/chrome to identify what the
# census's rows[last] actually caught. READ-ONLY (the v46 rule).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

DUMP='(async () => {
  const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
    (e) => (e.textContent || "").trim() === "Net Zero Breakdown" && e.children.length === 0
  );
  const card = leaf ? leaf.closest("div[class*=rounded-2xl]") : null;
  if (!card) return JSON.stringify({ err: "no card" });
  const sec = [...card.querySelectorAll("button")].find((b) => /Total Income/i.test(b.textContent || ""));
  if (!sec) return JSON.stringify({ err: "no section" });
  sec.click();
  await new Promise((r) => setTimeout(r, 600));
  const cat = [...card.querySelectorAll("button")].find(
    (b) => b.offsetParent !== null && /[$]/.test(b.textContent || "") && !/Total|Net Balance/i.test(b.textContent || "")
  );
  if (!cat) return JSON.stringify({ err: "no category" });
  const catText = (cat.textContent || "").trim().slice(0, 30);
  cat.click();
  await new Promise((r) => setTimeout(r, 600));
  const subArea = [...cat.parentElement.children].find(
    (c) => c !== cat && c.getBoundingClientRect().height > 0
  );
  if (!subArea) return JSON.stringify({ err: "no subArea", catText });
  const rows = [...subArea.querySelectorAll("div")].filter((d) => {
    const cs = getComputedStyle(d);
    return cs.display === "flex" && d.children.length >= 2 && Math.round(d.getBoundingClientRect().height) >= 12;
  });
  return JSON.stringify({
    catText,
    subAreaTag: subArea.tagName,
    subAreaClass: (subArea.className || "").toString().slice(0, 80),
    subAreaChildCount: subArea.children.length,
    directChildren: [...subArea.children].map((c) => ({
      tag: c.tagName, cls: (c.className || "").toString().slice(0, 60),
      h: Math.round(c.getBoundingClientRect().height),
      text: (c.textContent || "").trim().slice(0, 40),
    })),
    censusRows: rows.map((d) => {
      const cs = getComputedStyle(d);
      return {
        h: Math.round(d.getBoundingClientRect().height),
        pad: cs.padding, bg: cs.backgroundColor,
        cls: (d.className || "").toString().slice(0, 50),
        text: (d.textContent || "").trim().slice(0, 40),
        spans: [...d.querySelectorAll("span")].map((s) => ({
          t: (s.textContent || "").trim().slice(0, 16),
          maxW: getComputedStyle(s).maxWidth, trunc: getComputedStyle(s).textOverflow,
        })).slice(0, 4),
      };
    }),
  });
})()'

export AGENT_BROWSER_SESSION="refdump60"
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

echo "=== REF sub-area row dump at 1280 ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 4
agent-browser eval "$DUMP" 2>/dev/null | tail -1

echo "=== ref item dump done ==="
