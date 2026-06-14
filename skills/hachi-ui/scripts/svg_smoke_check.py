#!/usr/bin/env python3
"""Basic checks for standalone SVG UI prototype files."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"


def local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def attr(element: ET.Element, name: str) -> str | None:
    return element.attrib.get(name)


def has_numeric_dimension(value: str | None) -> bool:
    if not value:
        return False
    return bool(re.match(r"^\d+(?:\.\d+)?(?:px)?$", value.strip()))


def check_svg(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        return [f"invalid XML: {exc}"], warnings

    if local_name(root.tag) != "svg":
        errors.append("root element is not <svg>")
        return errors, warnings

    if attr(root, "viewBox") is None:
        errors.append("missing viewBox")

    if not has_numeric_dimension(attr(root, "width")):
        errors.append("missing numeric width")

    if not has_numeric_dimension(attr(root, "height")):
        errors.append("missing numeric height")

    tags = [local_name(element.tag) for element in root.iter()]
    if "title" not in tags:
        warnings.append("missing <title>")
    if "desc" not in tags:
        warnings.append("missing <desc>")
    if "script" in tags:
        errors.append("contains <script>; UI prototype SVGs must be static")

    ids: dict[str, int] = {}
    for element in root.iter():
        element_id = attr(element, "id")
        if element_id:
            ids[element_id] = ids.get(element_id, 0) + 1

        if local_name(element.tag) == "image":
            href = (
                element.attrib.get("href")
                or element.attrib.get(f"{{{XLINK_NS}}}href")
                or ""
            )
            if href.startswith(("http://", "https://", "//")):
                errors.append(f"external image reference: {href}")

    duplicate_ids = sorted(element_id for element_id, count in ids.items() if count > 1)
    if duplicate_ids:
        errors.append("duplicate ids: " + ", ".join(duplicate_ids))

    if root.tag.startswith("{") and not root.tag.startswith(f"{{{SVG_NS}}}"):
        warnings.append("root element uses an unexpected XML namespace")

    return errors, warnings


def main(argv: list[str]) -> int:
    if not argv:
        print("Usage: svg_smoke_check.py <file.svg> [more.svg ...]", file=sys.stderr)
        return 2

    failed = False
    for raw_path in argv:
        path = Path(raw_path)
        if not path.exists():
            print(f"FAIL {path}: file does not exist")
            failed = True
            continue

        errors, warnings = check_svg(path)
        if errors:
            failed = True
            print(f"FAIL {path}")
            for issue in errors:
                print(f"  error: {issue}")
        else:
            print(f"OK {path}")

        for issue in warnings:
            print(f"  warning: {issue}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
