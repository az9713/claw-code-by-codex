# Runbooks

Last updated: 2026-04-01

## Start Local CLI Session

```bash
python -m src.main summary
```

Expected: markdown output with command and tool surface details.

## Start Local Web Server

```bash
python -m uvicorn src.web_app:app --host 127.0.0.1 --port 8000 --reload
```

Health checks:
- `GET /` -> 200
- `GET /api/manifest` -> 200
- `GET /docs` -> 200

## Stop Server on Windows (PowerShell)

If process id is known:

```powershell
Stop-Process -Id <PID> -Force
```

If port owner lookup is needed:

```powershell
Get-NetTCPConnection -LocalPort 8000 | Select-Object OwningProcess
Stop-Process -Id <OwningProcess> -Force
```

## Troubleshooting

### Browser says "site cannot be reached"

Checks:
1. Is uvicorn process running?
2. Is host/port correct?
3. Is a firewall or VPN intercepting localhost?

### API returns 422

Cause:
- Invalid query parameters (for example `limit=0`).

Fix:
- Use values within documented constraints.

### Session load errors

- `Invalid session id` means rejected by pattern validation.
- `Session file not found` means no persisted file exists.

## Release Smoke Checklist

- [ ] Full tests pass.
- [ ] CLI summary command works.
- [ ] `/api/manifest` and `/api/route` return expected fields.
- [ ] Web UI renders command/tool lists.
- [ ] Docs updated in `docs/` and README links verified.
