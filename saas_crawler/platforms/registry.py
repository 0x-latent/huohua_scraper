"""Known platform definitions."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Platform:
    key: str
    name: str
    script: str
    description: str


PLATFORMS: dict[str, Platform] = {
    "huohua": Platform(
        key="huohua",
        name="火花",
        script="scripts/scraper_browser.py",
        description="B站火花平台 UP 主列表和详情采集",
    ),
    "feigua": Platform(
        key="feigua",
        name="飞瓜",
        script="scripts/feigua_scraper.py",
        description="飞瓜平台 B站 UP 主和 MCN 数据采集",
    ),
}


def list_platforms() -> list[Platform]:
    return list(PLATFORMS.values())
