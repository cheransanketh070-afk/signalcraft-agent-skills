---
name: repo-rescue
description: Diagnose a failing repository, build, test, dependency install, or deployment; isolate the cause and make the smallest verified fix.
---


# Repo Rescue

A calm, evidence-led debugging workflow for codebases that fail to install, test, build, or deploy.

## Operating principles
- Reproduce before changing code whenever possible.
- Follow the error to its earliest actionable cause; later errors may be cascading symptoms.
- Prefer a small, reviewable patch over a rewrite or a broad dependency upgrade.
- Preserve user work. Never reset, clean, force-push, delete data, or overwrite uncommitted changes without explicit approval.

## Workflow
1. **Establish the boundary.** Inspect the repository structure, README, runtime version, package manifests, lockfiles, CI configuration, recent diff, and exact command that failed.
2. **Capture the failure.** Re-run the narrowest safe reproduction. Record command, exit code, relevant log lines, OS/runtime details, and whether the failure is deterministic. Do not claim a test ran if it was not run.
3. **Form a ranked hypothesis list.** Tie each hypothesis to observed evidence and a low-cost discriminating check. Check version mismatch, missing files, path/case assumptions, environment variables, network/registry failure, permissions, and stale caches where relevant.
4. **Inspect before editing.** Read the implicated code and nearby tests. Search callers and configuration. Identify the behavior that must remain unchanged.
5. **Patch minimally.** Avoid changing unrelated formatting or upgrading major versions as a first response. Do not hardcode credentials, disable TLS, weaken security, or skip tests just to get a green build.
6. **Verify in layers.** Run the smallest relevant test, then the broader test suite or build if practical. For deployment issues, distinguish local verification from remote deployment verification.
7. **Review the diff.** Look for accidental files, secrets, debug output, changed defaults, compatibility regressions, and missing tests. Never stage or commit unless requested.
8. **Report accurately.** Explain root cause, patch, commands actually run, results, remaining risks, and the next diagnostic if unresolved.

## Required response
- **Diagnosis:** confirmed cause or best current hypothesis.
- **Change:** file and behavior changed.
- **Verification:** exact commands and observed outcomes.
- **Residual risk:** what is still untested or environment-specific.
- **Rollback:** how to revert the patch safely.

## Stop conditions
Stop and ask before destructive data migrations, production writes, credential rotation, force pushes, or changes that can incur material spend. If the evidence does not establish a cause, do not invent certainty; return the next two useful checks.

See [triage-checklist.md](references/triage-checklist.md).

