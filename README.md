# Hashrate Hearth

An interactive page about who builds bitcoin's blocks. Two template builders, Foundry and the AntPool group, build most of them (58% over the 30 days to 20 Oct 2026), so they decide which payments get confirmed. The page works out how much home hashrate it takes to break that majority, and why that means real machines heating homes or running on solar, not desk trinkets.

Built by [jasonb](https://stacker.news/jasonb).

## What's live and what isn't

**Live, read from [mempool.space](https://mempool.space/docs/api/rest) every time the page loads:**

- Pool shares over the last 30 days, by coinbase tag
- Template-builder shares: the same tags grouped using [mainnet.observer's list of pools that relay AntPool's templates](https://mainnet.observer/charts/mining-pools-antpool-and-friends/)
- Network hashrate, BTC price, average fees and recent block times, and the hashprice worked out from them
- The latest months of the hashrate chart, with its peak and low labels

Every number that depends on these (the homes needed, the censored-payment wait, the heat and solar earnings) follows them. If Foundry and the AntPool group ever drop below half, the page switches to a three-builder majority (adding F2Pool) and its wording changes to match.

If mempool.space can't be reached, the page shows its built-in figures from 20 Oct 2026 and says "as of" that date instead of "live".

**Fixed, with their dates on the page:**

- Electricity rates: EIA, July 2026
- Hashrate by country: Hashrate Index, Q1 2026
- Bitcoin owners (~106M): Onramp, early 2026
- Used S19j Pro price (~$185): eBay asks, October 2026
- Solar size and output: EnergySage and NREL
- Machine specs: manufacturer pages

## Files

- `hashrate-hearth.html` is the source: the page's markup, styles and script without the `<html>`, `<head>` and `<body>` wrapper.
- `make-site.py` wraps it into a full document at `site/index.html`.
- `vercel.json` tells Vercel to run that script and serve `site/`.

## Run it locally

```bash
python3 make-site.py && python3 -m http.server 8000 --directory site
```

Then open http://localhost:8000.

## Deploy to Vercel

Import this repository at [vercel.com/new](https://vercel.com/new). The settings come from `vercel.json`, so there's nothing to change; Vercel builds and redeploys on every push.

Or from this folder with the Vercel CLI:

```bash
vercel --prod
```

## Upkeep

- If mainnet.observer adds or drops a pool from AntPool's group, update `FRIENDS` in `hashrate-hearth.html` (it's keyed by mempool.space pool slug).
- The built-in fallback figures are `NOW`, `DATA`, `TAG` and `TPL` near the top of the script.

The page is an educational model built on public data, not a recommendation to buy any hardware or asset. Our advice: be the one securing your own wealth.
