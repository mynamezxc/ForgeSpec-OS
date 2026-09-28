# AI / Agent Tooling Capability Profile

Conditional profile for products containing LLMs, agents, tools, MCP/connectors or autonomous workflows.

## Separate control plane and model output
The model may propose actions; authoritative permission/policy code decides what is allowed and which tool arguments are valid.

## Tool contracts
Every tool should define:
- purpose;
- input schema;
- output schema;
- permission scope;
- side effects;
- timeout;
- retry/idempotency;
- audit event;
- error classes.

## Agent state
Persist only state needed for reliable continuation. Distinguish conversation context, durable memory, task state and external source-of-truth data.

## Loop control
Set explicit completion conditions, tool/action budgets and stuck-loop detection. “Do not stop until done” must not mean infinite retries; it means continue useful work until DoD or a real blocker.

## Human approval
High-impact/destructive actions should support approval gates according to Product SPEC.

## Evaluation
Test agent workflows with scenario suites and objective assertions, not only subjective transcript review.
