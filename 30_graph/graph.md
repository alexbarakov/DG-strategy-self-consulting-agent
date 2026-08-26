# Visual graph

Rendered from `objects.yaml`. GitHub renders these Mermaid blocks natively.
Solid arrows — relations drawn on the board or stated in its texts; dotted arrows — inferred by content logic (kept separate in `objects.yaml` under `inferred_relations`).

## Board-level dependency graph

```mermaid
flowchart TB
  subgraph classic["DG Program Guide — classic themes (11_dg_program_themes/)"]
    MM["Maturity & metrics · DDI"]
    GS["Getting started<br/>Natural → Common Sense → MVP"]
    FW["DG frameworks<br/>DGI · PwC · DAMA · your own"]
    RO["Roles & operating model"]
    RM["Program roadmap<br/>Program Map 3.0, stages 0–5"]
    DC["Data catalog 1.0 → 3.0"]
    DQ["Data quality / DQMS"]
    DM["Domains & Data Mesh"]
    DL["Data literacy"]
    KR["DG Kitchen research<br/>20 tech companies"]
  end

  subgraph aiera["AI-era extension (10_ai_era_themes/)"]
    CCL["Certified Core Layer"]
    SL["Semantic Layer"]
    DKB["Domain Knowledge Base"]
    CG["Context Governance"]
    SH["Skills Hub /<br/>agent-skill governance"]
    ARCH["LLM assistant architecture<br/>7 steps · loops A–E"]
    BCM["BI content management funnel"]
    ONT["Enterprise ontology"]
  end

  %% classic internal (inferred)
  MM -.->|entry gate: 5-of-12 test| GS
  GS -.->|precedes| RM
  FW -.->|structures streams| RM
  RO -.->|staffs stages| RM
  MM -.->|AS-IS baseline| RM
  DC <-.->|status ↔ metadata| DQ
  DM -.->|assigns ownership| RO
  DL -.->|scored dimension L1–L4| MM
  KR -.->|"40% run DG without a program"| GS
  KR -.->|"custodian works, steward fails"| RO
  KR -.->|"catalog as a shield (~70% DataHub)"| DC
  KR -.->|"tools without processes fail"| DQ

  %% classic → AI-era (inferred)
  DQ -.->|certification substance| CCL
  DC -.->|surfaces certified status| CCL
  DC -.->|metadata SSOT| CG
  DM -.->|one pack per domain| DKB
  DM -.->|cross-domain entities first| CCL
  MM -.->|AI-ready score| DKB
  DL -.->|evolves into| SH
  RO -.->|curators for verify gate| CG
  RM -.->|next stage of the map| ARCH

  %% AI-era (board-stated)
  BCM -->|archive + certify| CCL
  CCL -->|prerequisite| SL
  SL -->|prerequisite| DKB
  CG -->|governs| DKB
  SH -->|distributes| DKB
  ONT -->|skeleton| DKB
  ONT -.->|entities & join paths| SL
  BCM -.->|operates in catalog| DC
  SL -->|governed route| ARCH
  CG -->|loops A–E| ARCH
  ARCH -->|modeling queue| SL

  style aiera fill:#e8f7f9,stroke:#2fb9ca
  style classic fill:#f7f7f7,stroke:#808080
```

Reading order for strategy building: maturity self-assessment gates entry → getting started seeds the roadmap, structured by a framework and staffed by roles → the AI-era chain is the prerequisite triad `Certified Core Layer → Semantic Layer → Domain Knowledge Base`, wrapped by Context Governance and operated through the LLM assistant architecture, whose coverage loop feeds work back into the semantic layer.

## Templates → themes

```mermaid
flowchart LR
  subgraph tGS["serve Getting started"]
    T1["Pains analysis"]
    T2["Problems → Solutions canvas"]
    T3["Healthcare business case"]
  end
  subgraph tRM["serve Program roadmap"]
    T4["DG Vision Statement"]
    T5["Goals configurator"]
    T6["Scope configurator<br/>20 goals → 10 streams"]
  end
  subgraph tDM["serve Domains & Mesh"]
    T7["Data Domain Classifier"]
    T8["Domain/Subdomain map"]
    T9["Data Mesh canvas"]
    T10["Data products register"]
  end
  subgraph tMM["serve Maturity & metrics"]
    T11["Data-Driven Index<br/>13 components · 26 metrics"]
    T12["Maturity assessment map"]
    T13["Platform landscape AS-IS"]
  end
  T14["Data teams modeling"] --> RO2["Roles & operating model"]
  T15["Data catalog requirements"] --> DC2["Data catalog"]
  tGS --> GS2["Getting started"]
  tRM --> RM2["Program roadmap"]
  tDM --> DM2["Domains & Data Mesh"]
  tMM --> MM2["Maturity & metrics"]
```

## AI-era component detail

```mermaid
flowchart LR
  subgraph slc["Semantic Layer components"]
    MS["Metric Store"] -->|compiled by| SE["Semantic Engine"]
    SM["Semantic Model"] --- SE
    MT["Metric Tree"] --- MS
    T2S["Text-to-Semantic"] --> SE
    SE --> API["SQL API · REST · MCP"]
    AC["Access & Certification"] --- API
  end

  subgraph cgc["Context Governance components"]
    CM["Context Mining"] -->|yields candidate| CU["Context Unit"]
    CU --> CS["Context Store"]
    VG["Verify Gate"] -->|promotes to verified| TP["Trust Plane"]
    PF["Provenance & Freshness"] --- TP
    TP --> SHK["Serving Hook"]
    EL["Eval Loop"] -.->|accuracy feedback| VG
  end

  API -->|serves| SHK
```

## Runtime and feedback loops (LLM assistant architecture frame)

```mermaid
flowchart TB
  Q["1. Question + who asked"] --> U["2. Understand"] --> CL["3. Clarify<br/>42.5% → 92.5%"] --> R["4. Choose route"]
  R -->|governed| A5a["5a. Assemble<br/>text-to-semantics"]
  R -->|best-effort| A5b["5b. Generate<br/>text-to-SQL"]
  A5a --> P["6. Permissions in query"]
  A5b --> P
  P --> X["7. Execute + answer<br/>number · trust label · provenance"]

  X -->|prod answers & reactions| B["B. Online evals"]
  B --> C["C. Human error review"]
  C -->|cases into golden set| A["A. Offline evals"]
  C --> D["D. Coverage management"]
  D -->|modeling queue| SLx["Semantic layer"]
  E["E. Access & security"] -.- P
```

## Dependency chain (the budget-defense line)

```mermaid
flowchart LR
  A["Certified core"] --> B["Certified metrics"] --> C["Agent accuracy"] --> D["Self-service"]
```
