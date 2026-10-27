#!/usr/bin/env bash
# One-shot structural probe of the reference's Add Income quick-action
# button (the v125 tile-finder debugging form — NOT a census, an
# inspection: dump every span/svg child's tag/radius/box).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refqastruct125"
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
agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/dashboard" >/dev/null 2>&1
sleep 4

PROBE='(async () => {
  const b = [...document.querySelectorAll("button")].find((x) =>
    /^Add Income$/.test((x.textContent || "").trim()));
  if (!b) return "no button";
  b.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const dump = (el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return el.tagName + " r=" + cs.borderRadius + " " + Math.round(r.width) + "x" + Math.round(r.height);
  };
  const out = { btn: dump(b), children: [], spans: [] };
  for (const c of b.children) out.children.push(dump(c));
  for (const s of b.querySelectorAll("span")) out.spans.push(dump(s));
  const svgs = [...b.querySelectorAll("svg")].map((s) => {
    const r = s.getBoundingClientRect();
    return "svg " + Math.round(r.width) + "x" + Math.round(r.height);
  });
  out.svgs = svgs;
  return JSON.stringify(out);
})()'
agent-browser eval "$PROBE" 2>/dev/null | tail -1
pkill -f "agent-browser" 2>/dev/null
