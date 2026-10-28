# Repository triage checklist

## Environment
- [ ] Exact failing command and exit code captured
- [ ] OS, runtime, package manager, and relevant versions identified
- [ ] Lockfile and manifest reviewed together
- [ ] Required environment variables documented without printing secrets

## Reproduction
- [ ] Failure reproduced with the narrowest safe command
- [ ] First actionable error separated from cascading errors
- [ ] Local versus CI/deployment differences compared

## Fix quality
- [ ] Smallest plausible patch selected
- [ ] Existing behavior and public interfaces preserved
- [ ] Regression test added or existing test identified
- [ ] Security was not weakened to bypass the symptom
- [ ] No unrelated generated files or secret values added

## Verification report
- [ ] Exact commands and result summarized
- [ ] Not-run checks explicitly listed
- [ ] Residual risk and rollback path recorded
