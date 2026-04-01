# Architecture

Last updated: 2026-04-01

## High-Level View

```text
CLI (src.main)         Web UI (web/static)
      |                       |
      |                HTTP / JSON
      |                       |
      +------> FastAPI (src.web_app) <------+
                       |                     |
                 Runtime + Query             |
               (src.runtime, src.query_engine)
                       |
            Commands + Tools metadata
            (src.commands, src.tools)
                       |
          Manifest + Parity + Session Store
 (src.port_manifest, src.parity_audit, src.session_store)
```

## Module Responsibilities

- `src/main.py`
  - CLI command parsing, output routing, and JSON/text response selection.
- `src/web_app.py`
  - API and static file serving for browser clients.
- `src/runtime.py`
  - Prompt tokenization, route scoring, turn loop, bootstrap session orchestration.
- `src/query_engine.py`
  - Session turn output, usage budgeting, transcript handling.
- `src/commands.py`
  - Command snapshot load, index/search, execution shim.
- `src/tools.py`
  - Tool snapshot load, permission filtering, index/search, execution shim.
- `src/permissions.py`
  - Tool deny-name and deny-prefix policy.
- `src/port_manifest.py`
  - Python workspace inventory and markdown representation.
- `src/parity_audit.py`
  - Coverage and ratio checks against archive reference snapshots.
- `src/session_store.py`
  - Session persistence and load with validation.

## Data Sources

Primary reference files:
- `src/reference_data/commands_snapshot.json`
- `src/reference_data/tools_snapshot.json`
- `src/reference_data/archive_surface_snapshot.json`

These files are treated as source-of-truth snapshots for mirrored surface reporting.

## Request Flows

### CLI Route
1. `python -m src.main route "..."`
2. `PortRuntime.route_prompt()`
3. ranked `command` + `tool` matches returned.

### Web Route
1. Browser calls `GET /api/route?prompt=...`
2. `src.web_app.route()` delegates to `PortRuntime.route_prompt()`
3. JSON match payload returned to frontend.

### Summary
1. CLI or web asks for summary.
2. `QueryEnginePort(build_port_manifest()).render_summary()`
3. Markdown summary returned.

## Design Decisions

- Keep business behavior in Python modules (`src/`) and keep UI thin.
- Use dataclasses for predictable serialization and tests.
- Prefer deterministic text/JSON outputs for testing and automation.
- Enforce edge validation at boundaries (CLI parser and API query schema).

## Technical Constraints

- This is a compatibility and introspection workspace, not full model orchestration.
- Snapshots may include duplicate names; indices keep first-seen entries.
- API currently has no auth and is intended for local/dev usage.
