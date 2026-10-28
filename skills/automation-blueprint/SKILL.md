---
name: automation-blueprint
description: Design a reliable, secure automation with explicit triggers, idempotency, bounded retries, observability, and human approval for risky actions.
---


# Automation Blueprint

Design the automation as a dependable service, not a happy-path script. Use the simplest architecture that meets the requirement.

## Workflow
1. **Define the outcome.** Identify trigger, inputs, output, frequency, owner, success measure, volume, latency needs, budget, and failure cost.
2. **Map the state flow.** Describe states and transitions from intake through validation, processing, approval, action, and completion. Define what happens when any step fails.
3. **Choose local-first or hosted deliberately.** Consider data sensitivity, network needs, operating cost, uptime, maintenance, and portability. Avoid unnecessary services and credentials.
4. **Design idempotency.** Retries must not duplicate a payment, post, email, file write, or external side effect. Use idempotency keys, deduplication records, deterministic output names, or an outbox pattern appropriate to the stack.
5. **Make retries bounded.** Use timeouts, exponential backoff with jitter, maximum attempts, and a dead-letter/manual-review path. Do not retry permanent errors or rate-limit responses without respecting provider instructions.
6. **Handle secrets and permissions.** Store tokens outside source code, use least privilege, rotate/revoke safely, and redact secrets from logs. Never ask the model to print a secret to “check” it.
7. **Add human gates.** Require explicit review before destructive writes, publishing externally, spending money, sending high-volume communications, changing access, or acting on ambiguous high-impact inputs.
8. **Validate inputs and outputs.** Apply schemas, size limits, MIME/content checks, output escaping, and destination allowlists as relevant. Treat model output and uploaded content as untrusted.
9. **Plan observability.** Emit structured logs, correlation/run IDs, durations, retries, failures, and counts. Avoid sensitive payload logging. Alert on user-impacting failures, not every transient event.
10. **Plan recovery.** Define replay behavior, checkpoints, backup/restore, manual recovery, and data retention. Test duplicate delivery, timeout, partial success, bad input, expired credentials, and service outage.
11. **Estimate costs.** Model expected and worst-case volume, API/compute spend, storage, and failure loops. Add quotas or circuit breakers.
12. **Launch gradually.** Start with dry-run mode or a small canary. Compare outputs to expected behavior, record operator approval, then widen scope.

## Deliverables
- Architecture in plain language or diagram
- State machine and failure table
- Data/secret boundaries
- Retry and idempotency strategy
- Approval policy
- Monitoring and recovery runbook
- Cost assumptions and scale limits

See [reliability-patterns.md](references/reliability-patterns.md).

