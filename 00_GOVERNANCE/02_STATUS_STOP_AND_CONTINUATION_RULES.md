# Status, Stop and Continuation Rules

## Task state machine
`NOT_STARTED -> READY -> IN_PROGRESS -> VERIFYING -> DONE`

Alternative edges:
- any active state -> `BLOCKED`
- `BLOCKED -> READY` after blocker resolved
- `VERIFYING -> IN_PROGRESS` if verification fails
- `DONE -> IN_PROGRESS` only when regression/new approved scope reopens it

Task state is not Project Goal state. See `07_PROJECT_GOAL_AND_TERMINAL_STATE.md`.

## Project Goal state machine

`ACTIVE -> VERIFYING_RELEASE -> PRODUCTION_READY`

Exceptional terminal-for-now state:

`ACTIVE -> BLOCKED_GLOBAL`

## Valid stop conditions
An agent may stop the full Project Goal execution loop only when at least one is true:
1. The **full requested Project Goal** is `PRODUCTION_READY` with reconciled release evidence.
2. A genuine `GLOBAL_EXTERNAL` blocker prevents meaningful progress across the remaining critical path and all unaffected executable tasks have been advanced as far as practical.
3. The user explicitly asks to stop/pause/change scope.
4. A safety/security constraint prevents the requested action; safe alternatives and current state are documented.
5. The host/runtime forcibly ends the execution cycle. In this case the Project Goal remains non-terminal, state is recorded as `CONTINUATION_REQUIRED`, and the next cycle resumes from the checkpoint.

## Invalid stop reasons
Do not stop the Project Goal because:
- the UI renders;
- code compiles once;
- a mock/demo path works;
- one happy-path test passes;
- N local tests pass;
- a frontend production build passes;
- one vertical slice is complete;
- one milestone is complete;
- one industry/channel/role/module variant works while other mandatory variants remain;
- the first or earliest phase is complete;
- the task feels large;
- context is getting long;
- a subagent returned “done” without evidence;
- TODOs remain in required scope;
- required backend/storage/auth/integration is still fake;
- failures are dismissed as “environmental” without diagnosis and blocker classification;
- the agent can explicitly name executable required work that remains.

## Mandatory post-task continuation
When a task reaches `DONE`, the next action is **not** to terminate by default. The main agent must:
1. update evidence and coverage;
2. reconcile Project Goal state;
3. select the next executable mandatory task;
4. continue unless a valid stop condition exists.

## Mandatory post-milestone continuation
A milestone boundary is a verification boundary, not a delivery boundary. After milestone verification, continue to the next incomplete mandatory milestone/task unless the full Project Goal is terminal.

## Known-remaining-work guard
Any final-style statement that lists unfinished in-scope capabilities is proof that completion has not been reached. Convert those remaining items into/against task graph entries and continue.

## Partial completion
If an external execution boundary prevents continuation, clearly separate:
- verified completed work;
- implemented but unverified work;
- unimplemented scope;
- blockers and their class;
- exact next executable step.

Use `CONTINUATION_REQUIRED`, not `PRODUCTION_READY`, unless the release completion predicate is actually satisfied.
