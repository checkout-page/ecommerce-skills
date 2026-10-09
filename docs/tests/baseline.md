> Log of scenario runs *without* the skills, recorded at the time of each round (2026-08-27). Step numbers and figures refer to the skills as they were then; the skills have since been revised (see green.md and the codex review rounds).

# Baseline runs (RED) — no skill loaded

Model: sonnet, fresh context, one realistic user question per skill. Recorded 2026-08-27.
Purpose: see what an agent says by default, so each skill targets the actual gaps.

## pricing

Scenario: premium handmade leather bag ~$200; $199 / $200 / $197.50? Monogram add-on $12.35?

Baseline: rounded price ($195/$225), rounded add-on ($15). Reasoning generic ("confidence", "cost-plus spreadsheet").
Gaps: no rule for *when* just-below is right (promotions, price-led purchases); no 4-figure rule; no upgrade left-digit rule; no flat-rate/simple-component guidance; no display rules (price below product, red for men). Suggested "$225 over $200" with no basis.

## discounts

Scenario: $90 speaker, $30 off, plus a store-wide coupon; should we go to 60%?

Baseline: "$30 off" with strikethrough — **wrong**, price < 100 → percentage. Missed "was 50% higher" reframe (30/60). Store-wide % coupon ✓. 60% rejected ✓ but for margin/anchoring reasons, not the quality-signal finding and the 40% ceiling. Added "today only" urgency without the caveat that online time limits mainly drive awareness. No consistent-ending rule, no restriction-first phrasing.

## promotions

Scenario: fitness tracker pre-order, launch in 2 months, 15% off + "only 500 units" + FREE guide; we also sell a smart scale.

Baseline: dropped the unit cap ✓ (for a credibility reason, not the anger/switching finding). **Kept the discount** — for a 9-week launch a gift beats a discount. Dropped "FREE" but didn't switch to "for $0". Suggested a bundle with an extra % off instead of framing the tracker (the searched-for product) as the gift with the scale.

## price-research

Scenario: online course, 8,000-person newsletter, planned to survey "how much would you pay?" and average.

Baseline: rejected the average ✓, recommended Van Westendorp + Gabor-Granger. Did not know the de-biased direct-question method (open WTP question + randomised yes/no question, correction formula), sample-size rules (7 equal price steps, ≥30 per step, ~500 responses), outlier cleaning, or the profit calculation with a strategy override.

## product-copy

Scenario: detergent pods, 750g/30 pods, light blue, branded enzyme blend, dissolves in 3 min, six benefits.

Baseline: crammed all six benefits; led with "750g bag" and "30 pods" rather than "30 washes"; kept "light blue"; "3 minutes" not "180 seconds"; no science-based framing for a utilitarian product; ingredient brand mentioned but not featured. Headline fine.

## product-page

Scenario: $28 soy candle page — price above image, single Add to cart, "15,600 viewed this week", 2/8 colours sold out and hidden, 8×3×2 variant grid, candle alone on white, six benefits, "lab-formulated fragrance".

Baseline: partition the variant grid ✓; show sold-out greyed ✓ (for email-capture reasons, no 10–30% rule); "lab-formulated" wrong for this product ✓ (audience-fit reasoning, not the hedonic/science finding). **Told them to drop the view count** (should switch to purchase numbers at high counts, or show both if conversion ≥5%). No quantity CTAs (candles are multi-unit). Visual advice generic (lifestyle, scale) — no hand-touch, shine, spacing, right-side, complementary props. Price-above ranked last as a "layout oddity" — missed the 9% lower-perceived-price / 35% sales finding. No 3-benefit rule.

## product-visuals

Scenario: shot list for a premium chocolate truffle box.

Baseline: video yes but "secondary" (for a hedonic premium product video raised WTP 79% — should be primary); hands-only, no face; no gaze rule; hand lifting a truffle ✓ by accident; no right-side/graspable placement; explicitly **avoided reflections/shine** ("no harsh reflections") — the opposite of the finding; no slow-motion; no spacing rule; no complementary props rule; suggested dark backdrop with no basis.

## store-audit

Scenario: 4-person insect-repellent candle company — Instagram vs Google; horizontal carousel; "recommended by our algorithm"; mention small team?

Baseline: Google Search first ✓ (intent reasoning; no hedonic/utilitarian rule, no mention of comparison/review sites). Told them to **remove the algorithm label** as "fake sophistication" — for a utilitarian product an algorithm label is the better performer. Carousel: generic "carousels are weak" — no horizontal (quality focus) vs vertical (price focus) rule. Small team: yes ✓ (no high-tech exception, no employee-passion angle). Trust list generic — no cost transparency, no extraordinary warranty, no sustainability claim, no marketplace acquisition.

## post-purchase

Scenario: 30-min abandonment email; thank-you card with 10% code; customer-pays returns with 5-day inspection; 3-tier opt-in loyalty.

Baseline: **approved the 30-minute email** (should be 24–72 h; <1 h backfires vs no email). **Approved the promo on the thank-you card** (promo undermines the note's sincerity). Instant refund on ship-back ✓. Free returns "worth testing" (finding: expected standard, raises spend and variety). Loyalty: auto-enrol ✓, flat not tiered ✓ (reasoning about admin, not the 29.5% CLV finding); no variable-reward tip; no shipping-subscription or minimum-order guidance.

## reviews

Scenario: skincare; ask 1 day after delivery, 1–5 rating; remove a 1-star Guam-shipping review to protect 4.9; rude Instagram complaint.

Baseline: don't remove ✓ (legal reasoning; also mentioned too-perfect looks suspicious ✓ but no 4–4.5 range, no "irrelevant negatives help" finding). Ask at 10–14 days ✓ (close to 9–13). Suggested **score-gating** (route 1–3 to private) — not in the evidence and legally grey. No positive-framed open-ended feedback question (+131% spend). Public reply once + move to DM ✓; no humour-for-rude-complaints finding; no "reply to all reviews" finding.

## referrals

Scenario: "Earn $50 cash for every friend"; friend gets $50 off; share message combining "I bought this" and "you can earn too".

Baseline: lead with the friend's benefit ✓; move earning off the share message ✓ (but kept "I bought this" without the either/or rule). Store credit over cash ✓ (fraud reasoning; no non-monetary gift/upgrade recommendation). Economics check generic — no finding that high rewards attract unprofitable referrals (−48% profitability at €50 vs €20).

## Pattern across all 11

Baselines are sensible but generic: they get ~half the direction right on intuition, invert several findings outright (dollar-off under 100, drop the view count, avoid shine, remove the algorithm label, 30-minute abandonment email, promo on the thank-you note, discount for a far pre-order), and never carry effect sizes or citations. The skills need to (a) state the rule with its condition, (b) give the number, (c) flag the inversions explicitly as common mistakes.

# Round 2 — product-type pricing skills (2026-08-27)

## digital-product-pricing

Scenario: individual creator, LinkedIn course at $97, "FREE download" checklist, pre-orders 6 weeks out at 20% off, pay-what-you-want ebook.

Baseline: **kept the pre-order discount** (6 weeks out → a gift beats a discount); **recommended "first 50 spots" unit scarcity** (anger/switching finding says never); "FREE download" judged fine (should be "for $0"); PWYW → "set a floor" (evidence: PWYW reduces sales; use 3–4 fixed pick-your-price options); no view on $97 vs a rounded $100 for an unknown individual (source example: rounded to signal quality). Generic advice about proof/testimonials instead.

## subscription-pricing

Scenario: membership site — Basic $9.99, Pro $29.99, pay-per-video $2.49, extra seats $4.61 + $6 admin fee, opt-in 3-tier rewards; want more Basic→Pro upgrades.

Baseline: fold the $6 fee into the seat price ✓ (fairness reasoning, not the simplicity-bias finding; kept $4.61 — should be rounded, e.g. $5). Suggested a $17–19 mid-tier and gating rewards by plan — no evidence. **Missed the left-digit rule**: $9.99 → $29.99 crosses a threshold, which discourages upgrades; keep both tiers on the same left digit. Missed: flat rate priced above pay-per-use is the evidence-backed structure (pay-per-view as low-commitment entry only); auto-enrol single-tier rewards rather than opt-in tiers.

## service-pricing

Scenario: freelance designer, $85/h × ~40 h, quoting a procurement manager; $3,400 / $3,399 / $3,417.50 / hourly; show costs?

Baseline: flat over hourly ✓ (no mention that the flat fee can sit *above* the hourly equivalent — $6,000 vs $5,000 finding); rejected $3,399 ✓; **rejected precision outright** — for a negotiated B2B quote to an expert, a moderately precise number ($3,450) with a justification is the evidence-backed choice; **advised against showing costs** — cost transparency raised sales 22% and holds to 55% margin.

## event-pricing

Scenario: $149 pottery workshop; early-bird 25% off for 2 months; "Only 12 seats left"; sold-out dates hidden; "Recommended by our algorithm"; price above photo; instructor looking at camera.

Baseline: show sold-out dates ✓ (no 10–30% rule); price below the photo ✓ (for anchoring reasons, not the 9% finding). "Only 12 seats left" — objected only if fake; the finding is that unit caps anger people who miss out even when true → use a deadline. **Kept the early-bird discount** for a 2-month-out event (a gift beats a discount at that distance; hedonic events tolerate long windows). Told them to relabel the algorithm row as "You might also like" — for an experience, the human label ("others also booked", "instructor's pick") is the one that performs. **Kept the direct gaze** — for an experience, the model should look away.

# Round 3 — goal skills (2026-08-27)

## increase-aov

Scenario: coffee beans $16/250 g (most buy two), grinders, filters; single Add to cart; free shipping over $50; 10% first-order coupon; paid returns; "Buy 3 get a special bundle price".

Baseline: raise free-shipping threshold with a progress bar (+10–20%, invented number, no source); default the bundle in cart; cross-sell filters (generic "complete the kit"). Missed: quantity CTAs Buy 1 / 2 / 3 (sales +28% — the single most direct AOV finding); the bundle should be framed as a gift ("buy 2, get the third at no cost"), not "special bundle price" (returns −50%, sales +78% when the wanted product is the gift); store-wide % coupon mindset (+42% sales); paid free-shipping membership with a minimum (3× spend); **dismissed free returns as irrelevant to AOV** — the finding is higher spend per order and more variety; complementary products around the focal product; intuitive units ("~15 cups" not 250 g); token-fee upgrades. Effect sizes were all invented.

## increase-conversion

Scenario: $120 ceramic pour-over set, 6-person team, Instagram traffic; static photos on white, price above image, Add to cart, 8 benefits, "Only 40 left", "FREE shipping", one colour sold out and hidden, 4.9 from 30 reviews.

Baseline: video and lifestyle shots first ✓ (hedonic → video; no gaze/hand/shine/right-side rules, no 79% WTP figure); "Only 40 left" — objected only if fake (finding: unit caps anger those who miss out regardless; use a deadline); show sold-out colour ✓ (for email capture; no 10–30% rule); cut 8 benefits to 3 ✓ (no 10.4% figure). Missed: price below the image (+35% sales), quantity CTAs n/a, "FREE shipping" → "shipping for $0", say you're small (six-person, low-tech product → higher perceived quality), cost breakdown (+22%), extraordinary warranty (+34.8%), 4.9 is above the 4.0–4.5 range that sells best — leave irrelevant negatives in. All effect sizes invented ("30–50% relative lift").

## increase-repeat-purchases

Scenario: skincare, 12% repeat; "rate us 1–5" day after delivery; 15% code on packing slip; opt-in Silver/Gold/Platinum points; refund after inspection; abandoned-cart email at 45 min; no review replies.

Baseline: replenishment sequence (generic, no source); loyalty "default-visible" but **kept opt-in tiers** (finding: auto-enrol, single tier, +29.5% CLV over 5 years); reply to reviews ✓ (no +0.12 stars / +12% reviews finding); refund on scan ✓; rework the packing-slip code — kept a discount insert (finding: a handwritten thank-you note with no promotion attached; a promo cancels it). Missed: positive-framed open-ended feedback request (responders spent +131%); ask at 9–13 days, not day 1; **the 45-minute abandonment email wasn't mentioned at all** (under 1 h backfires; 24–72 h); variable rewards; free-shipping membership (3× spend); free returns raise spend and variety. Effect sizes invented ("potentially double").

# Round 4 — raise-prices (2026-08-27)

Scenario: natural deodorant $9.99 (75 g), competitors $12–14, "cheap-looking"; 3-person company; branded plant-based active; one photo on white; "75 g, aluminium-free, lab-tested formula"; travel size $4.61; subscribe & save $8.37/month.

Baseline: single jump to $14 ✓ (no rule on rounded vs just-below — $14 rounded is right for a quality signal, but no reasoning); lead with the branded ingredient ✓ (no +40% finding); more photos ✓ (generic — no hand-touching, shine, multiple copies for a single-function product); "reframe the value metric" to outcomes — missed the concrete unit rule (days/applications instead of 75 g); **told them to make "lab-tested" more specific** — for a utilitarian product science/effectiveness language is right, keep it; **kept $4.61 and $8.37** — fiddly components read as expensive; round them with the same ending; missed: say you're a 3-person company (low-tech → higher perceived quality), cost breakdown (+22%), extraordinary guarantee for an unknown brand (+34.8%), sustainability if real (+6.4%), price below the image, flat-rate subscription priced above pay-per-use rather than below it. No effect sizes at all.
