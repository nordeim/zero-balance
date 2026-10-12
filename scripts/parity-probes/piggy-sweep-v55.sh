#!/usr/bin/env bash
# piggy-sweep-v55.sh — the scope sweep: EVERY piggy-bank-class svg on the
# reference's five views + the login-adjacent nav surfaces, with size +
# shape data + the parent context (the nav rail vs the donut legend vs
# the classification chips vs the details sheet). READ-ONLY.
set -u
BASE="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="ref55b"
agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4

for view in "/" "/savings" "/income" "/expenses" "/networth"; do
  agent-browser open "$BASE$view" >/dev/null 2>&1
  sleep 3
  echo "=== REF $view: piggy-bank svgs ==="
  agent-browser eval "(async () => {
    const svgs = [...document.querySelectorAll('svg[class*=piggy]')];
    const shapeDump = (svg) => {
      const shapes = [...svg.querySelectorAll('path,circle,rect,line,polyline,polygon')];
      return shapes.map((s) => {
        const tag = s.tagName.toLowerCase();
        if (tag === 'path') return 'P:' + (s.getAttribute('d') || '').slice(0, 60);
        if (tag === 'circle') return 'C:' + (s.getAttribute('cx') || '') + ',' + (s.getAttribute('cy') || '') + ',r' + (s.getAttribute('r') || '');
        return tag + ':' + (s.getAttribute('d') || s.getAttribute('cx') || '').slice(0, 40);
      });
    };
    return JSON.stringify(svgs.map((svg) => {
      const r = svg.getBoundingClientRect();
      const p = svg.parentElement;
      return {
        cls: (svg.getAttribute('class') || '').slice(0, 46),
        w: Math.round(r.width), h: Math.round(r.height),
        shapes: shapeDump(svg),
        parentCls: (p ? (p.getAttribute('class') || '') : '').slice(0, 46),
        parentText: p ? (p.textContent || '').trim().slice(0, 22) : ''
      };
    }));
  })()" 2>/dev/null | tail -1
done
echo ""
echo "=== ref piggy sweep done ==="
