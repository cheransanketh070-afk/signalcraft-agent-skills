# Lightweight threat model

Answer briefly; unknowns are valid findings.

## Assets
- What data, credentials, accounts, money, or availability must be protected?
- What would be costly or irreversible if changed or exposed?

## Actors and trust boundaries
- Anonymous users, authenticated users, admins, service accounts, third-party APIs, dependencies, AI agents, local files, and retrieved content.
- Where does untrusted input cross into a trusted component?

## Abuse cases
- Read another user's data or act with another user's identity.
- Trigger a privileged tool or side effect through crafted content.
- Exfiltrate secrets through output, logs, URLs, telemetry, or generated files.
- Exhaust CPU, memory, quota, or financial spend.
- Persist malicious content into config, CI, or future prompts.
- Bypass approvals, rate limits, validation, or rollback.

## Controls to verify
- Least-privilege access and explicit authorization on every sensitive action.
- Validation at trust boundaries and contextual output encoding.
- Secrets outside source control and restricted logs.
- Timeouts, quotas, rate limits, idempotency, and bounded retries.
- Human approval for high-impact actions.
- Monitoring, audit trail, recovery and rollback.
