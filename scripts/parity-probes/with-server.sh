#!/bin/bash
# with-server.sh — run a command against a freshly-booted standalone server.
# This sandbox reaps every background process at command exit, so the parity
# server cannot survive across Bash commands. Wrapper contract:
#   ./with-server.sh <command...>
# Boots bun .next/standalone/server.js on :3200 (0.0.0.0, db/custom.db),
# waits for /api/health, runs the command, then kills the server.
set -u
cd "$(dirname "$0")/../.."
PORT=3200
LOG=/home/z/my-project/tool-results/parity3200.log

# kill any stale listener (ss sees it; lsof does not)
STALE=$(ss -tlnp 2>/dev/null | grep ":$PORT " | grep -oP 'pid=\K[0-9]+' | head -1)
[ -n "$STALE" ] && kill "$STALE" 2>/dev/null && sleep 1

DATABASE_URL="file:../db/custom.db" PORT=$PORT HOSTNAME="0.0.0.0" NODE_ENV=production \
  bun .next/standalone/server.js > "$LOG" 2>&1 < /dev/null &
SRV=$!
for i in $(seq 1 40); do
  curl -s --max-time 1 "http://localhost:$PORT/api/health" >/dev/null 2>&1 && break
  sleep 0.25
done
if ! curl -s --max-time 2 "http://localhost:$PORT/api/health" >/dev/null 2>&1; then
  echo "SERVER FAILED TO BOOT:"; tail -5 "$LOG"; kill $SRV 2>/dev/null; exit 1
fi

"$@"
RC=$?
kill $SRV 2>/dev/null
wait $SRV 2>/dev/null
exit $RC
