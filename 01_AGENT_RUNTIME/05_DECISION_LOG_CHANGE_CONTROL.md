# Decision Log and Change Control

## ADR required when
Create/modify an Architecture Decision Record when a change affects:
- major framework/runtime choice;
- database/storage strategy;
- public API/event contract;
- authentication/authorization model;
- deployment topology;
- cross-module shared abstraction;
- irreversible migration;
- significant third-party dependency.

## ADR format
- Context
- Decision
- Alternatives considered
- Why chosen
- Consequences
- Compatibility/migration impact
- Reversal cost
- Verification

## Scope control
New ideas discovered during implementation go to backlog unless they are required for correctness, security, operability or an explicit acceptance criterion.

## No opportunistic rewrite
Do not refactor unrelated subsystems while implementing a feature unless there is a clear blocking reason. If refactoring is necessary, isolate it, preserve behavior and test it separately.
