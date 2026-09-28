# Precedence, Scope and Conflict Rules

## 1. Authority order
Use the following priority when interpreting instructions:
1. Explicit current user instruction.
2. Target Product SPEC and approved Product ADRs.
3. ForgeSpec OS process/quality rules.
4. Existing repository conventions that do not conflict with 1–3.
5. Agent preferences/defaults.

## 2. Product decisions versus execution invariants
The ForgeSpec OS must not choose a database, framework, cloud, UI library, auth provider, message broker or architectural pattern unless the Product SPEC is silent and a temporary decision is required to proceed. Such a decision must be recorded as an ADR with alternatives and reversal cost.

ForgeSpec OS invariants include:
- trace requirements to implementation and evidence;
- preserve existing behavior unless change is intended;
- test changes according to risk;
- expose uncertainty rather than invent facts;
- checkpoint before context compression or risky refactor;
- prove completion before declaring done.

## 3. Conflict handling
When two requirements conflict:
1. Do not silently choose.
2. Record the conflict in `WORKLOG/OPEN_QUESTIONS.md` or equivalent.
3. Determine whether the conflict is resolvable from higher-priority instructions.
4. If resolvable, document the decision and affected requirements.
5. If not resolvable and implementation can continue safely, isolate the ambiguity and continue unaffected work.
6. If not resolvable and it blocks correctness, mark only that task `BLOCKED`; do not freeze the entire project.

## 4. No rule pollution
A rule discovered for one product must not be copied into ForgeSpec OS unless it is truly domain-independent. Product-specific rules remain in that Product SPEC.

## 5. Change impact obligation
Before changing a shared model, API, event, permission rule, persistence schema, base component or runtime contract, identify:
- direct callers/consumers;
- dependent modules;
- backward compatibility;
- data migration need;
- test suites impacted;
- deployment ordering;
- rollback implications.
