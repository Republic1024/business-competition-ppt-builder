# Visual Card System V2

Use this reference when creating or revising PPT pages after the data and charts are ready.

## Principles

- Make the chart or table the main object.
- Use cards to explain, prioritize, or group decisions.
- Keep each card short enough to read in three seconds.
- Use pale fills for hierarchy, not decoration.
- Use one accent color per group.

## Palette

- Meituan yellow: `#FFD100`
- Ink: `#111827`
- Muted gray: `#6B7280`
- Positive green: `#0B8F5A`
- Scenario blue: `#2563EB`
- Warning red: `#D94F4F`
- Pale yellow: `#FFF7CC`
- Pale green: `#E9F7EF`
- Pale blue: `#EEF4FF`
- Pale red: `#FFF1F1`
- Neutral gray fill: `#F3F4F6`

## Pattern A: Right-Side Explanation Card

Use for heatmap/story slides.

Layout:

- Place the card in the right-side whitespace.
- Add a 0.05-0.08 inch vertical accent bar.
- White card fill with subtle border.
- Sections:
  - Title: 5-8 Chinese characters or one short phrase.
  - `读图`: axis/metric explanation.
  - `结论`: highlighted pale yellow box with the strongest number.
  - `动作`: targeting or launch rule.

Example copy shape:

```text
反常识的早间机会

读图  横轴是小时桶；纵轴是城市层级。

结论  二线城市 × 早间 6-10 点是最强峰值，
      局部 τ +34.8pp，是大盘 2.4 倍。

动作  早间集中资源位和早餐券，避免全天平均铺量。
```

## Pattern B: Tiered Strategy Card Board

Use for final strategy pages.

Layout:

- Three horizontal bands or rows:
  - First tier: green.
  - Second tier: blue.
  - Third tier: red.
- Left rail names the tier and operating principle.
- Cards to the right contain:
  - Direction title.
  - Metric pill.
  - Basis line.
  - Action line.
  - Expected effect line.

Example card:

```text
饮品 -> 餐饮
τ +9.7pp
平衡性良好 · 20,524 跳转
饮品结算/完成页嵌入餐饮 Cross；建立组合券。
相对转化 +90%，估计最稳
```

## Pattern C: Colorful Overview Cards

Use for slide 3-style data or conclusion overview pages.

Layout:

- 4-6 cards in a grid.
- Use different pale fills to mark different meanings.
- Each card:
  - eyebrow label
  - large number / core phrase
  - one-line interpretation

Use this when the slide would otherwise become a dry table.

## Pattern D: Execution Logic Page

Use for slide 9-style decision or execution pages.

Good structures:

- left: decision rules or KPI cards
- right: SQL/pseudo-code panel
- bottom: rollout or validation note

Keep code/pseudo-code in a dark panel only if it is short and readable. Use surrounding cards to explain why the logic exists.

## Anti-Patterns

- Do not use long text paragraphs.
- Do not put cards inside cards.
- Do not use saturated full-card backgrounds for every card.
- Do not cover chart legends, labels, markers, or footnotes.
- Do not use a single color family for the whole deck.
