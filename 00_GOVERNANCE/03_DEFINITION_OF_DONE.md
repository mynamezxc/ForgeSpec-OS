# Definition of Done (DoD)

A task/feature is `DONE` only if every applicable item is satisfied.

## Requirements
- Acceptance criteria are explicit.
- Edge cases and error states are identified.
- No required behavior is represented by placeholder text, static fake data or hidden stub.

## Implementation
- End-to-end path exists across all required layers.
- Business rules are implemented at the correct authoritative layer, not duplicated randomly in UI and backend.
- Data validation and authorization are server-side where applicable.
- No debug-only bypass remains enabled.
- Configuration is externalized where environment-specific.

## Compatibility and migration
- Existing consumers remain compatible or migration/versioning is documented.
- Schema changes have forward migration; rollback/restore plan exists where destructive.
- Seed/demo data is separated from production data.

## Quality
- Required unit/integration/contract/E2E tests pass.
- Failure-path tests exist for risky flows.
- Static analysis/type/lint/build checks pass as applicable.
- UI states include loading, empty, error, partial and permission-denied where relevant.

## Operations
- Useful logs/metrics/traces exist for important runtime actions.
- Secrets are not committed or leaked to client/runtime logs.
- Deployment instructions and required environment variables are known.
- Rollback path is defined for release-affecting work.

## Evidence
The completion record names concrete evidence: tests, commands, screenshots where useful, API responses, migration results, benchmark results or review artifacts.

A claim such as “looks good” is not evidence.
