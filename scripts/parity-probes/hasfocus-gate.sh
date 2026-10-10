#!/usr/bin/env bash
# hasfocus-gate.sh — the v34 discipline formalized (the session-72
# tooling pass, T2 in docs/remediation-plan-v38.md).
#
#   source scripts/parity-probes/hasfocus-gate.sh
#   focus_gate <agent-browser-session>
#
# WHY: the sandbox's agent-browser daemon keeps sessions alive across
# tool calls but the PAGE loses OS focus between evals — a :focus /
# :focus-visible computed read on an unfocused page silently returns the
# UNFOCUSED styles (the v34 false-negative lesson). Every probe that
# reads focus-computed state must gate on document.hasFocus() first.
#
# The fix (v34): a REAL `press Shift` re-focuses the page (a modifier
# key press focuses the window without touching the DOM's focus target).
# This helper asserts the gate, applies the Shift re-focus once when
# needed, and re-asserts — a failed second assert aborts the calling
# script (set -u discipline: fail loud, never read unfocused chrome).
#
# Usage pattern in the standing scripts:
#   source "$PB/hasfocus-gate.sh"
#   focus_gate "$SESSION"   # before any :focus-computed read
focus_gate() {
  local session="${1:?focus_gate: missing agent-browser session}"
  local ok
  ok=$(agent-browser --session "$session" eval "document.hasFocus()" 2>/dev/null | tail -1)
  if [ "$ok" != "true" ]; then
    agent-browser --session "$session" press Shift >/dev/null 2>&1
    sleep 0.5
    ok=$(agent-browser --session "$session" eval "document.hasFocus()" 2>/dev/null | tail -1)
  fi
  if [ "$ok" != "true" ]; then
    echo "focus_gate: FAILED — page is not focused after the Shift re-focus; aborting the focus read" >&2
    return 1
  fi
  echo "focus_gate: ok (document.hasFocus() = true)"
}
