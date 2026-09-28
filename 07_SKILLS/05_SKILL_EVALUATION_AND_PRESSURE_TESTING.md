# Skill Evaluation and Pressure Testing

A skill is useful only if it changes agent behavior in the intended direction without unacceptable side effects.

ForgeSpec adopts a RED/GREEN/REFACTOR-style evaluation for high-impact process skills.

## RED — baseline

Run representative scenarios **without** the candidate skill and record actual failure modes, for example:

- UI looks polished but misses empty/error/loading states;
- agent declares completion after a screenshot;
- browser test relies on timing sleeps and flakes;
- security review misses authorization/business-logic abuse;
- design skill overrides the existing product token system;
- scanner results are copied directly into release blockers without triage.

## GREEN — candidate skill enabled

Run the same scenario with the skill. Verify observable behavior improves:

- required state coverage appears;
- evidence is produced;
- acceptance criteria are referenced;
- tool usage stays inside permissions;
- result quality improves without expanding product scope.

## REFACTOR — close loopholes

Add or adjust routing/guardrails for observed rationalizations and side effects. Re-run the scenario.

## Evaluation dimensions

Score with evidence, not intuition:

- task correctness;
- Product SPEC compliance;
- evidence quality;
- context cost;
- tool-call cost;
- latency;
- false-positive/false-negative behavior where measurable;
- overlap/conflict with existing skills;
- security/permission footprint;
- reproducibility across clean sessions;
- recovery after context compression.

## Skill promotion states

`CANDIDATE -> EVALUATING -> APPROVED -> PINNED`

Possible exits:

- `RESTRICTED` — useful only for defined cases;
- `DEPRECATED` — superseded or unsafe;
- `REJECTED` — insufficient value or unacceptable risk.

## Do not benchmark by vibes

Do not claim a skill is better because output appears more sophisticated. Use comparable prompts/tasks, fixed acceptance criteria, and independent review where the choice matters.
