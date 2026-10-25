#!/usr/bin/env bash
# nwheader-wrapper-v118.sh — the WRAPPER CHILDREN census: does the
# reference's /networth header wrapper (flex flex-col md:flex-row
# justify-between items-start md:items-center gap-4 mb-8) carry a SECOND
# child beyond the chip+title row — a right-side element the clone may be
# missing entirely (the clone's /networth header is the bare
# mb-8 flex items-center gap-3 row, no wrapper)? Also measures the
# reference's DASHBOARD header wrapper for the pattern comparison (the
# clone's dashboard header uses the wrapper form — line 927).
# READ-ONLY (login + passive navigation only).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

WRAP_JS="(async () => {
  const out = { view: 'nw-wrap-1280-v118', docSW: document.documentElement.scrollWidth, vw: window.innerWidth };
  const h1 = [...document.querySelectorAll('main h1')].find(h => (h.textContent || '').trim() === 'Net Worth');
  if (!h1) return JSON.stringify({ h1: 'not found' });
  const block = h1.parentElement;
  const row = block && block.parentElement;
  const wrapper = row && row.parentElement;
  if (!wrapper) return JSON.stringify({ wrapper: 'not found' });
  const wcs = getComputedStyle(wrapper);
  const wr = wrapper.getBoundingClientRect();
  out.wrapper = {
    cls: (typeof wrapper.className === 'string' ? wrapper.className : '').slice(0, 140),
    display: wcs.display,
    justifyContent: wcs.justifyContent,
    gap: wcs.gap,
    mb: wcs.marginBottom,
    w: Math.round(wr.width),
    h: Math.round(wr.height),
    childCount: wrapper.children.length,
  };
  out.children = [...wrapper.children].map(c => {
    const ccs = getComputedStyle(c);
    const cr = c.getBoundingClientRect();
    return {
      tag: c.tagName,
      cls: (typeof c.className === 'string' ? c.className : '').slice(0, 100),
      w: Math.round(cr.width),
      h: Math.round(cr.height),
      right: Math.round(window.innerWidth - cr.right),
      text: (c.textContent || '').trim().slice(0, 60),
    };
  });
  return JSON.stringify(out);
})()"

DASH_JS="(async () => {
  const out = { view: 'dash-wrap-1280-v118', docSW: document.documentElement.scrollWidth, vw: window.innerWidth };
  const h1 = [...document.querySelectorAll('main h1')].find(h => /dashboard/i.test((h1x.textContent || '')) );
  const h1b = [...document.querySelectorAll('main h1')].find(h => /dashboard/i.test((h.textContent || '').trim()));
  const hh = h1b || h1;
  if (!hh) return JSON.stringify({ h1: 'not found' });
  const block = hh.parentElement;
  const row = block && block.parentElement;
  const wrapper = row && row.parentElement;
  if (!wrapper) return JSON.stringify({ wrapper: 'not found' });
  const wcs = getComputedStyle(wrapper);
  const wr = wrapper.getBoundingClientRect();
  out.wrapper = {
    cls: (typeof wrapper.className === 'string' ? wrapper.className : '').slice(0, 140),
    display: wcs.display,
    justifyContent: wcs.justifyContent,
    gap: wcs.gap,
    mb: wcs.marginBottom,
    w: Math.round(wr.width),
    h: Math.round(wr.height),
    childCount: wrapper.children.length,
  };
  out.children = [...wrapper.children].map(c => {
    const ccs = getComputedStyle(c);
    const cr = c.getBoundingClientRect();
    return {
      tag: c.tagName,
      cls: (typeof c.className === 'string' ? c.className : '').slice(0, 100),
      w: Math.round(cr.width),
      h: Math.round(cr.height),
      right: Math.round(window.innerWidth - cr.right),
      text: (c.textContent || '').trim().slice(0, 60),
    };
  });
  return JSON.stringify(out);
})()"

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

echo "=== REFERENCE side (1280, /networth + / — the wrapper children) ==="
export AGENT_BROWSER_SESSION="refnwwrap118"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
for attempt in 1 2 3; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- networth wrapper census:"
agent-browser eval "$WRAP_JS" 2>/dev/null | tail -1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- dashboard wrapper census:"
agent-browser eval "$DASH_JS" 2>/dev/null | tail -1
echo "=== wrapper census v118 done ==="
