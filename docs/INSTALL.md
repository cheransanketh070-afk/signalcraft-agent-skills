# Installation guide

## Quick install

From the repository root, run:

```bash
python scripts/install_skills.py --target both --scope user
```

## Options

```text
--target {codex,claude,both}     Install to selected ecosystem(s)
--scope {user,project}           User home or a project directory
--project-dir PATH               Required when --scope project
--overwrite                     Replace same-named installed skill folders
--dry-run                       Print operations without changing files
```

User destinations:

- Codex: `~/.agents/skills/`
- Claude Code: `~/.claude/skills/`

Project destinations:

- Codex: `<project>/.agents/skills/`
- Claude Code: `<project>/.claude/skills/`

The installer copies from canonical `skills/`. It does not delete unrelated folders. Without `--overwrite`, an existing same-named target is skipped to avoid silently replacing user changes.

## Claude upload ZIPs

Use `dist/claude-uploads/<skill-name>.zip`. Each ZIP includes exactly one skill folder at its root. Upload through your Claude app's custom Skills interface, then enable the skill and test a realistic prompt.

## Troubleshooting

- If a skill does not appear, check the expected folder, restart/reopen the agent if needed, and confirm your host supports custom skills.
- Review the `description` field first if automatic invocation is inconsistent.
- Use explicit invocation where the host supports it.
- A skill is not a tool permission. Enable only the shell, browser, connectors, or file access required by your environment.
