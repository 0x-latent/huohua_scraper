"""Configuration loading helpers."""

from pathlib import Path
from typing import Any

import yaml

from .paths import CONFIG_FILE


def load_yaml_config(path: Path = CONFIG_FILE) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"找不到配置文件: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def require_cookie_list(config: dict[str, Any], key: str, fallback_key: str | None = None) -> list[str]:
    cookies = config.get(key, [])
    if not cookies and fallback_key:
        fallback = config.get(fallback_key)
        cookies = [fallback] if fallback else []

    if isinstance(cookies, str):
        cookies = [cookies]

    values = [cookie.strip() for cookie in cookies if str(cookie).strip()]
    if not values:
        raise ValueError(f"配置文件中未配置 {key}")
    return values


def build_browser_headers(cookie: str, referer: str) -> dict[str, str]:
    return {
        "Cookie": cookie,
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/136.0.0.0 Safari/537.36"
        ),
        "Referer": referer,
    }
