# Frontend / Backend Authority Boundaries

## Frontend owns
- presentation state;
- optimistic UX where safely reversible;
- client-side validation for feedback;
- local view/session preferences;
- interaction orchestration.

## Backend/domain owns
- authorization;
- canonical business invariants;
- authoritative state transition;
- monetary/accounting rules;
- cross-user/tenant constraints;
- persistence integrity;
- audit decisions.

## Duplication rule
Some validation can exist in both layers for UX, but authoritative behavior must have one source of truth.

## Optimistic UI
When used, define rollback/reconciliation if the server rejects the action. Never display a permanent success state before an irreversible server operation is confirmed unless Product SPEC intentionally allows eventual confirmation.
