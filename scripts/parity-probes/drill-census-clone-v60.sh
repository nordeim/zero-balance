#!/usr/bin/env bash
# drill-census-clone-v60.sh — the v60 dashboard drill-down EXPANDED-state
# DOM arbitration census, CLONE side (the v43 rule) + the v60 pin's
# measurement source. The v43 F3 family re-measured at the 1280x800 pair
# viewport against db/custom.db (the dev seed: 2 income categories, the
# first with 1 sub + 1 item — the v44 F2b arithmetic 364→481→535).
# Runs inside with-server.sh in ONE invocation (the v27 lesson).
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonedr60"
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

echo "=== CLONE / drill-down expanded census at 1280 ==="
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval '(async () => {
  const out = { view: "drilldown-clone-1280" };
  const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
    (e) => (e.textContent || "").trim() === "Net Zero Breakdown" && e.children.length === 0
  );
  const card = leaf ? leaf.closest("div[class*=rounded-2xl]") : null;
  if (!card) return JSON.stringify({ err: "no breakdown card" });
  out.pageSW = document.documentElement.scrollWidth;
  out.cardW = Math.round(card.getBoundingClientRect().width);
  out.collapsedH = Math.round(card.getBoundingClientRect().height);
  const sec = [...card.querySelectorAll("button")].find((b) => /Total Income/i.test(b.textContent || ""));
  if (!sec) return JSON.stringify({ err: "no section" });
  const sCs = getComputedStyle(sec);
  const secLabel = [...sec.querySelectorAll("span")].find((s) => /Total Income/i.test(s.textContent || ""));
  out.section = {
    h: Math.round(sec.getBoundingClientRect().height), pad: sCs.padding,
    ml: sCs.marginLeft, radius: sCs.borderRadius, cursor: sCs.cursor,
    labelH: secLabel ? Math.round(secLabel.getBoundingClientRect().height) : null,
  };
  sec.click();
  await new Promise((r) => setTimeout(r, 600));
  out.secExpandedH = Math.round(card.getBoundingClientRect().height);
  const cat = [...card.querySelectorAll("button")].find(
    (b) => b.offsetParent !== null && /[$]/.test(b.textContent || "") && !/Total|Net Balance/i.test(b.textContent || "")
  );
  if (!cat) return JSON.stringify({ err: "no category" });
  const cCs = getComputedStyle(cat);
  const cDot = [...cat.querySelectorAll("span")].find((s) => {
    const r = s.getBoundingClientRect();
    return r.width > 0 && r.width <= 8 && getComputedStyle(s).borderRadius === "9999px";
  });
  const catLabel = [...cat.querySelectorAll("span")].find((s) => {
    const t = (s.textContent || "").trim();
    return t.length > 1 && s.children.length === 0 && !/^[$]/.test(t);
  });
  out.category = {
    h: Math.round(cat.getBoundingClientRect().height), pad: cCs.padding,
    radius: cCs.borderRadius, bg: cCs.backgroundColor,
    dotW: cDot ? Math.round(cDot.getBoundingClientRect().width) : null,
    labelFont: catLabel ? getComputedStyle(catLabel).fontSize : null,
    labelWeight: catLabel ? getComputedStyle(catLabel).fontWeight : null,
    labelColor: catLabel ? getComputedStyle(catLabel).color : null,
  };
  cat.click();
  await new Promise((r) => setTimeout(r, 600));
  out.fullExpandedH = Math.round(card.getBoundingClientRect().height);
  const subArea = [...cat.parentElement.children].find(
    (c) => c !== cat && c.getBoundingClientRect().height > 0
  );
  if (subArea) {
    const rows = [...subArea.querySelectorAll("div")].filter((d) => {
      const cs = getComputedStyle(d);
      return cs.display === "flex" && d.children.length >= 2 && Math.round(d.getBoundingClientRect().height) >= 16;
    });
    const subRow = rows[0];
    const itemRow = rows[rows.length - 1];
    const subLabel = subRow ? [...subRow.querySelectorAll("span")].find((s) => {
      const t = (s.textContent || "").trim();
      return t.length > 1 && s.children.length === 0 && !/^[$]/.test(t);
    }) : null;
    const itemLabel = itemRow ? [...itemRow.querySelectorAll("span")].find((s) => {
      const t = (s.textContent || "").trim();
      return t.length > 1 && s.children.length === 0 && !/^[$]/.test(t);
    }) : null;
    out.sub = subRow ? {
      h: Math.round(subRow.getBoundingClientRect().height),
      pad: getComputedStyle(subRow).padding, bg: getComputedStyle(subRow).backgroundColor,
      labelFont: subLabel ? getComputedStyle(subLabel).fontSize : null,
      labelWeight: subLabel ? getComputedStyle(subLabel).fontWeight : null,
      labelColor: subLabel ? getComputedStyle(subLabel).color : null,
    } : null;
    out.item = itemRow ? {
      h: Math.round(itemRow.getBoundingClientRect().height),
      pad: getComputedStyle(itemRow).padding,
      color: getComputedStyle(itemRow).color, font: getComputedStyle(itemRow).fontSize,
      labelMaxW: itemLabel ? getComputedStyle(itemLabel).maxWidth : null,
      labelTrunc: itemLabel ? getComputedStyle(itemLabel).textOverflow : null,
    } : null;
  }
  const footP = [...card.querySelectorAll("span")].find(
    (e) => /categor/i.test(e.textContent || "") && e.children.length === 0
  );
  const footRow = footP ? footP.closest("div") : null;
  out.footer = footRow ? {
    h: Math.round(footRow.getBoundingClientRect().height),
    pad: getComputedStyle(footRow).padding,
    borderTop: getComputedStyle(footRow).borderTopWidth,
    font: getComputedStyle(footP).fontSize, weight: getComputedStyle(footP).fontWeight,
  } : null;
  return JSON.stringify(out);
})()' 2>/dev/null | tail -1

echo "=== clone drill census v60 done ==="
EOF
