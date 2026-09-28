# Anti Fake-Done / Anti-Hardcode Policy

The most common agent failure is implementing a visible shell and treating it as the product.

## Fake-done indicators
A feature is not complete when any required production behavior is replaced by:
- arrays/objects embedded in the UI instead of real data;
- buttons with no authoritative action;
- local-only state when persistence is required;
- dummy authentication/permissions;
- hardcoded success responses;
- TODO endpoints;
- stub provider adapters that always succeed;
- demo-only seed data presented as user data;
- static dashboards with invented metrics;
- disabled validation/error paths;
- frontend-only permission hiding;
- “temporary” bypasses still on the production path.

## Hardcoding distinction
Hardcoding is acceptable when the value is genuinely a product constant (for example a protocol version or mathematically fixed coefficient). It is not acceptable for environment/config/business values expected to vary.

## Proof obligation
Before marking a user-visible feature done, trace the real path:
`UI/input -> validation -> authz -> domain logic -> persistence/integration -> result -> UI/consumer -> observability`.
Only include applicable stages, but every required stage must be real.

## Prototype exception
If the Product SPEC explicitly asks for a prototype, mocks are allowed but must be clearly isolated and labeled. Prototype completion must never be upgraded to production-ready without replacing them.
