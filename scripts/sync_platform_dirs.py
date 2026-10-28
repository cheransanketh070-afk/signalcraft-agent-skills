#!/usr/bin/env python3
"""Regenerate .agents/skills and .claude/skills from canonical skills/."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
TARGETS = [ROOT / ".agents" / "skills", ROOT / ".claude" / "skills"]


def main() -> int:
    if not SOURCE.is_dir():
        print("ERROR: canonical skills/ directory not found")
        return 1
    skill_dirs = sorted(p for p in SOURCE.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    if not skill_dirs:
        print("ERROR: no skills with SKILL.md found")
        return 1
    for target in TARGETS:
        target.mkdir(parents=True, exist_ok=True)
        for skill in skill_dirs:
            destination = target / skill.name
            if destination.exists():
                shutil.rmtree(destination)
            shutil.copytree(skill, destination)
        print(f"Synced {len(skill_dirs)} skills -> {target.relative_to(ROOT).as_posix()}/")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
