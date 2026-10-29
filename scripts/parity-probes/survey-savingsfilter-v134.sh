#!/usr/bin/env bash
# survey-savingsfilter-v134.sh — the v134 candidate-survey probe (READ-ONLY,
# the v46 rule): read the REFERENCE's savings filter card's interaction
# families live at 1280x800 — (1) the SEARCH input's at-rest chrome + its
# FOCUS ring (focus reveals chrome, no click), (2) the CATEGORY combobox
# trigger's at-rest chrome + its OWN-HOVER ladder (hover reveals chrome,
# no click — the trigger OPENS the listbox on click, never clicked), so
# the census finder can be shaped TAG-AGNOSTIC and STATE-INDEPENDENT (the
# v107 lesson; the v131/v132/v133 survey precedents).
set -u
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refsurvey134"
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

echo "=== the filter card: at-rest structure (search + comboboxes, pointer parked) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div')].find(d => {
    const cs = getComputedStyle(d);
    return cs.borderRadius === '16px' && cs.backgroundColor === 'rgb(255, 255, 255)' && d.querySelector('input');
  });
  if (!card) return JSON.stringify({err: 'no filter card'});
  const search = card.querySelector('input');
  const triggers = [...card.querySelectorAll('button')].filter(b => {
    const cs = getComputedStyle(b);
    return cs.display === 'flex' && b.textContent.trim().length > 3;
  });
  const rd = (el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {tag: el.tagName, w: Math.round(r.width), h: Math.round(r.height), bg: cs.backgroundColor, border: cs.borderColor, shadow: cs.boxShadow.slice(0, 90), radius: cs.borderRadius, fs: cs.fontSize, color: cs.color, transition: cs.transitionDuration};
  };
  return JSON.stringify({
    search: rd(search),
    searchPlaceholder: search.getAttribute('placeholder'),
    triggerCount: triggers.length,
    trigger0: triggers[0] ? {text: triggers[0].textContent.trim().slice(0, 30), ...rd(triggers[0])} : null
  });
})()" 2>/dev/null | tail -1

echo "=== rung: the CATEGORY combobox's OWN-HOVER (pointer at its live center) ==="
CENTER="$(agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div')].find(d => {
    const cs = getComputedStyle(d);
    return cs.borderRadius === '16px' && cs.backgroundColor === 'rgb(255, 255, 255)' && d.querySelector('input');
  });
  const triggers = [...card.querySelectorAll('button')].filter(b => {
    const cs = getComputedStyle(b);
    return cs.display === 'flex' && b.textContent.trim().length > 3;
  });
  if (!triggers.length) return '';
  const r = triggers[0].getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + ',' + Math.round(r.y + r.height / 2);
})()" 2>/dev/null | tail -1 | tr -d '"')"
if [ -n "$CENTER" ]; then
  agent-browser mouse move "${CENTER%,*}" "${CENTER#*,}" >/dev/null 2>&1
  sleep 1
  agent-browser eval "(async () => {
    const card = [...document.querySelectorAll('div')].find(d => {
      const cs = getComputedStyle(d);
      return cs.borderRadius === '16px' && cs.backgroundColor === 'rgb(255, 255, 255)' && d.querySelector('input');
    });
    const triggers = [...card.querySelectorAll('button')].filter(b => {
      const cs = getComputedStyle(b);
      return cs.display === 'flex' && b.textContent.trim().length > 3;
    });
    const t = triggers[0];
    const cs = getComputedStyle(t);
    return JSON.stringify({hoverMatch: t.matches(':hover'), bg: cs.backgroundColor, color: cs.color, border: cs.borderColor, shadow: cs.boxShadow.slice(0, 90), transition: cs.transitionDuration});
  })()" 2>/dev/null | tail -1
fi

echo "=== rung: the SEARCH input's FOCUS ring (keyboard focus — no click) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const card = [...document.querySelectorAll('div')].find(d => {
    const cs = getComputedStyle(d);
    return cs.borderRadius === '16px' && cs.backgroundColor === 'rgb(255, 255, 255)' && d.querySelector('input');
  });
  const search = card.querySelector('input');
  search.focus();
  await new Promise((r) => setTimeout(r, 400));
  const cs = getComputedStyle(search);
  const direct = search.matches(':focus');
  return JSON.stringify({focusMatch: direct, shadow: cs.boxShadow.slice(0, 120), border: cs.borderColor, outline: cs.outline, transition: cs.transitionDuration});
})()" 2>/dev/null | tail -1

echo "=== survey done ==="
