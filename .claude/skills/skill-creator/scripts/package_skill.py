#!/usr/bin/env python3
"""Package a skill folder into a distributable .skill file (zip archive).

Usage:
    python -m scripts.package_skill <path/to/skill-folder>

Output:
    <skill-name>.skill written as a sibling to the skill folder.
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path


def read_skill_name(skill_path: Path) -> str:
    skill_md = skill_path / "SKILL.md"
    text = skill_md.read_text()
    m = re.search(r"^name:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else skill_path.name


def package(skill_path: Path) -> Path:
    skill_path = skill_path.resolve()

    if not (skill_path / "SKILL.md").exists():
        print(f"Error: no SKILL.md found in {skill_path}", file=sys.stderr)
        sys.exit(1)

    skill_name = read_skill_name(skill_path)
    out_path = skill_path.parent / f"{skill_name}.skill"

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in sorted(skill_path.rglob("*")):
            if file.is_file():
                zf.write(file, file.relative_to(skill_path.parent))

    print(out_path)
    return out_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_path", type=Path)
    args = parser.parse_args()
    package(args.skill_path)


if __name__ == "__main__":
    main()
