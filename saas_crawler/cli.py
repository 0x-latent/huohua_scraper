"""Project CLI for discovery and future platform jobs."""

from __future__ import annotations

import argparse

from .platforms.registry import list_platforms


def main() -> int:
    parser = argparse.ArgumentParser(prog="saas-crawler")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("platforms", help="列出已接入的平台")

    args = parser.parse_args()
    if args.command == "platforms":
        for platform in list_platforms():
            print(f"{platform.key}\t{platform.name}\t{platform.script}\t{platform.description}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
