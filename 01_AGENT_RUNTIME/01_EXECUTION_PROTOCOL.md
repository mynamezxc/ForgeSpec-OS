# Agent Execution Protocol

## Phase 0 — Rehydrate before acting
Before implementation:
1. Read `AGENT_ENTRYPOINT.md` and the ForgeSpec OS rules relevant to the active task and risk.
2. Read the Product SPEC from `SPEC/<product-name>/PRODUCT_SPEC_ENTRYPOINT.md`.
3. Read `07_DELIVERY/RELEASE_GOAL_AND_SCOPE.md` when present.
4. Inspect current repository state instead of assuming an empty project.
5. Read `WORKLOG/PROJECT_GOAL.md`, `WORKLOG/EXECUTION_STATE.md`, and the latest checkpoint/worklog if they exist.
6. Reconcile the Project Goal against the current user instruction, Product SPEC, repository truth, and acceptance matrix.

## Phase 0A — Bootstrap Project Goal
If the Product SPEC is implementation-ready but `WORKLOG/PROJECT_GOAL.md` does not exist, create it before treating any slice as the requested delivery boundary.

The Project Goal must inventory the full mandatory release scope, including explicit named variants such as industries, channels, roles, modules, integrations, editions, locales, devices, or deployment targets.

## Phase 1 — Build the full requirement-to-work graph
Create or refresh a graph covering the full requested release scope with:
- requirement IDs;
- scope/variant IDs;
- task IDs;
- dependencies;
- risk level;
- owner (main agent/subagent);
- expected evidence;
- status.

Prefer vertical slices that result in usable behavior over large layer-by-layer rewrites. A vertical slice controls order, not total scope.

## Phase 2 — Inspect before edit
Before modifying a nontrivial subsystem:
- locate existing implementation and conventions;
- identify reusable utilities/components;
- identify contracts and consumers;
- find relevant tests;
- check whether the requested feature already partially exists.

## Phase 3 — Implement the smallest coherent production slice
A coherent slice generally includes the minimum applicable combination of:
- domain/business logic;
- storage/migration;
- API/event/command contract;
- permission/validation;
- UI/client behavior;
- tests;
- observability.

Do not intentionally leave a required lower layer fake while polishing the top layer.

## Phase 4 — Verify locally and by risk
Run the cheapest high-signal checks first, then broader checks according to `04_QUALITY/01_TEST_STRATEGY_AND_CADENCE.md`.

Record what the test proves. Do not treat local/build evidence as release evidence.

## Phase 5 — Update state
After each meaningful task:
- update task status;
- update requirement and scope-variant coverage;
- record changed files;
- record decisions;
- record tests/evidence;
- record risks/open items;
- update `WORKLOG/EXECUTION_STATE.md`;
- determine the next executable task.

## Phase 6 — Continue automatically
After a task or milestone succeeds, execute the continuation controller in `10_AUTONOMOUS_CONTINUATION_CONTROLLER.md`.

If the Project Goal remains `ACTIVE`, select the next executable task and continue. Do not stop merely to report the completed slice.

## Phase 7 — Milestone verification
At milestone boundaries, run integration/E2E/regression checks sized to the affected surface.

A passing milestone transitions back to Phase 5/6 unless the full Project Goal is ready for release verification.

## Phase 8 — Release verification
Only when mandatory scope appears complete:
1. move the Project Goal to `VERIFYING_RELEASE`;
2. reconcile scope inventory, acceptance matrix, evidence ledger, skipped tests, blockers, TODO/stub/mock scans, operations, deployment, and rollback;
3. run full applicable release gates;
4. if any gate fails, reopen concrete tasks and return the Project Goal to `ACTIVE`;
5. set `PRODUCTION_READY` only after all mandatory evidence closes.

## Phase 9 — Forced execution boundary
If the host/runtime ends the cycle before Project Goal completion:
- checkpoint exact state;
- set continuation state to `CONTINUATION_REQUIRED`;
- record the exact next executable action;
- do not imply project completion.
