---
name: business-competition-ppt-builder
description: Build polished, data-driven business competition PowerPoint decks from raw data, notebooks, scripts, reports, or analysis outputs. Use when Codex is asked to make, remake, improve, or package a competition-style business analysis PPT; rerun code to generate charts/tables; preserve numeric consistency with notebooks; create causal/segmentation/storytelling slides; use a modern MiSans-style deck; or turn a messy analysis folder into a presentation-ready .pptx.
---

# Business Competition PPT Builder

## Version 2 Emphasis

Prefer the proven 15-slide competition deck shape when the user needs a concise final PPT: enough pages to tell the full analysis story, but short enough for judging and roadshow use.

Preserve and reuse these winning visual patterns:

- **Heatmap story pages**: put a compact explanation card in right-side whitespace with `读图 / 结论 / 动作`; keep it short and never cover the chart or legend.
- **Tiered strategy page**: use colored grouped cards for `重点投入 / 精准投放 / 审慎暂缓`; each card needs one metric, one basis, one action, and one expected effect.
- **Data overview pages**: use multi-color pale card backgrounds to separate data scope, category facts, caveats, and method checks.
- **Execution / summary pages**: use structured cards or code panels, not paragraphs.

## Core Rule

Treat the PPT as an evidence product, not a decoration task. Recompute needed tables and charts from the user's source data/code whenever possible, then build a clean deck around the verified numbers.

Do not reuse stale screenshots or old chart images unless the user explicitly asks. If a notebook or script is named as the source of truth, execute or port its logic so slide numbers match that source.

## Workflow

1. **Identify the source of truth**
   - Locate raw data, notebooks, scripts, reports, and existing PPTs.
   - Prefer named notebooks/scripts over inferred logic.
   - If a user says "numbers must match", run the source notebook/script or copy its exact computation path.
   - Record the command/environment used, e.g. `mamba activate <env> && python ...`.

2. **Rebuild evidence**
   - Write a new reproducible script in the working folder.
   - Generate fresh CSV tables and chart images into an output folder such as `deck_rebuild/tables/` and `deck_rebuild/charts/`.
   - Save intermediate tables for every chart used in slides.
   - Keep statistical labels honest: distinguish raw conversion, CEM/PSM/IPW estimates, HTE local tau, lift, and score.

3. **Create the PPT**
   - Use `python-pptx` unless the repository already has a better deck pipeline.
   - Use 16:9 layout.
   - Prefer MiSans for Chinese decks; if absent, use a close sans-serif fallback and document that.
   - Build native PPT text/shapes around chart images rather than flattening the whole slide into screenshots.
   - Use concise titles, KPI cards, and readable charts. Avoid long paragraphs.
   - Add restrained colorful card backgrounds where information is card-based; do not leave every card white if the slide needs hierarchy.

4. **Add story slides**
   - Convert analysis into a decision narrative:
     - problem / opportunity
     - evidence
     - mechanism
     - segment or scenario
     - action
     - risk or validation plan
   - For HTE/segmentation heatmaps, add small side annotations (`读图`, `结论`, `动作`) in whitespace. Never cover heatmaps, legends, axes, or existing insight strips.

5. **Validate**
   - Open or export slide previews when possible.
   - Check slide count, aspect ratio, image existence, readable Chinese text, and no overlap.
   - Spot-check key numbers against the source tables/notebook outputs.
   - Final response must link the PPT, generation script, and important tables.

## Business Analysis Patterns

Use these slide modules when they fit the data:

- **Executive Summary**: 3-5 quantified conclusions, each tied to a recommended action.
- **Data Scope**: records, users, orders, attribution coverage, date range, caveats.
- **Category Base**: users, penetration, order rate, contribution.
- **Cross Direction Flow**: source -> target transitions, target conversion, flow asymmetry.
- **Causal Increment**: raw tau vs CEM/PSM/IPW tau; include balance checks when available.
- **Direction Score**: rank-normalized weighted score, not just one metric.
- **Scenario Discovery**: period x path conversion, city/device/time/user activity slices.
- **HTE Story**: local effect heatmap with significant peaks/plateaus and action.
- **Tiered Strategy**: invest / targeted / pause based on increment, robustness, and reachability.
- **Execution Logic**: SQL or pseudo-SQL for user selection and experiment rollout.

For causal claims, phrase carefully:

- Use "去偏增量", "PSM/CEM 估计", or "局部 τ" rather than "必然导致".
- Mark weak balance or small samples as reliability caveats.
- If estimates conflict, include robustness comparison instead of hiding it.

## Visual System

Default to a quiet competition-deck style:

- Canvas: white or very light gray, 16:9.
- Font: MiSans / Microsoft YaHei / clean sans-serif.
- Primary color: Meituan yellow `#FFD100` for highlights, not as full-page saturation.
- Supporting colors: ink `#111827`, gray `#6B7280`, green `#0B8F5A`, blue `#2563EB`, red `#D94F4F`.
- Use flat cards with small radius or plain rectangles; avoid decorative gradients and stock imagery.
- Use pale but visibly different card fills for grouped concepts:
  - pale yellow `#FFF7CC` for key conclusion or Meituan-facing action
  - pale green `#E9F7EF` for invest / positive increment
  - pale blue `#EEF4FF` for targeting / HTE / scenario
  - pale red `#FFF1F1` for pause / negative increment
  - light gray `#F3F4F6` for neutral facts and caveats
- Use dense but organized information. Competition judges need scannability.
- Put chart titles in the slide, not only inside the image.
- Keep annotations short. A side card should usually contain only:
  - `读图`: how to read axes or metric
  - `结论`: one quantified insight
  - `动作`: one operating recommendation

## Reproducible Script Standards

Generated scripts should:

- Define paths at the top.
- Create output directories.
- Load raw data with explicit `usecols` and dtypes when large.
- Use structured APIs (`pandas`, `python-pptx`, `matplotlib`) instead of manual string hacks.
- Save every final chart and the table behind it.
- Print a short progress log.
- Be rerunnable without relying on hidden notebook state.

When porting notebook logic, preserve:

- category attribution rules
- target population definition
- treatment/control definition
- thresholds, bins, weights, and sorting
- rounded values shown in the notebook

## Useful Resources

- Use `references/deck_patterns.md` for reusable slide patterns and storyline decisions.
- Use `references/visual_card_system.md` for the v2 card layout patterns that worked well in the 15-page deck.
- Use `references/analysis_checks.md` for numeric consistency and causal-analysis checks.
- Use `scripts/pptx_sanity_check.py` to inspect a PPTX after generation.
- Use `scripts/export_pptx_slides.py` on Windows with PowerPoint installed to export slide previews for visual QA.

## Final Response

Keep the final answer short and operational:

- Link the generated `.pptx`.
- Link the generation script(s).
- Mention the verification performed.
- List any numbers that were explicitly calibrated to the source notebook/script.
