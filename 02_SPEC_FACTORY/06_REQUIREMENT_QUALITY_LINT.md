# Requirement Quality Lint

Before a Product SPEC is accepted, lint important requirements for ambiguity.

A requirement is weak if it uses terms such as:
- fast;
- secure;
- user friendly;
- scalable;
- realtime;
- seamless;
- robust;
- optimized;
without measurable or operational meaning.

## Rewrite questions
For each important requirement ask:
- Who triggers it?
- Under what conditions?
- What exact state/result changes?
- What happens on invalid input?
- What happens when dependency/network fails?
- Who can/cannot perform it?
- What persists across refresh/restart?
- What metric defines acceptable performance?
- How will a tester prove it works?

## Traceability lint
Critical requirements must have:
- unique ID;
- acceptance criteria;
- implementation owner/module candidate;
- planned evidence/test type.
