#!/usr/bin/env python3
"""Minimal validation scaffold for repo governance files."""

from __future__ import annotations

from pathlib import Path


REQUIRED = [
    Path("AGENTS.md"),
    Path("README.md"),
    Path(".ai/README.md"),
    Path(".ai/agents/README.md"),
    Path(".ai/contracts/README.md"),
    Path(".ai/skills/README.md"),
    Path(".ai/templates/README.md"),
]


def main() -> int:
    missing = [str(path) for path in REQUIRED if not path.exists()]
    if missing:
        print("Missing required files:")
        for item in missing:
            print(f" - {item}")
        return 1
    print("Governance skeleton present and valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
