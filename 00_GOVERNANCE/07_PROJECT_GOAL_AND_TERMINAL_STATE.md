# Project Goal and Terminal-State Contract

ForgeSpec OS distinguishes **task completion**, **milestone completion**, **release completion**, and **Project Goal completion**. A lower-level success must never be treated as a terminal project state.

## 1. Mandatory Project Goal

Before substantial implementation begins, the main coding agent must create or validate:

`SPEC/<product>/WORKLOG/PROJECT_GOAL.md`

The Project Goal is the machine-oriented execution contract for the active requested delivery. It must be derived from the Product SPEC and current user instruction, not invented independently.

It must contain at least:

- goal ID and title;
- authoritative Product SPEC entrypoint;
- requested release/delivery scope;
- explicit in-scope requirement groups;
- explicit variant/enumeration inventory when the Product SPEC contains multiple industries, channels, roles, editions, modules, integrations, regions, workflows, or other named variants;
- non-goals and deferred scope;
- release gates;
- terminal completion predicate;
- known blockers and whether they are local, scoped, or global;
- current goal state;
- link to the task graph and acceptance/evidence matrix.

## 2. Goal states

Use these goal states:

`ACTIVE -> VERIFYING_RELEASE -> PRODUCTION_READY`

Exceptional state:

`ACTIVE -> BLOCKED_GLOBAL`

`BLOCKED_GLOBAL` is valid only when a real external dependency prevents meaningful progress across the remaining critical path and all unaffected executable work has already been advanced.

A task or milestone being blocked does **not** make the Project Goal `BLOCKED_GLOBAL`.

## 3. Terminal completion predicate

The Project Goal may become `PRODUCTION_READY` only when all of the following are true:

1. every mandatory in-scope requirement is `DONE` with evidence or is explicitly removed by an authoritative scope change;
2. every mandatory named variant/category in the scope inventory has been implemented or explicitly excluded by the Product SPEC/user;
3. all required release gates pass;
4. no release-critical TODO, mock, stub, hardcoded production substitute, skipped verification, or unresolved blocker remains;
5. required migrations, configuration, deployment, rollback, observability, permissions, and operational paths are complete where applicable;
6. release acceptance evidence is reconciled against repository truth.

A passing build, a successful UI render, a set of passing unit tests, or completion of one vertical slice is evidence for part of the goal only.

## 4. Known-remaining-work guard

Before ending an execution session or producing a terminal completion message, the main agent must ask:

> Can I name any remaining in-scope executable task, unverified requirement, missing variant, failed gate, or unresolved release obligation?

If **yes**, the Project Goal is not terminal.

If the remaining work is executable now, the agent must select the next task and continue.

If the remaining work is blocked, the agent must classify the blocker and continue all unaffected work. Only a genuine `BLOCKED_GLOBAL` condition may justify stopping the full execution loop.

## 5. Incomplete-self-awareness trigger

The following type of statement is itself a continuation trigger:

> "X is complete, but A, B, and C remain to be built."

If the agent can state what remains, it has demonstrated that the Project Goal is not complete. It must not treat that statement as a final delivery. It must update state, select the next executable task, and continue.

## 6. Scope enumeration preservation

Named scope lists are contractual data, not prose decoration.

When product intent contains a list such as:

- industries;
- sales channels;
- roles;
- plans/editions;
- integrations;
- modules;
- devices;
- locales;
- workflows;
- deployment targets;

then the Product SPEC and Project Goal must preserve that list in a traceable scope inventory.

An example item does not silently replace the rest of the list. A representative implementation is not full coverage unless the Product SPEC explicitly defines it as representative-only scope.

## 7. "First slice" is ordering, never scope

Phrases such as:

- first slice;
- earliest incomplete phase;
- next milestone;
- first vertical path;
- initial implementation;

specify **execution order** only. They do not redefine the requested delivery boundary.

After a slice or milestone passes its local gate, the agent must transition to the next eligible work item unless the Project Goal is terminal.

## 8. Response boundary is not a stop condition

A model response, progress summary, test report, commit, milestone, or context compression boundary is not inherently a stop condition.

If the host/runtime forces a response before the Project Goal is terminal, the agent must:

1. persist the checkpoint and exact next action;
2. mark status as `CONTINUATION_REQUIRED`, not `DONE` or `PRODUCTION_READY`;
3. avoid language that implies the requested delivery is complete;
4. resume from the recorded next action on the next available execution cycle.

## 9. Scope changes

The Project Goal may shrink or change only through an authoritative user/Product SPEC decision. The coding agent must not silently redefine a large requested release as a smaller milestone because the smaller milestone is easier to finish.

## 10. Bounded completion and anti-scope-inflation

"Do not stop early" does not mean "improve forever." The Project Goal is bounded by the current authoritative release scope.

The agent must not delay `PRODUCTION_READY` by inventing new features, speculative abstractions, endless optimization, or quality work beyond the Product SPEC/release gates. New discoveries that are non-release-blocking should be recorded as backlog/risk items unless the user/Product SPEC promotes them into current scope.
