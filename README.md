# Ecommerce Skills for AI Agents

A collection of AI agent skills for ecommerce pricing, discounts, checkout, and product pages. Built for store owners, founders, and marketers who want their AI agent to give advice that comes from research instead of guesswork. Works with Claude Code, OpenAI Codex, Cursor, and any agent that supports the [Agent Skills spec](https://agentskills.io).

Built by [Checkout Page](https://checkoutpage.com), checkout pages for digital products, event tickets, and subscriptions.

**Found a rule that is wrong or out of date?** [Open an issue](https://github.com/checkout-page/ecommerce-skills/issues) with the DOI.

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge for specific tasks. When you add these to your project, your agent recognizes when you are working on a price, a discount, or a product page and applies the rule that fits.

Most rules here come from a peer-reviewed study. The agent tells you what to do, the condition it applies under, and the paper behind it.

## Example

Ask: "We sell a $90 speaker and want to take $30 off. How do we show it?"

| | Answer |
|---|---|
| Without the skill | "$30 off" with a strikethrough price |
| With `discounts` | ~~$90.00~~ **$60.00**, "was 50% higher". $30 is 33% of the full price but 50% of the sale price, and people react to the bigger number. |

## Available Skills

### By goal

Start here if you have a number you want to move. Each skill returns a ranked list of changes.

| Skill | Ask it to… |
|---|---|
| [increase-conversion](skills/increase-conversion/) | Rank what would get more visitors to buy |
| [increase-aov](skills/increase-aov/) | Rank what would raise spend per order |
| [increase-repeat-purchases](skills/increase-repeat-purchases/) | Rank what would bring customers back for a second order |
| [raise-prices](skills/raise-prices/) | Rank what has to change for a higher price to hold |

### By task

| Skill | Ask it to… |
|---|---|
| [pricing](skills/pricing/) | Choose a price: rounded or .99, flat rates, add-ons, where to show it |
| [discounts](skills/discounts/) | Word and size a discount or coupon: $ or %, "was X% higher", when a discount is too deep |
| [promotions](skills/promotions/) | Design a promotion that isn't a price cut: gifts, bundles, pre-orders, deadlines |
| [price-research](skills/price-research/) | Find the most profitable price with a customer survey (includes a calculator) |
| [product-page](skills/product-page/) | Audit a product page: social proof, sold-out options, quantity buttons, price placement |
| [checkout-ux](skills/checkout-ux/) | Audit cart and checkout: guest checkout, fields, wallets, totals, coupon fields, errors |
| [product-copy](skills/product-copy/) | Write or rewrite product descriptions |
| [product-visuals](skills/product-visuals/) | Brief product photos and video |
| [store-audit](skills/store-audit/) | Review store-wide choices: channels, layout, design style, trust signals |
| [post-purchase](skills/post-purchase/) | Set up shipping, returns, loyalty, and cart-abandonment emails |
| [reviews](skills/reviews/) | Get more reviews and respond to them |
| [referrals](skills/referrals/) | Design a referral program: rewards and share messages |

### By product type

| Skill | Ask it to… |
|---|---|
| [digital-product-pricing](skills/digital-product-pricing/) | Price and launch ebooks, courses, templates, and downloads |
| [subscription-pricing](skills/subscription-pricing/) | Structure plans, tiers, upgrade paths, and member perks |
| [event-pricing](skills/event-pricing/) | Price and promote tickets, classes, workshops, and bookings |

## Installation

### Option 1: CLI Install (Recommended)

Use [npx skills](https://github.com/vercel-labs/skills) to install the skills:

```bash
# Install all skills
npx skills add checkout-page/ecommerce-skills

# Install specific skills
npx skills add checkout-page/ecommerce-skills --skill pricing discounts

# List available skills
npx skills add checkout-page/ecommerce-skills --list
```

### Option 2: Claude Code Plugin

```
/plugin marketplace add checkout-page/ecommerce-skills
/plugin install ecommerce-skills@ecommerce-skills
```

Skills show up as `/ecommerce-skills:pricing`, `/ecommerce-skills:discounts`, and so on.

### Option 3: Clone and Copy

Clone the repo and copy or symlink the skill folders you want into `.claude/skills/` (per project) or `~/.claude/skills/` (per user).

```bash
mkdir -p ~/.claude/skills && ln -s "$(pwd)/skills/"* ~/.claude/skills/
```

## Usage

Once installed, ask your agent for help:

```
"Should this price end in .99 or .00?"
→ Uses the pricing skill

"We want to run a sale next week. How deep should the discount be?"
→ Uses the discounts skill

"Audit my product page and rank what would lift conversion"
→ Uses the increase-conversion and product-page skills
```

## The evidence

Each skill has two files: `SKILL.md` tells the agent what to do, and `reference.md` lists the rule, the measured effect, and the citation.

- Of 132 rules, 101 cite a paper by DOI. Every DOI is checked against Crossref.
- 6 point to a rule in another skill that has the citation.
- 25 have no primary paper. They are marked † in the skill and "practitioner tip" in the reference file, so you know which to trust less.

Effect sizes are what one study measured, in that study's context. They tell you the direction and the rough size, not what you will get. Test in your own store.

## License

MIT. See [LICENSE](LICENSE).
