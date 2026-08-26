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

## Links
- https://www.datamesh-architecture.com/datamesh-canvas
