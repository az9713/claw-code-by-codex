# Original Codebase Overview

Last updated: 2026-04-01

This section documents the original baseline state of this repository before web enablement.

## Baseline Characteristics

- Python-first porting workspace under `src/`.
- CLI-first interaction surface via `python -m src.main`.
- Mirrored command and tool metadata loaded from snapshot JSON files.
- Runtime simulation for routing, bootstrap session, and turn loop.
- Local test coverage under `tests/`.

## Baseline Functional Surfaces

- Manifest generation (`src/port_manifest.py`).
- Parity audit (`src/parity_audit.py`).
- Command inventory and filtering (`src/commands.py`).
- Tool inventory and filtering (`src/tools.py`).
- Prompt routing and session simulation (`src/runtime.py`, `src/query_engine.py`).

## Baseline Constraints

- No HTTP API.
- No browser UI.
- Existing behavior primarily available through CLI and Python imports.

## Primary Entry Commands (Baseline)

```bash
python -m src.main summary
python -m src.main manifest
python -m src.main commands --limit 10
python -m src.main tools --limit 10
python -m src.main route "review MCP tool"
python -m unittest discover -s tests -v
```

## Relationship to Web Enablement

Web enablement was implemented as an additive layer. Core Python logic remained in place and became reusable from both CLI and HTTP endpoints.

See [Web Enablement Change Log](./web-enablement-change-log.md).
