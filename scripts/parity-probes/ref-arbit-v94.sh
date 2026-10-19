#!/usr/bin/env bash
# arbit-v94.sh — the v94 re-run pair's flags, DOM-arbitrated per the v43
# rule, at DESKTOP 1280x800 on BOTH sides (the v88-era pair's fresh sweep —
# the networth view + the dashboard drill-down EXPANDED state, last re-shot
# v88; the pair's FIFTH re-run [v60 → v67 → v76 → v82 → v88 → v94] — the
# SEVENTEENTH consecutive queue/ledger agreement). The censuses (the v88
# census axes re-measured — a drift re-check):
#   (1) PART A — the DRILL-DOWN census on the expanded dashboard: the nav
#       highlight (the v56 class), the avatar letter (user identity), the
#       hero progress fill (the pct data class), the donut labels (the v60
#       perception class), the stat cards' footer TREND ICONS (the v67
#       path-signature axes).
#   (2) PART B — the NETWORTH summary-card HEIGHT family at 1280 (the v67
#       F4 pin's own axes): the card chrome, the head row, the label block,
#       the figure, the medallion, the stat grid + first tile, the ratio
#       footer.
# READ-ONLY on both sides (login + passive navigation + view-state
# expansion clicks only — the v46 rule). The v73 heredoc lesson: the QUOTED
# <<'EOF' with the env-injected censuses; no literal dollar sequences in
# the census JS (the v64 rule — the amount leaf is found via
# String.fromCharCode(36)). The seedcheck at the end (the v66 discipline).
set -u
REF="https://zero-balance-4885a8f3.base44.app"


# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92/v93 lesson):
# the combined arbit form's clone half is the chromium resource-exhaustion
# risk (the v89/v91-documented symptom class), so the census runs as two
# independent halves from the start; the census JS blocks are byte-identical
# across the halves (the md5 line-block contract).

ARBIT_A='(async () => {
  const out = { view: "drill-arbit-1280-v94" };
  const D = String.fromCharCode(36);
  // (1) the nav highlight at the root URL (the v56 class)
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
  // (3) the hero progress fill: the track + the fill width (the pct data class)
  const track = [...document.querySelectorAll("div")].find((d) => {
    const r = d.getBoundingClientRect();
    const c = getComputedStyle(d);
    return r.width > 400 && r.height >= 10 && r.height <= 16 && c.borderRadius === "9999px" && /rgba/.test(c.backgroundColor);
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
  // (4) the DONUT PERCENTAGE LABELS — the recharts pie label text nodes
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
  // (5) the STAT CARDS footer TREND ICONS — the h-4 w-4 svg in the count row
  // (the v67 axes: byte-identical d attributes = a perception artifact).
  const statCards = [...document.querySelectorAll("div")].filter((d) => {
    const t = (d.textContent || "");
    return /Total Income/.test(t) && /Total Savings/.test(t) === false && d.querySelectorAll("svg").length > 0 && d.getBoundingClientRect().width > 200 && d.getBoundingClientRect().width < 500;
  });
  const card = statCards[0];
  if (card) {
    const svgs = [...card.querySelectorAll("svg")];
    const trendIcons = svgs.filter((s) => {
      const r = s.getBoundingClientRect();
      return Math.round(r.width) === 16 && Math.round(r.height) === 16;
    });
    out.statTrendIcons = trendIcons.map((s) => {
      const r = s.getBoundingClientRect();
      const cs = getComputedStyle(s);
      const path = s.querySelector("path");
      return {
        w: Math.round(r.width), h: Math.round(r.height),
        color: cs.color,
        pathSig: path ? (path.getAttribute("d") || "").slice(0, 46) : null,
        glyphSig: (s.innerHTML || "").replace(/\s+/g, " ").slice(0, 110),
        viewBox: s.getAttribute("viewBox"),
      };
    });
    out.statCardCount = statCards.length;
  }
  // the hero trend glyph (sign-conditional — the data class): the h-5 w-5 svg
  const hero = [...document.querySelectorAll("div")].find((d) => /NET ZERO GOAL/.test((d.textContent || "")) && d.getBoundingClientRect().width > 300);
  if (hero) {
    const big = [...hero.querySelectorAll("svg")].filter((s) => {
      const r = s.getBoundingClientRect();
      return Math.round(r.width) === 20 && Math.round(r.height) === 20;
    });
    out.heroTrendGlyphs = big.map((s) => {
      const path = s.querySelector("path");
      return { color: getComputedStyle(s).color, pathSig: path ? (path.getAttribute("d") || "").slice(0, 46) : null };
    });
  }
  return JSON.stringify(out);
})()'

ARBIT_B='(async () => {
  const out = { view: "nw-height-1280-v94" };
  const D = String.fromCharCode(36);
  // The summary card: from the "Total Net Worth" leaf up to the rounded-2xl.
  const label = [...document.querySelectorAll("p, span, h2, div")].find(
    (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0
  );
  if (!label) return JSON.stringify({ err: "no label" });
  const card = label.closest("div.rounded-2xl");
  if (!card) return JSON.stringify({ err: "no card" });
  const cr = card.getBoundingClientRect();
  const cs = getComputedStyle(card);
  out.card = {
    w: Math.round(cr.width), h: Math.round(cr.height),
    pad: cs.padding, radius: cs.borderRadius,
    bg: (cs.backgroundImage || "").replace(/\s+/g, " ").slice(0, 110),
    shadow: (cs.boxShadow || "").replace(/\s+/g, " ").slice(0, 80),
  };
  // The head row: the flex justify-between holding the label block + the medallion.
  const headRow = label.closest("div").parentElement;
  if (headRow) {
    const hr = headRow.getBoundingClientRect();
    const hcs = getComputedStyle(headRow);
    out.headRow = { h: Math.round(hr.height), mb: hcs.marginBottom, display: hcs.display, items: hcs.alignItems };
    // The label block (the min-w-0 wrapper) + the figure.
    const labelBlock = label.parentElement;
    const lbr = labelBlock ? labelBlock.getBoundingClientRect() : null;
    out.labelBlock = lbr ? { w: Math.round(lbr.width), h: Math.round(lbr.height) } : null;
  }
  const lcs = getComputedStyle(label);
  const lr = label.getBoundingClientRect();
  out.label = { fs: lcs.fontSize, color: lcs.color, mb: lcs.marginBottom, h: Math.round(lr.height) };
  // The figure (the D-prefixed amount heading).
  const h2 = [...card.querySelectorAll("h1, h2, h3, p")].find(
    (e) => (e.textContent || "").includes(D) && e !== label
  );
  if (h2) {
    const h2cs = getComputedStyle(h2);
    const h2r = h2.getBoundingClientRect();
    out.figure = { fs: h2cs.fontSize, fw: h2cs.fontWeight, color: h2cs.color, lh: h2cs.lineHeight, h: Math.round(h2r.height) };
  }
  // The medallion.
  const chip = [...card.querySelectorAll("div")].find((d) => {
    const r = d.getBoundingClientRect();
    const c = getComputedStyle(d);
    return r.width > 40 && r.width < 90 && c.borderRadius === "9999px" && d.querySelector("svg");
  });
  if (chip) {
    const svg = chip.querySelector("svg");
    const sr = svg ? svg.getBoundingClientRect() : null;
    out.medallion = {
      w: Math.round(chip.getBoundingClientRect().width),
      h: Math.round(chip.getBoundingClientRect().height),
      bg: getComputedStyle(chip).backgroundColor,
      iconW: sr ? Math.round(sr.width) : null,
      iconH: sr ? Math.round(sr.height) : null,
    };
  }
  // The stat grid + the first tile (Total Assets).
  const assetsLabel = [...card.querySelectorAll("p, span")].find(
    (e) => (e.textContent || "").trim() === "Total Assets"
  );
  if (assetsLabel) {
    const grid = assetsLabel.closest("[class*=grid]");
    if (grid) {
      const gr = grid.getBoundingClientRect();
      const gcs = getComputedStyle(grid);
      out.statGrid = { template: gcs.gridTemplateColumns, rows: gcs.gridTemplateRows, gap: gcs.gap, h: Math.round(gr.height), w: Math.round(gr.width) };
    }
    const tile = assetsLabel.closest("[class*=rounded]");
    if (tile) {
      const tr = tile.getBoundingClientRect();
      const tcs = getComputedStyle(tile);
      const amt = [...tile.querySelectorAll("p, span")].find((e) => e !== assetsLabel && (e.textContent || "").includes(D));
      const acs = amt ? getComputedStyle(amt) : null;
      const ar = amt ? amt.getBoundingClientRect() : null;
      const alr = assetsLabel.getBoundingClientRect();
      const alcs = getComputedStyle(assetsLabel);
      out.statTile = {
        w: Math.round(tr.width), h: Math.round(tr.height),
        pad: tcs.padding, radius: tcs.borderRadius, bg: tcs.backgroundColor, blur: tcs.backdropFilter,
        labelFs: alcs.fontSize, labelH: Math.round(alr.height), labelMb: alcs.marginBottom,
        amtFs: acs ? acs.fontSize : null, amtFw: acs ? acs.fontWeight : null, amtH: ar ? Math.round(ar.height) : null,
      };
    }
    // The ratio footer (the mt-6 pt-6 border-t block).
    const ratioLabel = [...card.querySelectorAll("span, p, div")].find(
      (e) => /Asset to Liability Ratio/.test(e.textContent || "") && e.children.length === 0
    );
    if (ratioLabel) {
      let footer = ratioLabel.closest("div").parentElement;
      let node = ratioLabel;
      while (node && node !== card) {
        const s = getComputedStyle(node);
        if (parseInt(s.borderTopWidth || "0") > 0) { footer = node; break; }
        node = node.parentElement;
      }
      const fcs = getComputedStyle(footer);
      const fr = footer.getBoundingClientRect();
      const val = [...(ratioLabel.parentElement?.children || [])].find((e) => e !== ratioLabel);
      out.ratioFooter = {
        mt: fcs.marginTop, pt: fcs.paddingTop, borderTopW: fcs.borderTopWidth,
        borderTopC: fcs.borderTopColor, h: Math.round(fr.height),
        labelFs: getComputedStyle(ratioLabel).fontSize,
        valFs: val ? getComputedStyle(val).fontSize : null,
        valFw: val ? getComputedStyle(val).fontWeight : null,
      };
    }
  }
  return JSON.stringify(out);
})()'

########## REFERENCE SIDE (the half) ##########
# ---------- REFERENCE side ----------
export AGENT_BROWSER_SESSION="refar94"
agent-browser open "$REF/login" >/dev/null 2>&1
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

echo "=== PART A: REF drill-down arbitration census at 1280 (expanded first) ==="
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const sec = [...card.querySelectorAll('button')].find(b => /Total Income/i.test(b.textContent||''));
  if (!sec) return 'no section';
  sec.click();
  const cat = [...card.querySelectorAll('button')].find(b => b.offsetParent !== null && /\\\$/.test(b.textContent||'') && !/Total|Net Balance/i.test(b.textContent||''));
  if (cat) cat.click();
  return 'expanded';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$ARBIT_A" 2>/dev/null | tail -1

echo "=== PART B: REF networth summary-card census at 1280 ==="
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$ARBIT_B" 2>/dev/null | tail -1
echo "=== ref arbit v94 half done ==="
