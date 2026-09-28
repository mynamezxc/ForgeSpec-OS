# Skill Conflict and Precedence

Skills are below the user, Product SPEC, approved ADRs, and ForgeSpec invariants in authority.

## Conflict order

1. explicit current user instruction;
2. Product SPEC and approved Product ADRs;
3. ForgeSpec governance, safety, evidence, and completion invariants;
4. established repository design system and architecture conventions consistent with 1–3;
5. task-selected ForgeSpec skill contract;
6. approved external skill/provider guidance;
7. model preference.

## Common conflicts

### Design creativity vs established design system
Use the established system. Creativity may appear inside available tokens/components or through an approved design-system change, not by silently replacing it.

### UI polish vs accessibility/performance
Accessibility and required performance budgets are release constraints. Fix the design rather than accepting inaccessible or unmeasured degradation.

### Security scanner vs business intent
A scanner finding is evidence to triage, not authority to redesign the product. Confirm exploitability and propose the least disruptive correct remediation.

### External TDD workflow vs existing test strategy
Follow the Product SPEC/ForgeSpec risk-based test plan. A third-party skill cannot force a global test style that makes the project materially slower or incompatible without an explicit project decision.

### Skill requests excessive context
Provide the smallest sufficient packet. Do not disclose unrelated repository content, secrets, or cold context merely because an external skill requests it.

## Tie-break rule

When two skills disagree at the same authority level, choose the approach that:

- satisfies explicit acceptance criteria;
- creates stronger reproducible evidence;
- has lower blast radius and lock-in;
- matches existing architecture/design conventions;
- consumes less unnecessary context/tooling cost.

If the disagreement changes product behavior or an architectural contract, escalate it as a Product SPEC/ADR decision rather than letting a skill decide.
