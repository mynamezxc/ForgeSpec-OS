# ForgeSpec OS v1.0.1

**Production Engineering & Agent Execution Standard**

v1.0.1 focuses on one high-impact agent-control problem: **premature termination after partial success**.

A coding agent can correctly implement a meaningful slice, pass local tests, explicitly recognize that major required capabilities remain, and still end the execution turn as if the natural unit of work were complete. That behavior is incompatible with production end-to-end delivery.

## What changed

### Project Goal is now a first-class execution object

Every substantial implementation must create or validate `WORKLOG/PROJECT_GOAL.md` from the Product SPEC and current user request. The goal records the full release scope, mandatory variants, release gates, terminal completion predicate, blockers, and traceability.

### Task done is not project done

ForgeSpec now distinguishes:

`TASK_DONE != MILESTONE_DONE != RELEASE_DONE != PROJECT_GOAL_DONE`

Passing tests or finishing one vertical slice advances evidence but does not terminate execution while mandatory scope remains.

### Autonomous continuation controller

After each task or milestone the main agent must return to work selection. It may stop only when the Project Goal is production-ready, the user explicitly changes/stops the scope, or a genuine global external blocker prevents further meaningful progress.

### Known-remaining-work guard

If the agent can name executable remaining work, the goal is non-terminal. Statements such as "authentication and offline sync remain" now force continuation rather than serving as a final progress summary.

### Scope enumeration preservation

Explicit lists such as industries, channels, roles, modules, integrations, locales, or deployment targets must be preserved as a traceable scope inventory. A representative example or first implementation cannot silently stand in for the full named list.

### Blocker classification

Local environment limitations and task-scoped blockers no longer justify stopping the whole project when independent work remains. Host-enforced turn/token/tool boundaries are recorded as `CONTINUATION_REQUIRED`, not `DONE`.

## Upgrade impact

Existing Product SPECs remain valid. For stronger continuation guarantees, generate or add:

- `07_DELIVERY/RELEASE_GOAL_AND_SCOPE.md`
- `WORKLOG/PROJECT_GOAL.md`
- `WORKLOG/EXECUTION_STATE.md`

and reconcile their scope against the existing acceptance matrix and task graph.
