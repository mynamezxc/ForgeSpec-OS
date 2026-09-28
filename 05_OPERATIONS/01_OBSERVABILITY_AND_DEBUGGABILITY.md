# Observability and Debuggability

## Logs
Use structured, actionable logs with appropriate levels. Include identifiers needed to correlate a request/job/device/sync session while excluding secrets and unnecessary personal data.

## Metrics
Measure business/runtime signals relevant to the product: errors, latency, queue depth, sync failures, resource saturation, provider errors, success/failure rates, etc.

## Tracing/correlation
For multi-service/distributed flows, propagate correlation identifiers through APIs/jobs/events where feasible.

## Operator diagnostics
Expose enough health/config/version information to diagnose deployments without shell access when the Product SPEC requires managed operations.

## Error messages
User-facing messages should be actionable but not leak internals. Internal logs should preserve diagnostic context.
