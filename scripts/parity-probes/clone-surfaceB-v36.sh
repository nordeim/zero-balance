#!/usr/bin/env bash
# v36: clone-side Surface B (filter Selects' listbox keyboard contract) live probe.
# Runs INSIDE with-server.sh (the :3200 parity server). The REAL keys run via
# agent-browser press between the eval reads.
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone36"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 3

agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3

echo "=== CLONE Surface B: filter Select fresh-open (category) ==="
bash "$PB/run-probe.sh" clone36 "$PB/probe-filter-open-v36.mjs" 2>/dev/null | tail -1

echo ""
echo "=== CLONE Surface B: ArrowDown roving ==="
agent-browser press ArrowDown >/dev/null 2>&1
sleep 1
agent-browser eval "(() => { const opts = [...document.querySelectorAll('[role=listbox] [role=option]')]; const read = (o) => ({ t: o.textContent.trim().slice(0,12), hl: o.getAttribute('data-highlighted'), focusMatch: o.matches(':focus'), bg: getComputedStyle(o).backgroundColor, color: getComputedStyle(o).color }); return JSON.stringify({ open: !!document.querySelector('[role=listbox]'), opts: opts.map(read) }); })()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE Surface B: ArrowDown clamp at end ==="
agent-browser press ArrowDown >/dev/null 2>&1
sleep 1
agent-browser eval "(() => { const opts=[...document.querySelectorAll('[role=listbox] [role=option]')]; return JSON.stringify({ active: (document.activeElement.textContent||'').trim().slice(0,12), activeFocus: document.activeElement.matches(':focus'), opts: opts.map(o=>({t:o.textContent.trim().slice(0,12), hl:o.getAttribute('data-highlighted')!==null})) }); })()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE Surface B: ArrowUp back to first ==="
agent-browser press ArrowUp >/dev/null 2>&1
sleep 1
agent-browser eval "(() => { const opts=[...document.querySelectorAll('[role=listbox] [role=option]')]; return JSON.stringify({ active: (document.activeElement.textContent||'').trim().slice(0,12), opts: opts.map(o=>({t:o.textContent.trim().slice(0,12), hl:o.getAttribute('data-highlighted')!==null})) }); })()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE Surface B: End + Home jumps ==="
agent-browser press End >/dev/null 2>&1
sleep 1
agent-browser eval "(() => { const opts=[...document.querySelectorAll('[role=listbox] [role=option]')]; return JSON.stringify({ active: (document.activeElement.textContent||'').trim().slice(0,12), opts: opts.map(o=>({t:o.textContent.trim().slice(0,12), hl:o.getAttribute('data-highlighted')!==null})) }); })()" 2>/dev/null | tail -1
agent-browser press Home >/dev/null 2>&1
sleep 1
agent-browser eval "(() => { const opts=[...document.querySelectorAll('[role=listbox] [role=option]')]; return JSON.stringify({ active: (document.activeElement.textContent||'').trim().slice(0,12), opts: opts.map(o=>({t:o.textContent.trim().slice(0,12), hl:o.getAttribute('data-highlighted')!==null})) }); })()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE Surface B: Escape closes popup only, focus to trigger ==="
agent-browser press Escape >/dev/null 2>&1
sleep 1
agent-browser eval "(() => { const t = document.activeElement; return JSON.stringify({ listboxClosed: !document.querySelector('[role=listbox]'), activeTag: t.tagName, activeRole: t.getAttribute('role'), activeText: (t.textContent||'').trim().slice(0,20), pageStill: !!document.querySelector('main'), dialogOpen: !!document.querySelector('[role=dialog]') }); })()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE Surface B: Enter-open path + Enter-select ==="
agent-browser eval "(async () => { const t = document.activeElement; t.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', bubbles: true, cancelable: true })); await new Promise(r => setTimeout(r, 700)); const lb = document.querySelector('[role=listbox]'); return JSON.stringify({ open: !!lb, active: lb ? ((document.activeElement.getAttribute('role')||document.activeElement.tagName) + ':' + (document.activeElement.textContent||'').trim().slice(0,12)) : 'closed' }); })()" 2>/dev/null | tail -1
agent-browser press ArrowDown >/dev/null 2>&1
sleep 0.5
agent-browser press Enter >/dev/null 2>&1
sleep 1
agent-browser eval "(() => { const trig = document.querySelector('[role=combobox]'); return JSON.stringify({ listboxClosed: !document.querySelector('[role=listbox]'), triggerText: (trig ? trig.textContent : '').trim().slice(0,20), activeIsTrigger: document.activeElement === trig }); })()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE Surface B: reset filter to All Categories ==="
agent-browser eval "(async () => { const t = document.querySelector('[role=combobox]'); t.dispatchEvent(new PointerEvent('pointerdown', { bubbles: true, pointerId: 1 })); t.dispatchEvent(new MouseEvent('mousedown', { bubbles: true })); t.click(); await new Promise(r => setTimeout(r, 700)); return JSON.stringify({ open: !!document.querySelector('[role=listbox]') }); })()" 2>/dev/null | tail -1
agent-browser press Home >/dev/null 2>&1
sleep 0.5
agent-browser press Enter >/dev/null 2>&1
sleep 1
agent-browser eval "(() => { const trig = document.querySelector('[role=combobox]'); return JSON.stringify({ triggerText: (trig ? trig.textContent : '').trim() }); })()" 2>/dev/null | tail -1
agent-browser press Escape >/dev/null 2>&1
