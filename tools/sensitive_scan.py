#!/usr/bin/env python3
"""Lightweight sensitive-info scanner for public Markdown repos.

It is intentionally conservative: findings are warnings that require human review.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "dist", "build"}
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yml", ".yaml", ".toml", ".py", ".sh"}

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("macOS user path", re.compile(r"/Users/[A-Za-z0-9._-]+/")),
    ("possible API key", re.compile(r"(?i)(api[_-]?key|secret|token|password|passwd|pwd)\s*[:=]\s*['\"]?[^\s'\"]{8,}")),
    ("GitHub token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")),
    ("OpenAI-style key", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("Anthropic-style key", re.compile(r"sk-ant-[A-Za-z0-9_-]{20,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z_-]{20,}")),
    ("AWS access key", re.compile(r"\b(AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("JWT", re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("mainland phone", re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")),
]

ALLOWLIST_PATTERNS = [
    re.compile(r"/Users/<[^>]+>/"),
    re.compile(r"<TOKEN>|<API_KEY>|<SECRET>|<PASSWORD>"),
]


def should_scan(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    return path.suffix.lower() in TEXT_SUFFIXES


def is_allowlisted(line: str) -> bool:
    return any(pattern.search(line) for pattern in ALLOWLIST_PATTERNS)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    findings: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or not should_scan(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(root)
        for lineno, line in enumerate(text.splitlines(), 1):
            if is_allowlisted(line):
                continue
            for name, pattern in PATTERNS:
                if pattern.search(line):
                    snippet = line.strip()
                    if len(snippet) > 160:
                        snippet = snippet[:157] + "..."
                    findings.append(f"{rel}:{lineno}: {name}: {snippet}")
    if findings:
        print("Sensitive scan found warnings:\n")
        print("\n".join(findings))
        return 1
    print("Sensitive scan passed: no obvious sensitive patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
