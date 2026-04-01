# Getting Started

Last updated: 2026-04-01

## Prerequisites

- Python 3.11+ recommended.
- `pip` available in your environment.
- For web/API runtime: `fastapi`, `uvicorn`.
- For API tests (`fastapi.testclient`): `httpx`.

If needed:

```bash
python -m pip install fastapi uvicorn httpx
```

## Git Bash + Virtual Environment (Windows)

```bash
cd /c/Users/<your-user>/Downloads/claw-code-by-codex
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn httpx
```

Confirm venv Python:

```bash
which python
```

## 5-Minute Quickstart (CLI)

From repository root:

```bash
python -m src.main summary
python -m src.main manifest
python -m src.main commands --limit 10
python -m src.main tools --limit 10
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## 5-Minute Quickstart (Web)

Start server:

```bash
python -m uvicorn src.web_app:app --host 127.0.0.1 --port 8000 --reload
```

Open:
- `http://127.0.0.1:8000/` for the UI
- `http://127.0.0.1:8000/docs` for OpenAPI docs

## What to Explore First

1. Use the web Prompt Router with `review MCP tool`.
2. Search command entries in the Commands panel.
3. Search tool entries in the Tools panel.
4. Read runtime summary in the Summary panel.

## Common Setup Problems

- `ModuleNotFoundError: fastapi`
  - Install with `python -m pip install fastapi uvicorn`.
- Port already in use (`8000`)
  - Run with `--port 8001`.
- Browser cannot reach localhost
  - Confirm server process is still running and not auto-stopped.

## Next Docs

- [Claude Code Primer](./claude-code-primer.md)
- [Architecture](./architecture.md)
- [Web App and UI](./web-app.md)
