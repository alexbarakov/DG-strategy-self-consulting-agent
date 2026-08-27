---
theme: domains-and-data-mesh
type: dg-program-theme
frames:
  - "3458764611453525288" # Domain structure slide
  - "3458764611453561758" # Template: Data Domain Classifier
  - "3458764611453561759" # Domain/subdomain map — filled example
  - "3458764611453561760" # Domain/subdomain map — blank template
  - "3458764611453561761" # Data Mesh Canvas — worked example
  - "3458764611453561762" # Data Mesh Canvas — blank template
  - "3458764611487000941" # Data Products
---
# Domains and Data Mesh

## What the board teaches
"Domain structure is a key element in many DG practices going forward" — the board makes domain mapping the entry point into decentralized governance. Two complementary artifacts do the work: a registry-style Data Domain Classifier (domain / subdomain grid with Data Owner, Business Data Steward, and Tech Data Steward / Data Custodian columns — worked Finance and HR examples) and a visual hexagon domain map (six business domains with color-matched subdomain stickies and ~10 dotted cross-domain connectors, e.g. Sales-Operations via Client Master Data). From there the board steps into data-mesh territory: the Data Mesh Canvas (datamesh-architecture.com) classifies data products into source-aligned / aggregate / consumer-aligned swim lanes, with a worked example of 11 data products and 15 consumption dependencies (CRM's "360° Customer" aggregating source products; Controlling's "Profitability Reporting" drawing on both layers). Data Products themselves are defined as prepared, trusted, non-raw data ready for wide consumption — with concrete requirements (described/interpretable, guaranteed quality with transparent issues, change notifications, purpose-driven design, discoverability, interoperability) and the pragmatic advice that a simple spreadsheet register of critical sources is a perfectly good start.

## Key objects
- Takeaway: domain structure underlies modern DG practices (criticality labeling, stewardship, catalogs, mesh)
- Data Domain Classifier grid: Data Domain | Subdomain | Data Owner | Business Data Steward | Tech Data Steward / Data Custodian; examples — Finance (P&L, cost allocation, planning & forecasting) and HR (salary, attrition, trainings, headcount)
- Hexagon domain map (filled): Sales, Finance, Operations, Marketing, Human Resources, Services Delivery + subdomains; cross-domain connectors (Client Master Data shared Sales-Operations); peripheral placeholder hexagons; matching blank template
- Data Mesh Canvas layers: source-aligned (Search Queries, Articles, Orders, Customers, Shipment, Invoice) → aggregate (ML Model, 360° Customer) → consumer-aligned (Funnel Analytics, KPIs & Dashboard, Profitability Reporting)
- Data Product definition and 6 requirements: labeled/described data, guaranteed quality with issue transparency, change notifications, purpose-driven with captured consumer requirements, accessibility/discoverability, interoperability (connect/auth/download)
- "Simple register could be a good start": spreadsheet register of critical sources / data models with Google Sheets template
- Domain classifier, domain map, and mesh canvas are all workshop templates — see [templates.md](../12_templates/templates.md)

## Frames on the board
- [Domain structure](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525288)
- [Template - Data Domain Classifier of the Company](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561758)
- [Domain / subdomain structure — filled example](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561759)
- [Domain / subdomain structure — blank template](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561760)
- [Data Mesh Canvas — example, multiple use cases](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561761)
- [Data Mesh Canvas — template](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561762)
- [Data Products](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611487000941)

## From the course (Data Governance Fundamentals, 6 days)

### The centralization slider
- "Everyone sits on a centralization-decentralization slider, and the slider position — not the fashion — is the key strategic decision" of the DWH/platform head: it determines your roles system, stack and even architecture fit. Many companies "lost more than they gained precisely because of poor governance" of decentralized data work. (course day 2, transcript)
- Author's rule: build a data mesh starting from centralization; hand out freedom only after processes and culture are established — engineers seeded from the platform keep the platform culture in the domains. His company did the opposite: "immediately maximum Wild West — full decentralization, freedom, and governance activities never took root; we're still cleaning that up." (course day 2, transcript)
- Mesh critique from inside a fully decentralized platform: "this is the tax of a big platform" — big-tech culture presumes trust, every team accumulates tech debt along the chain, and the governance mesh theory promises "does not take off"; winning influence back means slowing TTM and taking freedom away. "Even the founder of data mesh is now rewriting the topic." (course day 5, transcript)
- Terminology hygiene: data mesh is an org model (plus governance), NOT a storage architecture — you can run Data Vault with a centralized team and still borrow mesh elements; confusing the two is widespread even among IT specialists. (course day 2, transcript)
- Centralized counterpoint: for regulatory/management reporting, an end-to-end-controlled centralized model can reach quality unreachable in a mesh (a large IT services company took ~8 years to build fully controlled executive reporting). (course day 2, transcript)

### How to slice domains
- Don't overthink splitting criteria: "the real value is just agreeing on a structure by common sense." Draft a spreadsheet with domain + owner columns; the correct structure reveals itself when you assign responsible people — a bad domain structure simply "won't stretch onto your people." (course day 3, transcript)
- Domains begin at the warehouse raw layer, not at source systems; systems map to domains 1:1, 1:N and M:N, so source teams participate poorly in the domain scheme by default. (course day 3, transcript)
- Today "any LLM will draft a better typical domain structure than I will" — feed it your warehouse schema and it maps domains; this class of consulting task is dying. (course day 3, transcript)
- Domains are needed even in a fully centralized model — there will just be far fewer expectations of them (glossary approval, requirements, no rights to build own datamarts). (course day 2, transcript)

### Sandbox / prod balance
- Balance case from a large fintech: very mature layered platform + many self-service ETL sandboxes with deliberately lighter governance for urgent business work; core-model changes go through multi-day reviewed pull requests. Cost of the balance: a large shadow ETL — production processes running on self-service objects. (course day 2, transcript)
- Environment design: separate archive / sandbox / prod; sandboxes carry lower documentation/health requirements but hard restrictions — no sharing objects outside the team, no schedules. "You don't cut a person's rights, but you keep the environment sane for everyone else." (course day 2, transcript)

### Metric ownership (case from a large classifieds player)
- Assigning ALL metrics to product teams failed: responsibility for a metric is distributed across functions (CPT revenue: Monetization, Pricing, Sales, Finance), cross-team coordination costs more than teams will pay, and data analysts are bad at writing methodology ("strong pushback on such tasks; it needs a business/systems-analyst skill set"). (course day 5, slides p.31)
- Working split: key metrics (top-level, cross-team, externally reported) → Data Steward, where DG focus must be; local product metrics (drivers) → Data Analyst, second priority; scoped one domain pair per year. (course day 5, slides p.32-33)
- War story: a domain claimed "it's our data, we do what we want, no governance for us"; their CIO shut it down with "these are not your data — they are the business group's data." (course day 3, transcript)

## Links
- https://www.datamesh-architecture.com/datamesh-canvas
