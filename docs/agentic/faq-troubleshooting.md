# FAQ and Troubleshooting

Last updated: 2026-04-01

## Q: Why do tests fail with `No module named httpx`?

`fastapi.testclient` requires `httpx`.

Fix:

```bash
python -m pip install httpx
```

## Q: Why does `scripts/test_agentic.sh` fail saying dependencies are missing?

Install runtime dependencies:

```bash
python -m pip install fastapi uvicorn
```

Optional test dependencies:

```bash
python -m pip install httpx
```

## Q: Browser says localhost is unreachable.

- Confirm uvicorn process is running.
- Confirm port is correct.
- Try another port:

```bash
python -m uvicorn src.web_app:app --host 127.0.0.1 --port 8001 --reload
```

## Q: Why do I get HTTP 422 from `/api/agentic-demo`?

The request body violates validation constraints.

Rules:
- prompts: 2 to 5 strings
- route_limit: 1 to 20

## Q: Does this prove full Claude Code agent parity?

No. This proves a minimal agentic pattern in this repository:
- parallel workers + orchestrator summary.

## Q: Where is the demo video?

Local file:
- `docs/demo_agents_github.mp4` (compressed, GitHub-friendly)

Placeholder URL (to replace later):
- `https://github.com/user-attachments/assets/19e2553d-d286-4a8a-bac6-d620fc1911f9`

