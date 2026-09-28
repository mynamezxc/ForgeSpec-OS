# Failure Pattern — Partial-Slice False Termination

## Signal

The coding agent completes one legitimate architectural or functional slice, reports passing local tests/builds, explicitly names major remaining required work, and then ends the execution cycle as though the delivered unit were sufficient.

Typical shape:

```text
Implemented: one core/control-plane/tenant/data/UI slice
Verified: local tests + build
Known remaining: authentication, sync, edge/runtime, business workflows, variants, operations
Agent behavior: returns a completion-style summary and stops
```

## Why this happens

### 1. Local task success is mistaken for session success
The prompt defines how to complete a task but does not operationally force transition to the next task.

### 2. "First slice" language becomes an accidental scope boundary
Words intended to establish implementation order are interpreted as the unit the agent is expected to deliver before responding.

### 3. `requested scope` is underspecified at runtime
The agent may interpret the active milestone as the requested scope even when the Product SPEC defines a larger release.

### 4. Tests are not scoped semantically
Passing local tests/builds create a strong completion signal even though they prove only one layer or slice.

### 5. Remaining-work awareness is not connected to control flow
The agent can accurately say "A/B/C remain" without a rule converting that awareness into mandatory continuation.

### 6. No root Goal node exists above milestones/tasks
Without a durable Project Goal, the task graph can terminate locally even though product coverage is incomplete.

### 7. Environment gaps are treated too broadly
A skipped dependency-specific test can be reported as an environment limitation without distinguishing whether it blocks one check, one task, or the full project.

## ForgeSpec countermeasures

- `00_GOVERNANCE/07_PROJECT_GOAL_AND_TERMINAL_STATE.md`
- `01_AGENT_RUNTIME/10_AUTONOMOUS_CONTINUATION_CONTROLLER.md`
- `02_SPEC_FACTORY/09_RELEASE_GOAL_AND_SCOPE_CLOSURE.md`
- mandatory `WORKLOG/PROJECT_GOAL.md`
- mandatory `WORKLOG/EXECUTION_STATE.md`
- known-remaining-work guard
- blocker classification
- scope-enumeration preservation
- evidence scoping by task/workflow/release

## Regression test for agent behavior

Give the agent a Product SPEC with at least three mandatory milestones. Arrange for milestone 1 to pass all local tests while milestones 2 and 3 are executable and incomplete.

Expected behavior:

1. milestone 1 becomes complete;
2. evidence is recorded;
3. Project Goal remains `ACTIVE`;
4. agent selects milestone 2's next executable task;
5. agent continues rather than returning a terminal completion verdict.

Fail the regression if the agent ends with a statement equivalent to "the first slice is complete; the rest remains" while no valid global stop condition exists.
