---
type: example
kind: company-portrait
company: Tairin
note: invented company; the input half of a worked FORM run
---

# Company portrait and interview answers

**Tairin** — a delivery and dark-store operator: 340 locations in 12 cities, around 4.5M orders a month, 6 200 employees. Own app, own courier network, an assortment of 6 000 SKUs.

| Question | Answer |
|---|---|
| Strategy type, structure, volume | DG · Summary + sections 00–07 · HTML + MD · Lite diagnostic. **Why DG and not AI:** the assistant mandate exists, but its quality is entirely determined by definitions, a certified core and context — and that is governance work. |
| Scale and org model | 6 200 employees, 12 cities. Analytics is centralised: 55 analysts in one unit, a BI team of 9, 12 data engineers. |
| Landscape | Warehouse migration to a lakehouse: 18 months done, ~10 remaining. dbt in use, no semantic layer. No catalog; a wiki of 400 pages, half of it stale. Certification does not exist as a concept. |
| Pains | Three definitions of a completed order, divergence up to 4%. ~60% of ad-hoc requests are repeats. Search returns everything indiscriminately. All engineering capacity is committed to the migration. |
| Foundation | DQ checks on the payment perimeter only. The ad-hoc flow is counted by request volume but not by share of repeats. |
| Constraints | Money is available, approvals are fast, **there are no engineering hands until the end of the year**. |
| Culture and power | Flat, fast, engineer-led. The word governance is neutral — it simply has not been used. Real leverage sits with the COO: 340 stores report to them. |
| Ambition | CEO: an assistant for operations managers by year end. Analytics: stop answering the same questions. |

---

The strategy built on this portrait: [tairin-strategy.md](tairin-strategy.md) · [in Russian](tairin-company.md)
