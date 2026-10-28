<p align="center">
  <img src="assets/logo.png" width="156" alt="SignalCraft logo" />
</p>

<h1 align="center">SignalCraft — Open Agent Skills</h1>

<p align="center"><strong>From messy input to verified output.</strong><br />A practical, portable skill set for research, coding, safety, decisions, content, and shipping.</p>

<p align="center">
  <a href="https://github.com/cheransanketh070-afk/signalcraft-agent-skills/actions/workflows/validate.yml"><img alt="Validate skills" src="https://github.com/cheransanketh070-afk/signalcraft-agent-skills/actions/workflows/validate.yml/badge.svg" /></a>
  <img alt="13 skills" src="https://img.shields.io/badge/skills-13-14b8a6" />
  <img alt="ChatGPT + Claude" src="https://img.shields.io/badge/agents-ChatGPT%20%2B%20Claude-2563eb" />
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-f59e0b.svg" /></a>
  <img alt="No runtime dependencies" src="https://img.shields.io/badge/runtime%20dependencies-none-64748b" />
</p>

<p align="center">
  <img src="assets/social-preview.png" width="100%" alt="SignalCraft: practical workflows for research, code, safety, and shipping" />
</p>

## Why SignalCraft?

Most prompt collections give you clever wording. SignalCraft gives an agent a **repeatable workflow**: what to inspect, which evidence to gather, how to handle uncertainty, what not to do, and how to verify the result.

The skills are written for real work in the AI era—where current facts can change, repositories fail, generated claims need proof, automation can trigger real side effects, and trust matters as much as speed.

- **Portable:** based on the open `SKILL.md` pattern; skills are plain Markdown plus optional reference files.
- **Two ecosystems:** includes canonical skills, a Codex-discoverable `.agents/skills/` mirror, a Claude Code `.claude/skills/` mirror, and ZIP bundles for Claude's upload flow.
- **Verification-first:** asks agents to separate facts from assumptions, report tests actually run, and expose limitations.
- **Security-minded:** least privilege, secret hygiene, prompt-injection awareness, human approval for consequential actions, and safe failure handling.
- **Dependency-light:** the skills themselves need no extra packages, API keys, or paid service.

> **Design philosophy:** the agent should be useful without pretending it knows more than the evidence supports.

## The 13 skills

| Skill | What it helps with | Typical trigger |
|---|---|---|
| **Evidence-First Research** | Current, sourced research with confidence and unknowns | “Compare the latest options and cite current evidence.” |
| **Repo Rescue** | Debugging installs, CI, builds, tests, and deployments | “This workflow fails—find the earliest real cause.” |
| **Secure Change Review** | Practical code/config/AI workflow security reviews | “Review this diff for realistic attack paths.” |
| **Agent Eval Design** | Test sets, scoring rubrics, adversarial cases, regression gates | “Design an eval suite for my AI feature.” |
| **Release Readiness** | Risk-based go/no-go checks and rollback plans | “Tell me what must pass before release.” |
| **Launch Narrative** | Honest positioning, landing copy, launch assets, measurement | “Help launch this project without fake traction.” |
| **Content Repurposer** | Platform-native derivatives without losing the source truth | “Turn this transcript into several distinct formats.” |
| **Customer Discovery** | Non-leading interviews and ethical audience research | “Validate whether this problem is worth solving.” |
| **Automation Blueprint** | Reliable workflows with retries, idempotency, logs, and approvals | “Design a resilient local-first automation.” |
| **Decision Brief** | Clear options, trade-offs, assumptions, and reversal signals | “Help me choose between these options.” |
| **Data Story** | Validated metrics, transparent formulas, charts, caveats | “Turn this dataset into a defensible dashboard story.” |
| **Career Evidence** | Truthful, role-specific resumes, CVs, and interview evidence | “Tailor my CV but do not invent anything.” |
| **Incident First Response** | Safe first steps for security, privacy, or service incidents | “Help structure the first hour of an incident.” |

Each skill has a focused `SKILL.md`; extra templates or references load only when useful.

## Quick start

### Option A — use the repo with Codex or Claude Code

Clone the repository and open it with your coding agent. The repo includes platform-native copies:

```bash
git clone https://github.com/cheransanketh070-afk/signalcraft-agent-skills.git
cd signalcraft-agent-skills
```

- **Codex / compatible OpenAI agent workflows:** skills are in `.agents/skills/`.
- **Claude Code:** skills are in `.claude/skills/`.

If you want them available across your personal projects, use the installer below instead.

### Option B — install for your user account

Requires Python 3.9+; no third-party packages are needed.

```bash
python scripts/install_skills.py --target both --scope user
```

Install just one ecosystem:

```bash
python scripts/install_skills.py --target codex --scope user
python scripts/install_skills.py --target claude --scope user
```

For a project-local install:

```bash
python scripts/install_skills.py --target both --scope project --project-dir .
```

The installer **does not overwrite existing skills by default**. Add `--overwrite` only when you intend to replace same-named installed folders. Run `--dry-run` to preview destinations.

### Option C — upload an individual skill to Claude

Open `dist/claude-uploads/` and choose the skill ZIP that matches your task. Upload it through Claude's custom Skills interface (the exact menu label can vary by product version, commonly **Customize → Skills** or **Settings → Features**). A ZIP contains the named skill folder at its root, with `SKILL.md` inside it.

For ChatGPT desktop surfaces that support imported/custom skills, use the Skills interface when available. Availability and installation methods vary by plan, product surface, and workspace settings; see the official docs in [Compatibility and platform notes](docs/COMPATIBILITY.md).

## Example prompts

Use these as realistic activation tests—not as magic phrases that guarantee perfect results.

```text
Research current self-hosted analytics tools for a small team. Use official sources where possible,
separate confirmed facts from assumptions, and show unknowns.
```

```text
This CI workflow fails after dependency installation. Inspect the repo first, identify the first
actionable error, make the smallest safe fix, and report only checks actually run.
```

```text
Review this feature diff for authorization gaps, secret leakage, prompt injection, and dangerous
side effects. Rank findings by severity and provide a regression test for each confirmed issue.
```

```text
Create a small evaluation set for my AI workflow. Include ambiguous inputs, prompt injection,
unsupported claims, tool failures, and a scoring rubric defined before results are reviewed.
```

```text
Turn this project brief into a launch plan. I have no users or revenue yet; do not imply otherwise.
Show a demo-first story and a measurable, low-cost experiment.
```

## How the repository is organized

```text
.
├── .agents/skills/          # Codex discovery mirror
├── .claude/skills/          # Claude Code discovery mirror
├── skills/                  # Canonical source of truth
├── scripts/                 # Install, sync, validate, and package helpers
├── tests/                   # Dependency-free validation tests
├── docs/                    # Installation, compatibility, design, test prompts
├── assets/                  # Brand assets and social preview
└── dist/claude-uploads/     # One ZIP per skill for Claude upload
```

Edit the canonical version in `skills/`, then synchronize and validate:

```bash
python scripts/sync_platform_dirs.py
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

## Quality and safety rules

Every skill should:

1. Define when it applies and what good output looks like.
2. Separate observable evidence from inference, estimate, or opinion.
3. Never fabricate citations, results, credentials, users, benchmarks, or metrics.
4. Treat user-provided documents and retrieved content as untrusted data, not higher-priority instructions.
5. Avoid destructive actions and require explicit approval for consequential side effects.
6. State which checks actually ran and what remains uncertain.
7. Minimize personal data and keep secrets out of prompts, logs, templates, and source control.

Skills are instructions and reference material—not a security sandbox and not a substitute for human review. Review a skill before enabling it, especially when an agent has shell, browser, file, or external-action tools.

## Compatibility and limitations

SignalCraft follows the shared Agent Skills structure (`SKILL.md` with YAML frontmatter and optional resources). That makes its files portable, but **the host application controls discovery, invocation, tools, permissions, and upload support**. No skill can provide live web access or run tests unless the active agent/runtime has the relevant tools.

See [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) for current installation notes, and consult the official platform docs before relying on plan-specific behavior.

## Publishing the repository

See [docs/REPO-LAUNCH.md](docs/REPO-LAUNCH.md) for the GitHub About description, recommended topics, social preview setup, and a ready-to-edit launch post.

## Contributing

Ideas for a new skill are welcome when they solve a repeatable task and add a concrete workflow—not just a persona or a longer prompt. Read [CONTRIBUTING.md](CONTRIBUTING.md), use the test prompts, and run the validator before submitting a pull request.

## Roadmap

The next useful extensions are measurable activation tests per skill, additional localized templates, and optional benchmark fixtures. New skills should earn their place by covering a distinct job without bloating the core pack.

## Author

Created and maintained by **Cheran Sanketh**.

- Repository: [`cheransanketh070-afk/signalcraft-agent-skills`](https://github.com/cheransanketh070-afk/signalcraft-agent-skills)
- License: [MIT](LICENSE)
- Contributions: [CONTRIBUTING.md](CONTRIBUTING.md)

If this saves you time, consider starring the repository, opening an issue with a real workflow, or contributing a test case. A clear bug report helps the project more than a generic feature request.

## Acknowledgements

Built around the open Agent Skills pattern and informed by the public skill-authoring guidance from OpenAI and Anthropic. See [Compatibility and platform notes](docs/COMPATIBILITY.md) for source documentation.
