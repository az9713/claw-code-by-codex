#!/usr/bin/env bash
set -euo pipefail

HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-8010}"
BASE_URL="http://${HOST}:${PORT}"
RUN_TESTS="${RUN_TESTS:-0}"

if ! command -v python >/dev/null 2>&1; then
  echo "[FAIL] python not found in PATH"
  exit 1
fi

if ! command -v curl >/dev/null 2>&1; then
  echo "[FAIL] curl not found in PATH"
  exit 1
fi

if ! python -c "import fastapi,uvicorn" >/dev/null 2>&1; then
  echo "[FAIL] missing dependencies for web runtime"
  echo "       install with: python -m pip install fastapi uvicorn"
  exit 1
fi

if [[ "$RUN_TESTS" == "1" ]]; then
  if ! python -c "import httpx" >/dev/null 2>&1; then
    echo "[FAIL] missing dependency for API tests: httpx"
    echo "       install with: python -m pip install httpx"
    exit 1
  fi
  echo "[INFO] Running targeted agentic tests"
  python -m unittest tests.test_agentic_demo tests.test_web_app -v
fi

echo "[INFO] Starting uvicorn on ${BASE_URL}"
python -m uvicorn src.web_app:app --host "$HOST" --port "$PORT" >/tmp/agentic_uvicorn.log 2>&1 &
SERVER_PID=$!

cleanup() {
  if kill -0 "$SERVER_PID" >/dev/null 2>&1; then
    kill "$SERVER_PID" >/dev/null 2>&1 || true
    wait "$SERVER_PID" 2>/dev/null || true
  fi
}
trap cleanup EXIT

for i in {1..30}; do
  if curl -fsS "${BASE_URL}/api/manifest" >/dev/null 2>&1; then
    break
  fi
  sleep 0.5
  if [[ "$i" -eq 30 ]]; then
    echo "[FAIL] server did not become ready in time"
    echo "---- uvicorn log ----"
    cat /tmp/agentic_uvicorn.log || true
    exit 1
  fi
done

echo "[PASS] server is healthy"

manifest_total=$(curl -fsS "${BASE_URL}/api/manifest" | python -c "import json,sys; print(json.load(sys.stdin)['total_python_files'])")
echo "[PASS] /api/manifest total_python_files=${manifest_total}"

agentic_body='{"prompts":["review MCP tool","summarize command graph","inspect tool pool"],"route_limit":5}'
agentic_response=$(curl -fsS -X POST "${BASE_URL}/api/agentic-demo" -H "Content-Type: application/json" -d "$agentic_body")
worker_count=$(printf "%s" "$agentic_response" | python -c "import json,sys; d=json.load(sys.stdin); print(d['worker_count'])")
summary_present=$(printf "%s" "$agentic_response" | python -c "import json,sys; d=json.load(sys.stdin); print('yes' if 'orchestrator_summary' in d else 'no')")

if [[ "$worker_count" -lt 2 ]]; then
  echo "[FAIL] /api/agentic-demo worker_count expected >=2, got ${worker_count}"
  exit 1
fi
if [[ "$summary_present" != "yes" ]]; then
  echo "[FAIL] /api/agentic-demo missing orchestrator_summary"
  exit 1
fi

echo "[PASS] /api/agentic-demo worker_count=${worker_count} summary=${summary_present}"

status_one=$(curl -s -o /dev/null -w "%{http_code}" -X POST "${BASE_URL}/api/agentic-demo" -H "Content-Type: application/json" -d '{"prompts":["only one"],"route_limit":5}')
if [[ "$status_one" != "422" ]]; then
  echo "[FAIL] expected 422 for one prompt, got ${status_one}"
  exit 1
fi
echo "[PASS] validation check (too few prompts) returned 422"

status_limit=$(curl -s -o /dev/null -w "%{http_code}" -X POST "${BASE_URL}/api/agentic-demo" -H "Content-Type: application/json" -d '{"prompts":["a","b"],"route_limit":0}')
if [[ "$status_limit" != "422" ]]; then
  echo "[FAIL] expected 422 for invalid route_limit, got ${status_limit}"
  exit 1
fi
echo "[PASS] validation check (invalid route_limit) returned 422"

echo "[DONE] Agentic smoke test passed"
