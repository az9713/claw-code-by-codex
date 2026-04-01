from __future__ import annotations

import asyncio
import unittest

from src.agentic_demo import TaskSpec, build_orchestrator_summary, orchestrate, run_parallel_agents


class AgenticDemoTests(unittest.TestCase):
    def test_parallel_agents_return_results(self) -> None:
        tasks = (
            TaskSpec(agent_id='agent-1', role='reviewer', prompt='review MCP tool'),
            TaskSpec(agent_id='agent-2', role='analyst', prompt='summarize command graph'),
        )
        results = asyncio.run(run_parallel_agents(tasks, route_limit=5))
        self.assertEqual(len(results), 2)
        self.assertTrue(all(result.agent_id for result in results))
        self.assertTrue(all(result.output for result in results))

    def test_orchestrator_summary_contains_worker_lines(self) -> None:
        tasks = (
            TaskSpec(agent_id='agent-1', role='reviewer', prompt='review MCP tool'),
            TaskSpec(agent_id='agent-2', role='analyst', prompt='inspect tool pool'),
        )
        outcome = asyncio.run(orchestrate(tasks, route_limit=5))
        self.assertEqual(outcome.worker_count, 2)
        self.assertIn('Main orchestrator merged parallel worker outputs:', outcome.orchestrator_summary)
        self.assertGreaterEqual(outcome.total_duration_ms, 0)

    def test_summary_for_empty_results(self) -> None:
        self.assertEqual(build_orchestrator_summary(()), 'No workers executed.')


if __name__ == '__main__':
    unittest.main()

