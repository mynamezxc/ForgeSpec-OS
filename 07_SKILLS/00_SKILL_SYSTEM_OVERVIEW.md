# ForgeSpec Skill System Overview

ForgeSpec OS uses skills as **task-scoped capability modules**, not as global prompt inflation.

The skill layer exists to improve specialist execution while preserving the central ForgeSpec contract:

- the Product SPEC defines product intent, behavior, constraints, and product-specific design authority;
- ForgeSpec OS defines execution, verification, evidence, continuity, and production discipline;
- skills provide focused methods, tools, checklists, and review lenses for a specific task;
- no skill may silently expand product scope, replace a Product SPEC decision, weaken a release gate, or declare completion by itself.

## Core principles

1. **Route, do not preload.** Load only skills justified by the current task, risk, or acceptance criteria.
2. **Separate maker and checker when useful.** A design-generation skill should not be the only authority reviewing its own output.
3. **Prefer evidence-producing skills.** Browser traces, test reports, accessibility results, security findings, and measured performance are more valuable than prose-only confidence.
4. **Keep tool choice conditional.** A Product SPEC may choose another stack. ForgeSpec defines capability expectations, not mandatory vendors.
5. **External skills are untrusted dependencies.** Review provenance, scripts, permissions, network behavior, and version before use.
6. **Pin for reproducibility.** Do not let an unattended `latest` update change agent behavior during a milestone or release candidate.
7. **Skill output is advisory until verified.** The main agent or assigned verifier owns acceptance.
8. **Do not create circular review loops.** Use bounded passes and an explicit exit condition.

## Skill layers

```text
Task / requirement
      |
      v
ForgeSpec Skill Router
      |
      +--> ForgeSpec-owned orchestration skill
      |
      +--> optional external specialist skill/tool
      |
      +--> evidence-producing runtime tool
      |
      v
Artifact / finding / measurement
      |
      v
Independent verification + Product SPEC acceptance criteria
      |
      v
Evidence ledger / task state
```

## Provider-neutral design

ForgeSpec-owned skills under `07_SKILLS/skills/` are portable routing and verification contracts. External repositories listed in `02_CURATED_GITHUB_SKILLS.md` are optional providers.

A provider may be replaced when:

- the product stack is incompatible;
- licensing or policy conflicts exist;
- the provider becomes unmaintained or compromised;
- another tool produces stronger evidence at lower cost;
- the Product SPEC explicitly chooses another workflow.

## Activation

Read `01_SKILL_ROUTER.md`. Skills are activated from current task signals, not because the repository contains them.

## Completion

A skill run can produce one of the following:

- evidence that satisfies an acceptance criterion;
- a finding that creates a new task or blocks a gate;
- a recommendation that requires explicit adoption before it becomes implementation scope;
- an inconclusive result that must be recorded as such.

A skill run cannot directly set a product requirement to `DONE` without the required ForgeSpec evidence path.
