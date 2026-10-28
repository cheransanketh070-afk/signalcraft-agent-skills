# Metric quality checklist

For every KPI, document:

- **Name and purpose:** What decision does it support?
- **Formula:** Exact numerator, denominator, and aggregation order.
- **Population:** Included/excluded rows, users, products, and periods.
- **Units and grain:** Seconds, dollars, percent, per user, per day, etc.
- **Source and lineage:** File/table, columns, transformations, joins, owner.
- **Missingness:** How nulls and unknowns are handled.
- **Edge cases:** Zero denominator, duplicate events, late arrivals, negative values.
- **Validation:** Independent reconciliation or known control total.
- **Refresh and version:** As-of date, timezone, code/workbook version.
- **Limitations:** Bias, sampling, uncertainty, and non-causal interpretation.

## Common traps
- Percentage change versus percentage-point change.
- Average of group averages instead of a correctly weighted aggregate.
- Denominators that change over time without disclosure.
- Duplicate joins multiplying facts.
- Treating “missing” as zero without justification.
- Comparing incomplete periods with complete ones.
- Presenting too many decimals or ranking tiny differences as meaningful.
