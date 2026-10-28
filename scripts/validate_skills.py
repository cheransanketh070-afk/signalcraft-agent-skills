#!/usr/bin/env python3
"""Validate SignalCraft metadata, local references, required files, and generated platform mirrors."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "skills"


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, None, text, "missing YAML frontmatter at start of file"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None, text, "unterminated YAML frontmatter"
    meta = {}
    for line in parts[1].strip().splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta.get("name"), meta.get("description"), parts[2], None


def local_links(body):
    # Skip image-only links and external URLs; match ordinary Markdown links.
    for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", body):
        dest = match.group(1).strip().split("#", 1)[0]
        if not dest or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", dest) or dest.startswith("//"):
            continue
        yield dest


def files_under(directory: Path):
    return sorted(p.relative_to(directory).as_posix() for p in directory.rglob("*") if p.is_file())


def main() -> int:
    errors = []
    if not CANON.is_dir():
        print("ERROR: missing skills/", file=sys.stderr)
        return 1
    skills = sorted(p for p in CANON.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    if not skills:
        errors.append("No skill directories with SKILL.md found")
    seen = set()
    for folder in skills:
        manifest = folder / "SKILL.md"
        name, description, body, problem = parse_frontmatter(manifest)
        if problem:
            errors.append(f"{manifest.relative_to(ROOT)}: {problem}")
            continue
        if not name:
            errors.append(f"{manifest.relative_to(ROOT)}: missing name")
        elif name != folder.name:
            errors.append(f"{manifest.relative_to(ROOT)}: name '{name}' does not match folder '{folder.name}'")
        if name in seen:
            errors.append(f"duplicate skill name: {name}")
        seen.add(name)
        if not description:
            errors.append(f"{manifest.relative_to(ROOT)}: missing description")
        elif len(description) > 200:
            errors.append(f"{manifest.relative_to(ROOT)}: description is {len(description)} chars (max 200)")
        if name and len(name) > 64:
            errors.append(f"{manifest.relative_to(ROOT)}: name is longer than 64 characters")
        if len(body.strip()) < 100:
            errors.append(f"{manifest.relative_to(ROOT)}: skill instructions are suspiciously short")
        for link in local_links(body):
            target = (manifest.parent / link).resolve()
            try:
                target.relative_to(manifest.parent.resolve())
            except ValueError:
                errors.append(f"{manifest.relative_to(ROOT)}: local link escapes skill directory: {link}")
                continue
            if not target.exists():
                errors.append(f"{manifest.relative_to(ROOT)}: broken local link: {link}")

    # Verify mirrors match canonical folders, including file contents.
    for mirror_rel in [Path('.agents/skills'), Path('.claude/skills')]:
        mirror = ROOT / mirror_rel
        if not mirror.is_dir():
            errors.append(f"missing platform mirror: {mirror_rel.as_posix()}")
            continue
        canon_names = {p.name for p in skills}
        mirror_names = {p.name for p in mirror.iterdir() if p.is_dir()}
        if canon_names != mirror_names:
            errors.append(f"{mirror_rel.as_posix()} has skill folders different from skills/: expected {len(canon_names)}, found {len(mirror_names)}")
        for folder in skills:
            target = mirror / folder.name
            if not target.is_dir():
                continue
            src_files, dst_files = files_under(folder), files_under(target)
            if src_files != dst_files:
                errors.append(f"mirror file list mismatch: {mirror_rel.as_posix()}/{folder.name}")
                continue
            for rel in src_files:
                if (folder / rel).read_bytes() != (target / rel).read_bytes():
                    errors.append(f"mirror content mismatch: {mirror_rel.as_posix()}/{folder.name}/{rel}")

    # Essential project metadata.
    for rel in ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'SECURITY.md', 'docs/COMPATIBILITY.md']:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required project file: {rel}")

    if errors:
        print(f"VALIDATION FAILED ({len(errors)} issue(s)):")
        for err in errors:
            print(f" - {err}")
        return 1
    print(f"VALIDATION PASSED: {len(skills)} skills; metadata, local references, platform mirrors, and project files look good.")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
