# Testing and Quality

Last updated: 2026-04-01

## Test Suite Overview

- Framework: Python `unittest`
- Entry command:

```bash
python -m unittest discover -s tests -v
```

## Test Modules

- `tests/test_porting_workspace.py`
  - Core CLI and workspace behavior checks.
- `tests/test_quick_wins.py`
  - Quality/safety improvements, JSON outputs, validation behavior.
- `tests/test_web_app.py`
  - FastAPI endpoint integration tests.

## Quality Gates

Required before merge:
- Full test suite green.
- No breaking changes to CLI/API without docs updates.
- New public behavior includes at least one regression test.

## Suggested Manual Verification

- CLI summary renders.
- Route command returns expected match format.
- Web UI loads and populates panels.
- API docs page `/docs` is reachable.

## Non-Functional Quality Priorities

- Deterministic outputs.
- Explicit validation errors.
- Small dependency surface.
- Clear interfaces between layers.

## Technical Debt Controls

- Do not bypass tests for user-facing changes.
- Do not add duplicate business logic to frontend.
- Do not introduce endpoint fields without docs/tests updates.
