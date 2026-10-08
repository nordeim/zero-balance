#!/usr/bin/env bash
# clone19 login + calculator error-tier live verification (v17).
# Usage: bash scripts/parity-probes/verify-v17.sh (inside with-server.sh)
set -u
S=clone19
agent-browser --session $S click @e7
agent-browser --session $S fill @e7 "demo@zerobalance.app"
agent-browser --session $S fill @e8 "Demo1234!"
agent-browser --session $S click @e4
sleep 3
echo "URL after login:"
agent-browser --session $S get url

# Route-abort the line-items API, then open the Rent calculator.
agent-browser --session $S open "http://localhost:3200/expenses"
sleep 2
agent-browser --session $S network route "**/api/line-items**" --abort
sleep 0.5
agent-browser --session $S snapshot -i > /tmp/c19-exp.txt 2>&1
CALC=$(grep -B2 '"Rent"' /tmp/c19-exp.txt | grep -oE 'button "Calculate" \[ref=(e[0-9]+)\]' | grep -oE 'e[0-9]+' | tail -1)
echo "Rent Calculate ref: $CALC"
agent-browser --session $S click @$CALC
sleep 2.5
echo "=== Calculator state under dead API (expect empty-state + toast) ==="
agent-browser --session $S eval "JSON.stringify({
  calcOpen: !![...document.querySelectorAll('h2')].find(x => /Rent Calculator/i.test(x.textContent)),
  emptyState: /No line items yet/i.test(document.body.innerText),
  zeroTotal: document.body.innerText.includes('\$0.00'),
  based0: /Based on 0 items/.test(document.body.innerText),
  toastTitle: /Could not load the line items/.test(document.body.innerText),
  toastDesc: /Network error — check your connection and try again/.test(document.body.innerText)
})"
