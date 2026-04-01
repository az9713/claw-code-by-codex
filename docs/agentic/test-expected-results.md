# Expected Test Results

Last updated: 2026-04-01

This document explains what successful test output should look like and what each success means.

## Targeted unittest command

```bash
python -m unittest tests.test_agentic_demo tests.test_web_app -v
```

Expected passing lines include:
- `test_parallel_agents_return_results ... ok`
- `test_orchestrator_summary_contains_worker_lines ... ok`
- `test_summary_for_empty_results ... ok`
- `test_agentic_demo_endpoint ... ok`

Expected summary:
- `Ran <N> tests in ...`
- `OK`

## Smoke script command

```bash
bash scripts/test_agentic.sh
```

Expected output pattern:
- `[PASS] server is healthy`
- `[PASS] /api/manifest total_python_files=...`
- `[PASS] /api/agentic-demo worker_count=... summary=yes`
- `[PASS] validation check (too few prompts) returned 422`
- `[PASS] validation check (invalid route_limit) returned 422`
- `[DONE] Agentic smoke test passed`

## UI expectation

In the Agentic Demo panel, after submitting 2-5 prompts:
- Main Orchestrator card appears first.
- Worker cards appear (`agent-1`, `agent-2`, ...).
- Each card shows command/tool match counts and execution timing.

## What failing output indicates

- Missing `httpx`: test dependency problem, not logic failure.
- HTTP `422` on valid request: request contract mismatch.
- worker_count less than expected: orchestration path regression.
- missing `orchestrator_summary`: aggregator output regression.
