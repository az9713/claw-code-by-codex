# Agentic Feature Documentation

Last updated: 2026-04-01
Audience: users with no prior agent experience, contributors, maintainers

This section fully documents the new minimal multi-agent demo in this repository.

Read in this order:

1. [What Is Agentic Here?](./what-is-agentic.md)
2. [Implementation Details](./implementation-details.md)
3. [Testing Instructions (Git Bash)](./test-instructions-gitbash.md)
4. [Expected Test Results](./test-expected-results.md)
5. [How To Interpret Results](./result-interpretation.md)
6. [Capabilities and Limitations](./capability-and-limitations.md)
7. [FAQ and Troubleshooting](./faq-troubleshooting.md)

Core files involved:
- `src/agentic_demo.py`
- `src/web_app.py` (`POST /api/agentic-demo`)
- `web/index.html` + `web/static/app.js` + `web/static/styles.css`
- `tests/test_agentic_demo.py`
- `tests/test_web_app.py`
- `scripts/test_agentic.sh`

Summary:
- This is a real parallel worker orchestration demo.
- It is intentionally minimal and educational, not full autonomous production multi-agent runtime.
