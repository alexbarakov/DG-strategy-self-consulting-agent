---
theme: dg-kitchen-research
type: dg-program-theme
frames:
  - "3458764611802674336" # Cover
  - "3458764611802674337" # Table of contents
  - "3458764611802674338" # Disclaimer / methodology
  - "3458764611802674339" # 1. DG Start and Sponsorship
  - "3458764611802674340" # 2. Pains and drivers
  - "3458764611802674395" # 3. Role model
  - "3458764611802674396" # 4. Data Catalog
  - "3458764611802674397" # 5. Business Glossary
  - "3458764611802674398" # 6. Data quality management
  - "3458764611802674399" # 7. Efficiency
  - "3458764611802674400" # 8. Challenges / Plans
  - "3458764611802674401" # How to start (Common Sense DG + MVP)
  - "3458764611802674402" # Land-and-expand roadmap
  - "3458764611802674403" # My thoughts: DG as coordination layer
  - "3458764611802674404" # My thoughts: success factors
---
# DG Kitchen of the Tech Industry (2024 research)

## What the board teaches
"Data Governance Kitchen of the Tech Industry" (Alex Barakov, 2024) is an interview study of 20 anonymous tech companies (5 countries, 3,000-100,000+ employees, all with advanced data platforms — incl. a top-5 neobank, a top-3 classified, top-10 delivery and e-commerce platforms), aiming to capture real DG practice "free from marketing". Headline picture: DG in tech is still semi-formal — 40% run no separate DG program (governance is embedded in data-platform processes), programs get justified via a catalog + DQ framework rather than "pure DG", and the final go-decision is usually "a leap of faith" by the data platform head since nobody tracks TTM effects. Top drivers are analyst-facing (data discovery, request TTM), not compliance. Roles adopt asymmetrically: Data Custodian works (65%), Business Data Steward mostly doesn't, committees are absent. DataHub dominates catalogs (~70%), but the author flags "catalog as a shield" — platform teams hiding behind tooling to avoid harder governance work. Glossaries are the biggest gap (2/20), DQ suffers from "tools without processes" (only 10% monitor incident SLAs), and 30% of companies are scaling DG back after prolonged effort without visible results. The research concludes with the author's playbook — Common Sense DG quick wins plus a DG MVP led by a respected internal veteran, expanding land-and-expand style only when sponsorship materializes.

## Key objects
- Methodology: 20 companies, 5 countries, anonymity for honesty; explicit critical-thinking caveat (described approaches may be immaturity, not best practice)
- 8 interview topics: DG start and sponsorship; pains and drivers; role model; data catalog; business glossary; DQ management; efficiency; challenges/plans
- Start & sponsorship: 40% no separate DG program; 45% have a CDO (top-down easiest); 30% bottom-up via infosec; both directions needed; reporting distrust as the "pure DG" trigger
- Ranked drivers: 1 data discovery for analysts; 2 TTM of data requests; 3 quality of critical data; 4 consistent reporting / metric discrepancies; 5 cross-functional data use; 6 compliance risks; 7 M&A data consolidation
- Role model: Data Custodian (aka domain curator / data partner) 65%, filled by systems analysts / data engineers; Data Object Owner rare (compensated by custodian or duty rotation); Business Data Steward hardest; DG committees largely absent (author: dedicated DG meetings are essential)
- Catalog: DataHub ~70%; selection criteria — push approach + contributor community; criticisms — "catalog as a shield"; chat-based data management works only in isolated domains
- Glossary: 2/20 with consolidated glossary + metrics tree; prerequisites — steward skills, cross-domain facilitation, parallel semantic-layer project; author: physical layer / metric store / golden layer more critical
- DQ: 3-level model (core platform contracts+ingestion checks / data engineers transformation checks / BI final cleaning); tooling — Airflow + Great Expectations, dbt test, custom, Soda, Ataccama, Monte Carlo, YAML-driven contracts; problem — tools without processes; 10% monitor DQ SLAs
- Efficiency: 20% cost saving on a 4 PB Hadoop cluster via deletion; catalog ROI proven by chat-search vs catalog-search comparison; 30% scaling DG back; fast benefits correlate with respected senior MVP leads
- Next-year plans: access-as-code, data contracts framework, dbt testing, object/domain ownership, catalog and platform courses
- Author's conclusions: DG = organizational and tooling coordination layer; informal "DG common sense" breaks at scale → formal DG MVP; Core BI / cross-functional analytics team as DG backbone; Custodian/Partner/Curator > Steward in foundational importance; DG leader must be a respected internal veteran (external hires face sabotage risk)

## Frames on the board
- [Cover — DG Kitchen of the Tech Industry](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674336)
- [Table of contents](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674337)
- [Disclaimer / methodology](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674338)
- [1. DG Start and Sponsorship](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674339)
- [2. Pains and drivers](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674340)
- [3. Role model](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674395)
- [4. Data Catalog](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674396)
- [5. Business Glossary](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674397)
- [6. Data quality management](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674398)
- [7. Efficiency](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674399)
- [8. Challenges / Plans](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674400)
- [How to start: Common Sense DG + DG MVP flow](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674401)
- [Land and expand DG roadmap (Stages 1-3)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674402)
- [My thoughts: the point of DG](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674403)
- [My thoughts: DG success factors](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674404)

## From the course (Data Governance Fundamentals, 6 days)

Note: on the course this peer material was presented with company names; here it is aggregated, matching the board's anonymity convention.

### Per-topic status across the surveyed big-tech peers
- **Catalogs** — one bought a commercial catalog (an open push API was the deciding factor) and rolled it out in under 6 months with 3 part-time people; one tested a popular open-source catalog and dropped it (docs live in the wiki and turn into tech debt); two built their own products, one of them now revising its "the catalog is not for input" concept; one custom build on Atlas has owners on only 30% of objects with an audience of ~30 analysts; one refused vendor lock and built custom on open source — MVP in a quarter with 3 engineers. One of the companies that failed the first attempt has since engaged a vendor for a second run — "if they found drivers for a second run, they accumulated investment reasons." (course day 4, slides p.87; transcript)
- **Data quality** — one avoids blanket checks on principle: "every check = money" on pay-as-you-go compute, with anomaly self-detection instead; one runs its own DQ product "voluntarily, without control or goals"; one covers ~10% of critical objects; one ships a two-check module — "the tool exists = the process doesn't." (course day 4, slides p.145)
- **Glossaries** — "in big techs the glossary simply doesn't take off": one never built one (a new attempt is riding on a metric-store project), one keeps it out of focus, one "sort of" maintains it. Punchline: everyone names metric divergence as almost their main pain, yet nobody builds glossaries — because a glossary needs facilitated cross-domain work with business experts plus a synchronous semantic-layer project. (course day 5, slides p.28)
- **Roles and culture** — one distributed engineers into domains and still failed to make data partners proactive (they stayed reactive); one has "no calm period for DG projects" thanks to quarterly transformations; in one the culture rejects "regulating rules and imposing roles" outright, so de-facto role acceptance never started; a delivery-tech player runs everything through code (data-access rules in GitHub, contracts planned). (course day 6, slides p.107)

### Role patterns worth stealing
- One big-tech player splits what most companies mash into a single role: a "BI governor" owns only certified reports and reporting standards, while Data Partners (system analysts) own core layers, marts, their certification and optimization. (course day 3, slides p.63)
- One large bank formally has no BI function at all — fully decentralized; a 50+ person cross-data team (templates, standards, courses, tools) informally acts as a BI CoE, at roughly 1 BI developer per 133 users and 10,000 MAU on the BI tool. (course day 3, slides p.62)
- Another large bank hired dedicated business Data Stewards straight from the market as full positions (strategy + DQ processes + project portfolio inside their block) — rare and expensive, but it greatly accelerates policy rollout. (course day 3, slides p.52-53)

### Effectiveness evidence and war stories
- Effectiveness evidence across the industry is "mostly emotional": data partners plus a catalog "gave positive vibes"; "entropy is decreasing"; TTM effects impossible to assess because nobody tracks Jira properly. Only one company in the survey ran an actual analysis — chat search time without a catalog vs catalog search stats, number of requests × analyst FTE cost — and its results green-lit further investment. (course day 6, slides p.34)
- Big techs never present DG at conferences as a revenue driver — governance there is dissolved into platform processes, "it runs by default"; external catalogs are unsellable to big tech, only mid/small tech buys. (course day 6, transcript)
- A large fintech recently cut its entire DG team — stewards and catalog support ("they'll probably resuscitate it later"). Standing lesson: in the fight for engineers between platform product streams, the catalog loses; DG lives in a structurally weak position — which is why the author refuses to build DG around a negative vibe and pushes "common sense DG." (course day 2, transcript)
- The research's framing question, stated explicitly on the course: "Maybe DG is the case where methodological complexity does more harm than good?" (course day 1, slides p.117)

## Links
- https://data-nature.com/
