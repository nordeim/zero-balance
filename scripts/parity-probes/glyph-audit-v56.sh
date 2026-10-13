#!/usr/bin/env bash
# glyph-audit-v56.sh — the FULL icon-glyph census: every lucide svg on the
# five authed views (+ login), grouped by lucide class name → shape dump.
# Diffs against the clone's equivalent reveal EVERY drifted glyph (the
# piggy-bank is the known v56 candidate; this sweep catches any others).
# READ-ONLY on the reference.
set -u
BASE="${1:-https://zero-balance-4885a8f3.base44.app}"
SESS="${2:-refglyph56}"
PORTSIDE="${3:-ref}"

export AGENT_BROWSER_SESSION="$SESS"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 5
LOGIN_JS=""
if [ "$PORTSIDE" = "ref" ]; then
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
else
  LOGIN_JS="(async () => {
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
  })()"
fi
# Retry the login until it submits (the page can still be mounting when
# the first eval lands — "no inputs" is the retry signal, NOT auth state).
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$BASE/login" >/dev/null 2>&1
  sleep 4
done
sleep 5
# Verify auth: the root view must show a nav landmark (the app shell) —
# if the login page still renders, bail loudly rather than census it.
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
AUTHCHECK=$(agent-browser eval "(() => JSON.stringify({ nav: !!document.querySelector('nav'), h1: (document.querySelector('h1')?.textContent || document.body.textContent || '').trim().slice(0, 30) }))()" 2>/dev/null | tail -1)
echo "auth check: $AUTHCHECK"

for view in "/" "/savings" "/income" "/expenses" "/networth" "/login"; do
  agent-browser open "$BASE$view" >/dev/null 2>&1
  sleep 3
  echo "=== $PORTSIDE $view: lucide glyph dictionary ==="
  agent-browser eval "(async () => {
    const svgs = [...document.querySelectorAll('svg[class*=lucide-]')];
    const dict = {};
    for (const svg of svgs) {
      const m = (svg.getAttribute('class') || '').match(/lucide-([a-z0-9-]+)/);
      if (!m) continue;
      const name = m[1];
      if (dict[name]) continue;
      const shapes = [...svg.querySelectorAll('path,circle,rect,line,polyline,polygon')].map((s) => {
        const tag = s.tagName.toLowerCase();
        if (tag === 'path') return 'P:' + (s.getAttribute('d') || '');
        if (tag === 'circle') return 'C:' + (s.getAttribute('cx') || '') + ',' + (s.getAttribute('cy') || '') + ',r' + (s.getAttribute('r') || '');
        if (tag === 'rect') return 'R:' + (s.getAttribute('x') || '') + ',' + (s.getAttribute('y') || '') + ',' + (s.getAttribute('width') || '') + 'x' + (s.getAttribute('height') || '') + (s.getAttribute('rx') ? ',rx' + s.getAttribute('rx') : '');
        if (tag === 'polyline' || tag === 'polygon') return tag + ':' + (s.getAttribute('points') || '');
        return tag + ':' + [s.getAttribute('x1'), s.getAttribute('y1'), s.getAttribute('x2'), s.getAttribute('y2')].join(',');
      });
      dict[name] = shapes.join(' || ');
    }
    return JSON.stringify(dict);
  })()" 2>/dev/null | tail -1
done
echo ""
echo "=== $PORTSIDE glyph audit done ==="
