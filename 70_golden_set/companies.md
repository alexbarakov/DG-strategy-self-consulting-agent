---
type: eval
purpose: Five invented company profiles that generate the golden-set questions
---

# Five companies

Chosen so that the KB's positions get tested from opposite directions: one company that should probably not run a DG program at all, one that is too advanced for the classic material, one drowning in a program it already has, one whose problem is content rather than data, and one that does not decide in money.

---

## 1. Nordwind Logistics — "do we even need this"

Third-party logistics operator. 12 000 employees, 40 warehouses, 2 800 trucks in four countries. Revenue is asset-heavy and thin-margin; the business model is contracts and utilisation, not data.

**Data estate.** An ERP that runs the company, a WMS per warehouse (three vendors, no common master), telematics from the fleet, and Excel everywhere between them. A DWH exists on paper — one engineer, built for financial reporting. BI is 60 Excel-based reports and one Power BI dashboard the CFO opens.

**People.** No analysts by title. Four "reporting specialists" in finance, two in operations. Nobody owns anything by name; the DWH engineer is the single point of failure and knows it.

**Trigger.** The CEO came back from a conference and told the CIO to "look into data governance". There is no incident, no regulator, no failed project — only the sentence.

**Constraint.** Budget would probably be found if asked for. Nobody has asked. The company has never run a cross-functional program of any kind.

**Why it is in the set.** It is the case where the KB's honest answer is most often "not yet, and here is what to do instead". An agent that sells a program here has failed regardless of how good the program is.

---

## 2. Kestrel Games — "we are already good at data, do not slow us down"

Mobile game studio, 800 people, four live titles, one in soft launch. Product analytics is genuinely excellent: an event pipeline handling billions of events, an in-house experimentation platform, analysts embedded in every squad.

**Data estate.** Modern stack, dbt, a warehouse nobody argues about, ~140 people who write SQL daily. No catalog. No glossary. No semantic layer — every squad hand-codes its own retention definition, and there are at least six of them. Marketing spend attribution disagrees with finance by 8% and always has.

**People.** Engineer-led culture. The phrase "data governance" produces visible irritation; a previous attempt to introduce a stewardship model lasted one quarter. Everyone is smart, everyone is busy, nobody wants a form.

**Trigger.** The CPO wants an internal AI analyst — "ask a question in Slack, get the number" — live in one quarter. A prototype demo answered eleven of fifteen questions correctly, which everyone read as success.

**Constraint.** Speed is the culture. Any proposal that adds a review step to a squad's workflow will be routed around within a month.

**Why it is in the set.** It tests the AI-era half of the KB, the culture objection, and whether the agent can say "your demo number is the problem" without losing the room.

---

## 3. Meridian Bank — "we have data governance and it is not working"

Retail and SME bank, 30 000 employees, one country, heavily regulated. A Data Governance function has existed for four years: a head of DG, four people centrally, and a network of 60 named data stewards across business units.

**Data estate.** A catalog bought two and a half years ago; 40% of critical objects have a description, most of them auto-generated and unread. A business glossary with 900 terms. DQ checks on the regulatory reporting perimeter only. Master data is a live wound: a customer exists in four systems and the "single customer view" project is on its second attempt.

**People.** The 60 stewards are business-unit employees with governance added to their job description and nothing removed from it. Median time actually spent: near zero. The quarterly Data Governance Committee reviews a slide with steward counts and glossary term counts, both rising.

**Trigger.** A new CDO arrives and asks the question nobody has answered in four years: what has this function changed?

**Constraint.** Money exists. Political capital is spent. A second failed relaunch closes the function.

**Why it is in the set.** It tests the roles material, the metric-theatre material, the dead-body material, and the KB's admitted weakness on MDM.

---

## 4. Verdant Retail — "we have too many dashboards and nobody trusts any of them"

Grocery chain, 45 000 employees, 210 stores plus a growing e-commerce arm. Category management is decentralised: eleven category teams, each with its own analysts and its own numbers.

**Data estate.** A solid DWH, a mature BI platform, and 3 100 dashboards of which roughly 400 are opened in a month. Fourteen versions of "margin". The commercial director stopped trusting the weekly pack after two consecutive meetings where two teams brought different sales figures for the same week.

**People.** ~90 analysts across categories, supply chain, e-commerce and finance; a central BI team of 12 that everyone treats as a ticket queue. Self-service was declared two years ago and interpreted by each team as permission to build whatever it wants.

**Trigger.** The CFO wants "one version of the truth" before the next planning cycle and has offered budget for a catalog.

**Constraint.** Category teams are powerful and will resist anything that looks like central control over their numbers.

**Why it is in the set.** It tests content management, certification, the catalog buy decision, self-service and the definitions problem — the parts of the KB with the most field evidence.

---

## 5. Helios Energy — "we do not decide in money"

Regional power distribution utility, 9 000 employees, majority state-owned. Tariffs are set by the regulator; the company does not compete and cannot price.

**Data estate.** SCADA and metering systems from three technology generations, the oldest predating the company's current legal form. An asset register that engineering trusts and finance does not. A DWH built for regulatory submissions. Reporting is a monthly PDF pack assembled semi-manually by four people.

**People.** Nine thousand employees, perhaps fifteen who would call themselves analysts. Data literacy across management is genuinely low — "the report says so" is the end of most discussions. Strong engineering culture in operations, no analytics culture anywhere.

**Trigger.** A new regulatory reporting standard lands in eighteen months. Separately, the board has read about AI and asked what the company is doing about it.

**Constraint.** Cost reduction is not a lever the organisation responds to — savings return to the tariff, not to the budget. Procurement takes nine months. Nobody can be fired for slowness.

**Why it is in the set.** It tests the branch the KB is worst at: an organisation that does not think in ROI, sits on legacy that will not be modified, and needs data literacy before it needs governance.
