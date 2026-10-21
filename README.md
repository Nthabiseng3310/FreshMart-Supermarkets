# FreshMart-Supermarkets
This repository hosts the FreshMart suspermarkets analysis ///
# FreshMart: Why Is Our Basket Getting Smaller?

A business analysis project for the BrightLearn Data & AI Academy (Business Analysis module).
Author: [Your name] | Date: [Month 2026]

FreshMart is a fictional grocery chain with 42 stores in Gauteng, Western Cape and KwaZulu-Natal. Leadership noticed that more people were walking into the stores, but sales were not growing. The Head of Retail Operations had a hunch: "people are buying less per visit." My job was to check whether that is true, find where it is happening, work out why, and suggest what to do about it.

## The short answer

The hunch is right, but the reason is a bit different from what you might expect.

- Between the first half (Jan to Jun) and second half (Jul to Dec) of 2025, trips went **up 6.8%**, the average basket went **down 10.0%** (R290 to R261), and sample revenue went **down 3.9%**.
- People are not buying cheaper things. Rand per item actually went up slightly (+1.6%).
- Big shops (9 or more items) barely changed in value (R413 to R408), and small top-up trips did not change at all (R90). What changed is how many trips are top-ups: 38% in H1 and 46% in H2, reaching 50% by December.
- About **91%** of the fall in the average basket comes from this shift in the mix of trips, and only 9% from baskets themselves getting smaller.
- At the 12 stores where a discount competitor opened nearby, baskets dropped by about **R46 more** than at comparable stores over the same dates. All 12 stores dropped more than the control group.
- Weekend stockouts of Household Cleaning at 6 stores made baskets about R32 (12%) smaller on the affected days, but they touch less than 1% of trips, so this is real but minor.
- Even the 30 stores with no competitor saw top-ups grow (36% to 48%). I could not explain that with this data, and I say so in the report instead of guessing.

## What is in this repo

| File | What it is |
|---|---|
| `FreshMart_Basket_Analysis.ipynb` | The full analysis in Python, run from top to bottom with outputs and charts saved |
| `FreshMart_Report.pdf` | The written report (problem framing, hypotheses, data quality, findings, recommendations, monitoring) |
| `FreshMart_Deck.pdf` | The 10-slide presentation for the steering group |
| `Project_Plan.pdf` | My 3-week plan and Gantt chart, made in Canva |
| `FreshMart_Dataset.xlsx` | The data from the course (Transactions, Stores, Stockouts). [Add it only if your course allows sharing it] |

## How to run it

1. Clone the repo and put `FreshMart_Dataset.xlsx` in the same folder as the notebook.
2. Install what the notebook needs:
   ```
   pip install pandas matplotlib scipy openpyxl jupyter
   ```
3. Open the notebook and run all cells:
   ```
   jupyter notebook FreshMart_Basket_Analysis.ipynb
   ```

If your file has a different name or sits somewhere else, change the `FILE` variable at the top of the notebook.

## How I approached it

I kept the code simple on purpose so that someone who does not code much can still follow the steps.

1. **Frame the question.** "Buying less per visit" can mean fewer rand or fewer items, so I measured both. Revenue is trips times average basket, so trips up 6.8% and basket down 10% gives revenue down about 3.9%. That arithmetic told me where to look.
2. **Check the data.** I looked for missing values, duplicates, impossible numbers, broken store links and mismatched dates. The data turned out to be clean. The only blanks were meaningful ones: no customer ID means the shopper is not a loyalty member, and no competitor date means no competitor nearby. I kept those on purpose.
3. **Build new columns.** Month, half-year, weekend flag, rand per item, and a trip type (top-up for 8 items or fewer, big shop for 9 or more). I chose 8 as the cut-off because the basket-size chart has two humps and 8 sits in the gap between them.
4. **Look past the average.** I split trips into top-ups and big shops and separated the change in mix from the change in basket size. This is what showed that the average fell mainly because the mix moved.
5. **Test the competing explanations.** For competitors, I compared each affected store 60 days before and after its competitor opened, against stores that never had one over the same dates. For stockouts, I compared affected and unaffected weekend days within the same six stores. I also checked store format, province, weekday, payment method and loyalty status.

## Hypotheses: what held up and what did not

| Hypothesis | Result |
|---|---|
| A nearby discounter pulls away big shops | Supported. About -R46 per basket against control stores |
| Stockouts shrink baskets | Supported, but minor (under 1% of trips) |
| Shoppers are trading down to cheaper items | Rejected. Rand per item went up |
| Shopping is shifting to more top-up trips | Supported. This is the main mechanism (91% of the fall) |
| Store format or province explains it | Mostly rejected. Differences follow where competitors opened |
| Payment method or day of the week matters | Rejected. Everything falls by about the same amount |

## Recommendations

1. **Defend big shops at the 12 exposed stores** with a tested offer (basket-threshold rewards or price-matching on staples), run as a pilot with control stores before rolling out.
2. **Fix the weekend replenishment gap** for Household Cleaning at the 6 affected stores. It is cheap and the problem is clear.
3. **Set up a competitor early-warning watchlist and fix loyalty ID capture**, so FreshMart can react quickly to the next opening and answer the questions this data could not.

The report has the owners, effort, risks, success metrics and a monitoring dashboard for each.

## Limitations

- The data is a **sample** of transactions, so I compare patterns and do not claim FreshMart's real total turnover.
- It only covers 2025, so I compared the first half with the second half. I could not check the year-on-year footfall figure in the brief.
- Loyalty IDs almost never repeat (about 1.02 trips per ID), so I could not follow individual customers. I cannot say whether the same shoppers switched to top-ups or a different type of shopper is visiting. My conclusion rests on trip mix.
- The competitor stores were not chosen at random, so the comparison with control stores is observational.
- The stockout result rests on 119 store-days, and one affected store also had a competitor open.
- There is no cost or margin data, so the cost of any offer still has to be worked out with Finance. The R23 per basket recovery target and the R15 pilot threshold in the report are my own proposals, not forecasts.

## What I would do next

- Get price and competitor data for all stores to test why top-ups are rising even where no competitor opened.
- Fix loyalty ID capture so a proper customer-level analysis is possible.
- Run the pilot for 8 weeks and track top-up share and big-shop basket value weekly.

## Tools

Python (pandas, matplotlib, scipy) in Jupyter, a Claude-built slide deck and report, and Canva for the project plan. I used an AI assistant (Claude) to help build and write up parts of this work, and I went through the analysis and numbers myself so that I can explain and defend them. [Edit this line so it matches how you actually worked and what your course asks you to disclose.]

## Contact

[Your name] | [LinkedIn or email]
