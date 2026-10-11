// v44: the drill-down EXPANDED-state census at the REMAINING viewports —
// 390x844 (the mobile indentation arithmetic + the overflow fully expanded)
// and 1280x800 (the category-row wrap behavior). The v43 session pinned the
// 640x960 class byte-for-byte; this completes the viewport matrix. ALSO
// probes the reference's expansion ANIMATION (its overflow-hidden wrappers
// carry style height/opacity — a JS-driven collapse animation the clone may
// lack: mount-instant vs animated). UI-state-only clicks; no data mutation.
// bash scripts/parity-probes/run-probe.sh <session> scripts/parity-probes/exp-vp-v44.mjs
(async () => {
  const leaf = (txt) =>
    [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(
      (e) => (e.textContent || '').trim() === txt && e.children.length === 0,
    );
  const bdH = leaf('Net Zero Breakdown');
  const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
  if (!card) return JSON.stringify({ found: false, step: 'card' });
  const cardR = card.getBoundingClientRect();
  const out = {
    vw: innerWidth,
    cardW: Math.round(cardR.width),
    collapsedH: Math.round(cardR.height),
  };

  // The section toggle (the row containing "Total Income").
  const sectionBtn = [...card.querySelectorAll('button,[role="button"]')].find(
    (b) => /Total Income/i.test(b.textContent || ''),
  );
  if (!sectionBtn) return JSON.stringify({ found: false, step: 'sectionBtn', out });
  const sR = sectionBtn.getBoundingClientRect();
  const sCs = getComputedStyle(sectionBtn);
  out.section = {
    h: Math.round(sR.height),
    w: Math.round(sR.width),
    pad: sCs.padding,
    font: sCs.fontSize,
    labelH: (() => {
      const l = [...sectionBtn.querySelectorAll('span')].find(
        (s) => /Total Income/i.test(s.textContent || '') && s.children.length === 0,
      );
      return l ? Math.round(l.getBoundingClientRect().height) : null;
    })(),
  };

  // EXPAND the section — SAMPLE the height mid-expansion (the animation
  // check: an animated wrapper reads intermediate heights; an instant mount
  // jumps straight to the end state).
  const t0 = performance.now();
  sectionBtn.click();
  const samples = [];
  for (let i = 0; i < 10; i++) {
    samples.push(Math.round(card.getBoundingClientRect().height));
    await new Promise((r) => setTimeout(r, 40));
  }
  out.expandSamples = samples; // ~400ms of samples post-click
  out.expandMs = Math.round(performance.now() - t0);
  out.secExpandedH = Math.round(card.getBoundingClientRect().height);

  // The expansion band + the indentation chain + the ANIMATION chrome.
  const wrap = sectionBtn.parentElement;
  const expArea = wrap
    ? [...wrap.children].find((c) => c !== sectionBtn && c.getBoundingClientRect().height > 0)
    : null;
  if (!expArea) return JSON.stringify({ found: false, step: 'expArea', out });
  const expCs = getComputedStyle(expArea);
  const inner = [...expArea.children].find((c) => c.getBoundingClientRect().height > 0) || expArea;
  const inCs = getComputedStyle(inner);
  out.indent = {
    expBox: {
      w: Math.round(expArea.getBoundingClientRect().width),
      ml: expCs.marginLeft,
      pl: expCs.paddingLeft,
      styleAttr: (expArea.getAttribute('style') || '').slice(0, 60),
      transition: expCs.transitionProperty,
      transitionDur: expCs.transitionDuration,
      overflow: expCs.overflow,
    },
    inner: { ml: inCs.marginLeft, mt: inCs.marginTop, w: Math.round(inner.getBoundingClientRect().width) },
  };

  // Category rows — h/w/pad/font/bg + the LABEL height (the wrap check: a
  // 2-line label reads ~2x the 16px line box).
  const catRows = [...inner.querySelectorAll('button,[role="button"]')].filter(
    (b) => b.offsetParent !== null && b !== sectionBtn,
  );
  const rowRead = (row) => {
    const r = row.getBoundingClientRect();
    const cs = getComputedStyle(row);
    const label = [...row.querySelectorAll('span')].find(
      (s) => (s.textContent || '').trim().length > 2 && s.children.length === 0,
    );
    return {
      h: Math.round(r.height),
      w: Math.round(r.width),
      pad: cs.padding,
      bg: cs.backgroundColor,
      font: cs.fontSize,
      ml: cs.marginLeft,
      labelH: label ? Math.round(label.getBoundingClientRect().height) : null,
      text: (row.textContent || '').replace(/\s+/g, ' ').slice(0, 24),
    };
  };
  out.cats = { count: catRows.length, list: catRows.slice(0, 3).map(rowRead) };

  // EXPAND the first category — sample mid-expansion heights again.
  if (catRows.length) {
    catRows[0].click();
    const catSamples = [];
    for (let i = 0; i < 10; i++) {
      catSamples.push(Math.round(card.getBoundingClientRect().height));
      await new Promise((r) => setTimeout(r, 40));
    }
    out.catExpandSamples = catSamples;
  }
  out.fullExpandedH = Math.round(card.getBoundingClientRect().height);

  // The sub band + its indentation; the sub rows (bg 250,250,250) and the
  // item rows (plain, gray) — classified by bg, nested rows deduped.
  const firstCatWrap = catRows.length ? catRows[0].parentElement : null;
  const subArea = firstCatWrap
    ? [...firstCatWrap.children].find((c) => c !== catRows[0] && c.getBoundingClientRect().height > 0)
    : null;
  if (subArea) {
    const subCs = getComputedStyle(subArea);
    out.subIndent = {
      ml: subCs.marginLeft,
      mt: subCs.marginTop,
      w: Math.round(subArea.getBoundingClientRect().width),
      styleAttr: (subArea.getAttribute('style') || '').slice(0, 60),
      transition: subCs.transitionProperty,
      transitionDur: subCs.transitionDuration,
    };
    const flexish = [...subArea.querySelectorAll('div')].filter((d) => {
      const cs = getComputedStyle(d);
      return cs.display === 'flex' && d.children.length >= 2 && Math.round(d.getBoundingClientRect().height) >= 14;
    });
    // dedupe: keep rows that contain no other matched row
    const rows = flexish.filter((d) => !flexish.some((o) => o !== d && d.contains(o)));
    const sub = rows.filter((d) => {
      const bg = getComputedStyle(d).backgroundColor;
      return bg !== 'rgba(0, 0, 0, 0)';
    });
    const item = rows.filter((d) => getComputedStyle(d).backgroundColor === 'rgba(0, 0, 0, 0)');
    out.subRows = sub.slice(0, 2).map(rowRead);
    out.itemRows = item.slice(0, 2).map((row) => {
      const r = rowRead(row);
      const lab = [...row.querySelectorAll('span')].find(
        (s) => (s.textContent || '').trim().length > 2 && s.children.length === 0,
      );
      const cs = lab ? getComputedStyle(lab) : null;
      r.labelChrome = cs
        ? {
            maxW: cs.maxWidth,
            textOverflow: cs.textOverflow,
            w: Math.round(lab.getBoundingClientRect().width),
            color: cs.color,
          }
        : null;
      return r;
    });
    const itemBand = item.length ? item[0].parentElement : null;
    if (itemBand) {
      const ibCs = getComputedStyle(itemBand);
      out.itemIndent = { ml: ibCs.marginLeft, mt: ibCs.marginTop };
    }
  }

  // The footer + the fully-expanded overflow guard.
  const footP = [...card.querySelectorAll('p,span')].find(
    (e) => /categor/i.test(e.textContent || '') && e.children.length === 0,
  );
  const footRow = footP ? footP.closest('div') : null;
  out.foot = footRow
    ? {
        h: Math.round(footRow.getBoundingClientRect().height),
        pad: getComputedStyle(footRow).padding,
        borderTop: getComputedStyle(footRow).borderTopWidth,
      }
    : null;
  out.sw = document.documentElement.scrollWidth;
  out.bodyScrollW = document.body.scrollWidth;
  return JSON.stringify(out);
})()
