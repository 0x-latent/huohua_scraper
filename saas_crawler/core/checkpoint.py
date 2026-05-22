"""JSON checkpoint helpers."""

import json
import os
import time
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> dict[str, Any]:
    checkpoint_path = Path(path)
    if checkpoint_path.exists():
        with checkpoint_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_json_atomic(path: str | Path, data: dict[str, Any], retries: int = 5) -> None:
    checkpoint_path = Path(path)
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = checkpoint_path.with_name(checkpoint_path.name + ".tmp")

    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    for attempt in range(retries):
        try:
            os.replace(tmp_path, checkpoint_path)
            return
        except PermissionError:
            if attempt == retries - 1:
                break
            time.sleep(1)

    with checkpoint_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def remove_file(path: str | Path) -> None:
    target = Path(path)
    if target.exists():
        target.unlink()
