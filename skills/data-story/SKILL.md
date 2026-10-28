---
name: data-story
description: Analyze a dataset and turn it into a transparent, decision-focused story with validated metrics, reproducible formulas, suitable visuals, and caveats.
---


# Data Story

Start with data quality and definitions, not chart decoration. The goal is a defensible answer to a real question.

## Workflow
1. **Define the decision question.** Identify audience, unit of analysis, time period, outcome, comparison, and what action could follow. Confirm what each row represents.
2. **Inspect the data.** Review schema, row counts, units, date coverage, duplicates, missingness, outliers, category drift, and join keys. Preserve raw data and create a documented analysis copy.
3. **Define metrics.** Write formulas, numerator/denominator, inclusion/exclusion rules, aggregation level, time zone, units, and rounding. Distinguish counts, rates, averages, medians, percent change, and percentage-point change.
4. **Validate calculations.** Recompute key totals independently, reconcile to known source totals, check denominator-zero cases, and test edge records. Use reproducible code or exposed spreadsheet formulas where appropriate.
5. **Choose comparisons that are fair.** Compare like periods and populations. Note seasonality, sample size, selection bias, survivorship, missing records, and any change in collection method.
6. **Separate signal from cause.** Describe associations accurately. Do not claim causality from correlation without a suitable design. If using estimates or forecasts, state assumptions and uncertainty intervals where supportable.
7. **Choose visual encoding by task.** Lines for trends, bars for categorical comparison, scatterplots for relationships, distributions for spread, maps only when geography matters. Label units, time range, denominator, and source.
8. **Tell the story in layers.** Lead with the key finding, quantify the size, show the evidence, explain why it may matter, then list limitations and a recommended next check.
9. **Make the work auditable.** Save source identifier, cleaning rules, formulas, code or workbook cells, chart definitions, and analysis date. Avoid manual number edits in charts.
10. **Review for misleading framing.** Check axis truncation, hidden categories, inconsistent denominators, over-precision, tiny samples, cherry-picked windows, and unsupported causal language.

## Deliverables
- Data-quality summary
- Metric dictionary with formulas
- Key findings ranked by decision value
- Visual recommendations or charts
- Assumptions, caveats, and reproducibility notes
- One practical follow-up analysis

See [metric-quality.md](references/metric-quality.md).

