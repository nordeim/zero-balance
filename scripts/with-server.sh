#!/usr/bin/env bash
# with-server.sh — boot the production standalone parity server on :3200 for
# the duration of ONE command, then kill it (the sandbox reaps background
# processes between tool calls; the agent-browser daemon survives instead).
# Usage: bash scripts/with-server.sh <command...>
# The clone's login flow must run INSIDE one invocation (server dies between
# split commands — "Network error").
set -u
PORT=3200
DB="/home/z/my-project/zero-balance/db/custom.db"
LOG="/home/z/my-project/parity-server.log"

DATABASE_URL="file:${DB}" AUTH_SECRET="dev-parity-secret" PORT="$PORT" \
  node .next/standalone/server.js >>"$LOG" 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null' EXIT
# wait for readiness
for i in $(seq 1 40); do
  if curl -sf "http://localhost:${PORT}/api/health" >/dev/null 2>&1; then
    break
  fi
  sleep 0.25
done
"$@"
