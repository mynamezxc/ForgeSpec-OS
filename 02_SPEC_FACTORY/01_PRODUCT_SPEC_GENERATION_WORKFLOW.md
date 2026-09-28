# Product SPEC Generation Workflow

The goal is to transform an idea into an implementation-grade Product SPEC folder that a coding agent can execute without inventing the product.

## Step 1 — Intent extraction
Capture:
- target users and operators;
- primary jobs-to-be-done;
- business goal and success criteria;
- must-have vs later scope;
- platforms and environments;
- constraints (budget, latency, offline, regulatory, integration, hardware, team);
- explicit non-goals.

## Step 2 — Assumption register
List assumptions by category: user, market, workflow, data, technology, integration, scale, operations. Mark each as:
- confirmed;
- likely;
- uncertain;
- must validate before build.

## Step 3 — Reality benchmark
Compare the proposed product/workflow with real alternatives and common industry patterns. Focus on measurable/product-relevant facts, not imitation. Record:
- baseline workflow today;
- competitor/adjacent patterns;
- performance/scale expectations;
- UX expectations;
- cost drivers;
- integration constraints;
- failure cases found in real deployments.

## Step 4 — Self-critique
Attempt to disprove the initial design:
- What breaks at 10x/100x usage?
- What assumptions are weakest?
- Which feature is expensive but low-value?
- Where is business logic likely to become inconsistent?
- What creates vendor lock-in?
- What becomes hard to migrate?
- What will support/debug teams need that the initial UX ignores?
- What can fail offline, concurrently, partially or across retries?

## Step 5 — Domain model and workflows
Define canonical entities, states, transitions, permissions, invariants and cross-module dependencies before UI details.

## Step 6 — Architecture and contracts
Specify components, data ownership, APIs/events/jobs, integration adapters, error semantics, retries, idempotency, configuration and extensibility.

## Step 7 — Product surfaces
Specify end-user, admin/operator, onboarding, settings, notification, audit, import/export and support surfaces as applicable.

## Step 8 — Production concerns
Specify security, observability, migration, backup, deployment, rollback, performance, cost and data lifecycle.

## Step 9 — Testable acceptance
Every important requirement receives an ID and acceptance criteria. Create a requirement-to-test matrix.

## Step 10 — Phased delivery
Order the roadmap to validate risks early and maintain deployable increments. Do not define “MVP” as fake architecture that must be discarded.
