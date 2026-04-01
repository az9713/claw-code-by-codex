# Development Workflow

Last updated: 2026-04-01

## Branch and Change Discipline

- Keep changes small and scoped.
- Update tests with code changes.
- Update docs in the same PR when behavior or interfaces change.

## Standard Local Loop

1. Implement code changes.
2. Run test suite.
3. Run representative CLI commands.
4. If API/UI touched, run web tests and endpoint smoke checks.
5. Update docs under `docs/` and root docs if required.

## Commands

Run full tests:

```bash
python -m unittest discover -s tests -v
```

Run API tests only:

```bash
python -m unittest tests.test_web_app -v
```

Run quick CLI sanity checks:

```bash
python -m src.main summary
python -m src.main route "review MCP tool" --json
```

Run web server:

```bash
python -m uvicorn src.web_app:app --host 127.0.0.1 --port 8000 --reload
```

## Code Style and Design Rules

- Keep business logic in `src/`; do not duplicate in frontend.
- Keep endpoint handlers thin and delegate to modules.
- Use explicit encoding for file IO (`utf-8`).
- Validate boundary inputs (CLI and API).
- Preserve deterministic outputs for stable tests.

## Definition of Done

A change is complete when all are true:
- Tests pass locally.
- New behavior is covered by tests.
- Relevant docs are updated.
- Manual smoke checks are recorded for user-facing changes.
