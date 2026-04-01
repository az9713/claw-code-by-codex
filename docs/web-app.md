# Web App and UI

Last updated: 2026-04-01

## Purpose

Provide a browser interface over existing Python runtime surfaces without rewriting backend behavior in JavaScript.

## Components

- Backend API: `src/web_app.py`
- Frontend shell: `web/index.html`
- Frontend logic: `web/static/app.js`
- Frontend style: `web/static/styles.css`

## UI Features

- Hero metrics (Python file count, command count, tool count).
- Prompt Router panel (calls `/api/route`).
- Searchable Commands panel (calls `/api/commands`).
- Searchable Tools panel (calls `/api/tools`).
- Runtime summary pane (calls `/api/summary`).

## Frontend Data Flow

1. On load, `app.js` calls:
   - `/api/manifest`
   - `/api/summary`
   - `/api/commands?limit=12`
   - `/api/tools?limit=12`
2. UI renders returned JSON/markdown.
3. User interactions trigger new API requests.

## Why Plain HTML/CSS/JS

- Small dependency surface.
- Faster onboarding for new contributors.
- Clear boundary: browser rendering only, all logic in Python.

## Accessibility and UX Notes

- Inputs are keyboard-accessible.
- Responsive layout supported for small screens.
- Visual hierarchy and contrast optimized for readability.

## Local Demo Script

```bash
python -m uvicorn src.web_app:app --host 127.0.0.1 --port 8000 --reload
```

## Alternatives Considered

1. Static HTML generated from CLI output
- Good for docs, not interactive.

2. React/Next.js frontend
- Better scale for large UI but adds build complexity.

3. No API, browser-only logic
- Causes behavior drift and duplicate implementation burden.

## Future Improvements

- Add dark mode toggle with persisted preference.
- Add endpoint latency and error banners.
- Add pagination/virtualization for very large inventories.
- Add auth if exposed beyond localhost.

## Demo Video

- Local compressed (GitHub-friendly): `docs/demo_agents_github.mp4`
- Placeholder URL (replace later): `https://example.com/TODO-claw-code-by-codex-agentic-demo-video`
