# Release Acceptance Checklist

Before release candidate:
- [ ] `WORKLOG/PROJECT_GOAL.md` matches the current user-requested delivery and Product SPEC.
- [ ] Every mandatory scope enumeration item is represented and either complete with evidence or explicitly removed by authoritative scope change.
- [ ] No executable mandatory work remains in `WORKLOG/EXECUTION_STATE.md`.
- [ ] All in-scope critical requirements have acceptance evidence.
- [ ] No production path relies on mocks/stubs.
- [ ] Relevant migrations tested.
- [ ] Permission/auth negative tests pass.
- [ ] Critical E2E journeys pass.
- [ ] Known skipped/failed tests are reviewed.
- [ ] Config/env requirements documented.
- [ ] Secrets absent from source/client bundles/logs.
- [ ] Observability covers critical paths.
- [ ] Backup/restore or data recovery considered where state is critical.
- [ ] Rollback procedure is known.
- [ ] Performance/cost risks evaluated.
- [ ] Support/admin/debug flows work where required.
- [ ] Requirement coverage matrix reviewed.
- [ ] Evidence ledger and Project Goal scope inventory reconcile exactly for release-blocking scope.
- [ ] No lower-level passing test/build result has been promoted into release completion without full release evidence.
- [ ] Open critical/high risks have explicit disposition.

A release candidate can still have known low-severity issues if they are documented and accepted by product scope. Production-ready is not synonymous with “zero bugs.”
