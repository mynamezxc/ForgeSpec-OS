# Autonomous Continuation Controller

This protocol converts ForgeSpec OS stop rules into an executable control loop.

## 1. Purpose

A common coding-agent failure is **false termination after partial success**:

1. inspect the Product SPEC;
2. implement one valid slice;
3. run local tests;
4. correctly identify substantial remaining work;
5. summarize progress;
6. stop anyway.

ForgeSpec OS v1.0.1 treats step 6 as a control-flow defect unless a valid terminal condition exists.

## 2. Main execution loop

The main agent should behave conceptually as follows:

```text
rehydrate()
ensure_project_goal()
reconcile_scope_inventory()
build_or_refresh_task_graph()

while ProjectGoal.state == ACTIVE:
    reconcile_repository_truth()
    candidate = select_next_executable_task()

    if candidate exists:
        implement(candidate)
        verify(candidate)
        record_evidence(candidate)
        update_task_graph()
        update_checkpoint()
        run_due_batch_gates_if_needed()
        continue

    classify_remaining_work()

    if all_mandatory_scope_complete_and_release_checks_due:
        ProjectGoal.state = VERIFYING_RELEASE
        run_release_gates()
        if gates_pass_and_evidence_closes_scope:
            ProjectGoal.state = PRODUCTION_READY
            break
        else:
            reopen_failed_requirements_as_tasks()
            ProjectGoal.state = ACTIVE
            continue

    if genuine_global_blocker_exists_and_no_unaffected_work_remains:
        ProjectGoal.state = BLOCKED_GLOBAL
        persist_blocker_packet()
        break

    repair_task_graph_or_scope_mapping()
```

The key invariant is: **task completion transitions back into work selection, not into conversation termination.**

## 3. Next-task selection order

Prefer the next task that:

1. unblocks the most mandatory downstream scope;
2. closes a critical end-to-end path;
3. validates a high-risk architecture or business assumption;
4. completes an already-started coherent feature;
5. resolves a failed release gate;
6. advances uncovered mandatory variants in the scope inventory;
7. reduces critical uncertainty without triggering speculative redesign.

Do not repeatedly select cosmetic work while core required flows remain incomplete.

## 4. Post-task continuation gate

After every meaningful task, run this gate before composing a final-style response:

- Is the Project Goal `PRODUCTION_READY`?
- Did the user explicitly stop/change scope?
- Is there a genuine `BLOCKED_GLOBAL` condition?

If all answers are **no**, do not terminate the execution loop. Select the next task.

## 5. Post-milestone continuation gate

A milestone passing its local tests means only:

`MILESTONE_DONE`

It does not imply:

`PROJECT_DONE`

After milestone verification:

1. reconcile requirement coverage;
2. select the next incomplete mandatory milestone/task;
3. continue automatically.

## 6. Test-result interpretation

Passing tests must be interpreted at the correct scope.

Examples:

- unit tests passing => local implementation evidence;
- frontend production build passing => build evidence;
- integration tests passing => contract evidence;
- critical E2E passing => workflow evidence;
- release suite passing + complete acceptance matrix => release evidence.

Never promote a lower-level test result into a release completion verdict while mandatory Product SPEC scope remains incomplete.

## 7. Blocker classification

Classify blockers as:

- `LOCAL_ENVIRONMENT`: current machine/tooling limitation;
- `TASK_SCOPED`: affects one task or subsystem;
- `DEPENDENCY_SCOPED`: waiting on one external dependency but other work can continue;
- `GLOBAL_EXTERNAL`: prevents safe progress across the remaining critical path.

Only `GLOBAL_EXTERNAL` can move the Project Goal to `BLOCKED_GLOBAL`.

Before classifying a blocker as global, evaluate safe alternatives such as another existing test layer, CI, a containerized dependency, a repository-provided harness, a deterministic fixture, or progressing independent tasks. Do not weaken required evidence merely to bypass a blocker.

## 8. Host-enforced boundaries

Some coding-agent hosts impose turn, token, execution, or tool limits. These are execution boundaries, not proof of completion.

When such a boundary is reached:

- checkpoint exact state;
- write the next safe executable action;
- keep Project Goal state non-terminal;
- emit `CONTINUATION_REQUIRED`;
- on next invocation, resume immediately instead of restarting planning.

## 9. No ceremonial progress stop

Do not stop merely to announce:

- a first slice is implemented;
- N tests pass;
- the frontend builds;
- one service starts;
- one subagent finished;
- architecture scaffolding exists;
- one industry/channel/role variant works;
- "the rest remains to be built."

Progress reporting may occur at natural boundaries, but reporting does not replace continuation.

## 10. Completion audit

Before setting `PRODUCTION_READY`, the agent must reconcile:

- Project Goal scope inventory;
- requirement-to-task graph;
- acceptance matrix;
- evidence ledger;
- release gates;
- skipped/failed tests;
- unresolved blockers;
- TODO/FIXME/stub/mock/hardcode scan in required scope;
- operational readiness.

Any unexplained gap reopens execution.
