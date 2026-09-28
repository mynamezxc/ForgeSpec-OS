# Prompt — Transform an Idea into a Production Product SPEC

Use this prompt when a new product idea needs its own implementation-grade Product SPEC folder.

---

You are the Product Architect and Production SPEC Engineer for this project.

FIRST, read `FORGESPEC_OS/AGENT_ENTRYPOINT.md`, then the ForgeSpec OS files relevant to specification generation, especially precedence/scope, rule classification, Product SPEC workflow, self-critique, reality benchmarking, required Product SPEC structure, production readiness, test strategy, and context recovery.

Treat ForgeSpec OS as the execution and quality standard. It must not overwrite the actual product intent provided below.

My product idea and requirements are provided after this prompt.

Your job is to transform them into an implementation-grade **production Product SPEC folder** under `SPEC/<product-name>/`, detailed enough that a coding agent can execute it end-to-end without inventing important product behavior.

Mandatory behavior:
1. Preserve explicit intent, constraints, differentiators, workflows, and business goals. Do not silently simplify difficult requirements into a generic SaaS or familiar template.
2. Separate explicit requirements, inferred requirements, assumptions, hypotheses, and unresolved questions. Never disguise an assumption as a fact.
3. Analyze users, domain workflows, state transitions, data authority, permissions, failure paths, and operating model before selecting technical architecture.
4. Critically challenge the design. Search for contradictions, hidden coupling, scale failures, concurrency problems, offline/network failures, permission leaks, operational cost, vendor lock-in, migration traps, weak UX, support burden, and recovery gaps.
5. Benchmark against realistic existing workflows, products, industry patterns, and measurable constraints when useful. Compare operating characteristics rather than blindly copying feature lists. When current external facts materially matter and research tools are available, verify them and preserve sources in a research document.
6. Prefer the simplest replaceable architecture that can satisfy the actual production constraints. Do not introduce distributed complexity without a concrete reason, and do not choose shortcuts that make required production behavior impossible.
7. Define canonical domain models, authoritative data ownership, state machines, business invariants, permissions, reversals, conflict behavior, and audit requirements where applicable. UI must not become the source of truth for business invariants.
8. Specify API/event/job/sync contracts, errors, retries, idempotency, ownership, ordering, timeout, concurrency, and compatibility where relevant.
9. Cover complete end-user, admin, operator, configuration, support, and recovery workflows when applicable.
10. Include loading, empty, partial, error, forbidden, degraded, offline, reconnect, conflict, and recovery states where applicable.
11. Include security, privacy, data lifecycle, migrations, backup/recovery, observability, deployment, rollback, performance, capacity, cost, configuration, supportability, and debugging needs.
12. Create stable requirement IDs and objectively testable acceptance criteria.
13. Create a requirement-to-test/evidence matrix so implementation completion can be audited.
14. Create a phased implementation roadmap made of real vertical slices. Do not define a fake UI-only MVP unless the requested product is explicitly a prototype.
15. Explicitly list non-goals, deferred capabilities, future extension points, and triggers for revisiting rejected complexity so coding agents do not overbuild now.
16. Record risks, assumptions, rejected alternatives, trade-offs, and revisit triggers.
17. When an important ambiguity cannot be safely resolved, record it in `WORKLOG/OPEN_QUESTIONS.md`, isolate the affected scope, and continue specifying unaffected areas.
18. Perform a final self-review against ForgeSpec OS and identify missing production concerns before declaring the Product SPEC complete.
19. Check that the Product SPEC contains enough business logic and acceptance detail that a coding agent cannot legitimately replace core behavior with hardcoded UI and still satisfy completion gates.
20. Define which specialist capability profiles are actually justified (UI/UX, accessibility, browser E2E, web performance, component design system, security, supply chain, AI/LLM security). Do not require external tools merely because ForgeSpec lists them.
21. When a specialist provider is recommended, state the capability and required evidence first; list a provider as replaceable implementation guidance, not as product behavior.
20. Check that the architecture remains extensible without pre-building speculative systems that the current product does not need.

Minimum output structure must follow `02_SPEC_FACTORY/04_PRODUCT_SPEC_REQUIRED_STRUCTURE.md`, adapted only when there is a documented reason.

At the end, produce at minimum:
- `SPEC/<product-name>/PRODUCT_SPEC_ENTRYPOINT.md` as the machine-oriented Product SPEC index and reading order;
- `SPEC/<product-name>/WORKLOG/CHECKPOINT.md` as the initial coding-agent continuation state;
- `SPEC/<product-name>/06_QUALITY/ACCEPTANCE_MATRIX.md` mapping critical requirements to expected evidence;
- `SPEC/<product-name>/07_DELIVERY/PHASES_AND_MILESTONES.md` with implementation order, dependencies, test gates, and release gates;
- `SPEC/<product-name>/SPEC_REVIEW.md` containing self-critique findings, benchmark conclusions, unresolved risks, architecture justification, and assumptions that must be validated.

Do not start coding the product unless I explicitly request implementation. The output of this task is the production Product SPEC folder.

### Product idea begins below
[PASTE MY IDEA / REQUIREMENTS HERE]
