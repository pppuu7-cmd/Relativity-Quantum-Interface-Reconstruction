# RQIR Candidate Gravity research log — Iteration 271

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Authority read before work

Read `candidate_gravity/recovery/CURRENT_QG_FRONT.md` (Iteration 270), `recovery/RECOVERY_DELTA_ITERATION_270.md`, `research_log/2026-09-02_iteration_270_vd_physical_b3_nonzero.md`, recent commits, and GitHub Actions. Actions had no active runs, so no calculation was duplicated.

## Question

Can the explicitly nonzero Iteration-270 open routed kernel `<p+K|B3|p>` be sent directly into the closed bubble/triangle master map frozen in Iterations 245/250?

## Result

No: a hard ordering/closure constraint appears before master reduction.

Expanding the 15 surviving null-soft `B3=[Q A Q]_3` terms through the already frozen exact inverse recursion gives 23 primitive branches. Their `Q0`-factor histogram is

- 2 factors: 1 branch;
- 3 factors: 10 branches;
- 4 factors: 12 branches.

At generic distinct external leg labels, all routed `Q0` shifts inside every primitive open branch are distinct. In particular, sequential `Q2` and `Q1 A1 Q1` sectors expose four distinct routed inverse factors before closure.

At the frozen Iteration-270 kinematics,

`K=k_s+k_a+k_b=(1.1,0.8,0.85,0.8)`, `K^2=0.7925`, so `K != 0`.

Therefore Iteration 270 is an open operator kernel, not by itself a closed loop trace. The Iteration-245/250 no-polygon-beyond-triangle statement remains frozen for closed composite traces, but cannot be imposed on the open fixed-p kernel until the linked insertion carrying `-K` (or equivalent closure rule) is specified.

A second constraint is independent: `B3(p0) != 0` at one generic loop momentum is sufficient for the algebraic nonzero certificate but insufficient to tensor-reduce an integral. Reduction requires `B3(p)` (or a certified exact interpolation basis) over loop momentum.

## Frozen statuses

`PASS_EXACT_OPEN_B3_RESOLVENT_RANK_CENSUS`

`BLOCKED_MASTER_REDUCTION_UNTIL_KINEMATIC_CLOSURE_AND_P_DEPENDENT_INTEGRAND`

Guardrails:

`DO_NOT_FORCE_OPEN_B3_BRANCHES_INTO_CLOSED_BUBBLE_TRIANGLE_MASTERS_BEFORE_CLOSURE`

`ITER245_250_TOPOLOGY_BOUND_APPLIES_TO_CLOSED_COMPOSITE_TRACE_FAMILIES_NOT_TO_AN_UNCLOSED_FIXED_P_KERNEL`

`NONZERO_AT_ONE_P_IS_NOT_A_LOOP_INTEGRAND_RECONSTRUCTION`

Iteration-270 nonzero status remains valid and is not downgraded.

## Classification

This is an **operational BLOCKED / hard-ordering correction**, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or absence/presence of a novelty certificate by itself.

No `ANSATZ-003`, Fisher/resources, or blind heavy-C5 run was launched.

## Reproducibility

Added:

- `candidate_gravity/code/iteration271_open_b3_resolvent_rank_census.py`
- `candidate_gravity/results/iteration271_open_b3_resolvent_rank_census.json`
- `candidate_gravity/C5_VD_OPEN_B3_INTEGRAND_CLOSURE_AUDIT_ITERATION271.md`

## Readiness

`MODEL_READINESS: 24%`

Delta from Iteration 270: **0 pp**. The work closes a logical ordering ambiguity and prevents an invalid reduction, but comparator foundation remains `24/25` and unique residual remains `0/20`.

## Exact next gate

Iteration 272: build the closure-aware **p-dependent** linked `T_cut` integrand for the certified null-soft `B3` sector, with explicit `-K` closing insertion/momentum semantics but before final source tensor projection. Re-derive the closed denominator family and verify the Iteration-245/250 bubble/triangle bound on the actual closed object; certify a finite numerator basis/degree for `p`; then and only then perform scoped tensor/master-integral reduction and nonanalytic hard-channel extraction.
