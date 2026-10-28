---
name: release-readiness
description: Run a risk-based pre-release review for an app, website, script, or library and produce a test-backed go/no-go recommendation.
---


# Release Readiness

A pragmatic release gate for shipping changes with fewer avoidable regressions.

## Workflow
1. **Set release context.** Identify release scope, users affected, critical user journeys, supported platforms, data touched, rollback constraints, and release window.
2. **Inspect the change set.** Review diff, dependency changes, config migrations, API/schema changes, permissions, assets, documentation, and deployment manifests.
3. **Select risk-based tests.** Cover core happy paths, important edge cases, input validation, access control, backward compatibility, mobile/accessibility if relevant, failure recovery, and the most likely regression. Prefer testing the risk rather than chasing a blanket percentage.
4. **Check operability.** Verify health checks, logs/metrics, timeouts, resource limits, retries, rate limits, secrets configuration, backup/restore needs, and alert ownership where applicable.
5. **Prepare recovery.** Name the rollback or roll-forward path, database compatibility considerations, who can execute it, and what signal triggers rollback. If rollback is impossible, plan a safer staged rollout.
6. **Check user-facing truth.** Confirm release notes, feature claims, screenshots, pricing/limits, known issues, privacy statements, and migration instructions match actual behavior.
7. **Run the gate.** Execute checks that are available. Separate automated results, manual checks, and checks not run. Capture exact commands or links to CI where possible.
8. **Recommend go/no-go.** Make blockers and accepted risks explicit. Never say “production-ready” as a substitute for evidence.

## Go/no-go rule
- **NO-GO:** confirmed security/data-loss risk, broken critical journey, failed required test, unsafe migration, exposed secret, or no viable recovery for a high-impact change.
- **CONDITIONAL GO:** non-critical issue has a named owner, mitigation, deadline, and explicit acceptance.
- **GO:** high-risk checks passed, recovery is understood, and remaining uncertainty is acceptable for this release.

## Output format
1. Decision: GO / CONDITIONAL GO / NO-GO
2. Tested: exact checks and observed results
3. Blockers and severity
4. Accepted risks with owner and follow-up
5. Rollback triggers and steps
6. User-facing release notes

Use [release-checklist.md](assets/release-checklist.md) as the quick pass.

