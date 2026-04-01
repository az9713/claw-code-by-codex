# Capabilities and Limitations

Last updated: 2026-04-01

## Implemented capabilities

1. Multiple worker tasks in one request.
2. Parallel execution (`asyncio.gather` + thread offload).
3. Main orchestrator summary combining worker outcomes.
4. Web and API interfaces for interactive demos.
5. Automated tests and smoke-script validation.

## Non-implemented capabilities (by design)

1. Recursive agent spawning.
2. Dynamic tool-call feedback loops between workers.
3. Worker-to-worker message passing protocols.
4. Persistent mission-level memory/state machine across sessions.
5. Production controls (auth, quotas, tenancy, audit pipelines).

## Why this scope is intentional

- Keep changes minimal and demo-focused.
- Reuse existing codebase behavior instead of replatforming architecture.
- Avoid introducing complexity that would create immediate tech debt.

## Safe claims for users

You can accurately say this repo now supports:
- "parallel worker tasks"
- "main-agent orchestration summary"
- "minimal agentic application demo"

You should not claim:
- "full Claude Code multi-agent runtime parity"
- "autonomous production-grade agent swarm"
