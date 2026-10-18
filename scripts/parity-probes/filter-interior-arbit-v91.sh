#!/usr/bin/env bash
# filter-interior-arbit-v91.sh — the ONE-SHOT both-sides census for the
# v91 pin's own axes (the v87/v88/v89/v90 supplemental precedent): the
# FILTER-CARD INTERACTIVE INTERIORS at desktop 1280 — the never-pinned
# families: the combobox triggers' RESTING chrome (pad/justify/bg/radius/
# border/chevron svg size+color — the v37 S1 pin holds the FOCUS state
# only, the v64/v70 pins the w/h/fs/text geometry) + the search input's
# TYPOGRAPHY (fs/fw/lh/color — the v64 pin holds the geometry+pad+radius+
# border, the v37 S2 pin the focus ring). Executed in the TWO-HALF
# controlled form (the v89 lesson — this cycle's combined arbit-v91.sh
# timed out in the chromium resource exhaustion; the JS-identity contract
# is the two halves' byte-identical census block).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences; no backticks;
# unquoted attribute-value selectors only.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  const out = { url: location.pathname };
  const search = [...document.querySelectorAll('input')].find(
    (i) => i.getBoundingClientRect().width > 100,
  );
  const filterCard = search ? search.closest('div.rounded-2xl') : null;
  if (search && filterCard) {
    const srcs = getComputedStyle(search);
    out.searchTypography = {
      tag: search.tagName,
      type: search.type,
      fs: srcs.fontSize,
      fw: srcs.fontWeight,
      lh: srcs.lineHeight,
      color: srcs.color,
      placeholder: (search.getAttribute('placeholder') || '').slice(0, 30),
      pad: srcs.padding,
      radius: srcs.borderRadius,
    };
    const inner = [...filterCard.children].find(
      (c) => getComputedStyle(c).display === 'grid',
    );
    out.triggers = inner
      ? [...inner.querySelectorAll('[role=combobox]')].map((c) => {
          const r = c.getBoundingClientRect();
          const cs = getComputedStyle(c);
          const chev = c.querySelector('svg');
          const chcs = chev ? getComputedStyle(chev) : null;
          const chr = chev ? chev.getBoundingClientRect() : null;
          return {
            tag: c.tagName,
            w: Math.round(r.width),
            h: Math.round(r.height),
            pad: cs.padding,
            justify: cs.justifyContent,
            align: cs.alignItems,
            bg: cs.backgroundColor,
            radius: cs.borderRadius,
            borderW: cs.borderTopWidth,
            borderC: cs.borderTopColor,
            fs: cs.fontSize,
            fw: cs.fontWeight,
            color: cs.color,
            text: (c.textContent || '').trim().slice(0, 22),
            chevW: chr ? Math.round(chr.width) : null,
            chevH: chr ? Math.round(chr.height) : null,
            chevColor: chcs ? chcs.color : null,
          };
        })
      : [];
  }
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="reffiltr91"
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
echo "--- ref income filter interiors ---"
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- ref expenses filter interiors ---"
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== filter-interior ref half done ==="
