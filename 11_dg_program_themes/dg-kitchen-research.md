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

## Links
- https://data-nature.com/
