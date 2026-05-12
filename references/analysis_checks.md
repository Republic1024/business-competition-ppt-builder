# Analysis Checks

## Numeric Consistency

When a notebook or script is the source of truth:

1. Run it if feasible.
2. Save exact output tables used by the deck.
3. Compare key slide values against those tables.
4. If porting logic, preserve grouping keys, filters, thresholds, bin labels, rounding, and ranking rules.

For each important slide, keep a table artifact:

- `category_base.csv`
- `directed_flow.csv`
- `causal_estimate.csv`
- `direction_score.csv`
- `scenario_or_hte_summary.csv`

## Cross Analysis Definitions

Common definitions:

- `source -> target`: user/session moves from source category to target category.
- `target CVR`: target orders divided by eligible transitions or target-population users. State which denominator is used.
- `raw tau`: treated target order rate minus control target order rate.
- `CEM/PSM tau`: adjusted difference after matching/stratification.
- `local tau`: tau within a segment or heatmap cell.
- `relative lift`: adjusted tau divided by target baseline conversion.

## Causal Guardrails

Use the target category population for treatment/control when estimating directional increment:

- Population: users who visited or were eligible for the target category.
- Treatment: population users exposed through `source -> target`.
- Control: population users not exposed through that source path.
- Outcome: target category order.

Avoid using all source users as controls unless the original analysis explicitly does so; that often inflates effects.

## Robustness Checks

Prefer at least one:

- Covariate balance table or SMD distribution.
- CEM vs IPW comparison.
- Weight sensitivity for composite score.
- Attribution strategy sensitivity.
- Minimum sample thresholds for HTE heatmap cells.

If balance is weak, keep the result but label it as less reliable.

## Visual QA Checklist

- No chart or text overlaps.
- Legends and axis labels are visible.
- Chinese text renders with a real CJK font.
- Long labels are abbreviated or moved outside the plot.
- PPT is 16:9.
- Image paths are embedded and not linked to missing files.
- Final deck opens in PowerPoint.
