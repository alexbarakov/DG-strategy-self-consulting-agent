---
type: meta
purpose: What this KB is missing and in what order to fix it
source: gaps found by running the skill on a deliberately awkward case (regulated insurer, legacy estate, MDM pain)
---

# Roadmap — what this knowledge base still needs

This file exists because the KB was stress-tested rather than admired. A full FORM run against a regulated mid-size insurer with a legacy estate — the least comfortable case we could construct — surfaced eight areas where the base had no material and one structural assumption it never declared. What follows is the repair plan, ordered by whether it can be done from existing sources or needs the author's own practice.

The organizing principle stays the same as everywhere else here: **an honest gap beats a padded chapter**. Nothing on this list should be closed by generating plausible textbook content — that would destroy the one property that distinguishes this base from DMBOK.

## Wave A — methodological, closeable from existing material

These are defects of framing rather than missing knowledge. They can be fixed now, without new sources, because the material to fix them is already in the base — it is just written for one kind of company.

**A1. The dependency chain has no non-AI variant.**
The central chain `core → semantic → context → AI accuracy → self-service` assumes a company with an AI ambition. Run against an insurer that has none, it is unusable — the strategy had to invent the equivalent (`identity → definitions → traceability → regulatory trust and cross-sell`) on the spot. Fix: state the general form of the chain (*foundation → meaning → provenance → the outcome your company actually buys*), then give two or three instantiations — AI-first tech company, regulated enterprise, cost-pressured retail. Touches: `README.md`, `30_graph/objects.yaml`, `skills/dg-strategy/SKILL.md`.

**A2. The base never declares who it was written for.**
Every number, war story and default assumes a large tech company with a managed platform, federated analytics and a budget problem. That is a legitimate scope — but it is currently implicit, so a reader from a bank silently receives advice calibrated for someone else. Fix: an explicit "who this base fits and who it does not" section in the README, plus a per-theme note where the advice is scope-bound. This is a half-day of work and the highest honesty-per-effort item on the list.

**A3. The inverted constraint: budget yes, speed no.**
All material is built on "they will not give you money", with a time quota as the central move. The insurer had money and lacked throughput — the binding constraint was the architecture committee. Fix: a short section in `getting-started.md` and `dg-program-roadmap.md` on programs constrained by approval velocity: packaging initiatives into existing mandates, minimising the number of approvals rather than the cost, and why "we already have budget" is not the good news it sounds like.

**A4. Reviving or burying a dead governance body.**
The base teaches how to create governing bodies and how to avoid bureaucracy. It has nothing on the far more common situation: a council that has existed for three years, meets quarterly, produces minutes and changes nothing — while occupying the political space where a working body would go. Fix: a section in `roles-and-operating-model.md` — the diagnosis (does anyone in the room control anyone's time?), the re-founding move (change the chair to whoever holds real leverage, strip the agenda to disputes and prioritisation, kill status reporting), and the case for burying it instead.

**A5. Regulatory lineage as its own use case.**
Lineage is currently discussed through the catalog and through agents. The regulator's question — "show me where this number came from" — is a different requirement with a different acceptance criterion, and it is the single strongest budget lever a regulated company has. Fix: a subsection in `data-catalog.md` or a short standalone file, grounded in what the base already says about lineage plus the distinction between provenance-for-humans and provenance-for-audit.

## Wave B — needs the author's own practice, not generation

These are real subject gaps. Each should be filled by interview, not by writing. If the author has no practice in one of them, the correct outcome is a stub that says so and points elsewhere — not a chapter.

**B1. MDM and identity resolution.** The largest initiative in the insurer's strategy had no method behind it in the base; the recommendations were assembled from the general "narrow the perimeter" principle and from failure patterns. Needed: why golden-record agreements between business lines fail, where to cut the perimeter, what "identity resolution without full MDM" looks like in practice, and how to restart after a failed attempt.

**B2. Privacy, PII and special-category data.** For an insurer with a health book this is the first compliance question. The base has ~13 incidental mentions and no material. Needed: sensitivity classification in practice, what it actually forbids in analytics, and how the privacy regime changes the DG operating model.

**B3. Retention and the legal side of lifecycle.** Archiving exists in the base as content hygiene. The legal layer — mandatory retention, deletion obligations, what you may not archive away — is absent.

**B4. Governance over a legacy estate.** The base assumes a platform you can change. Needed: what governance looks like over systems that will not be modified for five years, and how deep traceability can realistically go through them.

**B5. External data suppliers.** Data contracts are described for internal flows. Nothing covers hundreds of external counterparties whose data quality you influence only through contract and intake control.

## Wave C — structural work already scoped

**C1. Playbooks.** Fifteen initiative types still exist as one-line table rows in the skill ("method + template + reading"). A practitioner handed "certify the core layer" finds a pointer to a theme file, not steps, RACI, effort estimation and failure points. This is the gap that broke the first Trovato run — there was no capacity arithmetic to lean on because none exists in the base.

**C2. Four thin AI-era files.** `ai-governance`, `llm-assistant-architecture`, `semantic-layer` and `context-governance` remain at ~1k words because their primary source is the author's BI+AI course rather than the DG course. They need that source, not more extraction from this one.

**C3. Four board frames unreadable via API.** Legacy Miro table widgets (the 13×5 roadmap grid, the 26×7 DDI scoring grid, the capability matrix, the operational-models comparison) resist every extraction path. Either re-draw them on the board as native shapes, or transcribe them manually once.

## What NOT to do

- Do not close Wave B by generation. A well-written privacy chapter assembled from general knowledge is indistinguishable from a textbook and will be the first thing that betrays the base as a compilation.
- Do not expand the perimeter for completeness. The base is strong because it is opinionated about a specific kind of company; a base that covers everything covers nothing distinctively.
- Do not remove the honest gap markers already in the files (`## Что не покрыто этим источником`). They are load-bearing.

## Sequencing

Wave A first — it is cheap, needs nothing new, and fixes the framing that currently mis-serves half the potential readers. Wave C1 next, because it converts existing knowledge into executable form. Wave B only where the author has practice, in interview format, one topic at a time.
