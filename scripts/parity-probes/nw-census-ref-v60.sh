#!/usr/bin/env bash
# nw-census-ref-v60.sh — the v60 networth-view DOM arbitration census,
# REFERENCE side (the v43 rule: every VLM flag is DOM-verified before it
# counts) + the v60 pin's measurement source. Captures the summary card's
# full chrome, the tablist, the type-group header, the card grid + the
# first asset card at the 1280x800 pair viewport — the v41 (640/390) and
# v46/v50/v53 pin families' axes re-measured at 1280 on the reference's
# OWN data (1 asset, net +$25,000, ratio ∞:1 — the data classes).
# READ-ONLY (the v46 rule).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

CENSUS='(async () => {
  const out = { view: "networth-ref-1280" };
  // --- the summary card (the "Total Net Worth" label anchor) ---
  const label = [...document.querySelectorAll("p, span, h2, div")].find(
    (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0
  );
  if (!label) return JSON.stringify({ err: "no summary label" });
  const card = label.closest("div.rounded-2xl") || label.closest("[class*=\"rounded-2xl\"]");
  if (!card) return JSON.stringify({ err: "no summary card" });
  const cr = card.getBoundingClientRect();
  const cs = getComputedStyle(card);
  out.pageSW = document.documentElement.scrollWidth;
  out.columnW = Math.round(cr.width);
  out.summary = {
    w: Math.round(cr.width), pad: cs.padding, radius: cs.borderRadius,
    bg: (cs.backgroundImage || "").replace(/\s+/g, " ").slice(0, 110),
    shadow: (cs.boxShadow || "").replace(/\s+/g, " ").slice(0, 80),
    mb: cs.marginBottom,
  };
  // the figure (the net-worth amount)
  const h2 = [...card.querySelectorAll("h1, h2, h3, p")].find(
    (e) => /-?[$][\d,]+\.\d{2}/.test((e.textContent || "").trim()) && e !== label
  );
  if (h2) {
    const s = getComputedStyle(h2);
    out.figure = { fs: s.fontSize, fw: s.fontWeight, color: s.color, wb: s.wordBreak === "break-word" || s.overflowWrap === "break-word" };
  }
  // the label
  const ls = getComputedStyle(label);
  out.sumLabel = { fs: ls.fontSize, color: ls.color, mb: ls.marginBottom };
  // the medallion (the round icon chip in the card head)
  const chip = [...card.querySelectorAll("div")].find((d) => {
    const r = d.getBoundingClientRect();
    const c = getComputedStyle(d);
    return r.width > 40 && r.width < 90 && c.borderRadius === "9999px" && d.querySelector("svg");
  });
  if (chip) {
    const c = getComputedStyle(chip);
    const svg = chip.querySelector("svg");
    out.medallion = {
      w: Math.round(chip.getBoundingClientRect().width),
      h: Math.round(chip.getBoundingClientRect().height),
      bg: c.backgroundColor, svgW: svg ? Math.round(svg.getBoundingClientRect().width) : null,
    };
  }
  // the stats grid + tiles
  const assetsLabel = [...card.querySelectorAll("p, span")].find(
    (e) => (e.textContent || "").trim() === "Total Assets"
  );
  if (assetsLabel) {
    const grid = assetsLabel.closest("[class*=\"grid\"]");
    if (grid) {
      const g = getComputedStyle(grid);
      out.statGrid = { template: g.gridTemplateColumns, gap: g.gap, display: g.display };
      const tile = assetsLabel.closest("[class*=\"rounded\"]");
      if (tile) {
        const t = getComputedStyle(tile);
        const amt = [...tile.querySelectorAll("p, span")].find((e) => e !== assetsLabel && /[$]/.test(e.textContent || ""));
        out.statTile = {
          w: Math.round(tile.getBoundingClientRect().width), pad: t.padding, radius: t.borderRadius,
          bg: t.backgroundColor, blur: t.backdropFilter,
          labelFs: getComputedStyle(assetsLabel).fontSize, labelColor: getComputedStyle(assetsLabel).color,
          amtFs: amt ? getComputedStyle(amt).fontSize : null, amtFw: amt ? getComputedStyle(amt).fontWeight : null,
        };
      }
    }
  }
  // the ratio footer
  const ratioLabel = [...card.querySelectorAll("span, p, div")].find(
    (e) => /Asset to Liability Ratio/.test(e.textContent || "") && e.children.length === 0
  );
  if (ratioLabel) {
    const row = ratioLabel.closest("div");
    const r = getComputedStyle(row);
    const val = [...(ratioLabel.parentElement?.children || [])].find((e) => e !== ratioLabel);
    out.ratioFooter = {
      mt: r.marginTop, pt: r.paddingTop,
      borderTop: r.borderTopWidth + " " + r.borderTopStyle + " " + r.borderTopColor,
      labelFs: getComputedStyle(ratioLabel).fontSize,
      valText: val ? (val.textContent || "").trim().slice(0, 12) : null,
      valFs: val ? getComputedStyle(val).fontSize : null,
      valFw: val ? getComputedStyle(val).fontWeight : null,
    };
  }
  // --- the tablist ---
  const tablist = document.querySelector("[role=\"tablist\"]");
  if (tablist) {
    const t = getComputedStyle(tablist);
    const trigs = [...tablist.querySelectorAll("[role=\"tab\"]")];
    const first = trigs[0];
    const fcs = first ? getComputedStyle(first) : null;
    out.tablist = {
      w: Math.round(tablist.getBoundingClientRect().width),
      h: Math.round(tablist.getBoundingClientRect().height),
      template: t.gridTemplateColumns, gap: t.gap,
      trigH: first ? Math.round(first.getBoundingClientRect().height) : null,
      trigPad: fcs ? fcs.padding : null, trigFs: fcs ? fcs.fontSize : null, trigFw: fcs ? fcs.fontWeight : null,
      trigIconW: first && first.querySelector("svg") ? Math.round(first.querySelector("svg").getBoundingClientRect().width) : null,
      n: trigs.length,
    };
  }
  // --- the type-group header + the card grid + the first card ---
  // (the Assets tab is the default; the reference owns 1 asset)
  const h3 = [...document.querySelectorAll("h3")].find(
    (e) => /capitalize/.test((e.className || "").toString()) || (e.textContent || "").trim().length > 3
  );
  const groupH = h3 && h3.getBoundingClientRect().height > 0 ? h3 : [...document.querySelectorAll("h3")].find((e) => e.getBoundingClientRect().height > 0);
  if (groupH) {
    const s = getComputedStyle(groupH);
    out.groupHeader = {
      text: (groupH.textContent || "").trim().slice(0, 24), fs: s.fontSize, fw: s.fontWeight,
      color: s.color, mb: s.marginBottom, tt: s.textTransform,
    };
    const grid = groupH.nextElementSibling;
    if (grid && getComputedStyle(grid).display === "grid") {
      const g = getComputedStyle(grid);
      out.grid = {
        w: Math.round(grid.getBoundingClientRect().width),
        template: g.gridTemplateColumns, gap: g.gap, n: grid.children.length,
      };
      const c0 = grid.children[0];
      const ccs = getComputedStyle(c0);
      // the kebab (the actions trigger) — at-rest opacity
      const kebab = [...c0.querySelectorAll("button")].find((b) => {
        const r = b.getBoundingClientRect();
        return r.width <= 40 && (b.getAttribute("aria-label") || "").includes("Actions");
      });
      const dot = [...c0.querySelectorAll("div")].find((d) => {
        const r = d.getBoundingClientRect();
        return !d.children.length && r.width > 4 && r.width <= 12 && getComputedStyle(d).borderRadius === "9999px";
      });
      const name = c0.querySelector("h4");
      const badge = [...c0.querySelectorAll("span")].find((s) => {
        const r = s.getBoundingClientRect();
        const c = getComputedStyle(s);
        return r.height > 14 && r.height < 32 && c.fontSize === "12px" && !s.querySelector("svg");
      });
      const value = [...c0.querySelectorAll("p")].find((p) => /[$]/.test(p.textContent || ""));
      const footLine = [...c0.querySelectorAll("div")].find((d) => {
        const s = getComputedStyle(d);
        return s.display === "flex" && /Updated/.test(d.textContent || "") && d.children.length <= 2;
      });
      out.card = {
        w: Math.round(c0.getBoundingClientRect().width), pad: ccs.padding, radius: ccs.borderRadius,
        border: ccs.borderTopWidth + " " + ccs.borderTopStyle + " " + ccs.borderTopColor,
        bg: ccs.backgroundColor, shadow: (ccs.boxShadow || "").replace(/\s+/g, " ").slice(0, 60),
        kebabOpacityAtRest: kebab ? getComputedStyle(kebab).opacity : null,
        dotW: dot ? Math.round(dot.getBoundingClientRect().width) : null,
        dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
        nameFs: name ? getComputedStyle(name).fontSize : null, nameFw: name ? getComputedStyle(name).fontWeight : null,
        badgePad: badge ? getComputedStyle(badge).padding : null,
        badgeBg: badge ? getComputedStyle(badge).backgroundColor : null,
        valueFs: value ? getComputedStyle(value).fontSize : null,
        valueMb: value ? getComputedStyle(value).marginBottom : null,
        footFs: footLine ? getComputedStyle(footLine).fontSize : null,
      };
    }
  }
  return JSON.stringify(out);
})()'

export AGENT_BROWSER_SESSION="refnw60"
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

echo "=== REF /networth census at 1280 (summary + tablist + group + grid + card) ==="
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS" 2>/dev/null | tail -1

echo "=== ref networth census v60 done ==="
