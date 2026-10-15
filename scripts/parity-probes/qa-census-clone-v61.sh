#!/usr/bin/env bash
# qa-census-clone-v61.sh — the v61 DOM census, CLONE side: the Budget
# Guidelines card + the quick-action card row on the DASHBOARD at desktop
# 1280x800 (inside with-server on :3200). The same census body as the
# reference side + the CROSS-ROW GAP arbitration (the guidelines row's
# bottom edge to the quick-action grid's top edge — the reference's grid
# computes marginTop 0, its spacing may live on an ancestor; the GEOMETRY
# is the contract, the DOM shape is not — the v45 lesson).
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneqa61"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4

echo "=== GUIDELINES CENSUS (clone) ==="
agent-browser eval "(function () {
  const out = {};
  const heading = [...document.querySelectorAll(\"h1, h2, h3, div, span\")].find(
    (x) => (x.textContent || \"\").trim() === \"Budget Guidelines\" && x.children.length === 0
  );
  if (!heading) return JSON.stringify({ error: \"no guidelines heading\" });
  let card = heading;
  while (card.parentElement) {
    const cs = getComputedStyle(card);
    if (cs.boxShadow !== \"none\" && cs.borderRadius !== \"0px\" && card.querySelector(\"p\")) break;
    card = card.parentElement;
  }
  const csC = getComputedStyle(card);
  const rC = card.getBoundingClientRect();
  out.card = {
    w: Math.round(rC.width), h: Math.round(rC.height),
    radius: csC.borderRadius, border: csC.borderTopColor + \" \" + csC.borderTopWidth,
    bg: csC.backgroundColor, shadow: csC.boxShadow
  };
  const header = heading.parentElement;
  const csH = getComputedStyle(header);
  out.header = {
    pad: csH.padding, rowGap: csH.rowGap,
    fs: getComputedStyle(heading).fontSize, fw: getComputedStyle(heading).fontWeight,
    color: getComputedStyle(heading).color,
    lineHeight: getComputedStyle(heading).lineHeight, tracking: getComputedStyle(heading).letterSpacing
  };
  const body = [...card.children].find((c) => c !== header);
  if (!body) return JSON.stringify({ error: \"no body\", out: out });
  const csB = getComputedStyle(body);
  out.body = { pad: csB.padding, display: csB.display, rowGap: csB.rowGap };
  const tiles = [...card.querySelectorAll(\"div\")].filter((d) => {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return cs.borderRadius === \"8px\" && r.height > 40 && r.height < 200 &&
      d.querySelector(\"span, p\") && cs.backgroundColor !== \"rgba(0, 0, 0, 0)\" && d !== card;
  });
  out.tileCount = tiles.length;
  out.tiles = tiles.map((t) => {
    const cs = getComputedStyle(t);
    const r = t.getBoundingClientRect();
    const label = t.querySelector(\"span\");
    const pct = [...t.querySelectorAll(\"span\")].pop();
    const desc = t.querySelector(\"p\");
    return {
      w: Math.round(r.width), h: Math.round(r.height),
      radius: cs.borderRadius, pad: cs.padding,
      bg: cs.backgroundColor, border: cs.borderTopColor + \" \" + cs.borderTopWidth,
      label: label ? { text: (label.textContent || \"\").trim().slice(0, 10),
        fs: getComputedStyle(label).fontSize, fw: getComputedStyle(label).fontWeight,
        color: getComputedStyle(label).color } : null,
      pct: pct ? { text: (pct.textContent || \"\").trim().slice(0, 8),
        fs: getComputedStyle(pct).fontSize, fw: getComputedStyle(pct).fontWeight,
        color: getComputedStyle(pct).color } : null,
      desc: desc ? { fs: getComputedStyle(desc).fontSize,
        color: getComputedStyle(desc).color,
        lh: getComputedStyle(desc).lineHeight } : null
    };
  });
  return JSON.stringify(out);
})()" 2>/dev/null | tail -1

echo "=== QUICK-ACTION CENSUS (clone) ==="
agent-browser eval "(function () {
  const out = {};
  const qas = [...document.querySelectorAll(\"button\")].filter(
    (b) => /^Add (Income|Savings|Expense)$/.test((b.textContent || \"\").trim())
  );
  if (!qas.length) return JSON.stringify({ error: \"no quick-action buttons\" });
  const grid = qas[0].parentElement;
  const csG = getComputedStyle(grid);
  out.grid = {
    display: csG.display, template: csG.gridTemplateColumns,
    gap: csG.columnGap, w: Math.round(grid.getBoundingClientRect().width),
    mt: csG.marginTop
  };
  out.cards = qas.map((b) => {
    const cs = getComputedStyle(b);
    const r = b.getBoundingClientRect();
    const tileEl = [...b.querySelectorAll(\"span, div\")].find((s) => {
      const st = getComputedStyle(s);
      const sr = s.getBoundingClientRect();
      return st.borderRadius === \"12px\" && sr.width >= 30 && sr.width <= 60 && sr.height >= 30 && sr.height <= 60;
    });
    const label = [...b.querySelectorAll(\"span\")].find((s) =>
      /Add (Income|Savings|Expense)/.test((s.textContent || \"\").trim()));
    const svgs = [...b.querySelectorAll(\"svg\")];
    const iconSvg = svgs[0];
    const plusSvg = svgs[svgs.length - 1];
    return {
      text: (b.textContent || \"\").trim(),
      w: Math.round(r.width), h: Math.round(r.height),
      radius: cs.borderRadius, pad: cs.padding,
      bg: cs.backgroundColor, border: cs.borderTopColor + \" \" + cs.borderTopWidth,
      shadow: cs.boxShadow, textAlign: cs.textAlign, transition: cs.transitionDuration,
      tile: tileEl ? {
        w: Math.round(tileEl.getBoundingClientRect().width),
        h: Math.round(tileEl.getBoundingClientRect().height),
        radius: getComputedStyle(tileEl).borderRadius,
        bg: getComputedStyle(tileEl).backgroundColor
      } : null,
      icon: iconSvg ? {
        w: Math.round(iconSvg.getBoundingClientRect().width),
        h: Math.round(iconSvg.getBoundingClientRect().height),
        color: getComputedStyle(iconSvg).color
      } : null,
      label: label ? {
        fs: getComputedStyle(label).fontSize, fw: getComputedStyle(label).fontWeight,
        color: getComputedStyle(label).color
      } : null,
      plus: plusSvg && svgs.length > 1 ? {
        w: Math.round(plusSvg.getBoundingClientRect().width),
        h: Math.round(plusSvg.getBoundingClientRect().height),
        opacity: getComputedStyle(plusSvg).opacity,
        color: getComputedStyle(plusSvg).color
      } : null
    };
  });
  return JSON.stringify(out);
})()" 2>/dev/null | tail -1

echo "=== CROSS-ROW GAP (clone): guidelines card bottom -> quick grid top ==="
agent-browser eval "(function () {
  const qas = [...document.querySelectorAll(\"button\")].filter(
    (b) => /^Add Income$/.test((b.textContent || \"\").trim())
  );
  const heading = [...document.querySelectorAll(\"h1, h2, h3, div, span\")].find(
    (x) => (x.textContent || \"\").trim() === \"Budget Guidelines\" && x.children.length === 0
  );
  if (!qas.length || !heading) return JSON.stringify({ error: \"missing surfaces\" });
  let card = heading;
  while (card.parentElement) {
    const cs = getComputedStyle(card);
    if (cs.boxShadow !== \"none\" && cs.borderRadius !== \"0px\" && card.querySelector(\"p\")) break;
    card = card.parentElement;
  }
  let grid = qas[0].parentElement;
  const gap = grid.getBoundingClientRect().top - card.getBoundingClientRect().bottom;
  return JSON.stringify({
    gap: Math.round(gap),
    gridCls: (grid.className || \"\").toString().slice(0, 60),
    gridMt: getComputedStyle(grid).marginTop,
    gridParentMt: getComputedStyle(grid.parentElement).marginTop,
    cardBottom: Math.round(card.getBoundingClientRect().bottom),
    gridTop: Math.round(grid.getBoundingClientRect().top)
  });
})()" 2>/dev/null | tail -1
echo "=== clone qa census v61 done ==="
EOF
