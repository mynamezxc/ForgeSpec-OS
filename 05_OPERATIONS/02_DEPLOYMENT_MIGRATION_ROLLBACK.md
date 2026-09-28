# Deployment, Migration and Rollback

## Environment parity
Document supported dev/test/staging/production differences. Avoid logic that only works because of one developer machine.

## Configuration
Environment-specific values belong in configuration/secrets mechanisms, with validation at startup.

## Database/schema deployment
Define ordering where application and schema versions overlap. Prefer backward-compatible expand/migrate/contract strategies for high-availability systems.

## Rollback
A release plan should specify:
- what can be rolled back safely;
- which migrations are irreversible;
- how data created by the new version behaves after rollback;
- how to detect that rollback is needed.

## Deployment verification
After deploy, run smoke checks against critical workflows and health/telemetry, not only “process is running.”
