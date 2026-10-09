# Evidence: checkout-ux

Peer-reviewed findings behind the `checkout-ux` procedure. Effects are as reported in the studies, in the context they were measured. Practitioner cases (Spool, Baymard, Nielsen) have no DOI and are marked † in the skill.

## Guest continue; do not put a login wall in front of payment

**Rule.** Checkout must be completable without creating an account. Offer guest continue; invite an account after payment. A "returning customer? log in" link is optional, not a gate.
**Effect.** At one large retailer, replacing Register with Continue (and a line that no account was required) raised the number of customers purchasing 45%, about $300 million of additional annual revenue in that case. Not a peer-reviewed paper.
**Why.** People who already filled a cart were being asked to join a site. They wanted to pay.
**Source.** No primary citation on file; treat as a practitioner tip. Spool, J. M. The $300 million button. Originally written for Wroblewski, *Web Form Design* (2008).

**Related, different question.** Asking visitors to register at the *beginning of browsing* (not at the pay form) raised registration and long-run purchases and did not significantly hurt short-run sales on a crafts marketplace. That is not evidence for blocking checkout.
**Source.** Huang, N., Mojumder, P., Sun, T., Lv, J., & Golden, J. M. (2021). Not registered? Please sign up first: A randomized field experiment on the ex ante registration request. *Information Systems Research*. https://doi.org/10.1287/isre.2021.0999

## Format hints on restricted fields

**Rule.** Where a field has a required format (date, postcode, phone), show the format on the field.
**Effect.** Format specifications reduced errors and helped respondents complete restricted fields.
**Why.** People otherwise guess the pattern and fail validation after the fact.
**Source.** Bargas-Avila, J. A., Orsini, S., Piosczyk, H., Urwyler, D., & Opwis, K. (2011). Enhancing online forms: Use format specifications for fields with format restrictions to help respondents. *Interacting with Computers*. https://doi.org/10.1016/j.intcom.2010.08.001

## Required-field marking

**Rule.** Mark required fields more strongly than a small asterisk. A color cue outperformed asterisks in one experiment; pair any color cue with text so color is not the only signal.
**Effect.** Colored required-field backgrounds led to fewer errors, faster fill-in, and higher satisfaction than asterisks (24 professional users on one complex form).
**Why.** Asterisks are easy to miss; a field-level cue is seen while typing.
**Source.** Pauwels, S. L., Hübscher, C., Leuthold, S., Bargas-Avila, J. A., & Opwis, K. (2009). Error prevention in online forms: Use color instead of asterisks to mark required-fields. *Interacting with Computers*. https://doi.org/10.1016/j.intcom.2009.05.007

## Do not show errors while the person is still completing the form

**Rule.** Wait until they leave the field or submit. Instant in-flow errors were ignored.
**Effect.** Two studies (n = 77 and 90): presenting erroneous fields after the whole form was completed performed best; immediate feedback recommended by ISO performed worst. Users often kept filling as if nothing had happened.
**Why.** People are in "completion mode" and not ready to revise until the form is done.
**Source.** Bargas-Avila, J. A., Oberholzer, G., Schmutz, P., de Vito, M., & Opwis, K. (2007). Usable error message presentation in the World Wide Web: Do not show errors right away. *Interacting with Computers*. https://doi.org/10.1016/j.intcom.2007.01.003

## Put the error next to the field, not only at the top of the form

**Rule.** After submit, show the message beside the bad input (right of the field was the most satisfying).
**Effect.** In an online study (n = 303), locations next to the field beat messages at the top or bottom of the form on efficiency, effectiveness, and satisfaction.
**Why.** A top-of-form dump forces a search; a message on the field is the error.
**Source.** Seckler, M., Tuch, A. N., Opwis, K., & Bargas-Avila, J. A. (2012). User-friendly locations of error messages in web forms: Put them on the right side of the erroneous input field. *Interacting with Computers*. https://doi.org/10.1016/j.intcom.2012.03.002

## Field count and one-page vs multi-step

**Rule.** Ask only for what you need to ship and take payment. Collapse optional fields. Page count is secondary and mixed.
**Effect.** No peer-reviewed checkout experiment on file that isolates "one page vs three steps" or a per-field conversion penalty. Large-site checkout reviews (Baymard) report that typical checkouts ask for more fields than needed and that one-page is not automatically better.
**Why.** Each extra question is work; a wall of fields on one page and a long funnel are both work.
**Source.** No primary citation on file; treat as a practitioner tip.

## Do not drip shipping, tax, or fees until the last click

**Rule.** Show item, shipping, tax, and a running total before the pay button. A single, clearly labeled shipping line is fine; stacking many last-second surcharges is not.
**Effect.** Across six studies, when optional surcharges were dripped rather than shown up front, people more often picked the lower base price that became the higher total, then stuck with it even after seeing the total, and were less satisfied. In a grocery field experiment, posting tax-inclusive prices reduced demand by about 8% relative to adding tax at the register — which is why hiding tax looks attractive, and why a last-second tax line still feels like a jump. Online, a reasonable partitioned shipping charge can raise purchase intentions; adding multiple surcharges reversed that (inverted-U).
**Why.** People underweight later fees, then feel stuck once they have invested in the flow. Clarity of the structure can help; surprise does not.
**Source.** Santana, S., Dallas, S. K., & Morwitz, V. G. (2020). Consumer reactions to drip pricing. *Marketing Science*. https://doi.org/10.1287/mksc.2019.1207 — Chetty, R., Looney, A., & Kroft, K. (2009). Salience and taxation: Theory and evidence. *American Economic Review*. https://doi.org/10.1257/aer.99.4.1145 — Xia, L., & Monroe, K. B. (2004). Price partitioning on the Internet. *Journal of Interactive Marketing*. https://doi.org/10.1002/dir.20017 — related: Morwitz, V. G., Greenleaf, E. A., & Johnson, E. J. (1998). Divide and prosper: Consumers' reactions to partitioned prices. *Journal of Marketing Research*. https://doi.org/10.1177/002224379803500404

## Hide the coupon field until it is asked for

**Rule.** Do not greet every checkout with a promo-code box. Use "Have a code?" or auto-apply known codes.
**Effect.** In a lab checkout, prompting for a promotion code had strong negative effects on price fairness, satisfaction, and purchase completion among people who did not have a code, and positive fairness/satisfaction effects among people who did.
**Why.** The prompt tells people without a code that others are paying less, which feels unfair and sends them looking for a code (or leaving).
**Source.** Oliver, R. L., & Shor, M. (2003). Digital redemption of coupons: Satisfying and dissatisfying effects of promotion codes. *Journal of Product & Brand Management*. https://doi.org/10.1108/10610420310469805

## Express wallets

**Rule.** Offer Apple Pay, Google Pay, Shop Pay, or Link above the form, especially on mobile, as a way to skip address and card fields.
**Effect.** No peer-reviewed checkout conversion experiment on file for these wallets. Vendor and practitioner reports exist; they are not cited as measured findings here.
**Why.** The mechanism is fewer fields and less typing, which is the same work-reduction as steps 1–2.
**Source.** No primary citation on file; treat as a practitioner tip.

## One recognized seal can help; a badge wall does not

**Rule.** For an unknown store, one third-party assurance seal near pay can raise conversion. More than two lost effectiveness. Specific guarantee copy and an item–shipping–tax breakdown do the rest. Decorative lock icons are not a finding.
**Effect.** In a randomized field experiment (9,098 sessions on one retailer's site), the presence of an assurance seal increased the likelihood of purchase conversion (no percentage reported in the article record). In a later field dataset across 493 retailers, seals helped more for small retailers and new shoppers, and displaying more than two seals reduced the effect.
**Why.** A known certifier substitutes for seller reputation when the shopper has none. Extra badges look like decoration.
**Source.** Özpolat, K., Gao, G., Jank, W., & Viswanathan, S. (2013). The value of third-party assurance seals in online retailing: An empirical investigation. *Information Systems Research*. https://doi.org/10.1287/isre.2013.0489 — Özpolat, K., & Jank, W. (2015). Getting the most out of third party trust seals: An empirical analysis. *Decision Support Systems*. https://doi.org/10.1016/j.dss.2015.02.016 — cost breakdown: see `store-audit` (Mohan, Buell & John 2020), https://doi.org/10.1287/mksc.2019.1200

## Mobile layout, returning-customer login, payment-failure copy

**Rule.** Numeric keyboards on card/postcode/phone; tappable wallet buttons above the fold; never hide the form behind login for returners; on card decline, inventory clash, or 3-D Secure, keep the entered data and say what to do next.
**Effect.** No primary checkout trial on file for these three. They follow from the field-count and guest-continue findings plus standard error-message practice.
**Source.** No primary citation on file; treat as a practitioner tip. Nielsen error-message guidelines are the usual practitioner reference for recovery copy.
