from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

from src.commands import find_commands
from src.main import positive_int
from src.query_engine import QueryEnginePort
from src.runtime import PortRuntime
from src.session_store import load_session
from src.tools import find_tools


class QuickWinsTests(unittest.TestCase):
    def test_positive_int_validator(self) -> None:
        self.assertEqual(positive_int('3'), 3)
        with self.assertRaises(Exception):
            positive_int('0')

    def test_command_search_includes_responsibility(self) -> None:
        self.assertGreaterEqual(len(find_commands('command module mirrored', limit=5)), 1)

    def test_tool_search_includes_responsibility(self) -> None:
        self.assertGreaterEqual(len(find_tools('tool module mirrored', limit=5)), 1)

    def test_route_limit_zero_returns_empty(self) -> None:
        self.assertEqual(PortRuntime().route_prompt('review mcp', limit=0), [])

    def test_query_engine_reports_remaining_budget(self) -> None:
        result = QueryEnginePort.from_workspace().submit_message('review mcp tool')
        self.assertIn('Remaining budget tokens:', result.output)

    def test_load_session_rejects_invalid_session_id(self) -> None:
        with self.assertRaises(ValueError):
            load_session('../bad-id')

    def test_cli_commands_json_output(self) -> None:
        result = subprocess.run(
            [sys.executable, '-m', 'src.main', 'commands', '--limit', '3', '--json'],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertIn('entries', payload)
        self.assertEqual(payload['limit'], 3)

    def test_cli_tools_json_output(self) -> None:
        result = subprocess.run(
            [sys.executable, '-m', 'src.main', 'tools', '--limit', '3', '--json'],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertIn('entries', payload)
        self.assertEqual(payload['limit'], 3)

    def test_cli_route_json_output(self) -> None:
        result = subprocess.run(
            [sys.executable, '-m', 'src.main', 'route', 'review MCP tool', '--limit', '3', '--json'],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertIsInstance(payload, list)

    def test_cli_load_session_reports_error(self) -> None:
        result = subprocess.run(
            [sys.executable, '-m', 'src.main', 'load-session', 'does-not-exist'],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Session file not found:', result.stdout)

    def test_cli_show_command_json_output(self) -> None:
        result = subprocess.run(
            [sys.executable, '-m', 'src.main', 'show-command', 'review', '--json'],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload['name'].lower(), 'review')

    def test_cli_show_tool_json_output(self) -> None:
        result = subprocess.run(
            [sys.executable, '-m', 'src.main', 'show-tool', 'MCPTool', '--json'],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload['name'], 'MCPTool')

    def test_cli_limit_validation_rejects_zero(self) -> None:
        result = subprocess.run(
            [sys.executable, '-m', 'src.main', 'commands', '--limit', '0'],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('value must be a positive integer', result.stderr)

    def test_load_session_json_with_real_session(self) -> None:
        flush = subprocess.run(
            [sys.executable, '-m', 'src.main', 'flush-transcript', 'quick wins session'],
            check=True,
            capture_output=True,
            text=True,
        )
        path = Path(flush.stdout.splitlines()[0].strip())
        session_id = path.stem
        result = subprocess.run(
            [sys.executable, '-m', 'src.main', 'load-session', session_id, '--json'],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload['session_id'], session_id)


if __name__ == '__main__':
    unittest.main()
