# What Is Agentic Here?

Last updated: 2026-04-01

## Plain-language definition

In this repository, "agentic" means:
- one main orchestrator,
- multiple worker agents,
- workers run tasks in parallel,
- orchestrator combines their outputs into one summary.

Think of it like a team lead (orchestrator) asking several specialists (workers) to work at the same time, then merging their reports.

## What this feature is for

- Demonstrate a concrete multi-agent pattern with minimal code.
- Reuse existing runtime surfaces already present in this codebase.
- Give users a practical way to test parallel worker execution and orchestration.

## What this feature is not

- It is not a fully autonomous self-improving agent swarm.
- It does not implement iterative back-and-forth worker-to-worker messaging loops.
- It does not claim full proprietary Claude Code feature parity.

## User-facing surfaces

- Web UI panel: "Agentic Demo"
- API endpoint: `POST /api/agentic-demo`
- Automated script: `scripts/test_agentic.sh`
- Tests: `tests/test_agentic_demo.py`, `tests/test_web_app.py`
