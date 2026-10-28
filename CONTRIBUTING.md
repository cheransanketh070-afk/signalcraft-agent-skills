# Contributing to SignalCraft

Thank you for helping improve the skill pack. Contributions should improve a repeatable workflow and make its quality easier to inspect.

## What makes a good skill?

- One clear job with explicit trigger conditions.
- A practical sequence with input assumptions, expected outputs, and stop conditions.
- Useful examples or templates where they reduce ambiguity.
- Honest treatment of uncertainty, privacy, security, and irreversible actions.
- No claims that an agent can access tools or services unless those capabilities are provided by its host.

## Before opening a pull request

1. Edit the canonical skill in `skills/<skill-name>/`.
2. Keep `name` kebab-case and the same as the folder name.
3. Keep `description` concise (200 characters or fewer for compatibility with Claude's custom-skill requirements).
4. Add or update relative resources when they help; do not add secrets, proprietary data, or personal information.
5. Add activation and non-activation examples in `docs/test-prompts.md` when the trigger behavior changes.
6. Run:

   ```bash
   python scripts/sync_platform_dirs.py
   python scripts/validate_skills.py
   python -m unittest discover -s tests -v
   ```

7. Explain what changed, why it helps, and how you tested it. Do not state that model quality improved unless you ran a comparable evaluation.

## Security

Do not contribute instructions that encourage unauthorized access, credential theft, stealth, destructive actions, or bypassing safeguards. Report suspected vulnerabilities privately using `SECURITY.md`.

## Pull request style

Prefer focused changes. Please do not reformat every skill while fixing one issue. Keep examples synthetic and avoid screenshots or logs containing tokens, email addresses, private paths, or real customer data.
