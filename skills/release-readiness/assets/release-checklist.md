# Release checklist

## Correctness
- [ ] Critical user journeys tested
- [ ] Regression and boundary tests run
- [ ] Platform/runtime compatibility checked
- [ ] Failure states and empty states reviewed

## Security and data
- [ ] No secrets or sensitive user data in diff, logs, or generated artifacts
- [ ] Authorization and input validation reviewed
- [ ] Dependency and configuration changes reviewed
- [ ] Data migration/back-up/restore plan verified if relevant

## Operations
- [ ] Health checks and useful logs/metrics exist
- [ ] Timeouts, retries, rate limits, and resource ceilings are sensible
- [ ] Rollback or safe roll-forward steps documented
- [ ] Release owner and rollback trigger named

## Communication
- [ ] Release notes match shipped behavior
- [ ] User-visible pricing, limits, screenshots, and docs are accurate
- [ ] Known issues and support path documented

## Gate record
- Decision: [GO / CONDITIONAL GO / NO-GO]
- Evidence: [checks actually run]
- Accepted risks: [owner + due date]
