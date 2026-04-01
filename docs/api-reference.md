# API Reference

Last updated: 2026-04-01

Base URL (default local): `http://127.0.0.1:8000`

Interactive schema docs:
- `/docs` (Swagger UI)

## GET /

Serves `web/index.html`.

Response:
- `200 text/html`

## GET /api/summary

Returns markdown summary rendered by `QueryEnginePort`.

Response shape:

```json
{
  "markdown": "# Python Porting Workspace Summary\n..."
}
```

## GET /api/manifest

Returns current port manifest.

Response fields:
- `src_root: string`
- `total_python_files: number`
- `top_level_modules: Subsystem[]`

`Subsystem` fields:
- `name: string`
- `path: string`
- `file_count: number`
- `notes: string`

## GET /api/commands

Query params:
- `limit` (int, default `20`, min `1`, max `200`)
- `query` (optional string)
- `include_plugin_commands` (bool, default `true`)
- `include_skill_commands` (bool, default `true`)

Response shape:

```json
{
  "total": 123,
  "limit": 20,
  "query": "review",
  "entries": [
    {
      "name": "review",
      "responsibility": "...",
      "source_hint": "...",
      "status": "mirrored"
    }
  ]
}
```

## GET /api/tools

Query params:
- `limit` (int, default `20`, min `1`, max `200`)
- `query` (optional string)
- `simple_mode` (bool, default `false`)
- `include_mcp` (bool, default `true`)
- `deny_tool` (repeatable string list)
- `deny_prefix` (repeatable string list)

Response shape mirrors `/api/commands`.

## GET /api/route

Query params:
- `prompt` (required string, min length `1`)
- `limit` (int, default `5`, min `1`, max `50`)

Response shape:

```json
{
  "prompt": "review MCP tool",
  "total": 3,
  "matches": [
    {
      "kind": "tool",
      "name": "MCPTool",
      "source_hint": "tools/MCPTool/MCPTool.ts",
      "score": 2
    }
  ]
}
```

## POST /api/agentic-demo

Runs multiple worker tasks in parallel and returns an orchestrator summary.

Request body:

```json
{
  "prompts": ["review MCP tool", "summarize command graph"],
  "roles": ["reviewer", "analyst"],
  "route_limit": 5
}
```

Body constraints:
- `prompts`: list length 2-5
- `route_limit`: 1-20
- `roles`: optional list; defaults to `worker-{n}` roles when omitted

Response fields:
- `worker_count: number`
- `total_duration_ms: number`
- `workers: AgentResult[]`
- `orchestrator_summary: string`

## Error Behavior

- Validation errors return `422` (FastAPI default).
- Missing static files or path issues return standard `404/500` depending on failure mode.

## API Stability Policy

- Additive fields are allowed in minor updates.
- Field removal or type changes require explicit migration notes in `docs/web-enablement-change-log.md`.
- Tests in `tests/test_web_app.py` must be updated with API changes.
