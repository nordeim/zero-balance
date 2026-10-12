#!/usr/bin/env bash
# glyph-exact-v55.sh — capture the reference's EXACT svg outerHTML for the
# four drifted glyphs (piggy-bank, mail, search, trending-up) so the swap
# components carry byte-identical path data + attributes. The login-page
# icons are grabbed from a FRESH unauthenticated session first (the authed
# /login redirects); then login and grab the app icons. READ-ONLY.
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="ref55c"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 5

echo "=== REF login page: exact mail svg (unauthenticated) ==="
agent-browser eval "(async () => {
  const svg = document.querySelector('svg[class*=lucide-mail]');
  return svg ? svg.outerHTML : 'not found';
})()" 2>/dev/null | tail -1

echo ""
echo "=== login for the app-side glyphs ==="
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
sleep 5

echo "=== REF app: exact piggy-bank + trending-up svgs (on /) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const grab = (name) => {
    const svg = document.querySelector('svg[class*=lucide-' + name + ']');
    return svg ? svg.outerHTML : null;
  };
  return JSON.stringify({
    piggy: grab('piggy-bank'),
    trending: grab('trending-up')
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== REF app: exact search svg (on /savings) ==="
agent-browser open "$BASE/savings" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
  const svg = document.querySelector('svg[class*=lucide-search]');
  return svg ? svg.outerHTML : 'not found';
})()" 2>/dev/null | tail -1
echo ""
echo "=== ref exact glyph markup done ==="
