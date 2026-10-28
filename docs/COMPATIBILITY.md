# Compatibility and platform notes

SignalCraft uses the open Agent Skills pattern: a skill folder containing `SKILL.md`, YAML frontmatter with `name` and `description`, plus optional local resources. The format is portable; host behavior is not identical across products.

## ChatGPT and Codex

- Current OpenAI skill guidance describes a skill as a directory with `SKILL.md` and optional `scripts/`, `references/`, `assets/`, and `agents/openai.yaml`.
- Codex discovers repository skills from `.agents/skills/` and can also use personal skills from `$HOME/.agents/skills/`.
- In supported ChatGPT desktop / Codex surfaces, skills can be explicitly invoked (for example, with `@` or `$`) or selected automatically when relevant. Exact UI and availability can vary by plan, app version, and workspace configuration.
- This repository includes `.agents/skills/` for discovery when opened in a compatible environment. The canonical source remains `skills/`.

Official references:
- [Build skills — ChatGPT Learn](https://learn.chatgpt.com/docs/build-skills)
- [Skills & Plugins — ChatGPT Learn](https://learn.chatgpt.com/docs/skills-and-plugins)
- [Skills — OpenAI Developers](https://developers.openai.com/plugins/concepts/skills)

## Claude and Claude Code

- Claude custom skills use a directory with `SKILL.md`; the required frontmatter includes a name and description. The description is important for automatic invocation. For broad compatibility, the descriptions in this repository are at most 200 characters.
- Claude Code supports project-local skills in `.claude/skills/` and personal skills under `~/.claude/skills/`.
- Claude's web/app custom-skill import accepts a ZIP with the skill folder as the ZIP's root. The repository provides individual archives under `dist/claude-uploads/`.
- The exact import menu label and eligibility may vary as Anthropic changes its UI or plan features; follow the help article linked below.

Official references:
- [Agent Skills overview — Claude Platform](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [How to create custom skills — Claude Help Center](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

## What portability does not guarantee

- A skill cannot give an agent a browser, shell, filesystem, API, or external connector that its host has not made available.
- Automatic invocation is probabilistic; test trigger wording and explicit invocation for important workflows.
- A host may impose additional restrictions on dependencies, scripts, file access, or skill upload size.
- Do not assume a skill has been loaded just because it exists in a repository. Check the host's skill interface and run a realistic activation test.
- Review skills before enabling them. As with any agent instructions, skills can influence how an agent uses its available tools.
