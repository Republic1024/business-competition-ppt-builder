# Deck Patterns

## Recommended 15-Slide Order

1. Title: literal project name and concise thesis.
2. Executive conclusion: 3-5 quantified findings.
3. Data scope: records, users, time range, attribution coverage, caveats. Use colorful pale cards for this slide.
4. Base market: category penetration and order contribution.
5. Directional flow: top source -> target paths.
6. Causal increment: raw vs adjusted tau and reliability.
7. Scenario discovery: time/city/device/activity slices.
8. Robustness or scoring: SMD/IPW/sensitivity, preferably as chart + short cards.
9. Execution or decision logic: structured cards/code panel; this is often a strong judge-facing page.
10. HTE or scenario summary.
11. Strategy tier page.
12. HTE story A or B with the chart dominant.
13. HTE story with right-side explanation card.
14. HTE story with right-side explanation card.
15. Final tiered/combined action card page or compact rollout plan.

If the user's existing deck has different slide numbers after deletion, preserve their current order and apply these patterns to the equivalent pages.

## Strategy Tier Slide

Use one slide when the user gives many actions. Compress into cards:

- First tier: high increment, high business value, clear action.
- Second tier: targeted HTE segments with local peak effects.
- Third tier: zero/negative increment or weak robustness; recommend pause.

Each card should contain:

- Direction
- Key metric, e.g. `tau +14.6pp`
- One-line basis, e.g. "balance good" or "flow 20,524"
- One action sentence
- One expected effect sentence

Visual treatment:

- Left rail: tier label and operating principle.
- Cards: colored vertical accent bar, pale category fill, short metric pill.
- First tier: green accent and pale green fill.
- Second tier: blue accent and pale blue fill.
- Third tier: red accent and pale red fill.
- Avoid table borders. Cards should read as a decision board, not a spreadsheet.

## HTE Heatmap Annotation

Place side cards in whitespace, not over the heatmap:

- `读图`: identify x/y axes and what color means.
- `结论`: state the strongest local effect and sample/significance when available.
- `动作`: convert insight to targeting rule.

Keep each item under two short lines.

Recommended right-side card:

- Width around 15-20% of slide.
- White fill, subtle gray border, colored left accent.
- Title: one phrase, e.g. "反常识的早间机会".
- `读图`: one sentence about axes.
- `结论`: yellow highlight box with the main number.
- `动作`: one operational rule.

Do not add bullets on top of the chart image. Do not cover the heatmap, legend, axes, bottom insight strip, or significance markers.

## Colorful Card Overview Page

For data overview or method overview pages, use a grid of small cards with different pale fills:

- Yellow: headline conclusion.
- Blue: data scope or scenario.
- Green: positive evidence.
- Red: risk or pause.
- Gray: caveat or assumption.

Each card should have a short label, one large number or phrase, and one supporting line. This pattern is especially useful for slide 3-style overview pages.

## Competition Judge Biases

Judges usually reward:

- Reproducible data evidence over pretty but unsupported visuals.
- Clear incrementality reasoning.
- Actionability: who to target, when, where, and what to show.
- Explicit limitations and validation plans.

They usually penalize:

- Large text blocks.
- Unlabeled metrics.
- Old screenshots that cannot be traced to code.
- Overclaiming causal conclusions from correlation.
