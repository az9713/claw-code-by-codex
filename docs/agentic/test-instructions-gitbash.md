# Testing Instructions (Git Bash)

Last updated: 2026-04-01

These steps assume no prior agent experience.

## 1) Create and activate virtual environment

```bash
cd /c/Users/simon/Downloads/claw-code-by-codex
python -m venv .venv
source .venv/Scripts/activate
```

## 2) Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn httpx
```

Why `httpx`?
- `fastapi.testclient` uses Starlette `TestClient`, which requires `httpx`.

## 3) Run targeted agentic tests

```bash
python -m unittest tests.test_agentic_demo tests.test_web_app -v
```

## 4) Run full suite (recommended)

```bash
python -m unittest discover -s tests -v
```

## 5) Run one-command smoke script

```bash
bash scripts/test_agentic.sh
```

Optional custom port:

```bash
PORT=8020 bash scripts/test_agentic.sh
```

Optional mode to run targeted tests before smoke checks:

```bash
RUN_TESTS=1 bash scripts/test_agentic.sh
```

## 6) Manual UI test

Start web server:

```bash
python -m uvicorn src.web_app:app --host 127.0.0.1 --port 8000 --reload
```

Open `http://localhost:8000/`.

In Agentic Demo panel:
- Enter 2-5 prompts, one per line.
- Example lines:
  - `review MCP tool`
  - `summarize command graph`
  - `inspect tool pool`
- Click `Run Parallel Agents`.

## 7) Manual API test

```bash
curl -s -X POST "http://127.0.0.1:8000/api/agentic-demo" \
  -H "Content-Type: application/json" \
  -d '{"prompts":["review MCP tool","summarize command graph"],"route_limit":5}'
```

## 8) Negative validation checks (expect HTTP 422)

One prompt only:

```bash
curl -i -X POST "http://127.0.0.1:8000/api/agentic-demo" \
  -H "Content-Type: application/json" \
  -d '{"prompts":["only one"],"route_limit":5}'
```

Invalid route_limit:

```bash
curl -i -X POST "http://127.0.0.1:8000/api/agentic-demo" \
  -H "Content-Type: application/json" \
  -d '{"prompts":["a","b"],"route_limit":0}'
```

## 9) Deactivate virtual environment

```bash
deactivate
```
