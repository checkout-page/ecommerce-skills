> Log of scenario runs *with* the skills, recorded at the time of each round (2026-08-27). Step numbers refer to the skills as they were then; later revisions (e.g. `discounts` now has ten steps) are not back-ported into this log.

# Verification runs (GREEN) — skill loaded

Same scenarios as baseline.md, sonnet, fresh context, told to read the SKILL.md first.

## discounts — PASS

Chose percentage for the $90 item, reframed as "was 50% higher", kept .00 endings, store-wide coupon as %, condition-first wording, rejected 60% on the quality-signal finding, suggested a gift/bundle instead. All eight procedure steps applied.
Gaps reported: no coupon size guidance; silent on stacking. Fixed: step 6 now applies the depth check to the coupon and to the combined discount when stacking.

## product-page — PASS (one fix)

Price below image ranked first, sold-out shown (25% is in range), Buy 1/2/5, partitioned grid, hedonic visuals, three claims, no science wording. It judged "15,600 views" as fine — the skill said "views early" without a threshold. Fixed: step 1 now says switch to purchases once views hit the thousands. Added sub-grouping guidance for a single attribute with > 5 values.

## product-visuals — PASS (one tweak)

Video primary with slow-motion, gaze away, first-person hand, right-side placement, shine (explicitly contradicting the baseline's "no reflections"), spacing, props. Applied the multiples rule to truffles, which are not single-function; tightened the rule's wording.

## pricing — PASS

$200 rounded with the premium/hedonic reason, $15 add-on with matching ending, price below the image, red only for a mostly-male audience. Gap: no default when gender mix is unknown. Fixed: black.

## promotions — PASS

Dropped the discount for a 9-week launch in favor of a gift, tracker framed as the $0 item with the scale, "for $0" not "FREE", deadline instead of unit cap, optional invented occasion. Gap reported: combining a bundle gift with a second unrelated freebie — no evidence either way, left as is.

## product-copy — PASS (one fix)

Three claims, branded enzyme blend first, "30 washes" not 750 g, evocative color, utilitarian register, scent moved down. Kept "3 minutes" — the smaller-unit rule only gave the hours→minutes example. Fixed: rule now says "drop to the next unit down" with seconds/minutes/ounces examples.

## price-research — PASS (clarifications added)

Rejected the average, laid out the two-survey method with ladder, sample size, cleaning, correction, demand/profit curve. Generated synthetic data and ran `wtp_calc.py` as documented: ran cleanly, cleaning dropped the seeded zeros/outlier, demand curve monotonic, interior profit maximum. Gaps: trapezoid assumption only in the script docstring; meaning of `--cost` for digital goods and `--audience` vs list size; response-rate sizing; near-tie handling. All added to steps 4, 7, 8.

## store-audit — PASS (one note)

Classified insect-repellent candles as utilitarian → search over social, keep the algorithm label (the baseline removed it), carousel judged by quality-vs-price goal, say you're small, cost breakdown, marketplace listing. Gap: warranty rule for consumables — added a guarantee equivalent, marked untested.

## post-purchase — PASS (one note)

Rejected the 30-minute email (24–72 h), removed the promo from the thank-you card, free returns with instant refund on scan, auto-enrolled single-tier loyalty with a variable reward. Gap: which items need inspection — examples added.

## reviews — PASS

Ask later than 9–13 days for skincare, open-ended positive question first, no score-gating (the baseline recommended it), keep the Guam review and reply, stop protecting the 4.9, one public reply then DM, humor only for genuinely rude posts, reply to all reviews. Gaps reported (exact day offset for slow products, rudeness threshold) have no evidence to draw on; left as judgment calls.

## referrals — PASS

Friend's benefit as headline, one signal in the share message (both variants offered), in-kind over cash, reward capped against first-order margin with the €20→€50 finding, payout after return window. Gap: symmetric $50/$50 sizing — covered by the cap rule.

## Summary

11/11 pass on the same scenarios that produced the baseline inversions. Each gap the testers reported was either fixed in the skill or has no evidence behind it and was left as a judgment call.

# Round 2 — product-type pricing skills

## digital-product-pricing — PASS

$100 rounded for an unknown seller, "$0" not "FREE", gift instead of discount 6 weeks out, fixed price options instead of PWYW, dated deadline not a spot cap. Gap: no cutoff for a utilitarian pre-launch window — none in the evidence; added a line saying so.

## subscription-pricing — PASS

Removed .99 from the tiers, pay-per-view as entry only, $5 seat with no admin fee, auto-enrolled single-tier variable reward, no mid-tier. Worked example was overclaiming that $10→$30 satisfies the same-left-digit rule; reworded to "no just-below on the lower tier; same left digit is the stronger version".

## service-pricing — PASS

Flat fee above the hourly equivalent, moderately precise $3,450 for a procurement buyer (baseline had rejected precision outright), cost breakdown shown as structure not meter (baseline had said hide costs). Gap: no combined rule for where the precise number sits relative to the hourly total — judgment call, no evidence either way.

## event-pricing — PASS

$150 rounded, gift instead of early-bird discount, deadline instead of "12 seats left" (for the anger finding, not honesty), sold-out dates shown at 10–30%, human recommendation label, price below image, instructor looking away. All six baseline inversions corrected.

## Round 2 summary

4/4 pass. 15 skills total. All 34 DOIs in the new reference files resolve; one entry (science-based messaging for utilitarian products) remains a practitioner tip, as in `product-copy`.

# Round 3 — goal skills

## increase-aov — PASS

Quantity CTAs first (+28%), bundle reframed as a gift with the wanted product as the gift, store-wide % coupon kept, free returns as a spend lever (baseline had dismissed it), membership with minimum, $50 threshold correctly flagged as unevidenced, indirect levers last. Every number labelled as the study's. Gap: stacking — added "measured one at a time, don't add them up" to all three goal skills.

## increase-repeat-purchases — PASS

Open-ended positive question at 3–4 weeks for skincare, 24–72 h abandonment email (baseline had ignored the 45-minute send), handwritten note with no code, reply to reviews, refund on scan, auto-enrolled single-rule variable loyalty flagged as a multi-year effect. Gap: whether to surface unmentioned levers — added an instruction to include applicable ones and list the rest as considered.

## increase-conversion — PASS

Free fixes first (price below image, deadline not unit cap, three claims, "$0", show the sold-out colour), then the shoot (video, hand, shine, gaze away), then trust (small team, cost breakdown, warranty) and the 4.0–4.5 rating point. Explicitly refused to forecast the user's rate. Gap: no rule for trading a large-effect costly fix against several free small ones — it sequenced by cost, which is the sensible default; left as is.

## Round 3 summary

3/3 pass. 18 skills total. No new DOIs introduced (all reused from verified entries); 3 practitioner-tip entries carried over in `increase-conversion`.

# Round 4 — raise-prices

## raise-prices — PASS

$14 rounded in one move (99-ending only for a promo), $5 and $12 add-ons, "60 applications" instead of 75 g, branded active in the headline, "lab-tested" kept for a utilitarian product (the baseline had softened it), three claims, hand/shine/multiples, price below image, "made by three people", cost breakdown, guarantee, video correctly skipped. Gap: replace vs add photos — the evidence is per-shot, not gallery size; left as a judgment call.

19 skills total. 4/4 rounds, 19/19 GREEN passes.

# Codex cross-model review (2026-08-28 → 2026-09-03)

Four rounds of `codex exec review` over the whole repo, each finding verified against the files before acting; fixes applied between rounds.

- Round 1: 20 reported → 14 confirmed and fixed (licence, † marking regime, unverified 49% figure withdrawn, wrong journal, selective review solicitation, bona fide reference price, science-claim substantiation, tiers overclaim, RTL/handedness, red-price scrutiny condition, three wtp_calc.py fixes, sample-threshold consistency).
- Round 2: 15 → 11 confirmed and fixed (missed † markers, AOV direct/adjacent split, compound attributions, invented facts in worked examples, "$0" vs "free" consistency, first-review reference wording, placebo citation, exact paper titles, underpowered-survey guard, test-log pinning).
- Round 3: 23 → 19 confirmed and fixed (population/outcome transfers flagged, one-move † mark, referral disclosure, truthful seat inventory carve-out, digital-gloss representativeness, Duke & Amir metadata, warranty title, mkdir in install command).
- Round 4: 19 → 19 confirmed and fixed (manifest overclaims, ladder validation in wtp_calc.py, rounded-vs-utilitarian boundary, gift-direction error in the AOV example, second referral template disclosure, recurring-plan notice, outcome-class labels in goal skills, variable-reward/auto-enroll combination, 3× membership figure marked uncited, mixed-color DOI, systematic year corrections against Crossref).

Recurrent dropped items (judged not defects): wtp_calc.py dropping $0 answers (the published method does), trapezoid tail-step assumption, deliberate cross-skill duplication.
