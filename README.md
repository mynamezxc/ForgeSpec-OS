<div align="center">

# ⚒️ ForgeSpec OS

### Production Engineering & Agent Execution Standard

**GOAL-DRIVEN · EVIDENCE-GATED · CONTEXT-RESILIENT**

[![Version](https://img.shields.io/badge/version-v1.0.1-2563eb?style=for-the-badge)](#-release-v101)
[![Agent First](https://img.shields.io/badge/agent--first-execution-111827?style=for-the-badge)](#-agent-first-architecture)
[![Production](https://img.shields.io/badge/target-production--ready-16a34a?style=for-the-badge)](#-production-definition-of-done)
[![Evidence](https://img.shields.io/badge/completion-evidence--required-f59e0b?style=for-the-badge)](#-evidence-gated-completion)

**A reusable operating standard for turning product intent into production-grade specifications and driving coding agents from the first task to verified end-to-end delivery.**

<<<<<<< HEAD
[Quick Use](#-quick-use) · [How It Works](#-how-it-works) · [Ratings](#-framework-coverage-rating) · [Benchmarks](#-modeled-efficiency-targets) · [Structure](#-repository-structure)

</div>
=======
**Current version:** 1.0.0
>>>>>>> 650ad77840d2f10290b420a7f604b45b7c0c82c7

---

## 🧭 What is ForgeSpec OS?

ForgeSpec OS is an **agent execution and production engineering standard** for long-running software projects.

It is built around one strict separation of authority:

> **ForgeSpec OS defines HOW engineering work must be executed.**  
> **Product SPEC defines WHAT the product must become.**

That distinction is deliberate. ForgeSpec can enforce engineering discipline without silently changing a product's business model, architecture, workflows, domain rules, or intended user experience.

ForgeSpec OS focuses on the failure modes that repeatedly appear in autonomous coding work:

- stopping after the first valid slice while mandatory scope remains;
- declaring a UI, prototype, mock, or hardcoded path "done";
- losing project state after context compression;
- re-planning instead of continuing execution;
- collapsing a multi-industry or multi-channel requirement into one example implementation;
- spawning subagents without ownership, acceptance criteria, or integration control;
- over-testing tiny changes while still missing release-critical E2E paths;
- ignoring permissions, migrations, rollback, observability, support, and recovery;
- treating a local blocker as a reason to stop unrelated executable work;
- trusting agent confidence instead of requiring verifiable evidence.

ForgeSpec converts those failure modes into **state machines, scope inventories, task graphs, evidence obligations, context checkpoints, specialist skills, quality gates, and release controls**.

---

## ⚡ Quick Use

### 1. Create a production Product SPEC

Give the agent the `FORGESPEC_OS/` folder and your product idea, then use:

```text
FORGESPEC_OS/PROMPT_BUILD_PRODUCT_SPEC.md
```

Expected result:

```text
SPEC/<product-name>/
└── PRODUCT_SPEC_ENTRYPOINT.md
    + domain / architecture / UX / quality / delivery / operations docs
```

### 2. Start the coding agent

The coding agent must begin with:

```text
FORGESPEC_OS/AGENT_ENTRYPOINT.md
```

Then use:

```text
FORGESPEC_OS/AGENT_START_PROMPT.md
```

The agent loads only relevant rules through:

```text
FORGESPEC_OS/AGENT_FILE_INDEX.md
```

### 3. Let the Project Goal control completion

The agent must maintain the full requested delivery as the root state:

```text
PROJECT GOAL
   ↓
Scope inventory
   ↓
Task graph
   ↓
Implement → Verify → Record evidence
   ↓
Mandatory work remains?
   ├─ YES → select next executable task → continue
   └─ NO  → run release gates
                 ↓
          PRODUCTION_READY
```

**A finished task is not a finished project. A finished milestone is not a finished release.**

---

## ⭐ Framework Coverage Rating

> These ratings describe **ForgeSpec's built-in control coverage**, not an independent third-party quality score and not measured runtime performance.

| Area | Coverage | What ForgeSpec provides |
|---|:---:|---|
| 🎯 Goal continuity | ★★★★★ | Project Goal root state, terminal predicate, continuation controller |
| 🧩 Scope preservation | ★★★★★ | Requirement inventory, variant closure, anti-scope-collapse rules |
| 🧠 Context resilience | ★★★★★ | Hot/warm/cold context, checkpoints, compression recovery |
| 🤖 Subagent orchestration | ★★★★★ | Bounded ownership, task packets, return evidence, integration authority |
| ✅ Completion integrity | ★★★★★ | Definition of Done, proof obligations, evidence ledger, release gates |
| 🧪 Test discipline | ★★★★★ | Targeted → integration → E2E → release cadence based on risk |
| 🎨 UI/UX quality routing | ★★★★☆ | Task-scoped design, accessibility, browser and component quality skills |
| 🛡️ Security coverage | ★★★★☆ | SAST/SCA/DAST, supply-chain, skill security, AI/LLM security profiles |
| 📈 Operational readiness | ★★★★★ | Observability, deployment, rollback, migration, incident readiness |
| 📊 Empirical benchmark maturity | ★★★☆☆ | Benchmark protocol and modeled targets; project-specific measurements required |

---

## 🧱 Fixed Logic

These are non-negotiable execution invariants across projects.

### 01 — Product intent remains authoritative

ForgeSpec must not silently replace explicit Product SPEC choices with generic framework preferences.

### 02 — `DONE` requires evidence

Agent confidence, a screenshot, a successful build, or a prose summary is not sufficient proof of production completion.

### 03 — UI-only is not end-to-end

If a feature requires backend logic, persistence, permissions, integrations, jobs, sync, observability, or operational behavior, those paths must exist and be verified.

### 04 — Mocked required behavior is not final behavior

Mocks, fixtures, placeholders, hardcoded records, fake APIs, and temporary fallbacks cannot masquerade as completed production implementation.

### 05 — Task completion always reconciles the Project Goal

```text
TASK_DONE
   ≠
MILESTONE_DONE
   ≠
PROJECT_DONE
```

After a task or milestone completes, the agent returns to **next-task selection** unless the entire Project Goal terminal predicate is satisfied.

### 06 — Known remaining work forces continuation

If the agent can name executable mandatory work that remains, the Project Goal cannot be terminal.

### 07 — Explicit scope lists cannot silently shrink

Industries, roles, channels, modules, integrations, locales, device classes, plans, or other named scope variants must remain individually traceable until closed or explicitly removed from scope.

### 08 — Context compression is state transfer

Compression must preserve the active goal, completed work, decisions, blockers, changed files, evidence state, and next executable action.

### 09 — Blockers are scoped

A local environment or task-specific blocker does not stop unrelated executable work.

### 10 — Release completion belongs to release gates

Only verified scope closure plus applicable release gates can transition the Project Goal to `PRODUCTION_READY`.

---

## 🧠 Agent-First Architecture

`README.md` is intentionally written for GitHub visitors. **Agents do not use this file as their primary instruction source.**

```text
GitHub / Human Entry
        │
        └── README.md

Agent Entry
        │
        ├── AGENT_ENTRYPOINT.md
        │       ↓
        ├── AGENT_FILE_INDEX.md
        │       ↓
        ├── Product SPEC / PRODUCT_SPEC_ENTRYPOINT.md
        │       ↓
        └── AGENT_START_PROMPT.md
                ↓
         Project Goal Controller
                ↓
         Task / Subagent Runtime
                ↓
         Verification + Evidence
                ↓
            Release Gates
```

This separation reduces accidental instruction pollution from public-facing documentation.

---

## 🔄 How It Works

```text
Idea / Existing Product
        │
        ▼
┌───────────────────────────────┐
│  ForgeSpec SPEC Factory       │
│  research · critique ·        │
│  benchmark · requirements     │
└───────────────────────────────┘
        │
        ▼
┌───────────────────────────────┐
│  Product SPEC                 │
│  WHAT must be built           │
└───────────────────────────────┘
        │
        ▼
┌───────────────────────────────┐
│  Project Goal                 │
│  complete requested delivery  │
└───────────────────────────────┘
        │
        ├──────────────┐
        ▼              ▼
┌───────────────┐  ┌───────────────┐
│ Agent Runtime │  │ Governance    │
│ tasks/context │  │ scope/DoD     │
│ subagents     │  │ evidence      │
└───────────────┘  └───────────────┘
        │              │
        └──────┬───────┘
               ▼
┌───────────────────────────────┐
│ Engineering Execution         │
│ domain · data · API · UI      │
│ integration · reliability     │
└───────────────────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ Quality & Verification        │
│ targeted → integration → E2E │
│ security → release evidence  │
└───────────────────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ Production Operations         │
│ deploy · migrate · rollback   │
│ observe · support · recover   │
└───────────────────────────────┘
               │
               ▼
        PRODUCTION_READY
```

---

## 🎯 Project Goal Controller

v1.0.1 strengthens autonomous continuation around a single rule:

> **The current task is an execution unit. The Project Goal is the delivery boundary.**

After every completed task:

```text
Complete task
   ↓
Verify task acceptance criteria
   ↓
Record evidence
   ↓
Reconcile requirement + scope coverage
   ↓
Check release-critical blockers
   ↓
Select next executable mandatory task
   ↓
Continue
```

The agent may stop the full execution loop only when one of these is true:

1. the complete bounded Product SPEC passes applicable release gates;
2. the user explicitly stops, pauses, or changes the requested scope;
3. a genuine global external blocker makes all remaining mandatory work non-executable.

Host-imposed turn, token, or tool boundaries become `CONTINUATION_REQUIRED`, with the exact next executable action persisted before handoff.

---

## 🧠 Context Optimization

ForgeSpec treats context as a limited engineering resource.

### Hot context

Current task, active contracts, relevant files, nearby tests, and immediate dependencies.

### Warm context

Current subsystem architecture, recent decisions, adjacent tasks, shared interfaces.

### Cold context

Completed history, superseded investigation, older evidence, archived decisions.

Before context compression, ForgeSpec preserves durable execution state such as:

```text
WORKLOG/
├── PROJECT_GOAL.md
├── EXECUTION_STATE.md
└── CHECKPOINT.md
```

After compression, recovery follows persisted state and repository truth instead of re-planning the project from scratch.

---

## 🤖 Subagent Orchestration

Subagents are used for **bounded parallel work**, not uncontrolled extra reasoning.

Each subagent receives:

- objective;
- in-scope and non-goal boundaries;
- owned files/modules;
- relevant contracts;
- dependencies;
- expected outputs;
- acceptance criteria;
- required evidence;
- return format.

The main agent retains **integration authority** and does not accept a subagent's self-declared completion without verification.

---

## 🛠️ Specialist Skill System

ForgeSpec uses a task-scoped Skill Router rather than loading every specialist capability into every agent session.

```text
Current task
   ↓
Capability detection
   ↓
Minimum relevant ForgeSpec skill(s)
   ↓
Optional reviewed + pinned external provider
   ↓
Measured / inspectable evidence
   ↓
Independent acceptance
```

Built-in skill profiles cover:

- 🎨 UI/UX and interface craft;
- 🌐 browser/E2E verification;
- ♿ accessibility;
- ⚡ web quality and performance;
- 🧩 component quality;
- 🛡️ application security;
- 📦 software supply chain;
- 🧠 AI/LLM security;
- 🔍 external agent-skill inspection;
- 🚀 release verification.

Curated optional providers include tooling and methodologies from ecosystems such as Playwright, axe-core, Storybook, Lighthouse, Semgrep, OSV-Scanner, Trivy, ZAP, Nuclei, NVIDIA SkillSpector, NVIDIA garak, and specialist UI/design guidance.

**External popularity is not trust.** ForgeSpec requires provenance review, permission/script inspection, controlled activation, version/commit pinning where reproducibility matters, and re-validation after material updates.

---

## 🧪 Testing Strategy

ForgeSpec avoids both extremes: **under-testing** and **running the full suite after every tiny edit**.

```text
Code change
   ↓
Targeted test
   ↓
Coherent task / contract boundary
   ↓
Integration test
   ↓
Meaningful task batch OR high-risk change
   ↓
Critical E2E / regression
   ↓
Release boundary
   ↓
Full applicable release suite
```

High-risk changes can expand verification earlier, including:

- authentication and authorization;
- tenant isolation;
- payments and financial logic;
- migrations and destructive data changes;
- shared contracts;
- concurrency and idempotency;
- synchronization/offline logic;
- security-critical surfaces;
- cross-module platform behavior.

---

## ✅ Production Definition of Done

A release is not considered production-ready merely because it builds or launches.

Applicable completion evidence may include:

- requirement traceability;
- business-invariant verification;
- real integration paths;
- persistence correctness;
- authorization and negative permission tests;
- migration safety;
- error and recovery behavior;
- observability;
- targeted, integration and E2E tests;
- security checks;
- realistic UI states;
- deployment readiness;
- rollback readiness;
- operational runbooks;
- release-gate evidence.

---

## 🔎 Evidence-Gated Completion

For a production workflow, ForgeSpec expects proof across the applicable real path:

```text
Input
  → Validation
  → Authorization
  → Domain Logic
  → Persistence / Integration
  → Result
  → Consumer / UI
  → Observability
```

Not every feature requires every stage, but **every stage required by the Product SPEC must be real, connected, and verifiable**.

---

## 📊 Modeled Efficiency Targets

> The values below are **engineering targets**, not empirical claims. Actual results depend on repository size, model behavior, tool latency, test duration, task separability, and Product SPEC quality. ForgeSpec includes a benchmark protocol so each project can replace these estimates with measured data.

| Workflow dimension | Typical unstructured long-run behavior | ForgeSpec modeled target |
|---|---|---|
| Context rehydration after compression | broad re-read and partial re-planning | ~15–35% of the previous context payload with a healthy checkpoint |
| Re-discovery after compression | repeated subsystem inspection | ~50–80% lower on stable milestones |
| Unnecessary expensive E2E/full-regression runs | frequent or inconsistent | ~60–85% fewer while preserving risk/release gates |
| Parallel throughput for separable work | mostly serial | ~1.3×–2.5× potential task throughput with bounded subagents |
| Critical requirement traceability | ad hoc | target: 100% mapped to evidence or explicit unresolved status |
| Release-critical fake-done detection | agent self-assessment | target: explicit proof obligations for all release-critical flows |
| Context sent to specialist subagents | broad project history | task-scoped context packet only |

Project-specific validation should use:

```text
02_SPEC_FACTORY/03_REALITY_BENCHMARK_PROTOCOL.md
04_QUALITY/04_PERFORMANCE_CAPACITY_AND_COST_VALIDATION.md
```

---

## 🗂️ Repository Structure

```text
FORGESPEC_OS/
├── README.md                         # public GitHub overview
├── AGENT_ENTRYPOINT.md               # mandatory first agent document
├── AGENT_FILE_INDEX.md               # selective rule loading
├── AGENT_START_PROMPT.md             # implementation / continuation prompt
├── PROMPT_BUILD_PRODUCT_SPEC.md      # idea → production Product SPEC
├── CAPABILITY_ACTIVATION_MATRIX.md   # conditional profile activation
├── FORGESPEC_OS_REVIEW_CHECKLIST.md
├── CHANGELOG.md
├── RELEASE_NOTES_v1.0.1.md
├── PACKAGE_MANIFEST.json
├── forgespec-policy.json
│
├── 00_GOVERNANCE/                    # precedence, scope, DoD, release logic
├── 01_AGENT_RUNTIME/                 # tasks, subagents, context, continuation
├── 02_SPEC_FACTORY/                  # product-spec generation and benchmarking
├── 03_ENGINEERING/                   # implementation and architecture discipline
├── 04_QUALITY/                       # tests, evidence, security, validation
├── 05_OPERATIONS/                    # deployment, rollback, observability
├── 06_TEMPLATES/                     # reusable execution artifacts
├── 07_SKILLS/                        # specialist skill routing and security gates
└── 08_FAILURE_PATTERNS/              # regression patterns from real failures
```

Recommended project integration:

```text
/repository
├── FORGESPEC_OS/
├── SPEC/
│   └── <product-name>/
│       └── PRODUCT_SPEC_ENTRYPOINT.md
├── src/
├── tests/
└── tools/
```

---

## 🚫 What ForgeSpec Does Not Dictate

ForgeSpec OS deliberately does **not** force a specific:

<<<<<<< HEAD
- programming language;
- frontend/backend framework;
=======
ForgeSpec OS 1.0.0 adds a task-scoped skill router for UI/UX, browser verification, accessibility, web quality, security, supply-chain review, AI/LLM security, and release verification.

The design deliberately avoids copying a large external skill pack into every agent session. Instead:

```text
Task
  -> ForgeSpec Skill Router
  -> minimum specialist skill(s)
  -> optional pinned GitHub provider/tool
  -> measured / inspectable evidence
  -> independent acceptance
```

Curated upstream providers currently include:

- Anthropic frontend-design, Impeccable, Vercel web-design-guidelines, and Addy Osmani frontend-ui-engineering for complementary UI/design roles;
- Addy Osmani web-quality-skills, Lighthouse, axe-core, Playwright, and Storybook for measured web/component quality;
- Semgrep, OSV-Scanner, Trivy, ZAP, and conditional Nuclei for layered application and supply-chain security;
- NVIDIA SkillSpector for pre-install review of external agent skills;
- NVIDIA garak for conditional AI/LLM security evaluation;
- Superpowers methodology as a reference for pressure-testing skill behavior.

Third-party skills are **not trusted merely because they are popular or on GitHub**. ForgeSpec requires provenance review, permission/script inspection, version pinning for reproducible production work, and re-validation after material updates. See `07_SKILLS/`.

## Production SPEC Factory

`PROMPT_BUILD_PRODUCT_SPEC.md` converts an idea into a separate, implementation-grade Product SPEC without starting product code prematurely.

The SPEC Factory requires the specification agent to:

- preserve explicit product intent and differentiators;
- separate facts, requirements, assumptions, and unresolved questions;
- analyze domain workflows before selecting architecture;
- self-critique for contradictions, scale failures, permissions, concurrency, offline/network behavior, operational cost, migration traps, and UX gaps;
- benchmark against realistic products, workflows, and measurable constraints when useful;
- model canonical states, business rules, permissions, data ownership, APIs, jobs, events, and sync contracts where applicable;
- define objective acceptance criteria and requirement-to-evidence mapping;
- plan real vertical slices rather than a fake UI-only MVP;
- include release gates, observability, rollback, supportability, and production operations.

---

## Context optimization

ForgeSpec OS treats model context as an engineering resource rather than an unlimited scratchpad.

The runtime separates information into **hot**, **warm**, and **cold** context, requires a compact execution checkpoint before compression, and restores work from recorded state instead of re-reading or re-planning the whole project.

Expected benefits include:

- less repeated repository discovery;
- less duplicated architecture reasoning;
- smaller subagent context packets;
- more deterministic continuation after context compression;
- lower risk of silently dropping requirements during long sessions.

---

## Subagent model

Subagents are used for parallelizable, bounded work rather than as unstructured extra reasoning capacity.

Each assignment defines objective, non-goals, ownership boundaries, contracts, expected evidence, and return format. The main agent retains integration authority and verifies the result before accepting it.

This model is intended to improve parallel throughput while reducing merge conflicts, duplicated implementation, and false completion signals.

---

## Testing strategy

ForgeSpec OS uses an adaptive test cadence:

```text
change
  -> targeted test
  -> coherent task / contract boundary
  -> integration test
  -> 3-7 meaningful tasks or high-risk change
  -> critical E2E / regression
  -> release gate
  -> full applicable release suite
```

The exact cadence is risk-sensitive. Authentication, migrations, shared contracts, concurrency, financial logic, permissions, and other high-blast-radius changes can trigger broader verification earlier.

---

## Estimated workflow benchmarks

The values below are **modeled engineering targets, not empirical benchmark claims**. Actual results depend on repository size, model, tool latency, test runtime, task separability, and Product SPEC quality. ForgeSpec OS includes a reality-benchmark protocol so projects can replace these estimates with measured data.

| Workflow dimension | Unstructured long-running agent baseline | ForgeSpec OS modeled target | Why improvement is plausible |
|---|---|---|---|
| Context rehydration after compression | broad re-read / partial re-planning | ~15–35% of prior context payload for a well-maintained checkpoint | hot/warm/cold loading plus explicit checkpoint state |
| Re-discovery/re-planning effort after compression | repeated subsystem inspection | ~50–80% lower on stable milestones | decisions, changed files, tests, blockers, and next action are persisted |
| Expensive E2E/full-regression invocations in multi-task milestones | often run after every change or inconsistently | ~60–85% fewer unnecessary expensive runs while preserving release gates | targeted/integration checks absorb low-risk feedback; broad suites run by batch/risk |
| Parallel throughput for separable work | single-agent serial execution | ~1.3x–2.5x potential task throughput | bounded subagent ownership can parallelize independent work; integration remains centralized |
| Requirement traceability at release | ad hoc | target: 100% of critical requirements mapped to evidence or explicit unresolved status | acceptance matrix + evidence ledger + completion audit |
| Fake-done detection | dependent on agent self-assessment | target: all release-critical flows pass explicit proof obligations | completion state requires real-path evidence rather than prose confidence |
| Context sent to a subagent | broad project history | task-scoped packet only | ownership, contracts, non-goals, and acceptance criteria constrain the payload |

These estimates should be validated per project using `02_SPEC_FACTORY/03_REALITY_BENCHMARK_PROTOCOL.md` and `04_QUALITY/04_PERFORMANCE_CAPACITY_AND_COST_VALIDATION.md`.

---

## What ForgeSpec OS deliberately does not dictate

ForgeSpec OS does not force a specific:

- language or framework;
>>>>>>> 650ad77840d2f10290b420a7f604b45b7c0c82c7
- database;
- cloud provider;
- UI toolkit;
- authentication vendor;
- queue or event broker;
- monolith/microservice architecture;
- AI provider;
- offline-first model;
- hardware platform.

Those decisions belong to the Product SPEC and project constraints.

ForgeSpec activates conditional engineering obligations only when the product requires them.

---

## 🧬 Design Principles

| Principle | Meaning |
|---|---|
| **Goal-driven** | The root Project Goal controls termination, not the current task |
| **Evidence-gated** | Completion requires inspectable proof |
| **Context-resilient** | Long-running work survives compression and handoff |
| **Product-authoritative** | Framework rules cannot silently redesign the product |
| **Risk-adaptive** | Testing and review depth follow blast radius |
| **Task-scoped** | Agents and skills load only relevant context/capabilities |
| **Production-aware** | Migration, rollback, security, observability and operations are first-class |
| **Bounded** | ForgeSpec finishes when the requested Product SPEC is actually complete |

---

## 🚀 Release v1.0.1

v1.0.1 focuses on preventing **false termination** in long-running autonomous coding sessions.

### Highlights

<<<<<<< HEAD
- 🎯 mandatory Project Goal and terminal-state contract;
- 🔁 autonomous post-task and post-milestone continuation controller;
- 🚧 known-remaining-work guard;
- 🧩 explicit scope-enumeration preservation;
- 🧱 task/milestone/workflow/release evidence separation;
- ⛔ blocker classification so local limitations do not stop unrelated work;
- 💾 `CONTINUATION_REQUIRED` semantics for host-imposed execution boundaries;
- 🧪 behavioral regression tests for agent orchestration;
- 🛠️ task-scoped specialist Skill Router;
- 🔐 security gates for optional external agent skills and tools.
=======
## v1.0.0 highlights
>>>>>>> 650ad77840d2f10290b420a7f604b45b7c0c82c7

See [`RELEASE_NOTES_v1.0.1.md`](./RELEASE_NOTES_v1.0.1.md) for the detailed release notes.

---

## 💡 The Core Idea

<div align="center">

### Think deeply where failure is expensive.
### Execute decisively when the next safe action is clear.
### Stop only when the requested goal is proven complete.

**ForgeSpec OS — Goal-Driven · Evidence-Gated · Context-Resilient**

</div>
