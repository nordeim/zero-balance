#!/usr/bin/env bash
# v36: clone-side VLM captures (dashboard + filter-open on /income).
# Runs INSIDE with-server.sh (the :3200 parity server).
set -u
BASE="http://localhost:3200"
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

agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 4
agent-browser eval "(() => JSON.stringify({ vw: window.innerWidth, vh: window.innerHeight, path: location.pathname }))()" 2>/dev/null | tail -1
agent-browser screenshot /tmp/vlm36/clone-dashboard.png 2>&1 | tail -1

agent-browser open "$BASE/income" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => { const t = document.querySelector('[role=combobox]'); t.dispatchEvent(new PointerEvent('pointerdown', { bubbles: true, pointerId: 1 })); t.dispatchEvent(new MouseEvent('mousedown', { bubbles: true })); t.click(); await new Promise(r => setTimeout(r, 800)); return JSON.stringify({ open: !!document.querySelector('[role=listbox]') }); })()" 2>/dev/null | tail -1
agent-browser screenshot /tmp/vlm36/clone-filter-open.png 2>&1 | tail -1
agent-browser press Escape >/dev/null 2>&1
