# Documentation Portal

Last updated: 2026-04-01

This documentation set is designed for two goals:
1. Fast onboarding for users and developers who are new to Claude Code style harness systems.
2. Low long-term maintenance cost by keeping docs close to code, testable, and versioned.

## Read This First

- [Getting Started](./getting-started.md)
- [Claude Code Primer](./claude-code-primer.md)
- [Architecture](./architecture.md)
- [Original Codebase Overview](./original-codebase-overview.md)

## Reference

- [CLI Reference](./cli-reference.md)
- [API Reference](./api-reference.md)
- [Web App and UI](./web-app.md)
- [Agentic Demo](./agentic-demo.md)
- [Agentic Handbook](./agentic/README.md)
- [Media Policy](./media-policy.md)
- [Testing and Quality](./testing-and-quality.md)

## Operations and Contribution

- [Runbooks](./runbooks.md)
- [Development Workflow](./development-workflow.md)
- [Web Enablement Change Log](./web-enablement-change-log.md)
- [Documentation Governance](./documentation-governance.md)

## Scope of this Repository

This repository is a Python-first porting workspace and compatibility harness, not a full production Claude Code replacement runtime.

Core capabilities in this repo:
- Python manifest and parity summaries.
- Mirrored command and tool inventory metadata.
- Runtime routing and turn-loop simulation.
- Optional web UI powered by a lightweight FastAPI layer.

Non-goals in current scope:
- Full proprietary upstream feature parity.
- Production multi-tenant backend.
- Browser-only runtime without server support.

## Audience Paths

- New user path: `Getting Started` -> `Claude Code Primer` -> `Web App and UI`.
- App developer path: `Architecture` -> `API Reference` -> `Development Workflow`.
- Maintainer path: `Testing and Quality` -> `Runbooks` -> `Documentation Governance`.
