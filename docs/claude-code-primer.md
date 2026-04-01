# Claude Code Primer (For Newcomers)

Last updated: 2026-04-01

## What is a Claude Code style harness?

A harness is the runtime shell around an LLM model that manages:
- prompts and system instructions,
- tool calling,
- session state,
- permissions,
- output formatting.

In simple terms: the model is the brain, the harness is the operating system around that brain.

## Terms You Will See In This Repo

- `Command`: a user-facing capability route (for example review or setup).
- `Tool`: an execution primitive (for example MCP, file read, shell).
- `Manifest`: current Python workspace file structure summary.
- `Parity audit`: a comparison against archived TypeScript surface snapshots.
- `Runtime session`: simulated stateful turn execution and routing output.

## How This Repo Maps to Those Ideas

- `src/main.py`: CLI entry point.
- `src/commands.py`: mirrored command metadata and lookup.
- `src/tools.py`: mirrored tool metadata and filtering.
- `src/runtime.py`: prompt routing and turn-loop simulation.
- `src/query_engine.py`: summary rendering and turn output.
- `src/parity_audit.py`: parity metrics.
- `src/web_app.py`: HTTP interface for browser clients.

## What This Repo Is Not

- Not a full production Claude Code clone.
- Not a complete replacement for proprietary runtime internals.
- Not a browser-native-only app.

## Why an API Layer Exists

Browsers cannot directly execute this server-side Python logic. The API layer exposes stable JSON endpoints so the frontend can call existing Python features without re-implementing logic in JavaScript.

## Suggested Learning Sequence

1. Run CLI summary and manifest.
2. Run route command on a prompt.
3. Launch web UI and compare route behavior.
4. Read [Architecture](./architecture.md).
