# Context Compression and Recovery Protocol

Context compression must not destroy project truth.

## Before compression / long-session checkpoint
First persist `WORKLOG/PROJECT_GOAL.md` and `WORKLOG/EXECUTION_STATE.md`, then write or update a durable checkpoint containing:
- current product goal;
- current milestone;
- active task IDs and statuses;
- requirements completed and pending;
- key architecture decisions and reasons;
- files changed recently;
- exact unresolved bugs;
- latest test results;
- known environment facts;
- migrations/configuration changes;
- open risks/blockers;
- next 3–7 executable actions;
- explicit “do not repeat” work;
- explicit “must re-verify” items.

Recommended file: `WORKLOG/CHECKPOINT.md`.

## After compression
The agent must:
1. Read `WORKLOG/PROJECT_GOAL.md`, `WORKLOG/EXECUTION_STATE.md`, then `WORKLOG/CHECKPOINT.md`.
2. Read the target Product SPEC index and active requirement sections.
3. Inspect repository diff/status.
4. Verify that referenced files/tasks still exist.
5. Re-run only cheap high-signal checks necessary to validate the checkpoint.
6. Reconcile that the Project Goal is still non-terminal/terminal correctly.
7. Resume from the recorded next action without waiting for a new planning cycle.

## Anti-regression rules
After compression, do not:
- recreate files that already exist without inspection;
- restart architecture planning from zero;
- reopen completed tasks without evidence of regression;
- forget known failed tests;
- replace a prior approved decision merely because context was summarized.

## Minimum checkpoint quality
A new agent with repository access should be able to continue correctly from the checkpoint without needing the entire historical chat.
