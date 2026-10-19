#!/usr/bin/env bash
# savings-filter-arbit-v92.sh — the ONE-SHOT census for the v92 pin's own
# axes, REFERENCE half (the v87/v88/v89/v90/v91 supplemental precedent,
# BUILT TWO-HALF from the start — the cycle's combined arbit-v92.sh
# already showed the chromium resource exhaustion once): the SAVINGS
# variant's FILTER-CARD interior census at desktop 1280 — the v91 pin
# family's THIRD variant (income + expenses pinned v91; the savings
# variant never) PLUS the SEARCH ICON's computed chrome (the filter
# card's last never-pinned element — the magnifier svg's w/h/color/
# position/left never pinned at ANY viewport on ANY view; the glyph
# spec holds the PATH data only, the class-string test the w-5
# SUBSTRING only).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences; no
# backticks; no literal attribute-value selectors with brackets in
# strings.
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
    const sr = search.getBoundingClientRect();
    out.search = {
      tag: search.tagName,
      type: search.type,
      w: Math.round(sr.width),
      h: Math.round(sr.height),
      fs: srcs.fontSize,
      fw: srcs.fontWeight,
      lh: srcs.lineHeight,
      color: srcs.color,
      placeholder: (search.getAttribute('placeholder') || '').slice(0, 30),
      pad: srcs.padding,
      radius: srcs.borderRadius,
    };
    const wrapper = search.parentElement;
    const icon = wrapper ? wrapper.querySelector('svg') : null;
    if (icon) {
      const ics = getComputedStyle(icon);
      const ir = icon.getBoundingClientRect();
      out.searchIcon = {
        tag: icon.tagName,
        w: Math.round(ir.width),
        h: Math.round(ir.height),
        color: ics.color,
        position: ics.position,
        left: ics.left,
      };
    }
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
    const fcs = getComputedStyle(filterCard);
    const fr = filterCard.getBoundingClientRect();
    out.filterCard = {
      w: Math.round(fr.width),
      h: Math.round(fr.height),
      pad: fcs.padding,
      radius: fcs.borderRadius,
      bg: fcs.backgroundColor,
      borderC: fcs.borderTopColor,
    };
  }
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (1280, savings) ==="
export AGENT_BROWSER_SESSION="reffiltsv92"
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
echo "--- ref savings filter interiors + search icon ---"
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== savings-filter ref half done ==="
