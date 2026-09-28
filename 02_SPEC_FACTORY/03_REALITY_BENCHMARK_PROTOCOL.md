# Reality Benchmark Protocol

A benchmark is valid only if its environment and workload are relevant to the intended product.

## Benchmark dimensions
Depending on product, compare:
- user journey time and clicks;
- throughput;
- cold/warm latency;
- p50/p95/p99;
- memory/CPU/GPU/disk/network;
- database size and query shape;
- sync delay and conflict rate;
- error/retry behavior;
- deployment complexity;
- developer/operator effort;
- infrastructure and third-party cost;
- recoverability after failure.

## Scenario design
Use at least:
1. realistic normal scenario;
2. high-but-plausible load;
3. degraded dependency/network scenario;
4. worst-case data shape likely in the domain.

## Benchmark integrity
Record:
- hardware/instance;
- software versions;
- dataset scale and distribution;
- test duration/warmup;
- concurrency;
- cache state;
- exact metric definitions.

Do not compare a local toy dataset to a production SaaS claim as though they are equivalent.

## Market/product benchmarking
When using external products as references, distinguish:
- documented fact;
- observed behavior;
- user/reviewer claim;
- design inference.

Do not copy features merely because competitors have them. Tie each borrowed pattern to a user or operational need.
