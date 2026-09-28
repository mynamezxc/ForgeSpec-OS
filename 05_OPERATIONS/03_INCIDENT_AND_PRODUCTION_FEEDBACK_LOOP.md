# Incident and Production Feedback Loop

When production defects occur:
1. Preserve evidence/logs/timeline.
2. Mitigate user impact safely.
3. Reproduce with the smallest reliable case.
4. Identify root cause and contributing system conditions.
5. Fix and add regression coverage.
6. Improve observability/runbook if diagnosis was difficult.
7. Feed recurring issues back into Product SPEC or ForgeSpec OS only at the correct scope.

Do not treat a one-off hotfix as complete if the same class of bug remains undetectable and untested.
