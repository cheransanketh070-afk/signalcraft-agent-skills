# Repository architecture

- `skills/` is the canonical source. Each skill includes a short `SKILL.md` and optional local references/templates.
- `.agents/skills/` is a generated mirror for compatible Codex/OpenAI agent surfaces.
- `.claude/skills/` is a generated mirror for Claude Code project-level discovery.
- `scripts/sync_platform_dirs.py` refreshes both mirrors from canonical files.
- `scripts/install_skills.py` installs canonical skills to user-level or project-level directories without overwriting by default.
- `scripts/package_claude_zips.py` creates one upload ZIP per skill, with the named skill folder at the archive root.
- `scripts/validate_skills.py` verifies metadata, linked local resources, description length, mirror parity, and required files.
- `tests/` contains dependency-free tests of repository packaging and metadata rules.

The skills do not make network calls or require runtime secrets. Host tools determine whether a workflow can browse, edit files, execute code, or interact with external services.
