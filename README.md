# ForgeSpec OS

## Production Engineering & Agent Execution Standard

ForgeSpec OS is a reusable engineering standard for turning product intent into production-grade specifications and for governing AI coding agents through implementation, verification, context compression, subagent coordination, testing, release, and operational readiness.

It is designed around a simple separation of authority:

> **ForgeSpec OS defines how engineering work is executed. Product SPEC defines what the product must become.**

This separation prevents a global agent rulebook from quietly rewriting domain behavior while still enforcing production discipline across very different projects.

**Current version:** 1.0.0

---

## Why ForgeSpec OS exists

Coding agents are very effective at producing code, but long-running software projects expose recurring failure modes:

- declaring completion when only the UI or happy path exists;
- using hardcoded data, mocks, or stubs as if they were production integrations;
- losing critical decisions after context compression;
- repeatedly re-planning work that was already decided;
- spawning subagents without clear ownership or verifiable outputs;
- running either too few tests or the entire expensive suite after every tiny change;
- changing shared contracts without impact analysis;
- ignoring migrations, rollback, observability, permissions, admin flows, or operator recovery;
- optimizing a generic architecture instead of the actual product;
- stopping because a task is large rather than because the requested scope is actually complete.

ForgeSpec OS converts these failure modes into explicit engineering contracts, evidence requirements, task states, checkpoints, verification gates, and recovery procedures.

---

## Core architecture

```text
Product Idea / Existing Product
            |
            v
+------------------------------+
| ForgeSpec SPEC Factory       |
| research / critique /        |
| benchmark / requirements     |
+------------------------------+
            |
            v
+------------------------------+
| Product SPEC                 |
| WHAT must be built           |
+------------------------------+
            |
            +---------------------------+
            |                           |
            v                           v
+------------------------------+   +------------------------------+
| ForgeSpec Agent Runtime      |   | ForgeSpec Governance         |
| task graph / context /       |   | precedence / scope / DoD /   |
| subagents / recovery         |   | stop rules / evidence        |
+------------------------------+   +------------------------------+
            |                           |
            +-------------+-------------+
                          v
              +--------------------------+
              | Engineering Execution    |
              | implementation / data /  |
              | APIs / reliability       |
              +--------------------------+
                          |
                          v
              +--------------------------+
              | Quality & Verification   |
              | targeted -> integration  |
              | -> E2E -> release gate   |
              +--------------------------+
                          |
                          v
              +--------------------------+
              | Production Operations    |
              | deploy / rollback /      |
              | observability / support  |
              +--------------------------+
```

---

## Fixed logic: non-negotiable invariants

These rules are intentionally stable across projects:

1. **Product intent has authority over product design.** ForgeSpec OS must not silently replace explicit Product SPEC choices.
2. **`DONE` requires evidence.** Confidence, screenshots, or an agent statement are not completion proof.
3. **UI-only is not production completion** when backend, persistence, permissions, integration, or operational behavior is required.
4. **Hardcoded, mocked, or stubbed required behavior cannot masquerade as the final implementation.**
5. **Requirements remain traceable** to tasks, implementation, tests, and acceptance evidence.
6. **Context compression is a state transfer, not a reset.** Checkpoint before compression; recover from checkpoint plus repository truth.
7. **Subagents have bounded ownership.** Their output must be independently inspectable and integrated by the main agent.
8. **Testing is risk-based and staged.** Expensive suites are not spammed after every micro-change, and critical checks are not skipped to save time.
9. **Shared changes require blast-radius analysis**, including callers, compatibility, migration, deployment ordering, and rollback.
10. **A blocker is scoped.** One blocked task does not stop unrelated executable work.
11. **Production concerns are part of the product when applicable:** security, observability, configuration, migration, rollback, support, and debug paths.
12. **Global rules cannot pollute product scope.** Conditional capabilities activate only when the Product SPEC requires them.

---

## Agent-first document layout

`README.md` is intentionally public-facing. Agents should start with `AGENT_ENTRYPOINT.md` instead.

```text
FORGESPEC_OS/
├── README.md                         # GitHub/public overview
├── AGENT_ENTRYPOINT.md               # first file an agent reads
├── AGENT_START_PROMPT.md             # coding/continuation prompt
├── PROMPT_BUILD_PRODUCT_SPEC.md      # idea -> production SPEC prompt
├── CAPABILITY_ACTIVATION_MATRIX.md
├── AGENT_FILE_INDEX.md
├── FORGESPEC_OS_REVIEW_CHECKLIST.md
├── forgespec-policy.json
├── 00_GOVERNANCE/
├── 01_AGENT_RUNTIME/
├── 02_SPEC_FACTORY/
├── 03_ENGINEERING/
├── 04_QUALITY/
├── 05_OPERATIONS/
└── 06_TEMPLATES/
```

A repository using ForgeSpec OS can use:

```text
/repo
├── /FORGESPEC_OS
├── /SPEC
│   └── /<product-name>
│       └── PRODUCT_SPEC_ENTRYPOINT.md
├── /src
├── /tests
└── /tools
```

---


## Curated specialist skill ecosystem

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
- database;
- cloud provider;
- UI toolkit;
- authentication vendor;
- queue or event broker;
- monolith/microservice architecture;
- AI provider;
- offline-first architecture;
- hardware stack.

Those are product decisions. ForgeSpec OS only provides conditional engineering profiles and quality obligations when the Product SPEC activates the relevant capability.

---

## Quick start

### Build a new Product SPEC

1. Give the agent the `FORGESPEC_OS` folder.
2. Start from `AGENT_ENTRYPOINT.md`.
3. Use `PROMPT_BUILD_PRODUCT_SPEC.md` with the product idea appended.
4. Review the generated Product SPEC and unresolved decisions.

### Start implementation

1. Keep `FORGESPEC_OS` and the target `/SPEC/<product-name>` in the repository/workspace.
2. Start the coding agent with `AGENT_START_PROMPT.md`.
3. Require the agent to maintain the task graph, checkpoint, requirement coverage, and evidence state throughout execution.
4. Release only after the applicable production gates pass.

---

## Design goal

ForgeSpec OS is not intended to make an agent verbose or bureaucratic. Its goal is the opposite: preserve only the reasoning and process that materially improve correctness, continuity, production readiness, and execution efficiency.

The standard should cause the agent to **think deeply where failure is expensive, act quickly when the next safe action is clear, and prove completion instead of declaring it.**

## v1.0.0 highlights

- task-scoped ForgeSpec Skill Router instead of global skill preloading;
- curated GitHub provider registry for UI/UX, browser/E2E, accessibility, performance, component testing, SAST/SCA/DAST, supply-chain, skill security, and AI/LLM security;
- external skill provenance/security gate and pin/update policy;
- ForgeSpec-owned provider-neutral `SKILL.md` modules with explicit evidence contracts;
- pressure-testing methodology for validating skills themselves;
- Product SPEC template support for a capability-first Skill and Tool Activation Plan.
