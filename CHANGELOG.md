# Changelog

## v1.0.1

### Fixed

- Added a mandatory Project Goal and terminal-state contract so task or milestone completion cannot be mistaken for project completion.
- Added an autonomous continuation controller: after each task or milestone, the agent must select the next executable task unless the Project Goal is truly terminal.
- Added the known-remaining-work guard: if the agent can name remaining executable in-scope work, it cannot terminate as complete.
- Added the incomplete-self-awareness trigger for summaries that explicitly acknowledge unfinished work.
- Clarified that "first slice", "earliest incomplete phase", and "next milestone" define ordering only, never the requested delivery boundary.
- Added strict separation between task evidence, milestone evidence, workflow evidence, and release evidence.
- Added blocker classification so local environment limitations cannot stop unrelated implementation work or be promoted automatically to a global blocker.
- Added host-boundary semantics using `CONTINUATION_REQUIRED` for forced turn/token/tool boundaries.
- Added release scope closure and enumeration preservation so multi-industry/multi-channel/multi-role requirements cannot collapse into one representative implementation.

### Added

- `00_GOVERNANCE/07_PROJECT_GOAL_AND_TERMINAL_STATE.md`
- `01_AGENT_RUNTIME/10_AUTONOMOUS_CONTINUATION_CONTROLLER.md`
- `02_SPEC_FACTORY/09_RELEASE_GOAL_AND_SCOPE_CLOSURE.md`
- `06_TEMPLATES/PROJECT_GOAL_TEMPLATE.md`
- `06_TEMPLATES/EXECUTION_STATE_TEMPLATE.md`
- stronger Product SPEC generation requirements for release goals, scope inventories, and continuation state.

### Behavioral change

ForgeSpec OS v1.0.1 treats a successful vertical slice as a transition back into work selection. It is no longer a natural stopping point unless the full requested Project Goal is release-complete.
