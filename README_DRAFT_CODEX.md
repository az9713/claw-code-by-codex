# Claw Code by Codex

> Minimal Claude Code style harness workspace, rebuilt and expanded with Codex (`gpt-5.3-codex`).

## Identity

- Primary authoring agent: **Codex**
- Model: **gpt-5.3-codex**
- Repository: `az9713/claw-code-by-codex`
- Focus: Python porting workspace + web-enabled demo + comprehensive docs
- Status (2026-04-01): runnable, tested, web UI live-ready

## What This Project Is

This repository provides a Python-first harness workspace that mirrors command/tool surfaces, includes route/runtime simulation, and now ships a lightweight web UI powered by FastAPI.

It is designed for:
- learning harness architecture,
- exploring mirrored command/tool registries,
- testing CLI + HTTP interfaces,
- onboarding newcomers quickly.

## What Is Different From `claw-code-tutorial`

This variant is intentionally Codex-led and includes:
- web API + frontend (`src/web_app.py`, `web/`),
- expanded docs portal (`docs/`),
- stronger CLI ergonomics and safety checks,
- added test coverage for web and quick-win improvements.

See comparison matrix below.

## Comparison Matrix

| Category | `claw-code-by-codex` | `claw-code-tutorial` |
|---|---|---|
| Primary authoring agent | Codex | Claude Code (Opus) |
| Main model | gpt-5.3-codex | Opus variant |
| Primary interface | CLI + Web | CLI-first (and its own modifications) |
| FastAPI layer | Yes | Varies by that repo state |
| Frontend demo | Yes (`web/`) | Varies by that repo state |
| Docs strategy | Full docs portal in `docs/` | Independent docs strategy |
| Test suite | `unittest` + web tests | Independent test setup |

> Cross-link: https://github.com/az9713/claw-code-tutorial

## Quickstart

### CLI

```bash
python -m src.main summary
python -m src.main route "review MCP tool" --json
python -m unittest discover -s tests -v
```

### Web

```bash
python -m uvicorn src.web_app:app --host 127.0.0.1 --port 8000 --reload
```

Open:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

## Documentation

Start here:
- `docs/README.md`

Key docs:
- `docs/getting-started.md`
- `docs/architecture.md`
- `docs/cli-reference.md`
- `docs/api-reference.md`
- `docs/web-app.md`
- `docs/documentation-governance.md`

## Validation Snapshot

Latest local verification:
- full suite: **42/42 tests passed**

## Scope and Disclaimer

- This repository is a reconstruction/porting workspace and educational harness project.
- It is not an official Anthropic repository and is not a full proprietary runtime replacement.
