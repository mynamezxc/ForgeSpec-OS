# Project Goal

```yaml
goal_id: GOAL-001
title: ""
state: ACTIVE # ACTIVE | VERIFYING_RELEASE | BLOCKED_GLOBAL | PRODUCTION_READY
product_spec_entrypoint: SPEC/<product>/PRODUCT_SPEC_ENTRYPOINT.md
release_goal_source: SPEC/<product>/07_DELIVERY/RELEASE_GOAL_AND_SCOPE.md
created_from_user_request: ""
last_reconciled_at: ""
```

## Terminal outcome

Describe the concrete production-ready outcome that must exist before this goal may become `PRODUCTION_READY`.

## Mandatory scope inventory

| Scope ID | Category | Item | Requirement IDs | Release blocking? | Status | Evidence |
|---|---|---|---|---:|---|---|
| SCOPE-001 |  |  |  | yes | NOT_STARTED |  |

## Shared/core obligations

- [ ]

## Release gates

- [ ] Functional acceptance
- [ ] Critical E2E
- [ ] Security/permission gates as applicable
- [ ] Migration/data gates as applicable
- [ ] Performance/capacity gates as applicable
- [ ] Deployment/rollback/configuration readiness
- [ ] Evidence reconciliation

## Explicit non-goals / deferred scope

- 

## Current blockers

| Blocker | Class | Affected scope | Global? | Mitigation / alternate work |
|---|---|---|---:|---|

## Continuation invariant

If any mandatory scope row or release gate remains incomplete and executable work exists, select the next executable task and continue. Do not terminate merely because a task, slice, build, test batch, or milestone succeeded.
