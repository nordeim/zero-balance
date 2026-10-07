#!/bin/bash
# Run a parity probe on a browser session: ./run-probe.sh <session> <probe-file>
# Encodes the probe as base64 to survive shell quoting ($ in regexes, quotes).
SESSION="$1"; FILE="$2"
B64=$(base64 -w0 "$FILE")
agent-browser --session "$SESSION" eval "eval(atob('$B64'))"
