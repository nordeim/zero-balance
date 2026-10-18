#!/usr/bin/env bash
# wrapper-arbit-v85.sh — the ONE-SHOT both-sides census for the v85 pin's
# family: the expense card's CONTENT WRAPPER (the expenses-conditional
# pr-24 left column — the room reserved for the hover action row) + the
# TITLE ROW's full geometry on the expenses view (the never-pinned orange
# dot family) + the income twin's paddingRight-0 control. The v80
# precedent: the savings titleRow's full geometry was pinned from its own
# one-shot census; this probe completes the per-type trilogy's expenses
# twin + the wrapper family never censused at 1280.
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors (geometry + text-content
# filters only).
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
      // titleRow = h4's parent; wrapper = titleRow's parent (the flex-1
      // pr-24 column on expenses / the plain flex-1 on income+savings)
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
        // the subtitle P inside the wrapper (the conditional twin)
        const subP = [...wrapper.children].find((ch) => ch.tagName === 'P');
        out.subtitle = subP
          ? {
              h: Math.round(subP.getBoundingClientRect().height),
              fs: getComputedStyle(subP).fontSize,
              text: (subP.textContent || '').trim().slice(0, 16),
            }
          : null;
      }
      // the header row (the wrapper's parent) for context
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
    // the hover action row (the expenses-only absolute family — the
    // pr-24's reason): top/right/opacity re-measured
    const actionRow = [...card.children].find(
      (ch) => getComputedStyle(ch).position === 'absolute' && (ch.textContent || '').includes('Calculate'),
    );
    if (actionRow) {
      const ar = actionRow.getBoundingClientRect();
      const acs = getComputedStyle(actionRow);
      out.actionRow = {
        top: Math.round(ar.top),
        right: Math.round(window.innerWidth - ar.right),
        opacity: acs.opacity,
        display: acs.display,
        gap: acs.gap,
      };
    }
  }
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="refwrap85"
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
echo "--- ref expenses ---"
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- ref income (the pr-0 control) ---"
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonewrap85"
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
echo "--- clone expenses ---"
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- clone income (the pr-0 control) ---"
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== wrapper arbit v85 done ==="
