# Production Readiness Gates

Use risk-based gates. Not every project needs every technology, but every applicable risk must be addressed.

## Gate 0 — Project Goal closure
- `WORKLOG/PROJECT_GOAL.md` matches the current Product SPEC and user-requested delivery.
- Every release-blocking scope item/variant is complete with evidence or explicitly removed by authoritative scope change.
- No executable mandatory work remains.
- No release-critical check remains skipped merely because the local environment could not run it.
- `WORKLOG/EXECUTION_STATE.md` is no longer `CONTINUE` or `CONTINUATION_REQUIRED`.

## Gate A — Functional completeness
- Requirement coverage matrix has no critical gaps.
- Key user journeys work end-to-end with real persistence/integration.
- Admin/operator journeys required by the Product SPEC are implemented.

## Gate B — Reliability
- Retry, timeout, idempotency and concurrency behavior are defined where distributed/network operations exist.
- Error recovery is tested.
- Background work survives restart if persistence is required.

## Gate C — Security and access
- Authentication and authorization boundaries are explicit.
- Privileged actions are auditable.
- Input, upload, serialization and injection surfaces are reviewed.
- Secrets/configuration handling is production-safe.

## Gate D — Data safety
- Migration tested against realistic dataset shape/volume.
- Backup/restore procedure is known for critical state.
- Destructive operations require explicit protections.

## Gate E — Performance and cost
- Representative benchmark scenarios defined.
- p50/p95/p99 or equivalent are measured where latency matters.
- Load/volume limits and cost-sensitive paths are understood.

## Gate F — UX and accessibility
- Responsive behavior, keyboard/focus, errors, empty states and destructive confirmations are validated when relevant.
- UI does not expose internal implementation errors to end users.

## Gate G — Operations
- Health/readiness behavior is defined.
- Logs are actionable and contain correlation/context.
- Deployment, rollback and incident diagnostics are documented.

## Release verdict
Use one of:
- `NOT_RELEASE_READY`
- `RELEASE_CANDIDATE`
- `PRODUCTION_READY`

Never infer `PRODUCTION_READY` from percentage complete alone.
