#!/usr/bin/env bash
# ZeroBalance end-to-end API smoke test.
# Boots the production standalone server, exercises auth + budget-item CRUD
# + the calculator's parent-recalculation pipeline + asset/liability CRUD,
# prints PASS/FAIL per step, cleans up, exits non-zero on any failure.
set -u
cd "$(dirname "$0")/.."
PROJECT_DIR="$(pwd)"

BASE="${SMOKE_BASE:-http://localhost:3210}"
CJ="/tmp/zb-smoke-cookies.txt"
PASS=0; FAIL=0

say() { printf '%s\n' "$*"; }
ok()  { PASS=$((PASS+1)); say "PASS: $*"; }
bad() { FAIL=$((FAIL+1)); say "FAIL: $*"; }

jqget() { python3 -c "import json,sys;d=json.load(open('$1'));print(d$2)" 2>/dev/null; }

# ---- 0. clean slate: kill any server holding port 3000 ----
pkill -f "standalone/server.js" 2>/dev/null
sleep 1
rm -f "$CJ" /tmp/zb-smoke-*.json

# ---- 1. boot server ----
# Pin the DB URL explicitly: a relative `file:` URL resolves against
# prisma/schema.prisma (via src/lib/db-path.ts) exactly like the CLI, while
# an inherited absolute DATABASE_URL (e.g. a parent-workspace path exported
# by the operator's shell) passes through untouched and the server boots
# against a database that does not exist (Error code 14). The Playwright
# webServer pins its own value the same way (playwright.config.ts).
DATABASE_URL="file:../db/custom.db" \
PORT="${SMOKE_PORT:-3210}" HOSTNAME="127.0.0.1" \
bun .next/standalone/server.js > /tmp/zb-smoke-server.log 2>&1 < /dev/null &
SRV=$!
disown $SRV 2>/dev/null || true

ready=0
for i in $(seq 1 30); do
  if curl -s --max-time 2 "$BASE/api/health" | grep -q '"ok"'; then ready=1; break; fi
  sleep 1
done
if [ "$ready" != "1" ]; then
  bad "server did not become ready"; kill $SRV 2>/dev/null; exit 1
fi
ok "server ready (health check)"

# ---- 2. login ----
code=$(curl -s -o /tmp/zb-smoke-login.json -w "%{http_code}" --max-time 10 \
  -c "$CJ" -X POST "$BASE/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"demo@zerobalance.app","password":"Demo1234!"}')
if [ "$code" = "200" ] && grep -q '"ok":true' /tmp/zb-smoke-login.json; then ok "login (200)"; else bad "login -> $code $(cat /tmp/zb-smoke-login.json)"; fi

# ---- 3. wrong password must be rejected ----
code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 \
  -X POST "$BASE/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"demo@zerobalance.app","password":"WrongPassword!"}')
if [ "$code" = "401" ]; then ok "wrong password rejected (401)"; else bad "wrong password -> $code"; fi

# ---- 4. unauthenticated access must be 401 ----
code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$BASE/api/budget-items")
if [ "$code" = "401" ]; then ok "unauthenticated budget-items blocked (401)"; else bad "unauth budget-items -> $code"; fi

# ---- 5. reads ----
for ep in auth/me budget-items assets liabilities; do
  case "$ep" in
    auth/me) path="auth/me"; file="auth-me";;
    *) path="$ep"; file="$ep";;
  esac
  code=$(curl -s -o "/tmp/zb-smoke-$file.json" -w "%{http_code}" --max-time 10 -b "$CJ" "$BASE/api/$path")
  if [ "$code" = "200" ] && grep -q '"ok":true' "/tmp/zb-smoke-$file.json"; then ok "GET /api/$path"; else bad "GET /api/$path -> $code"; fi
done
if [ "$(jqget /tmp/zb-smoke-budget-items.json "['data'].__len__()")" -ge 1 ]; then
  ok "seeded budget items listed"
else
  bad "seeded budget items missing"
fi

# ---- 6. create a budget item ----
code=$(curl -s -o /tmp/zb-smoke-item.json -w "%{http_code}" --max-time 10 -b "$CJ" \
  -X POST "$BASE/api/budget-items" -H "Content-Type: application/json" \
  -d '{"type":"expense","classification":"need","amount":100,"category":"SMOKE Utilities","frequency":"monthly","date":"2026-10-07"}')
if [ "$code" = "201" ] && grep -q '"ok":true' /tmp/zb-smoke-item.json; then ok "create budget item (201)"; else bad "create item -> $code $(cat /tmp/zb-smoke-item.json)"; fi
ITEM_ID=$(jqget /tmp/zb-smoke-item.json "['data']['id']")

# ---- 7. invalid payloads must be rejected ----
code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 -b "$CJ" \
  -X POST "$BASE/api/budget-items" -H "Content-Type: application/json" \
  -d '{"type":"windfall","classification":"need","amount":1,"category":"x","frequency":"monthly","date":"2026-10-07"}')
if [ "$code" = "400" ]; then ok "invalid type rejected (400)"; else bad "invalid type -> $code"; fi
code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 -b "$CJ" \
  -X POST "$BASE/api/budget-items" -H "Content-Type: application/json" \
  -d '{"type":"expense","classification":"need","amount":1,"category":"x","frequency":"monthly","date":"2026-02-30"}')
if [ "$code" = "400" ]; then ok "impossible calendar date rejected (400)"; else bad "impossible date -> $code"; fi
code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 -b "$CJ" \
  -X POST "$BASE/api/budget-items" -H "Content-Type: application/json" \
  -d '{"type":"expense","classification":"need","amount":-5,"category":"x","frequency":"monthly","date":"2026-10-07"}')
if [ "$code" = "400" ]; then ok "negative amount rejected (400)"; else bad "negative amount -> $code"; fi

if [ -n "${ITEM_ID:-}" ]; then
  # ---- 8. patch the item (calculator prep: rename + set amount 0) ----
  code=$(curl -s -o /tmp/zb-smoke-patch.json -w "%{http_code}" --max-time 10 -b "$CJ" \
    -X PATCH "$BASE/api/budget-items/$ITEM_ID" -H "Content-Type: application/json" \
    -d '{"amount":150,"subcategory":"Smoke Sub"}')
  if [ "$code" = "200" ] && grep -q '"ok":true' /tmp/zb-smoke-patch.json; then ok "patch budget item (200)"; else bad "patch item -> $code"; fi

  # ---- 9. calculator: line items recalculate the parent ----
  code=$(curl -s -o /tmp/zb-smoke-line.json -w "%{http_code}" --max-time 10 -b "$CJ" \
    -X POST "$BASE/api/line-items" -H "Content-Type: application/json" \
    -d "{\"budgetItemId\":\"$ITEM_ID\",\"name\":\"SMOKE Line\",\"amount\":25}")
  if [ "$code" = "201" ] && grep -q '"ok":true' /tmp/zb-smoke-line.json; then ok "create line item (201)"; else bad "create line -> $code $(cat /tmp/zb-smoke-line.json)"; fi
  LINE_ID=$(jqget /tmp/zb-smoke-line.json "['data']['lineItem']['id']")
  PARENT=$(jqget /tmp/zb-smoke-line.json "['data']['parentAmount']")
  if [ "$PARENT" = "25" ]; then ok "parent recalculated to line total (25)"; else bad "parent recalc -> $PARENT"; fi

  # ---- 10. delete the line item; parent returns to 0 ----
  code=$(curl -s -o /tmp/zb-smoke-linedel.json -w "%{http_code}" --max-time 10 -b "$CJ" \
    -X DELETE "$BASE/api/line-items/$LINE_ID")
  PARENT=$(jqget /tmp/zb-smoke-linedel.json "['data']['parentAmount']")
  if [ "$code" = "200" ] && [ "$PARENT" = "0" ]; then ok "delete line item + parent back to 0"; else bad "line delete -> $code parent=$PARENT"; fi

  # ---- 11. delete the budget item ----
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 -b "$CJ" -X DELETE "$BASE/api/budget-items/$ITEM_ID")
  if [ "$code" = "200" ]; then ok "delete budget item (200)"; else bad "delete item -> $code"; fi
fi

# ---- 12. asset round-trip ----
code=$(curl -s -o /tmp/zb-smoke-asset.json -w "%{http_code}" --max-time 10 -b "$CJ" \
  -X POST "$BASE/api/assets" -H "Content-Type: application/json" \
  -d '{"type":"vehicle","name":"SMOKE Car","value":1,"lastUpdated":"2026-10-07"}')
ASSET_ID=$(jqget /tmp/zb-smoke-asset.json "['data']['id']")
if [ "$code" = "201" ] && [ -n "$ASSET_ID" ]; then ok "create asset (201)"; else bad "create asset -> $code"; fi
if [ -n "${ASSET_ID:-}" ]; then
  curl -s -o /dev/null --max-time 10 -b "$CJ" -X DELETE "$BASE/api/assets/$ASSET_ID"
fi

# ---- 13. logout + session invalidated ----
code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 -b "$CJ" -c "$CJ" -X POST "$BASE/api/auth/logout")
if [ "$code" = "200" ]; then ok "logout (200)"; else bad "logout -> $code"; fi
code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 -b "$CJ" "$BASE/api/budget-items")
if [ "$code" = "401" ]; then ok "post-logout budget-items blocked (401)"; else bad "post-logout -> $code"; fi

# ---- 14. page render ----
code=$(curl -s -o /tmp/zb-smoke-page.html -w "%{http_code}" --max-time 15 "$BASE/login")
if [ "$code" = "200" ] && grep -q "<!DOCTYPE html" /tmp/zb-smoke-page.html; then ok "login page renders (200)"; else bad "login page -> $code"; fi

# ---- 15. app routes render the client shell ----
for path in "" dashboard income expenses savings networth; do
  code=$(curl -s -o /tmp/zb-smoke-path.html -w "%{http_code}" --max-time 10 "$BASE/$path")
  if [ "$code" = "200" ] && grep -q "<!DOCTYPE html" /tmp/zb-smoke-path.html; then ok "GET /$path (200)"; else bad "GET /$path -> $code"; fi
done
code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$BASE/not-a-real-page")
if [ "$code" = "404" ]; then ok "unknown path 404s"; else bad "unknown path -> $code"; fi

# ---- 16. rate limiting on /api/auth/login (10 attempts / 15 min / IP) ----
# Steps 2 and 3 consumed 2 attempts; the 10th attempt is still ALLOWED
# (the limiter blocks when the bucket is already AT the limit), so the
# 11th attempt — one more than the loop's earlier count — must 429.
limited=0
for i in $(seq 1 9); do
  code=$(curl -s -o /tmp/zb-smoke-rl.json -w "%{http_code}" --max-time 10 \
    -X POST "$BASE/api/auth/login" -H "Content-Type: application/json" \
    -d '{"email":"demo@zerobalance.app","password":"WrongPassword!"}')
  if [ "$code" = "429" ]; then limited=$((limited+1)); fi
done
if [ "$limited" -ge 1 ] && grep -q 'Too many attempts' /tmp/zb-smoke-rl.json; then
  ok "login rate limit engages (429)"
else
  bad "rate limit -> last code $code $(cat /tmp/zb-smoke-rl.json)"
fi

# ---- shutdown ----
kill $SRV 2>/dev/null
say ""
say "RESULT: $PASS passed, $FAIL failed"
[ "$FAIL" = "0" ]
