# Configuration, Feature Flags and Environment Rules

## Configuration classes
Separate:
- build-time constants;
- deploy-time environment config;
- secrets;
- tenant/admin settings;
- user preferences;
- feature flags.

Do not mix them in one untyped settings blob.

## Validation
Fail early with clear diagnostics when mandatory configuration is missing/invalid.

## Feature flags
Flags should have owner, purpose, default, rollout scope and removal trigger. Avoid permanent flags that create untested combinatorial states.

## Secrets
Never expose server secrets through client bundles, public logs, debug pages or generated fixtures.
