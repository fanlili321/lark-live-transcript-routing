#!/usr/bin/env python3
"""Convert a Feishu Minutes transcript into bounded XML fragments for Docx."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


def parse_blocks(text: str) -> list[str]:
    lines = text.replace("\r\n", "\n").split("\n")
    blocks: list[str] = []
    skip_next = False
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("Keywords:"):
            # Skip the "Keywords:" marker and the line that follows it
            skip_next = line.startswith("Keywords:")
            continue
        if skip_next:
            skip_next = False
            continue
        if "CST|" in line and line[:4].isdigit():
            continue
        escaped = html.escape(line, quote=False)
        if len(line) < 40 and any(ch.isdigit() for ch in line) and ":" in line:
            blocks.append(f"<p><b>{escaped}</b></p>")
        else:
            blocks.append(f"<p>{escaped}</p>")
    return blocks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output_dir")
    parser.add_argument("--title", required=True)
    parser.add_argument("--chunk-chars", type=int, default=12000)
    args = parser.parse_args()

    source = Path(args.input)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    blocks = parse_blocks(source.read_text(encoding="utf-8"))

    chunks: list[str] = []
    current = ""
    for block in blocks:
        if current and len(current) + len(block) > args.chunk_chars:
            chunks.append(current)
            current = ""
        current += block
    if current:
        chunks.append(current)

    paths: list[str] = []
    for index, chunk in enumerate(chunks):
        prefix = f"<title>{html.escape(args.title, quote=False)}</title>" if index == 0 else ""
        path = out_dir / f"chunk-{index:03d}.xml"
        path.write_text(prefix + chunk, encoding="utf-8")
        paths.append(str(path))

    print(json.dumps({"chunks": paths, "block_count": len(blocks)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
