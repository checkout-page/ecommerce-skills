# Skill conventions

Applies to every skill in `skills/`. `skills/discounts/` is the exemplar — match its shape.

## Files

```
skills/<name>/
  SKILL.md       # the procedure; roughly 600–1100 words by wc -w (tables count)
  reference.md   # the evidence; one entry per finding
  scripts/       # only if there is something to compute
```

## SKILL.md

Frontmatter: `name` (lowercase, hyphens) and `description`. The description is third person, starts with "Use when", lists triggering situations and the phrases a user would say, and does NOT summarize the procedure. Under 500 characters.

Body sections, in this order:

1. `# Title` + one-paragraph overview: what job this does and the core principle.
2. `## When to use` / `## When not to use` — bullets.
3. `## Inputs` — what to collect from the user before deciding; say what to assume if missing.
4. `## Procedure` — numbered steps. Every rule is a conditional on something observable ("if the full price is 100 or more → amount off"), with the number the evidence gives. Where the product type matters, include the standard classification block below verbatim.
5. `## Output` — the exact shape of what to hand back (table or template).
6. `## Common mistakes` — the baseline inversions from `docs/tests/baseline.md`, phrased as "X — do Y instead".
7. `## Quick reference` — one table.
8. Final line: `Evidence and effect sizes: see [reference.md](reference.md).`

## Standard classification block

Use this text wherever a rule depends on product type:

> **Classify the product first.** *Hedonic* = bought for enjoyment, pleasure, or the experience (chocolate, fashion, decor, travel, spa, perfume). *Utilitarian* = bought to do a job, judged on function and value (detergent, appliances, insect repellent, tools, accounting software). If it's mixed, decide by what the buyer is optimizing for at the moment of purchase.

## reference.md

Title `# Evidence: <skill>`. One entry per finding:

```
## <Short rule as a heading>

**Rule.** One or two sentences, with the condition.
**Effect.** The number(s) from the study, with the context they were measured in.
**Why.** The mechanism in one or two sentences.
**Source.** Authors (Year). Title. *Journal*. https://doi.org/...
```

If a rule came to us without a primary citation, write `**Source.** No primary citation on file; treat as a practitioner tip.` and append ` †` to the rule where it appears in SKILL.md, with the footnote line `† No primary citation on file for this rule — a practitioner tip, not a measured finding.` above the closing evidence link. Cite the primary paper only — never a paywalled summary, newsletter, or secondary write-up.

## Language

Skill content is a published product: US English (color, optimize), plain words, no hedging, no marketing tone. Effect sizes are stated as reported ("sales were 22% higher"), not inflated ("up to 22%!").

## Goal routers and product-type overlays

Goal routers (`increase-conversion`, `increase-aov`, `increase-repeat-purchases`, `raise-prices`) are metric-first checklists. Keep When / When not / Inputs / Output. Procedure is a ranked list of levers with a one-line why and a `Depth: skill-name` handoff. Leave numbers, studies, and how-to in the task skills. `reference.md` is a short index of which task-skill references apply, plus any finding that lives only on the router.

Product-type overlays (`digital-product-pricing`, `subscription-pricing`, `event-pricing`) are deltas only. Typed When / When not, one short worked example, and the 2–5 rules that actually change versus `pricing` / `promotions` / `discounts` / `product-page`. Do not repeat the shared price-ending or framing catalog; link back with Depth.

Cart, checkout, and the payment step belong to `checkout-ux`, not `product-page` or the conversion router.
