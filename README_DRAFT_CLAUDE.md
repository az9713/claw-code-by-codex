# Claw Code Tutorial (Claude/Opus Variant)

> Minimal Claude Code style harness workspace, modified with Claude Code using Opus.

## Identity

- Primary authoring agent: **Claude Code**
- Model: **Opus**
- Repository: `az9713/claw-code-tutorial`
- Focus: tutorial-oriented variant and Claude-led modifications
- Status: maintain according to this repo's current branch state

## What This Project Is

This repository documents and demonstrates a Claude/Opus-driven modification path for a Claude Code style harness workspace.

It is designed for:
- tutorial workflows,
- Claude-led coding iterations,
- learning by progressive changes.

## Relationship to `claw-code-by-codex`

This is one of two sibling variants:
- `claw-code-tutorial`: Claude/Opus-authored path
- `claw-code-by-codex`: Codex/gpt-5.3-codex-authored path

Use both to compare model/operator style, architecture decisions, and implementation choices.

## Comparison Matrix

| Category | `claw-code-tutorial` | `claw-code-by-codex` |
|---|---|---|
| Primary authoring agent | Claude Code | Codex |
| Main model | Opus | gpt-5.3-codex |
| Project framing | Tutorial-first | Engineering docs + web demo |
| Web API/UI layer | Per this repo state | Included (`src/web_app.py`, `web/`) |
| Docs strategy | Per this repo state | Full docs portal in `docs/` |
| Tests | Per this repo state | `unittest` + web tests |

> Cross-link: https://github.com/az9713/claw-code-by-codex

## Suggested Readme Sections To Keep Updated

1. Identity block (authoring agent/model/date).
2. Exact quickstart commands that currently work.
3. Major architecture notes for this repo only.
4. Differences versus sibling repo.
5. Validation status (tests/checks).

## Quickstart (Template)

Replace with commands that match this repository's current implementation.

```bash
python -m src.main summary
python -m unittest discover -s tests -v
```

## Documentation and Governance

Recommended:
- add a `docs/` portal similar to the Codex repo,
- include a `documentation-governance.md` file,
- require docs updates in each behavior-changing PR.

## Scope and Disclaimer

- This repository is an educational/tutorial reconstruction workspace.
- It is not an official Anthropic repository and is not a full proprietary runtime replacement.
