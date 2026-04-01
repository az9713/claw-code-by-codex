from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .agentic_demo import TaskSpec, orchestrate
from .commands import get_commands
from .permissions import ToolPermissionContext
from .port_manifest import build_port_manifest
from .query_engine import QueryEnginePort
from .runtime import PortRuntime
from .tools import get_tools

PROJECT_ROOT = Path(__file__).resolve().parent.parent
WEB_ROOT = PROJECT_ROOT / 'web'
STATIC_ROOT = WEB_ROOT / 'static'
INDEX_PATH = WEB_ROOT / 'index.html'

app = FastAPI(
    title='Claw Code Port Web API',
    description='Lightweight API and UI for the Python porting workspace.',
    version='0.1.0',
)

app.mount('/static', StaticFiles(directory=STATIC_ROOT), name='static')


class AgenticDemoRequest(BaseModel):
    prompts: list[str] = Field(min_length=2, max_length=5)
    roles: list[str] | None = Field(default=None)
    route_limit: int = Field(default=5, ge=1, le=20)


def _matches_query(query: str, *values: str) -> bool:
    needle = query.lower()
    return any(needle in value.lower() for value in values)


@app.get('/', response_class=FileResponse)
def index() -> FileResponse:
    return FileResponse(INDEX_PATH)


@app.get('/api/summary')
def summary() -> dict[str, str]:
    engine = QueryEnginePort(build_port_manifest())
    return {'markdown': engine.render_summary()}


@app.get('/api/manifest')
def manifest() -> dict[str, object]:
    result = build_port_manifest()
    return {
        'src_root': str(result.src_root),
        'total_python_files': result.total_python_files,
        'top_level_modules': [asdict(module) for module in result.top_level_modules],
    }


@app.get('/api/commands')
def commands(
    limit: int = Query(default=20, ge=1, le=200),
    query: str | None = Query(default=None),
    include_plugin_commands: bool = Query(default=True),
    include_skill_commands: bool = Query(default=True),
) -> dict[str, object]:
    modules = list(
        get_commands(
            include_plugin_commands=include_plugin_commands,
            include_skill_commands=include_skill_commands,
        )
    )
    if query:
        modules = [
            module
            for module in modules
            if _matches_query(query, module.name, module.source_hint, module.responsibility)
        ]
    return {
        'total': len(modules),
        'limit': limit,
        'query': query,
        'entries': [asdict(module) for module in modules[:limit]],
    }


@app.get('/api/tools')
def tools(
    limit: int = Query(default=20, ge=1, le=200),
    query: str | None = Query(default=None),
    simple_mode: bool = Query(default=False),
    include_mcp: bool = Query(default=True),
    deny_tool: list[str] = Query(default=[]),
    deny_prefix: list[str] = Query(default=[]),
) -> dict[str, object]:
    permission_context = ToolPermissionContext.from_iterables(deny_tool, deny_prefix)
    modules = list(get_tools(simple_mode=simple_mode, include_mcp=include_mcp, permission_context=permission_context))
    if query:
        modules = [
            module
            for module in modules
            if _matches_query(query, module.name, module.source_hint, module.responsibility)
        ]
    return {
        'total': len(modules),
        'limit': limit,
        'query': query,
        'entries': [asdict(module) for module in modules[:limit]],
    }


@app.get('/api/route')
def route(
    prompt: str = Query(..., min_length=1),
    limit: int = Query(default=5, ge=1, le=50),
) -> dict[str, object]:
    matches = PortRuntime().route_prompt(prompt, limit=limit)
    return {
        'prompt': prompt,
        'total': len(matches),
        'matches': [asdict(match) for match in matches],
    }


@app.post('/api/agentic-demo')
async def agentic_demo(payload: AgenticDemoRequest) -> dict[str, object]:
    roles = payload.roles or []
    tasks = tuple(
        TaskSpec(
            agent_id=f'agent-{idx + 1}',
            role=roles[idx] if idx < len(roles) and roles[idx].strip() else f'worker-{idx + 1}',
            prompt=prompt,
        )
        for idx, prompt in enumerate(payload.prompts)
    )
    result = await orchestrate(tasks, route_limit=payload.route_limit)
    return {
        'worker_count': result.worker_count,
        'total_duration_ms': result.total_duration_ms,
        'workers': [asdict(worker) for worker in result.workers],
        'orchestrator_summary': result.orchestrator_summary,
    }
