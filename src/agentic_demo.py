from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass

from .query_engine import QueryEnginePort
from .runtime import PortRuntime


@dataclass(frozen=True)
class TaskSpec:
    agent_id: str
    role: str
    prompt: str


@dataclass(frozen=True)
class AgentResult:
    agent_id: str
    role: str
    prompt: str
    matched_commands: tuple[str, ...]
    matched_tools: tuple[str, ...]
    output: str
    stop_reason: str
    duration_ms: int


@dataclass(frozen=True)
class OrchestrationResult:
    worker_count: int
    total_duration_ms: int
    workers: tuple[AgentResult, ...]
    orchestrator_summary: str


def _run_worker_sync(task: TaskSpec, route_limit: int) -> AgentResult:
    started = time.perf_counter()
    runtime = PortRuntime()
    matches = runtime.route_prompt(task.prompt, limit=route_limit)
    command_names = tuple(match.name for match in matches if match.kind == 'command')
    tool_names = tuple(match.name for match in matches if match.kind == 'tool')
    engine = QueryEnginePort.from_workspace()
    turn = engine.submit_message(task.prompt, matched_commands=command_names, matched_tools=tool_names)
    elapsed_ms = int((time.perf_counter() - started) * 1000)
    return AgentResult(
        agent_id=task.agent_id,
        role=task.role,
        prompt=task.prompt,
        matched_commands=command_names,
        matched_tools=tool_names,
        output=turn.output,
        stop_reason=turn.stop_reason,
        duration_ms=elapsed_ms,
    )


async def run_parallel_agents(tasks: tuple[TaskSpec, ...], route_limit: int = 5) -> tuple[AgentResult, ...]:
    if not tasks:
        return ()
    jobs = [asyncio.to_thread(_run_worker_sync, task, route_limit) for task in tasks]
    results = await asyncio.gather(*jobs)
    return tuple(results)


def build_orchestrator_summary(results: tuple[AgentResult, ...]) -> str:
    if not results:
        return 'No workers executed.'
    lines = ['Main orchestrator merged parallel worker outputs:']
    for result in results:
        lines.append(
            f"- {result.agent_id} ({result.role}): commands={len(result.matched_commands)} "
            f"tools={len(result.matched_tools)} stop={result.stop_reason} duration_ms={result.duration_ms}"
        )
    return '\n'.join(lines)


async def orchestrate(tasks: tuple[TaskSpec, ...], route_limit: int = 5) -> OrchestrationResult:
    started = time.perf_counter()
    workers = await run_parallel_agents(tasks, route_limit=route_limit)
    total_duration_ms = int((time.perf_counter() - started) * 1000)
    return OrchestrationResult(
        worker_count=len(workers),
        total_duration_ms=total_duration_ms,
        workers=workers,
        orchestrator_summary=build_orchestrator_summary(workers),
    )

