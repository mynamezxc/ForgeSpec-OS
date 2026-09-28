# Action Bias and Planning Budget

Agents must reason enough to avoid expensive mistakes, then execute. Deep thinking is a tool, not a substitute for building.

## Planning depth by risk
- **Low risk/local change:** inspect affected code, define acceptance, implement, targeted test.
- **Medium/cross-module:** short impact map + contract review + targeted plan.
- **High/irreversible:** ADR/impact analysis, migration/rollback design, independent review before execution.

## Stop-planning trigger
Planning is sufficient when:
- current requirement is understood;
- dependencies and affected interfaces are known;
- major irreversible risks are addressed;
- acceptance evidence is defined;
- the next concrete edit/test is clear.

At that point, implement. Do not continue producing alternative architectures without a new unresolved risk.

## Exploration budget
Time/token-heavy exploration must answer a named uncertainty. Once evidence resolves it, record the decision and leave exploration mode.

## Anti-loop
If the agent repeatedly rewrites plans/checklists without changing code, tests, evidence or resolving a blocker, treat it as a stuck loop. Return to the next executable task.
