---
theme: AI-era DG Library
type: reading-list
status: draft
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681744960974"
---

# AI-era Data Governance — Library

The full link library of the board: canonical articles per AI-era theme, classic-DG community and standards, and the author's working resources. AI-era links verified 2026-08-25/26; the classic-DG section mirrors the board's resource library (Program Map 3.0 and template frames).

## Semantic Layer
- Spider 2.0 — enterprise text-to-SQL benchmark (6% vs 86% academic): https://spider2-sql.github.io/
- Anthropic — self-service analytics with Claude (21% → 95%+): https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- dbt MetricFlow — metric definitions as code: https://docs.getdbt.com/docs/build/about-metricflow
- dbt Semantic Layer — docs: https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl
- dbt — Semantic layer vs text-to-SQL (Apr 2026): https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026
- Cube — semantic layer for AI agents (2026): https://cube.dev/articles/semantic-layer-for-ai-agents-2026
- Cube — pre-aggregations: https://docs.cube.dev/docs/pre-aggregations
- Snowflake Cortex Analyst — semantic models in production: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst
- Open Semantic Interchange — vendor-neutral spec (now Apache Ossie): https://www.snowflake.com/en/blog/open-semantic-interchange-ai-standard/ · spec: https://github.com/open-semantic-interchange/OSI
- Airbnb Minerva — metric consistency at scale: https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70

Concepts: metric store · semantic model · semantic compilation · SQL API · text-to-semantic · headless BI

## Context Governance
- Anthropic — Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic — Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Anthropic — governance scope of a service account (Claude tAg for ad-hoc): https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
- Clarify before answering, 42.5% → 92.5% (arXiv): https://www.arxiv.org/pdf/2508.15276
- LangChain — LLM evals: https://www.langchain.com/resources/llm-evals
- Arize — what is an evaluation harness: https://arize.com/blog/what-is-an-evaluation-harness/
- Galileo — calibrating an LLM judge with human annotations: https://galileo.ai/blog/calibrate-llm-judge-human-annotations

Concepts: context unit · status lifecycle · trust plane · freshness TTL · golden set · offline/online evals · false-accept · provenance

## Domain Knowledge Base
- Google — Introducing the Knowledge Graph: things, not strings: https://blog.google/products/search/introducing-knowledge-graph-things-not/
- Ontologies and relationship graphs for LLM data access (arXiv): https://arxiv.org/pdf/2604.00555

Concepts: knowledge pack · domain profile · few-shot · trap · golden set · AI-ready score

## Skills Hub / Agent-skill governance
- Anthropic — Agent Skills: https://claude.com/blog/skills
- Model Context Protocol: https://modelcontextprotocol.io/
- Hosseini & Lichtinger (Harvard) — GenAI as seniority-biased change (−7.7% junior employment in 6 quarters): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5425555

Concepts: skill · trace · skill registry · contribution flow · confirmed value · penetration

## Certified Core Layer
- Kimball Group — Dimensional modeling techniques: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/
- dbt — best practices: https://docs.getdbt.com/best-practices

Concepts: conformed dimensions · grain · certification · data contract · DQ checks · health score · Jevons paradox

## AI Governance
- NIST AI Risk Management Framework (govern / map / measure / manage): https://www.nist.gov/itl/ai-risk-management-framework
- EU AI Act (Regulation 2024/1689): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- ISO/IEC 42001 — AI management systems: https://www.iso.org/standard/81230.html

Concepts: risk tiering · model inventory · human-in-the-loop · audit trail · accountable owner

## Classic DG — standards and communities (board resource library)
- DAMA International (DMBOK home): https://www.dama.org/cpages/home
- DAMA UK — community feed: https://www.linkedin.com/company/dama-uk-ltd/posts
- EDM Council (DCAM, CDMC): https://edmcouncil.org
- Data Management Wiki (source of the DQMS concept map): https://datamanagement.wiki/
- Data Crossroads — free DG resources (Irina Steenbeek): https://datacrossroads.nl/free-resources/
- TDAN — The Data Administration Newsletter, DG section: https://tdan.com/category/data-topics/data-governance-articles-blogs-education
- Dataversity — DG blogs: https://www.dataversity.net/category/data-topics/data-governance/data-governance-blogs/
- DataGovernance.com (Bob Seiner, non-invasive DG): https://datagovernance.com/blog-2/
- Data Mesh Learning community: https://datameshlearning.com/
- Data Mesh Architecture — canvas used on the board: https://www.datamesh-architecture.com/datamesh-canvas
- 360WorkX — community feed: https://www.linkedin.com/company/360workx/posts

Vendor blogs (tool-side view of DG):
- Collibra: https://www.collibra.com/us/en/blog
- Informatica: https://www.informatica.com/blogs.html
- Precisely: https://www.precisely.com/category/datagovernance
- Atlan: https://atlan.com/

## Classic DG — people to follow (from Program Map 3.0)
- Nicola Askham — The Data Governance Coach: https://www.nicolaaskham.com/about
- George Firican — Lights on Data: https://www.lightsondata.com/
- Dave Wells — Eckerson blog: https://www.eckerson.com/blogs/data-management
- Robert S. Seiner: https://www.linkedin.com/in/robert-s-seiner-445313/
- Willem Koenders — Medium: https://medium.com/@willemkoenders
- Charlotte Ledoux: https://www.linkedin.com/in/charlotte-ledoux-53b43253/ · ebook: https://www.charlotte-ledoux.xyz/ebook
- Animesh Kumar — Modern Data 101: https://moderndata101.substack.com/
- Chad Sanderson (data contracts): https://www.linkedin.com/in/chad-sanderson/
- Piotr Czarnas (DQOps): https://www.linkedin.com/in/piotr-czarnas/
- Peter van Nederpelt (data quality dimensions): https://www.linkedin.com/in/petervannederpelt/
- Irina Steenbeek: https://www.linkedin.com/in/irina-steenbeek/

## Classic DG — book shelf (from Program Map 3.0)
- DAMA-DMBOK 2nd Edition: https://amzn.to/2R8NDEr
- Seiner — Non-Invasive Data Governance: https://www.amazon.com/Non-Invasive-Data-Governance-Robert-Seiner/dp/1935504851
- Ladley — Data Governance: How to Design, Deploy and Sustain: https://amzn.to/3xir6Zu
- Madsen — Disrupting Data Governance: https://amzn.to/3K0Z7Vy
- Eryurek et al. — Data Governance: The Definitive Guide: https://amzn.to/3jXlkcn
- O'Neal — Data Governance: Perspectives and Practices: https://amzn.to/3YHNkzy
- Cotrupe — Get Governed: https://amzn.to/3YLNw0Q
- Plotkin — Data Stewardship: https://amzn.to/40Nrooy
- Soares — The CDO Handbook for Data Governance: https://amzn.to/3ZqoyEm
- Data Governance for Dummies: https://amzn.to/3ZSYm5J

## Classic DG — article shelf (from Program Map 3.0)
- Koenders — Intelligent Data Governance by Design: https://medium.com/@willemkoenders/intelligent-data-governance-by-design-a-practical-example-30f2bbf1bf91
- Koenders — My Simple Data Strategy Framework: https://medium.com/@willemkoenders/my-simple-data-strategy-framework-c2cf90265d7a
- Koenders — What's the big deal about Data Products: https://medium.com/@willemkoenders/whats-the-big-deal-about-data-products-26ac347b7d7a
- Active Data Governance Methodology (Dataversity, PDF): https://content.dataversity.net/rs/656-WMW-918/images/Active-DG-Methodology_9.10.21.pdf
- Establishing Data Governance as a Service (Dataversity): https://www.dataversity.net/establishing-data-governance-as-a-service/
- Modern Data Governance: Strategies for Data Policies that Stick (TU Berlin, PDF): https://www.user.tu-berlin.de/komm/CD/paper/050141.pdf
- ADDA — Data Catalog Implementation Guidelines (PDF): https://adda.gov.ae/-/media/Project/TAMM/ADDA/ICT-Publications/ADDA-DMP-Data-Catalog-Implementation-Guidelines.pdf
- Data Product Manager: The Most Crucial Job of the 21st Century: https://medium.com/@seckindinc/data-product-manager-the-most-crucial-job-of-the-21st-century-3f2daa4f94ee
- Why and How to Run Data Teams as Product Teams: https://medium.com/@seckindinc/why-and-how-to-run-data-teams-as-product-teams-3adc464c004f
- The Modern Data Stack Through 'The Gervais Principle': https://medium.com/@laurengreerbalik/the-modern-data-stack-through-the-gervais-principle-bfd4b4e33ac7
- Big Data is Dead (MotherDuck): https://motherduck.com/blog/big-data-is-dead/
- Data product toolkit incl. Data Product Canvas (dataproductbusiness.com): https://www.dataproductbusiness.com/get-started
- Gamified Data Governance Programs (YouTube): https://www.youtube.com/watch?v=__oSuavpGDA

Full raw registry with labels as they appear on the board: `../20_dg_program_guide/frame-3458764611453577668.md` (note: frame extraction is capped at 500 items — the tail may hold more links).

## Author's resources (Alex Barakov / data nature)
- Site: https://data-nature.com · DG guide (RU): https://datanature.ru/datagovernance
- Channel: https://t.me/datanature · LinkedIn: https://www.linkedin.com/in/alexanderbarakov/
- D&A Maturity Assessment model (Miro board): https://miro.com/app/board/o9J_lha8MnM=/
- Lords of the Boards (Miro board): https://miro.com/app/board/uXjVOAch4J8=/
- Data Governance Map — Excel version of this guide: https://barakov.gumroad.com/l/DataGovernanceMap · [view-only Sheets](https://docs.google.com/spreadsheets/d/17VvUlbZy6pV2KAmHRnKhheUUXheUsc3NpqFPq2WrxCI/edit?gid=1919735239)
- Data & Analytics Maturity Map / Scorecard: https://barakov.gumroad.com/l/dataanalyticsmaturitymap · [Sheets](https://docs.google.com/spreadsheets/d/1KMz58b8uLopevzp04kh3rGF8YLW6HmsVFw-UegV1-Is/edit?gid=1568926272)
- BI Adoption Guide: https://barakov.gumroad.com/l/BIAdoptionGuide
- DG Vision Statement template (Sheets): https://docs.google.com/spreadsheets/d/1ZNnuGQrdlYCN6QgYwWb4ISFtcKl8gV-PvfyCtV3cGJE/edit?usp=sharing
- 1:1 coaching: https://calendly.com/alexander-barakov/1-hour-coaching

## Visuals on the Library frame
Semantic Web stack (W3C), Star schema (Kimball), DIKW pyramid — Wikimedia Commons.
