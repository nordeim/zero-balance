#!/usr/bin/env bash
# wrapper-arbit-v86.sh — the ONE-SHOT both-sides census for the v86 pin's
# family: the savings goal-card's SUBTITLE P (the 1280 state of the v51
# F3 390-only family — the fs/color held at 390, the lh + the full box
# never, and NO 1280 subtitle pin anywhere) + the HEADER-ROW's
# with-subtitle arithmetic (the 48 = 24 titleRow + 4 mb-1 + 20 P twin of
# the 390 Rent-card family) + the WRAPPER's savings paddingRight-0 THIRD
# LEG (the v85 conditional trilogy's savings twin — expenses 96px /
# income 0px pinned, savings never). The v84/v85 one-shot precedent: the
# pin's expected values are THIS census's own measured values,
# byte-identical on both sides' savings views at 1280x800.
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors (geometry + text-content
# filters only — the v78 rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const out = { url: location.pathname };
  const grid = [...document.querySelectorAll('div')].find(
    (d) => typeof d.className === 'string' && d.className.includes('grid-cols-3'),
  );
  if (grid) {
    const card = grid.children[0];
    // the h4: the category title
    const h4 = [...card.querySelectorAll('h1,h2,h3,h4')][0];
    if (h4) {
      // titleRow = h4's parent; wrapper = titleRow's parent (the plain
      // flex-1 column on savings — the pr-24 conditional's third leg)
      const row = h4.parentElement;
      const wrapper = row ? row.parentElement : null;
      if (row) {
        const rcs = getComputedStyle(row);
        const dot = [...row.querySelectorAll('div,span')].find((d) => {
          const b = d.getBoundingClientRect();
          return b.width > 0 && b.width <= 12 && b.height > 0 && b.height <= 12;
        });
        out.titleRow = {
          display: rcs.display,
          alignItems: rcs.alignItems,
          gap: rcs.gap,
          h: Math.round(row.getBoundingClientRect().height),
          dotW: dot ? Math.round(dot.getBoundingClientRect().width) : null,
          dotH: dot ? Math.round(dot.getBoundingClientRect().height) : null,
          dotRadius: dot ? getComputedStyle(dot).borderRadius : null,
          dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
          h4Fs: getComputedStyle(h4).fontSize,
          h4Fw: getComputedStyle(h4).fontWeight,
          h4Color: getComputedStyle(h4).color,
          h4Text: (h4.textContent || '').trim().slice(0, 16),
        };
      }
      if (wrapper) {
        const wcs = getComputedStyle(wrapper);
        out.wrapper = {
          display: wcs.display,
          flexGrow: wcs.flexGrow,
          paddingRight: wcs.paddingRight,
          w: Math.round(wrapper.getBoundingClientRect().width),
          h: Math.round(wrapper.getBoundingClientRect().height),
        };
        // the subtitle P inside the wrapper (the v86 pin's own family:
        // the full chrome — h + fs + lh + color + text; the text the
        // seed/user-data class, the chrome the pin)
        const subP = [...wrapper.children].find((ch) => ch.tagName === 'P');
        out.subtitle = subP
          ? {
              h: Math.round(subP.getBoundingClientRect().height),
              fs: getComputedStyle(subP).fontSize,
              lh: getComputedStyle(subP).lineHeight,
              color: getComputedStyle(subP).color,
              mt: getComputedStyle(subP).marginTop,
              text: (subP.textContent || '').trim().slice(0, 20),
            }
          : null;
        // the titleRow's mb (the 4px mb-1 spacing between the row and P)
        out.titleRowMb = row ? getComputedStyle(row).marginBottom : null;
      }
      // the header row (the wrapper's parent): the with-subtitle
      // arithmetic context (h 48 = 24 + 4 + 20 on both sides)
      const headerRow = wrapper ? wrapper.parentElement : null;
      if (headerRow) {
        const hrs = getComputedStyle(headerRow);
        out.headerRow = {
          display: hrs.display,
          justify: hrs.justifyContent,
          alignItems: hrs.alignItems,
          h: Math.round(headerRow.getBoundingClientRect().height),
          mb: hrs.marginBottom,
        };
      }
    }
    // the card's own box for the height-arithmetic context (the v80
    // heights pin's own family — the 200/230 decomposition)
    out.cardH = Math.round(card.getBoundingClientRect().height);
  }
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280, /savings) ==="
export AGENT_BROWSER_SESSION="refwrap86"
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /savings) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonewrap86"
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
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== wrapper arbit v86 done ==="
