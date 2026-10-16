#!/usr/bin/env bash
# arbit-v67b.sh — the v67 arbitration census, CLONE side (the v43 rule).
# The same two-part census as arbit-v67.sh against the :3200 parity server.
# Runs inside with-server.sh in ONE invocation. The quoted heredoc keeps the
# census JS free of bash expansion; the dollar sequences still avoided via
# String.fromCharCode(36) (the v64/v65/v66 rule).
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonear67"
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

echo "=== PART A: CLONE drill-down flag arbitration census at 1280 ==="
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval '(async () => {
  const out = { view: "drill-arbit-clone-1280-v67" };
  const D = String.fromCharCode(36);
  const links = [...document.querySelectorAll("a")];
  const dash = links.find((l) => /dashboard/i.test((l.textContent || "")) && l.getBoundingClientRect().height > 0 && l.getBoundingClientRect().left < 300);
  if (dash) {
    const s = getComputedStyle(dash);
    out.navHighlight = { bg: s.backgroundColor, color: s.color, radius: s.borderRadius, fw: s.fontWeight };
  }
  const avatar = [...document.querySelectorAll("div,span")].find((d) => {
    const r = d.getBoundingClientRect();
    const c = getComputedStyle(d);
    return !d.children.length && r.width > 24 && r.width < 60 && c.borderRadius === "9999px" && /^[A-Z]$/.test((d.textContent || "").trim());
  });
  out.avatarLetter = avatar ? (avatar.textContent || "").trim() : null;
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
})()' 2>/dev/null | tail -1

echo "=== PART B: CLONE networth summary-card HEIGHT family at 1280 ==="
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser eval '(async () => {
  const out = { view: "nw-height-clone-1280-v67" };
  const D = String.fromCharCode(36);
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
  const headRow = label.closest("div").parentElement;
  if (headRow) {
    const hr = headRow.getBoundingClientRect();
    const hcs = getComputedStyle(headRow);
    out.headRow = { h: Math.round(hr.height), mb: hcs.marginBottom, display: hcs.display, items: hcs.alignItems };
    const labelBlock = label.parentElement;
    const lbr = labelBlock ? labelBlock.getBoundingClientRect() : null;
    out.labelBlock = lbr ? { w: Math.round(lbr.width), h: Math.round(lbr.height) } : null;
  }
  const lcs = getComputedStyle(label);
  const lr = label.getBoundingClientRect();
  out.label = { fs: lcs.fontSize, color: lcs.color, mb: lcs.marginBottom, h: Math.round(lr.height) };
  const h2 = [...card.querySelectorAll("h1, h2, h3, p")].find(
    (e) => (e.textContent || "").includes(D) && e !== label
  );
  if (h2) {
    const h2cs = getComputedStyle(h2);
    const h2r = h2.getBoundingClientRect();
    out.figure = { fs: h2cs.fontSize, fw: h2cs.fontWeight, color: h2cs.color, lh: h2cs.lineHeight, h: Math.round(h2r.height) };
  }
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
})()' 2>/dev/null | tail -1

echo "=== clone arbit v67 done ==="
EOF
