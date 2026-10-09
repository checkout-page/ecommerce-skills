# Ecommerce optimization skills

Nineteen agent skills for pricing, promotions, and conversion in online stores: four by goal, twelve by task, three by what you sell. The rules come from peer-reviewed studies, carry their condition and effect size, and cite the paper by DOI (every DOI is verified against Crossref). Not everything is sourced: of 132 rule entries across the shipped skills, 24 have no primary paper on file. Those are marked † in the skill and "practitioner tip" in its reference file, so you can weigh them accordingly.

Skills follow the [Agent Skills](https://agentskills.io) layout (`skills/<name>/SKILL.md`), so they work in Claude Code and any other runtime that reads that format.

## Skills

### By goal

Start here if you have a metric you want up. Each returns a backlog ranked by measured effect, pointing to the detailed skill for each item.

| Skill | Ask it to… |
|---|---|
| `increase-conversion` | Rank what would get more visitors to buy on a page or store |
| `increase-aov` | Rank what would raise spend per order |
| `increase-repeat-purchases` | Rank what would bring customers back for a second order |
| `raise-prices` | Rank what has to change on the product and page for a higher price to hold |

### By task

| Skill | Ask it to… |
|---|---|
| `pricing` | Choose the digits and structure of a price: rounded vs .99 vs precise, flat rates, add-ons, where and how to display the price |
| `discounts` | Word and size a markdown or coupon: $ vs %, "was X% higher", endings, the 40% ceiling |
| `promotions` | Design a promotion that isn't just a price cut: gifts, bundles, pre-orders, special days, time limits |
| `price-research` | Find the profit-maximizing price with a de-biased willingness-to-pay survey (includes a calculator script) |
| `product-page` | Audit a product page: social proof, sold-out options, quantity CTAs, choice architecture, price placement |
| `checkout-ux` | Audit cart, checkout, and the payment step: guest checkout, fields, wallets, totals, coupon fields, errors |
| `product-copy` | Write or rewrite product descriptions and benefit messaging |
| `product-visuals` | Brief product photography and video: format, gaze, hands, shine, spacing, props |
| `store-audit` | Site-wide decisions: channels, recommendation labels, layout direction, design style, trust signals |
| `post-purchase` | Shipping, returns, refunds, loyalty, and cart-abandonment email timing |
| `reviews` | Get more and better reviews; respond to reviews and public complaints |
| `referrals` | Design a referral program: framing, rewards, share messages |

### By product type

These are deltas on the core pricing, promotions, discounts, and product-page skills: typed examples and the few rules that actually change.

| Skill | Ask it to… |
|---|---|
| `digital-product-pricing` | Price and launch ebooks, courses, templates, downloads, lead magnets |
| `subscription-pricing` | Structure plans, tiers, upgrade paths, per-seat and overage pricing, member perks |
| `event-pricing` | Price and promote tickets, classes, workshops, bookings |

## Example

Ask: "We sell a $90 speaker and want to take $30 off. How do we show it?"

| | Answer |
|---|---|
| Without the skill | "$30 off" with a strikethrough price |
| With `discounts` | ~~$90.00~~ **$60.00**, "was 50% higher". Under 100, a percentage is the bigger numeral, and $30 is 50% of the sale price but only 33% of the full price. |

The before and after for every skill is in [docs/tests](docs/tests).

## Install

Any agent that reads Agent Skills (Claude Code, Cursor, Codex, and others):

```
npx skills add checkout-page/ecommerce-skills
```

Claude Code, as a plugin (skills show up as `/ecommerce-skills:pricing`, `/ecommerce-skills:discounts`, and so on):

```
/plugin marketplace add checkout-page/ecommerce-skills
/plugin install ecommerce-skills@ecommerce-skills
```

Or clone the repo and copy or symlink the skill folders you want into `.claude/skills/` (per project) or `~/.claude/skills/` (per user). They then show up unprefixed, as `/pricing`.

```sh
mkdir -p ~/.claude/skills && ln -s "$(pwd)/skills/"* ~/.claude/skills/
```

## Layout

```
skills/<name>/
  SKILL.md       # when to use, inputs, procedure, output, common mistakes
  reference.md   # the evidence: rule, effect, mechanism, citation
  scripts/       # only where there is something to compute
docs/            # design notes and test logs
parked/          # skills kept out of the shipped catalog
```

## License

MIT. See [LICENSE](LICENSE).

## A note on the evidence

Effect sizes are reported as measured in the cited study, in that study's context. They tell you the direction and rough magnitude, not what you will get. Test in your own store before rolling anything out fully.

## Who made this

[Checkout Page](https://checkoutpage.com): checkout pages for digital products, event tickets, and subscriptions. Found a rule that is wrong or out of date? Open an issue with the DOI.
