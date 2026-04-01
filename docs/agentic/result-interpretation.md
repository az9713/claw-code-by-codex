# How To Interpret Results

Last updated: 2026-04-01

This guide explains what the agentic output means in practical terms.

## Response fields and interpretation

- `worker_count`
  - Number of worker tasks executed in parallel.
  - Should equal number of input prompts.

- `total_duration_ms`
  - Wall-clock duration for overall orchestration.
  - Helps compare perceived speed for multi-worker runs.

- `workers[]`
  - Per-worker output entries.
  - Important fields:
    - `agent_id`, `role`: worker identity
    - `matched_commands`, `matched_tools`: routing decisions
    - `output`: generated summary text
    - `stop_reason`: usually `completed`
    - `duration_ms`: per-worker elapsed time

- `orchestrator_summary`
  - Main-agent aggregate view across all workers.
  - Quick health signal for orchestration quality.

## What results tell us about "agentic capabilities" here

Positive signals:
- Parallel worker execution is real (not mocked in UI).
- Main orchestrator combines worker outcomes.
- Existing runtime surfaces are reused consistently.

Current limits:
- No long-running inter-agent conversation graph.
- No iterative planning-feedback loops between workers.
- No persistent autonomous objective management.

So this demonstrates a valid minimal agentic pattern:
- fan-out (parallel workers) + fan-in (main orchestrator summary).

## Practical quality checks

- If worker outputs are all empty: check routing and prompt quality.
- If only one worker runs: input prompt list may be invalid.
- If all stops are `completed` and summary exists: orchestration path is healthy.
