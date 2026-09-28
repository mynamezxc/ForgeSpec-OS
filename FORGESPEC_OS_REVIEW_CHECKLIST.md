# ForgeSpec OS Review Checklist

Use this checklist when changing the reusable ForgeSpec OS standard itself.

A proposed rule belongs in ForgeSpec OS only when the answer remains strong after the following review:

- Does the rule generalize across materially different products?
- Could it accidentally override Product SPEC behavior, architecture, or domain intent?
- Is it an execution/quality invariant, a default, or a conditional capability profile?
- Is its activation condition explicit?
- Does it improve correctness, continuity, evidence, or production readiness more than it increases bureaucracy?
- Can a coding or verifier agent evaluate compliance objectively?
- Does it avoid forcing unnecessary technology, topology, vendors, or frameworks?
- Does it remain compatible with context compression and deterministic recovery?
- Does it work with scoped subagent delegation and independent verification?
- Does it encourage executable work rather than endless planning?
- Does it avoid repeated expensive full-suite testing without weakening risk coverage?
- Could it create a loop where the agent can never legitimately finish?
- Does it preserve explicit user and Product SPEC authority?
- Can the rule be expressed with a clear proof obligation or observable behavior?
- Is the rule already better placed in a Product SPEC, ADR, repository convention, or capability-specific profile?

If the rule fails this review, keep it at the narrowest correct scope instead of promoting it into ForgeSpec OS.

## Skill-system changes
- [ ] New skills are task-scoped and do not become global product requirements.
- [ ] External providers remain replaceable unless a Product SPEC explicitly depends on one.
- [ ] External skill/tool additions include provenance, license, permission/script review, pin/update strategy, and rollback/removal path.
- [ ] Overlapping maker skills are not all activated by default.
- [ ] Security scanning language restricts active testing to owned/explicitly authorized scope.
- [ ] Skill output is evidence/findings, not automatic `DONE` authority.
- [ ] Skill docs stay English and provider-neutral ForgeSpec rules do not copy large third-party copyrighted instruction bodies.
