# Runbook, Support and Admin Requirements

Production readiness includes the people operating the product.

## Runbook should answer
- How do I know the service is healthy?
- How do I inspect version/config?
- Where are logs/metrics?
- How do I diagnose a failed job/sync/provider?
- How do I retry/replay safely?
- How do I disable a failing integration/feature?
- How do I restore/rollback?
- Which actions are dangerous?

## Admin capability
Where Product SPEC requires admin, distinguish product configuration from infrastructure operations. Privileged actions need authorization, confirmation and auditability appropriate to risk.

## Support diagnostics
Expose stable IDs/timestamps/version info that users/support can provide without exposing secrets.
