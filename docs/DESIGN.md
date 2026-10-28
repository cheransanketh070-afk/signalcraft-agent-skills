# Design principles

SignalCraft is built around the point where general-purpose AI often becomes unreliable: transitioning from a plausible answer to a verifiable action.

## 1. Evidence before confidence

Important claims should be linked to evidence; assumptions should be labeled; uncertainty should be actionable.

## 2. Reversible before irreversible

Prefer previews, diffs, dry runs, narrow patches, and staged rollout. Require explicit approval for high-impact external actions.

## 3. Specific workflow over persona

A skill defines triggers, inputs, steps, outputs, and stop conditions. “Act like a genius expert” is not an implementation plan.

## 4. Progressive disclosure

Keep the top-level `SKILL.md` focused. Put detailed checklists and templates into separate files so they can be loaded only when needed.

## 5. One source of truth

Edit `skills/`; regenerate `.agents/skills/`, `.claude/skills/`, and ZIP uploads with the helper scripts. Validation checks mirrors against canonical files.

## 6. Honest measurement

Do not claim a skill improved accuracy, conversion, or productivity until comparable evaluation evidence exists. The repository ships validation checks for packaging and metadata, not model-performance benchmarks.
