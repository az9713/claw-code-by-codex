# Agentic Demo

Last updated: 2026-04-01

## Goal

Show a minimal, demoable agentic application using the existing Python runtime surfaces:
- multiple workers,
- parallel task execution,
- main-agent orchestration summary.

## Implementation

Backend:
- `src/agentic_demo.py`
  - `TaskSpec`: worker task contract.
  - `run_parallel_agents(...)`: executes workers concurrently via `asyncio.gather`.
  - `orchestrate(...)`: aggregates worker outputs and produces a main-agent summary.

API:
- `POST /api/agentic-demo` in `src/web_app.py`
  - input: `prompts` (2-5), optional `roles`, `route_limit`
  - output: worker results + orchestration summary + timing

Frontend:
- `web/index.html`: new Agentic Demo panel
- `web/static/app.js`: `runAgenticDemo(...)`
- `web/static/styles.css`: result rendering styles

## Reuse of Existing Architecture

Each worker reuses existing runtime components:
- `PortRuntime.route_prompt(...)` for command/tool matching
- `QueryEnginePort.submit_message(...)` for turn generation

No duplicate business logic was added in frontend JavaScript.

## Request Example

```json
{
  "prompts": [
    "review MCP tool",
    "summarize command graph",
    "inspect tool pool"
  ],
  "route_limit": 5
}
```

## Response Shape

```json
{
  "worker_count": 3,
  "total_duration_ms": 123,
  "workers": [
    {
      "agent_id": "agent-1",
      "role": "worker-1",
      "prompt": "review MCP tool",
      "matched_commands": ["..."],
      "matched_tools": ["..."],
      "output": "Prompt: ...",
      "stop_reason": "completed",
      "duration_ms": 41
    }
  ],
  "orchestrator_summary": "Main orchestrator merged parallel worker outputs: ..."
}
```

## Limits

- Demonstration orchestration only; this is not a full autonomous multi-agent runtime.
- Workers execute independent tasks in parallel; no iterative inter-agent message passing loop is implemented.

## Validation

- `tests/test_agentic_demo.py`
- `tests/test_web_app.py::test_agentic_demo_endpoint`

Targeted test command:

```bash
python -m unittest tests.test_agentic_demo tests.test_web_app -v
```

Dependency note:
- `httpx` is required for `fastapi.testclient`-based tests.
- Install with: `python -m pip install httpx`

Smoke script (Git Bash):

```bash
bash scripts/test_agentic.sh
```

Optional custom port:

```bash
PORT=8020 bash scripts/test_agentic.sh
```
