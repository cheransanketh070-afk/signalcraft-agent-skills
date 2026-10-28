#!/usr/bin/env python3
"""Package each canonical skill as a Claude upload ZIP with <skill-name>/ at archive root."""
from pathlib import Path
import zipfile
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
OUT = ROOT / "dist" / "claude-uploads"


def main() -> int:
    skill_dirs = sorted(p for p in SOURCE.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    if not skill_dirs:
        print("ERROR: no skills found")
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    for archive in OUT.glob("*.zip"):
        archive.unlink()
    for skill in skill_dirs:
        archive = OUT / f"{skill.name}.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for path in sorted(skill.rglob("*")):
                if path.is_file():
                    # include the folder itself as first path component, as required by Claude's upload convention
                    zf.write(path, arcname=(Path(skill.name) / path.relative_to(skill)).as_posix())
        print(f"Created {archive.relative_to(ROOT).as_posix()}")
    print(f"Packaged {len(skill_dirs)} skills.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
