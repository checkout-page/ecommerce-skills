#!/usr/bin/env python3
"""De-biased willingness-to-pay calculator (two-survey method).

Usage:
  wtp_calc.py --open open.csv --closed closed.csv [--cost 20] [--audience 10000]
              [--max-multiple 5]

open.csv   : one column `wtp`  — answers to "How much would you pay, at most?"
closed.csv : columns `price,answer` — answers to "Would you buy it for <price>?"
             answer = yes/no, y/n, true/false, or 1/0.

Method: open answers overstate; the closed survey is unbiased but coarse.
Shift every open answer by (mean_closed - mean_open), then read demand and
profit off the corrected answers at each price step.
"""
import argparse, csv, statistics, sys


def read_open(path):
    with open(path, newline="") as f:
        return [float(r["wtp"]) for r in csv.DictReader(f) if r.get("wtp", "").strip()]


def read_closed(path):
    yes = {"yes", "y", "true", "1"}
    no = {"no", "n", "false", "0"}
    rows = []
    with open(path, newline="") as f:
        for i, r in enumerate(csv.DictReader(f), start=2):
            a = (r.get("answer") or "").strip().lower()
            if a in yes:
                rows.append((float(r["price"]), 1))
            elif a in no:
                rows.append((float(r["price"]), 0))
            else:
                sys.exit(f"closed.csv line {i}: unrecognised answer {a!r} (use yes/no); fix the row rather than guess")
    if not rows:
        sys.exit("closed.csv has no rows")
    return rows


def clean_open(values, max_multiple):
    """Drop non-positive answers and anything above max_multiple x the median."""
    positive = [v for v in values if v > 0]
    if not positive:
        sys.exit("open.csv has no positive answers after cleaning; nothing to estimate")
    med = statistics.median(positive)
    kept = [v for v in positive if v <= max_multiple * med]
    return kept, len(values) - len(kept)


def closed_shares(rows):
    by_price = {}
    for p, a in rows:
        by_price.setdefault(p, []).append(a)
    return sorted((p, sum(v) / len(v), len(v)) for p, v in by_price.items())


def validate_ladder(shares):
    prices = [p for p, _, _ in shares]
    if len(prices) < 4:
        sys.exit(f"closed.csv has only {len(prices)} distinct price(s); the method needs a ladder of several equally spaced prices (7 recommended)")
    steps = [b - a for a, b in zip(prices, prices[1:])]
    if max(steps) - min(steps) > 0.01 * max(steps):
        sys.exit(f"price ladder steps are uneven ({', '.join(f'{s:g}' for s in steps)}); the method needs equal spacing — fix the ladder or rerun the survey")


def mean_from_shares(shares):
    """Mean WTP = area under the yes-share curve (trapezoid rule).
    Assumes everyone would accept a price of 0 and nobody accepts one step
    above the highest price asked."""
    step = shares[1][0] - shares[0][0] if len(shares) > 1 else shares[0][0]
    pts = [(0.0, 1.0)] + [(p, s) for p, s, _ in shares] + [(shares[-1][0] + step, 0.0)]
    return sum((s0 + s1) / 2 * (p1 - p0) for (p0, s0), (p1, s1) in zip(pts, pts[1:]))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--open", required=True)
    ap.add_argument("--closed", required=True)
    ap.add_argument("--cost", type=float, default=0.0, help="unit cost (default 0)")
    ap.add_argument("--audience", type=float, default=1000.0, help="reachable buyers (default 1000)")
    ap.add_argument("--max-multiple", type=float, default=5.0, help="outlier cutoff as multiple of median (default 5)")
    a = ap.parse_args()

    raw_open = read_open(a.open)
    open_vals, dropped = clean_open(raw_open, a.max_multiple)
    shares = closed_shares(read_closed(a.closed))
    validate_ladder(shares)

    mean_open = statistics.mean(open_vals)
    mean_closed = mean_from_shares(shares)
    shift = mean_closed - mean_open
    corrected = [v + shift for v in open_vals]

    print(f"Open survey: {len(raw_open)} answers, {dropped} dropped (<=0 or >{a.max_multiple:g}x median)")
    print(f"Closed survey: {sum(n for _, _, n in shares)} answers across {len(shares)} prices")
    for p, share, n in shares:
        flag = "" if n >= 30 else "  <-- fewer than 30 answers"
        print(f"  {p:>10.2f}  yes {share:6.1%}  n={n}{flag}")
    print(f"\nmean_open   = {mean_open:.2f}")
    print(f"mean_closed = {mean_closed:.2f}")
    print(f"correction  = mean_closed - mean_open = {shift:+.2f}  (applied to every open answer)")
    print(f"corrected mean WTP = {statistics.mean(corrected):.2f}\n")

    print(f"{'price':>10} {'share willing':>14} {'buyers':>10} {'profit':>12}")
    results = []
    for p, _, _ in shares:
        share = sum(1 for v in corrected if v >= p) / len(corrected)
        buyers = share * a.audience
        profit = (p - a.cost) * buyers
        print(f"{p:>10.2f} {share:>14.1%} {buyers:>10.0f} {profit:>12.0f}")
        results.append((p, profit))
    underpowered = [p for p, _, n in shares if n < 30]
    if len(open_vals) < 30 * len(shares):
        underpowered.append("open survey")
    best_p, best_profit = max(results, key=lambda r: r[1])
    if underpowered:
        print(f"\nUNDERPOWERED: fewer than 30 answers at {', '.join(str(u) for u in underpowered)}. The table above is indicative only; collect more answers before acting on a price.")
        return 2
    if best_profit <= 0:
        print(f"\nNo price on the ladder is profitable at cost {a.cost:g}: not launching (profit 0) beats every option. Revisit the cost or the ladder.")
        return 1
    ties = [p for p, pr in results if p != best_p and pr >= 0.9 * best_profit]
    print(f"\nProfit-maximizing price: {best_p:.2f}  (profit {best_profit:.0f} at cost {a.cost:g}, audience {a.audience:g})")
    if ties:
        print(f"Near-ties (within 10% of the best profit): {', '.join(f'{p:.2f}' for p in ties)} — treat as tied; decide by strategy or a live A/B test.")
    print("Override for strategy: a premium brand may pick a higher price; a reach-first launch a lower one.")


if __name__ == "__main__":
    sys.exit(main())
