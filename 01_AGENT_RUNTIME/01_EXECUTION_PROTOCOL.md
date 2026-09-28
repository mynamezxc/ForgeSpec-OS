# Agent Execution Protocol

## Phase 0 — Rehydrate before acting
Before implementation:
1. Read `AGENT_ENTRYPOINT.md` and the ForgeSpec OS rules relevant to the active task and risk.
2. Read the Product SPEC from `SPEC/<product-name>/PRODUCT_SPEC_ENTRYPOINT.md`, then the requirements/ADRs relevant to the active milestone.
3. Inspect current repository state instead of assuming an empty project.
4. Read the latest checkpoint/worklog if it exists.
5. Identify the current task and its acceptance criteria.

## Phase 1 — Build a requirement-to-work graph
Create a task graph with:
- requirement IDs;
- task IDs;
- dependencies;
- risk level;
- owner (main agent/subagent);
- expected evidence;
- status.

Prefer vertical slices that result in a usable behavior over large layer-by-layer rewrites.

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

## Phase 5 — Update state
After each meaningful task:
- update status;
- record changed files;
- record decisions;
- record tests/evidence;
- record risks/open items.

## Phase 6 — Milestone verification
At milestone boundaries, run integration/E2E/regression checks sized to the affected surface.

## Phase 7 — Completion review
Before saying done:
- run the completion checklist;
- scan for TODO/FIXME/stubs in required scope;
- compare implementation against acceptance matrix;
- review unresolved failures and skipped tests;
- ensure production operations are addressed.
