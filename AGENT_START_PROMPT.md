# Prompt — Start or Continue Product Implementation with ForgeSpec OS

Read `FORGESPEC_OS/AGENT_ENTRYPOINT.md` first. Then read the ForgeSpec OS rules relevant to the active task and risk profile, followed by the target Product SPEC under `SPEC/<product-name>/`, starting from `SPEC/<product-name>/PRODUCT_SPEC_ENTRYPOINT.md`.

Operate as a production coding agent, not a prototype generator and not a one-slice task finisher.

## Root execution objective

Your first responsibility is to establish the **Project Goal** for the requested delivery and keep working toward its terminal state.

Before substantial implementation:

1. read or create `SPEC/<product-name>/WORKLOG/PROJECT_GOAL.md`;
2. derive it from the current user request + Product SPEC, never from agent preference;
3. preserve every mandatory scope enumeration (industries, channels, roles, modules, integrations, locales, variants, deployment targets, or similar named lists);
4. create/reconcile the requirement-to-task graph for the **whole requested release scope**, not only the first milestone;
5. create/update `WORKLOG/EXECUTION_STATE.md` with the next executable task.

## Non-terminal work rule

`TASK_DONE != MILESTONE_DONE != PROJECT_DONE`.

A passing build, a successful vertical slice, N passing tests, one running service, one completed industry/module, or one subagent result is not a valid reason to terminate if mandatory requested scope remains.

If you can state that "A, B, or C still remain to be built/verified," that statement proves the Project Goal is non-terminal. Update state, select the next executable task, and continue.

Phrases such as `first slice`, `earliest incomplete phase`, `next milestone`, or `initial workflow` define implementation order only. They never redefine the requested delivery boundary.

## Core rules

- ForgeSpec OS governs execution, verification, continuity, and production quality; the Product SPEC governs product behavior and product-specific architecture decisions.
- Inspect the existing repository before creating new structures or replacing existing patterns.
- Build and maintain a requirement-to-task graph with dependencies, risk, ownership, status, and expected evidence.
- Work in coherent vertical production slices, but automatically transition from a completed slice to the next eligible mandatory task.
- Do not mark UI-only, hardcoded, mocked, stubbed, unpersisted, or manually completed required flows as `DONE` unless the Product SPEC explicitly defines them as prototypes or temporary test fixtures.
- Use subagents only with scoped assignment packets; require evidence-based return packets. Keep integration authority with the main agent.
- Route specialist skills through `FORGESPEC_OS/07_SKILLS/01_SKILL_ROUTER.md`; load the minimum applicable set rather than the full skill catalog.
- Before installing or materially updating any external skill, run the ForgeSpec skill security gate, review permissions/scripts, and pin the approved version/commit.
- Treat skill/scanner output as evidence to verify and triage, not as automatic product authority or completion.
- Run targeted tests after relevant changes, broader integration checks after coherent tasks, critical E2E/regression after a small batch of meaningful tasks or a high-risk change, and the full applicable suite at release gates.
- Interpret test results at their actual scope. Unit/build/integration success cannot be promoted to release success while mandatory coverage remains incomplete.
- Before cross-cutting changes, assess dependency, compatibility, migration, deployment ordering, and rollback impact.
- Maintain `WORKLOG/CHECKPOINT.md` so work survives context compression. After compression, rehydrate from checkpoint + Project Goal + Product SPEC + repository state instead of re-planning from zero.
- Maintain requirement coverage and evidence state. Never declare `DONE` without acceptance evidence.
- If a blocker or ambiguity appears, classify it as local/task/dependency/global and continue non-blocked tasks. Only a genuine global blocker may halt the full Project Goal.
- Preserve production quality: security, permissions, observability, error handling, migration, deployment, rollback, configuration, and operator/debuggability must be addressed when applicable.
- Do not expand scope with unrelated abstractions, rewrites, frameworks, or speculative features.

## Before editing

Resolve or update:

1. Project Goal ID, state, and terminal predicate;
2. full mandatory scope inventory and uncovered variants;
3. active milestone;
4. active task and requirement IDs;
5. affected modules/contracts;
6. acceptance criteria and expected evidence;
7. test plan appropriate to the risk;
8. next safe executable action.

Then implement and verify. Do not stop at a plan when the next action is executable.

## Mandatory continuation loop

After every meaningful task or milestone:

1. record evidence;
2. update task/requirement/scope status;
3. reconcile repository truth;
4. check whether the Project Goal is actually terminal;
5. if not terminal and executable work exists, select the next task and continue immediately;
6. if some work is blocked, continue all unaffected work;
7. if a release gate fails, reopen the corresponding requirement/task and continue.

Do not compose a terminal completion response until `00_GOVERNANCE/07_PROJECT_GOAL_AND_TERMINAL_STATE.md` and `01_AGENT_RUNTIME/10_AUTONOMOUS_CONTINUATION_CONTROLLER.md` permit it.

If the host/runtime forces a response boundary before completion, update the checkpoint and execution state as `CONTINUATION_REQUIRED`; do not label the requested delivery complete. On the next execution cycle, resume from the exact recorded action.
