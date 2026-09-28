# Self-Critique and Design Review Protocol

Before freezing a Product SPEC, perform at least three passes.

## Pass 1 — Correctness challenge
Ask whether workflows, state transitions, permissions, calculations and failure handling are internally consistent.

## Pass 2 — Production challenge
Attack the design from:
- scale;
- latency;
- concurrency;
- unreliable network;
- partial dependency failure;
- malformed input;
- schema evolution;
- user error;
- operational recovery;
- cost growth;
- security misuse.

## Pass 3 — Simplicity challenge
For every major subsystem ask:
- Is it required now?
- Can a simpler design satisfy current requirements without blocking future expansion?
- Does it introduce unnecessary third-party dependency?
- Is the abstraction solving a real repeated problem or a hypothetical future one?

## Contradiction table
Document major rejected alternatives:
| Decision | Strongest alternative | Why alternative is attractive | Why rejected now | Revisit trigger |

## Critical rule
Self-critique must improve the design, not cause endless redesign. After major risks are resolved and acceptance criteria are stable, freeze a version and move to implementation. New discoveries use change control.
