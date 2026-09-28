# Performance, Capacity and Cost Validation

## Start from SLO-like targets
Where performance matters, define measurable targets such as:
- API p95 under representative load;
- sync completion target;
- startup time;
- frame/render budget;
- background job delay;
- memory ceiling;
- infrastructure cost per active user/workload.

## Realistic datasets
Benchmark with realistic row counts, object sizes, cardinality/skew, cache states and concurrency.

## Regression budgets
If a change materially worsens latency/resource/cost, document whether the tradeoff is acceptable. Do not hide regressions behind average metrics.

## Capacity model
For scalable services, estimate which resource saturates first and what horizontal/vertical scaling changes are available.
