# Iteration 462 Recovery Delta

Date: 2026-09-05

## Exact algebra/provenance closure
The frozen central4 first-derivative stencil has dimensionless nodes `(-2,-1,+1,+2)` and coefficients `(1/12,-2/3,+2/3,-1/12)`. Exact rational audit gives moments `m0=0, m1=1, m2=0, m3=0, m4=0, m5=-4`, with `L1=3/2`. The tensor-product mixed operator therefore has pre-scaling `L1=9/4`, matching the Iteration-458 norm derivation.

For every monomial `u^a v^b` with `0<=a,b<=4`, the normalized tensor moment is exactly zero except `(a,b)=(1,1)`, which is exactly one. Post-support assembly must therefore pass exact operator sanity tests: constant and pure-u/pure-v degree<=4 probes annihilate; normalized `u*v` returns one. Violation is implementation/provenance `BLOCKED`, never physics FAIL.

Classification: `PASS_CENTRAL4_TENSOR_MOMENT_INVARIANTS__NON_PROMOTING`.

Code: `candidate_gravity/code/iteration462_central4_tensor_moment_invariants.py`.
Result: `candidate_gravity/results/iteration462_central4_tensor_moment_invariants.json`.

`MODEL_READINESS: 24%`

Readiness change: 0 pp; no stable rubric component closed.

## Retained authority
Physical/operator authority: Iteration 411. Physical blocker: Iteration 421, unresolved set `[2]`. Latest completed numerical mass-support authority remains Iteration 461 unless the active rank-4 run is subsequently raw-consumed. Run `33957232727` remains the sole authorized numerical gate while in progress. No later coordinate is authorized before its raw consumption. `ANSATZ-003` remains uncreated; Fisher/resources forbidden.
