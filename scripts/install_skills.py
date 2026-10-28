#!/usr/bin/env python3
"""Install SignalCraft skills for Codex, Claude Code, or both without overwriting by default."""
from pathlib import Path
import argparse
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"


def discover_skills():
    return sorted(p for p in SOURCE.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())


def destinations(args):
    if args.scope == "user":
        base = Path.home()
        codex = base / ".agents" / "skills"
        claude = base / ".claude" / "skills"
    else:
        if not args.project_dir:
            raise ValueError("--project-dir is required when --scope project")
        project = Path(args.project_dir).expanduser().resolve()
        if not project.exists() or not project.is_dir():
            raise ValueError(f"project directory does not exist: {project}")
        codex = project / ".agents" / "skills"
        claude = project / ".claude" / "skills"
    all_dest = {"codex": codex, "claude": claude}
    return all_dest if args.target == "both" else {args.target: all_dest[args.target]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=["codex", "claude", "both"], default="both")
    parser.add_argument("--scope", choices=["user", "project"], default="user")
    parser.add_argument("--project-dir", help="Target project directory (required for --scope project)")
    parser.add_argument("--overwrite", action="store_true", help="Replace a same-named installed skill")
    parser.add_argument("--dry-run", action="store_true", help="Print planned operations without copying files")
    args = parser.parse_args()

    try:
        dests = destinations(args)
    except ValueError as exc:
        parser.error(str(exc))

    skills = discover_skills()
    if not skills:
        print("ERROR: no canonical skills found in skills/", file=sys.stderr)
        return 1

    copied = skipped = 0
    for platform, base in dests.items():
        for source in skills:
            target = base / source.name
            if target.exists() and not args.overwrite:
                print(f"SKIP existing {platform}: {target} (use --overwrite to replace)")
                skipped += 1
                continue
            action = "WOULD INSTALL" if args.dry_run else "INSTALL"
            print(f"{action} {source.name} -> {target}")
            if not args.dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists():
                    shutil.rmtree(target)
                shutil.copytree(source, target)
            copied += 1
    print(f"Done. {'Planned' if args.dry_run else 'Installed'}: {copied}; skipped: {skipped}.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
