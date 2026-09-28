# Skill Evidence and Handoff Contract

Every significant skill invocation must return an inspectable result.

## Minimum return packet

- skill/provider and pinned version when external;
- task/requirement IDs;
- exact target scope;
- inputs/environment relevant to reproducibility;
- commands/tools executed;
- findings or produced artifacts;
- severity/priority with rationale;
- false-positive or uncertainty notes;
- files/screens/routes/contracts affected;
- tests/measurements performed;
- evidence locations;
- unresolved risks;
- recommended next executable action.

## UI/UX evidence

Use representative rendered states, viewport/device coverage, interaction behavior, and issue-to-fix mapping. A screenshot alone is insufficient for interactive correctness.

## Performance evidence

Record test environment, build mode, cache state, device/network emulation where relevant, repeated samples when variance matters, before/after values, and whether data is lab or field.

## Accessibility evidence

Record automated rule results plus the manual checks required by the target flow. Do not report an accessibility percentage as proof of full conformance.

## Security evidence

Record tool/ruleset/version, target scope, authentication context if any, findings, manual validation, exploitability/reachability, remediation, and residual risk. Never print secrets into the evidence ledger.

## Handoff acceptance

The receiving agent verifies that evidence corresponds to the actual current repository and acceptance criteria. Stale evidence from an earlier diff must be revalidated when the relevant behavior changed.
