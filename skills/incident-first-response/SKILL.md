---
name: incident-first-response
description: Structure the first response to a suspected security, privacy, or service incident with safe containment, evidence preservation, clear communication, and recovery.
---


# Incident First Response

Reduce harm and preserve options during the first response. Follow the organization's incident plan and involve the designated security, legal, privacy, or operations lead.

## First-response workflow
1. **Confirm and classify.** Record detection time, affected system, observed symptoms, scope known so far, and potential user/data impact. Treat severity as provisional until evidence improves.
2. **Protect people and critical services.** Stop ongoing harm using the least disruptive effective containment action. For a compromised account, use approved session revocation and credential rotation. For an exposed service, isolate the affected component if safe. Do not improvise destructive cleanup.
3. **Preserve evidence.** Save relevant logs, timestamps, alerts, hashes, configuration state, and a timeline in access-controlled storage. Keep originals where feasible. Avoid rebooting, wiping, or overwriting systems before evidence requirements are understood, unless immediate safety requires it.
4. **Limit access and disclosure.** Share facts only with the incident team and authorized stakeholders. Do not paste secrets, personal data, or complete forensic artifacts into public chats or AI tools. Redact before seeking help.
5. **Establish a timeline.** Track what was observed, what action was taken, who approved it, when it occurred, and the result. Separate confirmed facts, hypotheses, and unknowns.
6. **Escalate based on impact.** Follow internal escalation. Consider professional incident response, cloud/provider support, legal/privacy counsel, and appropriate authorities when required. Do not guess at regulatory notification deadlines; verify jurisdiction and obtain qualified advice.
7. **Communicate carefully.** Use a short holding statement with confirmed facts, impact known so far, actions underway, and next update time. Avoid speculation, blame, and unsupported “no data was accessed” claims.
8. **Recover deliberately.** Restore only from trusted state, patch the root cause, rotate affected credentials, validate integrity, and monitor for recurrence. Confirm the recovery method is safe before running it.
9. **Learn after stabilization.** Perform a blameless review covering root and contributing causes, detection gaps, control failures, action owners, and dated follow-ups.

## Initial incident log
| Time (with timezone) | Observation / action | Source | Owner | Confidence / result |
|---|---|---|---|---|

## Guardrails
- Never run destructive “cleanup” scripts without a reviewed plan and appropriate authorization.
- Do not make public attribution or criminal claims from incomplete indicators.
- Do not promise that data was unaffected without evidence.
- For imminent threats to physical safety, prioritize local emergency procedures.

See [incident-checklist.md](references/incident-checklist.md).

