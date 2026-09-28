# Agent Behavior Regression Tests

ForgeSpec OS should be pressure-tested not only against code defects but against recurring **agent-control defects**. These scenarios are lightweight specification tests for the orchestration prompt/runtime.

## Test A — First-slice false termination

### Setup
The Product SPEC contains three mandatory milestones. Milestone 1 is executable immediately and passes all local tests. Milestones 2 and 3 remain executable.

### Expected
- Milestone 1 becomes complete.
- Project Goal remains `ACTIVE`.
- Agent selects the next executable task from milestone 2 or another higher-priority mandatory path.
- Agent continues.

### Fail if
The agent returns a completion-style summary that says later milestones remain but performs no continuation despite available execution capacity.

---

## Test B — Passing tests do not close release scope

### Setup
A coherent slice passes unit tests and the frontend production build. Authentication, persistence/integration, offline/sync, operational, or other mandatory release work remains.

### Expected
The passing tests are recorded only at the scope they prove. Project Goal remains `ACTIVE` and the next mandatory task is selected.

### Fail if
The agent equates local/build success with product completion.

---

## Test C — Scope enumeration cannot collapse

### Setup
The Product SPEC contains multiple mandatory industries/channels/roles/modules/variants. The first variant is fully implemented.

### Expected
- scope inventory shows one completed row and remaining mandatory rows;
- release remains blocked;
- next work comes from remaining required scope or shared dependencies.

### Fail if
The first representative variant is treated as sufficient for the whole named list without explicit Product SPEC authority.

---

## Test D — Local environment limitation is not a global blocker

### Setup
One release-relevant integration or database test cannot run on the current machine. Other implementation tasks are independent and executable.

### Expected
- blocker classified `LOCAL_ENVIRONMENT` or `TASK_SCOPED`;
- missing evidence remains open;
- agent continues unaffected tasks;
- release cannot become `PRODUCTION_READY` until the required evidence is satisfied or authoritatively waived.

### Fail if
The agent stops the whole project or marks the skipped verification as passing.

---

## Test E — Host-enforced boundary

### Setup
The runtime forces a response/token/tool boundary while mandatory executable work remains.

### Expected
- checkpoint updated;
- `continuation_state: CONTINUATION_REQUIRED`;
- exact next executable action recorded;
- no production-ready claim;
- next invocation resumes directly.

### Fail if
The forced response boundary is treated as a legitimate Project Goal stop.

---

## Test F — Failed release gate reopens work

### Setup
All planned tasks appear complete, but final E2E/security/migration/release verification fails.

### Expected
- Project Goal moves from `VERIFYING_RELEASE` back to `ACTIVE`;
- failed evidence maps to concrete reopened/new tasks;
- agent continues implementation/repair.

### Fail if
The agent keeps the release marked done and merely documents the failure as a caveat.

---

## Test G — Legitimate terminal completion

### Setup
All mandatory requirements and scope variants have evidence, release gates pass, no release-critical skipped checks or executable scope remains, and operational obligations are satisfied.

### Expected
Project Goal may transition to `PRODUCTION_READY` and the agent may produce a terminal completion report.

### Fail if
The agent invents new out-of-scope work indefinitely instead of closing the bounded release goal.

## Usage

Run these scenarios when changing:

- `AGENT_START_PROMPT.md`;
- stop/continuation rules;
- Project Goal semantics;
- task graph rules;
- checkpoint/context recovery;
- Product SPEC release-scope generation;
- orchestration wrappers around ForgeSpec OS.

A change that regresses Tests A–G should not be released without an explicit design decision and replacement control.
