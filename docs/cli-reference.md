# CLI Reference

Last updated: 2026-04-01

CLI entrypoint:

```bash
python -m src.main <command> [options]
```

## Core Workspace Commands

- `summary`: Render workspace summary markdown.
- `manifest`: Print current Python manifest.
- `parity-audit`: Compare against local ignored archive snapshot.
- `subsystems --limit N`: List module counts.

## Inventory Commands

- `commands [--limit N] [--query Q] [--no-plugin-commands] [--no-skill-commands] [--json]`
- `tools [--limit N] [--query Q] [--simple-mode] [--no-mcp] [--deny-tool X] [--deny-prefix X] [--json]`

## Routing and Session Commands

- `route <prompt> [--limit N] [--json]`
- `bootstrap <prompt> [--limit N]`
- `turn-loop <prompt> [--limit N] [--max-turns N] [--structured-output]`
- `flush-transcript <prompt>`
- `load-session <session_id> [--json]`

## Runtime Mode Simulation Commands

- `remote-mode <target>`
- `ssh-mode <target>`
- `teleport-mode <target>`
- `direct-connect-mode <target>`
- `deep-link-mode <target>`

## Lookup and Execution Commands

- `show-command <name> [--json]`
- `show-tool <name> [--json]`
- `exec-command <name> <prompt>`
- `exec-tool <name> <payload>`

## Graph and Setup Commands

- `setup-report`
- `command-graph`
- `tool-pool`
- `bootstrap-graph`

## Exit and Validation Behavior

- Positive integer options reject zero/negative values.
- Unknown command/tool lookups return non-zero status.
- `load-session` rejects invalid IDs and missing files with explicit errors.

## Example Workflows

### Find route matches

```bash
python -m src.main route "review MCP tool" --limit 5 --json
```

### Inspect tool inventory without MCP entries

```bash
python -m src.main tools --no-mcp --limit 20
```

### Persist and load a session

```bash
python -m src.main flush-transcript "sample prompt"
python -m src.main load-session <session_id> --json
```
