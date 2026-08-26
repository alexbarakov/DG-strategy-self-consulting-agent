# Visual graph

Rendered from `objects.yaml`. GitHub renders these Mermaid blocks natively.

## Board-level dependency graph

```mermaid
flowchart TB
  subgraph classic["DG Program Guide — classic themes (11_dg_program_themes/)"]
    GS["Getting started<br/>Natural → Common Sense → MVP"]
    FW["DG frameworks<br/>DGI · PwC · your own"]
    RM["Program roadmap<br/>Program Map 3.0, stages 0–5"]
    RO["Roles & operating model"]
    DC["Data catalog 1.0 → 3.0"]
    DQ["Data quality / DQMS"]
    MM["Maturity & metrics · DDI"]
    DM["Domains & Data Mesh"]
    DL["Data literacy"]
    KR["DG Kitchen research"]
  end

  subgraph aiera["AI-era extension (10_ai_era_themes/)"]
    CCL["Certified Core Layer"]
    SL["Semantic Layer"]
    DKB["Domain Knowledge Base"]
    CG["Context Governance"]
    SH["Skills Hub /<br/>agent-skill governance"]
    ARCH["LLM assistant architecture"]
    BCM["BI content management funnel"]
    ONT["Enterprise ontology"]
  end

  GS --> RM
  FW --> RM
  RO --> RM
  MM --> RM
  KR -.->|field evidence| GS

  DQ -->|foundation| CCL
  DM -->|domain map| DKB
  DC -->|metadata SSOT| CG

  BCM -->|"archive + certify"| CCL
  CCL -->|prerequisite| SL
  SL -->|prerequisite| DKB
  CG -->|governs| DKB
  SH -->|distributes| DKB
  ONT -->|skeleton| DKB
  SL -->|"governed route"| ARCH
  CG -->|"loops A–E"| ARCH

  style aiera fill:#e8f7f9,stroke:#2fb9ca
  style classic fill:#f7f7f7,stroke:#808080
```

Reading order for strategy building: bottom of the classic block gives the program skeleton (getting started → roadmap), the AI-era chain is the prerequisite triad `Certified Core Layer → Semantic Layer → Domain Knowledge Base`, wrapped by Context Governance and operated through the LLM assistant architecture.

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
    EL["Eval Loop"] -.->|"accuracy feedback"| VG
  end

  API -->|serves| SHK
```

## Dependency chain (the budget-defense line)

```mermaid
flowchart LR
  A["Certified core"] --> B["Certified metrics"] --> C["Agent accuracy"] --> D["Self-service"]
```
