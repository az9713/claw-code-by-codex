from __future__ import annotations

import unittest

from fastapi.testclient import TestClient

from src.web_app import app


class WebAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)

    def test_index_page_serves(self) -> None:
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Claw Port Studio', response.text)

    def test_summary_endpoint(self) -> None:
        response = self.client.get('/api/summary')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn('markdown', payload)
        self.assertIn('Python Porting Workspace Summary', payload['markdown'])

    def test_manifest_endpoint(self) -> None:
        response = self.client.get('/api/manifest')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn('total_python_files', payload)
        self.assertGreaterEqual(payload['total_python_files'], 1)
        self.assertTrue(payload['top_level_modules'])

    def test_commands_endpoint(self) -> None:
        response = self.client.get('/api/commands', params={'limit': 5, 'query': 'review'})
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['limit'], 5)
        self.assertIn('entries', payload)

    def test_tools_endpoint(self) -> None:
        response = self.client.get('/api/tools', params={'limit': 5, 'query': 'mcp'})
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['limit'], 5)
        self.assertIn('entries', payload)

    def test_route_endpoint(self) -> None:
        response = self.client.get('/api/route', params={'prompt': 'review MCP tool', 'limit': 5})
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['prompt'], 'review MCP tool')
        self.assertIn('matches', payload)

    def test_agentic_demo_endpoint(self) -> None:
        response = self.client.post(
            '/api/agentic-demo',
            json={
                'prompts': ['review MCP tool', 'summarize command graph', 'inspect tool pool'],
                'route_limit': 5,
            },
        )
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['worker_count'], 3)
        self.assertIn('workers', payload)
        self.assertIn('orchestrator_summary', payload)
        self.assertEqual(len(payload['workers']), 3)


if __name__ == '__main__':
    unittest.main()
