---
theme: AI-Ready BI Content Management
type: author-frame
status: accepted (author-made)
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681721125845"
related:
  - "[[certified-core-layer]] — certification produces the trusted layer this funnel feeds"
---

# AI-Ready BI Content Management

Building an autonomous process for reproducing a layer of high-quality BI dashboards, datamarts & metrics. We improve search and navigation for users and AI agents by archiving unused items and marking the key and healthy objects.

## The content funnel (concentric circles on the frame)

- **100% — all dashboards** (including test ones, development copies, outdated-but-useful, forgotten, made-for-yourself, one-off). Call to action: archive all unused.
- **70% — non-sandbox dashboards** — what the developer considers production, shared with business roles. Call to action: move reports to sandbox and archive (no mass access) & certify the rest.
- **25% — dashboards actually in regular use.**
- **10% — "healthy" dashboards** — meet quality criteria (trusted data sources, metadata etc.), based on (automatic) certification.
- **5% — recommended key reports** — "real products", maintained, manual review by BI partners: recommended as first choice for an entity, cover a significant domain use case, must stay in the green health zone. Call to action: grow user traffic, maintain health, develop BI products, increase MAU.

Strategy in short: grow the "healthy ∩ recommended" inner join.

## Why it is a DG/AI theme

An AI assistant navigating thousands of stale dashboards produces plausible garbage; archiving + certification turn the content pool into a searchable, trustworthy corpus for both humans and agents.

## From the course (Data Governance Fundamentals, 6 days)

**Certification designs**
- Two fundamentally different designs by org model: centralized BI → hybrid certification with business ("Recommended by <function>" badge: the function confirms data correctness and logic actuality, joins semi-annual reviews; only cross-functional reports certified, zero bureaucracy — everything in wiki report cards); decentralized self-service → content management at scale: split all server content into "good" (certified) and "bad", hide sandboxes from search. (course day 3, slides p.91-97; transcript)
- For business users a huge share of pain is solved by just two things: archiving and certification — cheap, and packages well as a DG win. But certification has an upstream chain: certified dashboard requires certified datamart requires data contracts/checks requires a role model. (course day 2, transcript)
- The co-ownership manipulation that works: release notes say "Team FP&A together with Reporting & Analytics are glad to announce a new report…" although BI did all the work — business stakeholders feel like co-owners and in exchange give sign-offs, glossary decisions, access-matrix approvals and 2nd-line support. (course day 3, transcript)
- Auto-certification checks used by a large tech company: start-page metadata filled, owner in title, documentation ≥300 chars, objects in prod folders, report is fast; data certification standard = 5 parameters, simplified = 3; non-certified reports carry a public "failed certification" plaque; authors get achievements plus an owner-rating used in reviews; re-confirmation once a year during a cleanup event. (course day 3, slides p.97-101)

**Funnel numbers behind the circles**
- Order-of-magnitude funnel at a large marketplace: ~13k dashboards → ~90% outside sandboxes → roughly a third actually in use → a few hundred key reports; metrics ~15k → ~30% important → ~10% in use. (course day 3, slides p.103)
- Why cleanup pays, in money: performance is the #1 user dissatisfaction cause (seconds of waiting × thousands of users = hours / hundreds of thousands of rubles per day); navigation is #2 (double work, slower TTM); unused objects burn real DWH cash — CPU/disk limits, failed refreshes. (course day 3, slides p.105)
- Metric sprawl reverses after certification: counts shrink via auto-tests, auto-archiving and auto-certification; content is moved to sandbox/archive, not deleted — you keep growth and agility while sieving content. (course day 2, transcript)

**The subbotnik habit machine**
- The cleanup-day growth hack: announce "let's tidy our reports and data", appoint a per-team responsible, run it a month, celebrate contributors — they've unknowingly done data-steward work (archiving, certification, documentation). Then "let's repeat" → "why repeat — let's just do it monthly", and the role has been institutionalized. This is exactly how the author bootstrapped his BI-partner program; bots now replace subbotniks by telling partners what to archive. (course day 2, transcript)
- Realistic subbotnik targets: archive 20% of black-status objects, move 30% of grey/black out of prod-like folders, -10% average open time for red/yellow reports, 50% of spawned tech-debt tasks closed within 3 months; a June run processed 36.6% of low-use objects (299/817) and certified 97. "The goal is not to do everything — the goal is to create a habit." (course day 3, slides p.104-109)

**Bots and intake discipline**
- Content-bot check catalog: extract size vs threshold, filter-click performance, doc links, freshness timestamp, style guide, certified sources vs inefficient custom SQL, field naming, rights hygiene; folder checks (DEV holds nothing older than a month, archive has no live schedules/subscriptions); regular digests, alerts and shamelists. Next stage: a DG bot that walks up to owners — "can I archive this?" / "this looks certification-worthy, fill the docs" — with AI drafting the documentation by button. (course day 3, slides p.102, 108; transcript)
- Report intake discipline: "challenging requests" is a named competency in the BI skill matrix; after delivery the customer owes adoption — audit the numbers together ("target was 10% of the intended audience — what do you say?") before accepting their next urgent request. (course day 3, transcript)
- BI-side glossary surfacing: dashboard properties let the creator pick metrics from the metric store (M42), giving clickable metric context and drill-through from every dashboard; boxed catalogs barely support this — buy maximally open products (API/MCP access) and code the integrations yourself. (course day 5, transcript)
