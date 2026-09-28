# SPEC Freeze and Change Management

A Product SPEC is expected to evolve, but implementation cannot remain stable if the target changes silently.

## Baseline freeze
Before major implementation, baseline a Product SPEC version containing:
- current requirements;
- domain invariants;
- critical contracts;
- acceptance criteria;
- selected architecture/ADRs;
- release scope.

## Change classification
- **Clarification:** no behavior/scope change.
- **Compatible enhancement:** additive behavior with limited impact.
- **Breaking behavior change:** changes contract/workflow/data semantics.
- **Scope change:** adds/removes planned capability.

## Change procedure
For material changes:
1. identify affected requirement IDs;
2. update workflow/domain/contracts first;
3. identify code/tests/migrations affected;
4. update delivery plan;
5. record compatibility/rollback implications;
6. continue implementation from the new baseline.

Do not let implementation drift become undocumented specification.
