---
theme: maturity-and-metrics
type: dg-program-theme
frames:
  - "3458764611453561784" # Template: D&A Maturity Assessment map
  - "3458764611453525296" # DG Maturity Models (DMM, DCAM)
  - "3458764611455329213" # Data-Driven Index (DDI) template
  - "3458764611455329214" # DDI dashboard mockup + data literacy scoring
---
# Maturity and Metrics

## What the board teaches
Two instruments answer "where are we and is it working". The Data & Analytics Maturity Map is a self-assessment canvas of 7 dimensions and 25 sub-areas, where capability blocks are laid out along a progression from *Data informed* → *Data Driven* → *Data Led* and color-coded by status (done / in progress / to be done / not applicable / done-but-improvable). Its worked progressions are the most reusable part — e.g. reporting evolves from on-request reports through central BI and federated CoE to GenAI BI; DQ from custom checks through monitoring tools and criticality coverage to data contracts and observability; roles engagement from "natural chaotic DG with no driver" through data-people stewardship and business engagement to a federated DG model "dissolved in processes". The Data-Driven Index then turns maturity into a single weighted number: DD Index = Σ(weights × component) over 13 components and 26 example metrics with weights summing to 1.00 (worked example: 62.99), explicitly to be tailored to what a company can actually calculate and what is meaningful for its business. Reference industry models (CMMI's DMM, EDM Council's DCAM, plus comparisons) are catalogued separately for calibration.

## Key objects
- Maturity map dimensions: 1 Getting value from data; 2 Analytics services (reporting factory, self-serve, experiments, advanced analytics); 3 Analytics Governance (content management, customer development, knowing the data); 4 Data Platform Architecture (storage, ingestion, transformation, BI, ML/DS/AI); 5 Data Governance (discovery & cataloging, DQ system, security, roles engagement); 6 Data Team (people management, roles, structure, project management); 7 Culture (executive leadership, decision-making, data culture)
- Maturity stages: Data informed → Data Driven → Data Led; status legend (6 statuses); caveat that block order isn't always a level-up
- Reference models: DMM (CMMI Institute, link now 404), DCAM (EDM Council), model comparison cluster, other models
- Data-Driven Index formula: DD Index = Σ(weights × Component); 26-row grid (component / metric example / complexity / formula / value / weight / contribution)
- 13 DDI components with example weights: Data Literacy 0.15, Tools Adoption 0.15, Direct Business Value 0.13, Data Management 0.12, Data Accessibility 0.12, Organisational Model 0.09, Culture 0.06, Analytics Maturity 0.03, Innovation 0.03, Customer Insights 0.03, Data Security 0.03, Data Infrastructure 0.03, Leadership 0.03
- Worked example: total 62.99; weakest metrics NPS improvement (10%), cost reduction from data decisions (14%); strongest infrastructure uptime (99%), ad-hoc duration (95%)
- DDI dashboard mockup: index card 62.9 (+11.1 YoY); note that formula and component list are company-specific
- Data Literacy component detail: role skill profiles with L1-L4 targets, individual and team scores (see [data-literacy.md](data-literacy.md))
- Both instruments are working templates — see [templates.md](../12_templates/templates.md)

## Frames on the board
- [Template — Current Data & Analytics Maturity Assessment](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561784)
- [Data Governance Maturity Models](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525296)
- [Data-Driven Index (DDI) template](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611455329213)
- [Company Data-Driven Index / Data Literacy scoring](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611455329214)

## From the course (Data Governance Fundamentals, 6 days)

### ROI methods that survive scrutiny
- Financial ROI of data quality is nearly unmeasurable: you can measure concrete things, but "it will almost never be the sexy number for which you'd be handed a real budget." (course day 6, transcript)
- Only three legitimate ROI sources: revenue growth via linking DG to business initiatives, cost savings, regulator-risk mitigation. "Operational efficiency" and "innovation" petals of the classic ROI wheel are "air"; data quality always resolves into revenue or cost. (course day 6, slides p.4-5)
- Method 1 — cost of a "cleaned record": 100k duplicates x 100 RUB + 100k bad records x 1,000 RUB/yr profit per cleaned record = 110M RUB income vs 11.5M RUB cost; works only for large customer bases with real quality problems. (course day 6, slides p.10)
- Method 2 — catalog as labor savings: 120 analysts x 2.4M RUB x 23% productivity gain + 3 more role groups = 92.3M RUB benefit vs 35M RUB cost; the productivity % is a "huge zone of speculation." (course day 6, slides p.20; transcript)
- Method 3 — business cases and freed-up profit in business projects; all three approaches shipped ready-to-fill as sheet "11 Ekonomika" (Economics) of the DG Planner xls. (course day 5, slides p.36)
- Anti-case to memorize: an MDM saving $500k/yr gross but $100k net (after $400k process upkeep) against a $3M investment = 30-year payback — "they won't buy this either"; recompute the revenue side, don't polish the savings side. (course day 6, slides p.16-18)
- Big-tech attribution pattern: benefits are never credited to "data governance" — value goes to the platform/products; the practical move is to negotiate upfront what share of the analyst-driven metric uplift is attributed to the data platform. (course day 6, transcript)
- Decision-speed metrics are a dead end: "attempts to measure decision-making acceleration were worked over ten years ago; no fools are left who try." (course day 6, transcript)
- Brutal self-disclosure from the author: an honest calculation of his whole DG slice produced a monthly money effect that looked "very little" against the scale of the company — small enough that he hesitated to show the number at all. Expect the same: a truthful DG ROI rarely looks impressive next to product economics. (course day 6, transcript)

### Benchmarks (mythology / marketing — use critically)
- Data Management Institute: only 30% of stored data used regularly; storage support eats 33-70% of hardware IT spend. Gartner: 70-80% of analyst time can go to data wrangling; 15-35% of annual budget spent inefficiently due to poor DQ, up to 40% in service industries. Explicitly labeled "DG mythology" on the slide. (course day 1, slides p.43)
- DIS Group: unproductive time due to missing/low-quality data is 29-36% of working time (finance worst at 36%); market leaders run at 5-10%. Author's counter-datapoint: his own "share of analysts' target tasks" metric runs 60-70%. (course day 2, slides p.44; transcript)
- A large bank's publicly presented MDM case: 320M client records, 230M duplicates, initial contact-data quality 50%, ~$300 per failed direct communication, claimed effect >4B RUB. (course day 6, slides p.11)
- Bad-data rules of thumb: data grows ~40%/yr, ~20% of a typical base is bad; $1 prevent / $10 correct / $100 do-nothing per record — "beautiful but unrealistic" per the author. (course day 6, slides p.12-15)
- Eckerson/RateMyData: average DG maturity 2.88/5.0 ("Initiating"); top challenges — lack of stewards 54%, conflicting priorities 46%, no plan 46%, unclear responsibilities 46%; only 2% of DG programs deliver high business value, 22% deliver none. (course day 6, slides p.40-43)
- Vendor ROI claims (Collibra: 23% analyst / 26% steward productivity; Forrester TEI for Alation: $3.8M benefits PV vs $813K costs): "copy the evaluation logic, not the numbers" — realistically expect 5-7% provable, and saved time doesn't convert to output ("people just go drink coffee more often"). (course day 4, slides p.80-86; transcript)

### Metrics that actually carry communication
- When money fails, operational metrics carry it: % critical data with owners, metadata completeness/age, incident resolution %, and the killer metric "days without incidents in critical reporting." Often business doesn't ask for money at all — "just rid me of this pain, make it not every day." (course day 6, slides p.28-29; transcript)
- Allianz shift: from quantity of governance (# standards, # stewards, # glossary terms) to business impact (% call-center calls caused by data defects, % manual processes with automated validations, % reserves held due to data issues). "What we governed 10 years ago is not what we want to govern now." (course day 6, slides p.30-31)
- Data-product adoption metric: count of joins / reuse parameters of certified marts — reuse is the point of the whole exercise. (course day 1, transcript)
- Scale reference points from a large marketplace: ~16,000 metrics in the semantic layer (probably a few hundred truly unique; dedup target ~5-6k), ~6,500 scheduled datamarts, ~8,000 production dashboards, ~600 analysts. (course day 2, transcript)

### Maturity models in practice
- Target maturity starts with deleting: gray out the bricks you don't need, then benchmark against archetypes. Maturity != complexity — a simpler centralized platform can be perfectly mature; there is no single maturity ladder. (course day 2, transcript)
- Maturity models work when a company appropriates one — builds its own version and embeds domain/department maturity scores into top-management yearly goals; that launches real top-down cascades. (course day 6, transcript)
- Assessment mechanics: no single person holds the whole picture — either ~20 interviews (an audit) or a facilitation session with stickers and voting; questionnaires sent by mail must be radically simplified or nobody answers. (course day 6, transcript)
- Author's pick of open models: UK Government Data Maturity Framework — 10 topics, 97 criteria, "neither overloaded nor superficial", free self-assessment Excel; Central Bank of Russia model flagged as a rare national-standard candidate since Western DG certifications are inaccessible in Russia. (course day 6, slides p.44-45; transcript)
- Shortcut: feed any maturity model to an LLM, have it interview you (~30 questions) and produce the positioning report — "check what a good LLM dialog gives you before doing it by hand." (course day 6, transcript)

## Links
- https://edmcouncil.org (DCAM)
- CMMI Institute DMM link on the board returns 404
