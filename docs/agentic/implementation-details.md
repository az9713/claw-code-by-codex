# Implementation Details

Last updated: 2026-04-01

## Architecture

```text
Client/UI
  -> POST /api/agentic-demo
       -> src.web_app.agentic_demo(...)
            -> src.agentic_demo.orchestrate(...)
                 -> run_parallel_agents(...)
                      -> N workers in parallel (asyncio.gather)
                           -> PortRuntime.route_prompt(...)
                           -> QueryEnginePort.submit_message(...)
                 -> build_orchestrator_summary(...)
            -> JSON response returned to client
```

## Backend module

File: `src/agentic_demo.py`

Main elements:
- `TaskSpec`: input unit per worker (`agent_id`, `role`, `prompt`).
- `AgentResult`: output per worker (matches, output, stop reason, duration).
- `OrchestrationResult`: aggregate output from orchestrator.
- `_run_worker_sync(...)`: worker execution using existing runtime/query components.
- `run_parallel_agents(...)`: uses `asyncio.gather` with thread offloading.
- `orchestrate(...)`: orchestration entrypoint and summary generation.

## Existing architecture reused

No duplicate business logic was added.
Workers call:
- `PortRuntime.route_prompt(...)`
- `QueryEnginePort.submit_message(...)`

This ensures the agentic demo is consistent with existing command/tool routing behavior in the codebase.

## API contract

File: `src/web_app.py`

Endpoint:
- `POST /api/agentic-demo`

Request model:
- `prompts`: list[str], length 2-5 (required)
- `roles`: list[str] optional
- `route_limit`: int (1-20), default 5

Response fields:
- `worker_count`
- `total_duration_ms`
- `workers[]`
- `orchestrator_summary`

## UI integration

- `web/index.html`: Agentic Demo panel and input controls.
- `web/static/app.js`: `runAgenticDemo(...)` sends POST request and renders worker + orchestrator cards.
- `web/static/styles.css`: presentation styles for result cards and output blocks.

## Why this is minimal

- One new backend module.
- One new API endpoint.
- One additional UI panel.
- Focused tests and docs.

This is sufficient to show real parallel execution and orchestration without introducing unnecessary framework complexity.
