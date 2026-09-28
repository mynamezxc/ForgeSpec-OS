# Status, Stop and Continuation Rules

## Task state machine
`NOT_STARTED -> READY -> IN_PROGRESS -> VERIFYING -> DONE`

Alternative edges:
- any active state -> `BLOCKED`
- `BLOCKED -> READY` after blocker resolved
- `VERIFYING -> IN_PROGRESS` if verification fails
- `DONE -> IN_PROGRESS` only when regression/new approved scope reopens it

## Valid stop conditions
An agent may stop a work session only when at least one is true:
1. The requested scope is `DONE` with evidence.
2. A real external blocker prevents safe progress and all unaffected tasks have been advanced as far as practical.
3. The user explicitly asks to stop/pause/change scope.
4. A safety/security constraint prevents the requested action; safe alternatives and current state are documented.

## Invalid stop reasons
Do not stop because:
- the UI renders;
- code compiles once;
- a mock/demo path works;
- one happy-path test passes;
- the task feels large;
- context is getting long;
- a subagent returned “done” without evidence;
- TODOs remain in required scope;
- required backend/storage/auth/integration is still fake;
- failures are dismissed as “environmental” without diagnosis.

## Partial completion
If the full scope cannot be completed, clearly separate:
- verified completed work;
- implemented but unverified work;
- unimplemented scope;
- blockers;
- next executable steps.
Never rename partial delivery as production-ready.
