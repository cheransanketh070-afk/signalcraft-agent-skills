---
name: agent-eval-design
description: Design a lightweight evaluation set for an AI feature or agent, including success criteria, adversarial cases, scoring rubrics, and regression checks.
---


# Agent Evaluation Design

Turn “the model seems good” into a small, repeatable test suite that measures whether an AI workflow actually helps users.

## Workflow
1. **Define the job.** Name the user, task, expected output, costly failures, supported inputs, and out-of-scope cases. Separate product requirements from stylistic preferences.
2. **Choose observable success criteria.** Prefer measurable outcomes: factual support, correct tool selection, schema validity, task completion, latency, cost, refusal when appropriate, and recoverability. Define pass/fail thresholds before looking at results.
3. **Build a representative set.** Include common cases, boundary cases, missing/ambiguous input, multilingual or format variation where relevant, and realistic difficult cases. Start with 15–30 examples if feasible; use a smaller seed set when resources are tight and label it as a pilot.
4. **Add safety and robustness cases.** Include prompt injection in quoted/retrieved text, conflicting instructions, sensitive-data requests, permission boundaries, malformed tool output, timeouts, duplicate events, and requests for unsupported facts. Test the failure mode, not just a benign paraphrase.
5. **Create a scoring rubric.** Specify exact evidence required for each score. Example: 0 = incorrect/unsafe, 1 = partially useful but missing a critical requirement, 2 = correct and complete. Use binary checks for mechanical requirements and human review for nuanced quality.
6. **Separate evaluation dimensions.** Do not collapse correctness, style, safety, tool use, latency, and cost into one opaque score. Track per-case pass rate and severity-weighted failure rate.
7. **Run a baseline.** Save model/version, prompt/skill version, tool configuration, date, dataset identifier, and raw outputs where privacy policy permits. Redact personal data. Do not claim improvement without a comparable baseline.
8. **Analyze failure clusters.** Sort failures by pattern and user impact. Prioritize fixes by severity × frequency × reach, not by which example is easiest to patch.
9. **Make it repeatable.** Add a compact regression set to CI or a manual release gate. Version the dataset and rubric. Never alter expected answers merely to make a failing system pass; record justified changes.
10. **Report honest limits.** Small samples are directional, not proof of broad reliability. Identify judge-model bias, label disagreement, stochasticity, and distribution shift.

## Deliverables
- Task definition and non-goals
- Dataset schema and 10–30 starter cases
- Scoring rubric with examples
- Baseline results by dimension
- Top failure clusters and proposed fixes
- Release gate and next evaluation date

## Minimal case schema
`case_id`, `input`, `context`, `expected_behavior`, `must_not_do`, `checks`, `severity`, `notes`.

## Example trigger
“Create an eval plan for an AI support bot that summarizes bug reports and proposes fixes. Include prompt injection, uncertainty, unsupported claims, and measurable release gates.”

