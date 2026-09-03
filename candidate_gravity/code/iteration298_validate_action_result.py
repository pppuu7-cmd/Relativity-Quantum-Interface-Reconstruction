#!/usr/bin/env python3
"""Validate that a GitHub Actions scientific result is one authoritative JSON payload.

The validator deliberately accepts concatenated JSON as input so it can detect stdout
contamination from imported scripts.  A scientific Action result passes only when the
file contains exactly one top-level JSON object and its `iteration` sentinel equals the
expected iteration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def decode_all(text: str) -> list[Any]:
    decoder = json.JSONDecoder()
    objects: list[Any] = []
    i = 0
    n = len(text)
    while True:
        while i < n and text[i].isspace():
            i += 1
        if i >= n:
            return objects
        obj, end = decoder.raw_decode(text, i)
        objects.append(obj)
        i = end


def audit(path: Path, expected_iteration: int) -> dict[str, Any]:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    objects = decode_all(text)
    iterations = [obj.get("iteration") if isinstance(obj, dict) else None for obj in objects]
    valid_single_top_level = len(objects) == 1 and isinstance(objects[0], dict)
    valid_expected_iteration = valid_single_top_level and iterations == [expected_iteration]
    return {
        "schema": "rqir_action_result_authority_audit_v1",
        "path": str(path),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "expected_iteration": expected_iteration,
        "top_level_object_count": len(objects),
        "found_iterations": iterations,
        "valid_single_top_level": valid_single_top_level,
        "valid_expected_iteration": valid_expected_iteration,
        "scientific_authority_pass": valid_expected_iteration,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("result_file", type=Path)
    parser.add_argument("--expected-iteration", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = audit(args.result_file, args.expected_iteration)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if result["scientific_authority_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
