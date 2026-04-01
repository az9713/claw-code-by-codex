from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class StoredSession:
    session_id: str
    messages: tuple[str, ...]
    input_tokens: int
    output_tokens: int


DEFAULT_SESSION_DIR = Path('.port_sessions')
SESSION_ID_PATTERN = re.compile(r'^[A-Za-z0-9_-]+$')


def save_session(session: StoredSession, directory: Path | None = None) -> Path:
    target_dir = directory or DEFAULT_SESSION_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / f'{session.session_id}.json'
    path.write_text(json.dumps(asdict(session), indent=2), encoding='utf-8')
    return path


def load_session(session_id: str, directory: Path | None = None) -> StoredSession:
    if not SESSION_ID_PATTERN.fullmatch(session_id):
        raise ValueError(f'Invalid session id: {session_id!r}')
    target_dir = directory or DEFAULT_SESSION_DIR
    path = target_dir / f'{session_id}.json'
    if not path.exists():
        raise FileNotFoundError(f'Session file not found: {path}')
    data = json.loads(path.read_text(encoding='utf-8'))
    return StoredSession(
        session_id=data['session_id'],
        messages=tuple(data['messages']),
        input_tokens=data['input_tokens'],
        output_tokens=data['output_tokens'],
    )
