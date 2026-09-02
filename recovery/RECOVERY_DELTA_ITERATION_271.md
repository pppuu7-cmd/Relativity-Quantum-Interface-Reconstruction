# RQIR Candidate Gravity — Recovery Delta Iteration 271

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Authoritative advancement

Iteration 270 remains the source of the explicit physical routed null-soft nonzero certificate

`PASS_SCOPED_PHYSICAL_ROUTED_NULLSOFT_B3_EXPLICIT_NONZERO_AND_TRANSPOSE_VALIDATED`,

with `||B3(p0)||_F=2.2209140981` at the frozen generic `p0`.

Iteration 271 audits the next proposed tensor/master-integral step and finds a mandatory closure/integrand reconstruction gate before integration.

## New exact result

The 15 surviving null-soft `B3=[Q A Q]_3` terms, expanded through the frozen exact `Q1/Q2` inverse recursion, give **23 primitive branches**:

- 1 branch with 2 `Q0` factors;
- 10 branches with 3 `Q0` factors;
- 12 branches with 4 `Q0` factors.

For generic distinct leg labels the routed shifts are all distinct inside each open branch. The four-resolvent branches arise from the sequential `Q2 N1N1` pieces and `Q1 A1 Q1` pieces.

Freeze:

`PASS_EXACT_OPEN_B3_RESOLVENT_RANK_CENSUS`.

## Closure scope correction

The frozen external sum is

`K=(1.1,0.8,0.85,0.8)`, with `K^2=0.7925`, hence `K != 0`.

So Iteration 270 certifies the open kernel `<p+K|B3|p>`. It is not by itself a closed one-loop trace integrand.

Iterations 245/250 remain authoritative that the **closed composite Vilkovisky trace families** at this order need no polygon beyond raised bubbles/triangles. Iteration 271 does not weaken or contradict that result. It establishes that the theorem cannot be applied to the open fixed-p kernel before the linked `-K` closure is specified.

Operational freeze:

`BLOCKED_MASTER_REDUCTION_UNTIL_KINEMATIC_CLOSURE_AND_P_DEPENDENT_INTEGRAND`.

Guardrails:

`DO_NOT_FORCE_OPEN_B3_BRANCHES_INTO_CLOSED_BUBBLE_TRIANGLE_MASTERS_BEFORE_CLOSURE`;

`ITER245_250_TOPOLOGY_BOUND_APPLIES_TO_CLOSED_COMPOSITE_TRACE_FAMILIES_NOT_TO_AN_UNCLOSED_FIXED_P_KERNEL`;

`NONZERO_AT_ONE_P_IS_NOT_A_LOOP_INTEGRAND_RECONSTRUCTION`.

## Why fixed-p is insufficient

The Iteration-270 one-point result is fully adequate to prove algebraic nonzero. It is not a tensor-integral numerator representation. Master reduction requires loop-momentum dependence `B3(p)` or an exact/certified reconstruction basis over `p`, including the routed denominators.

Accordingly, `BLOCKED_NOT_ZERO` remains superseded; the new blocker is strictly downstream of algebraic nonzero.

## Classification

This is operational `BLOCKED`, not:

- consistency FAIL;
- exact comparator identity;
- regime-specific non-identifiability;
- near-degeneracy;
- novelty certificate;
- Candidate Gravity residual.

`ANSATZ-003`, Fisher/resources, final source projection, and blind heavy full-C5 remain forbidden.

## Reproducible artifacts

- `candidate_gravity/code/iteration271_open_b3_resolvent_rank_census.py`
- `candidate_gravity/results/iteration271_open_b3_resolvent_rank_census.json`
- `candidate_gravity/C5_VD_OPEN_B3_INTEGRAND_CLOSURE_AUDIT_ITERATION271.md`
- `research_log/2026-09-02_iteration_271_open_b3_integrand_closure_audit.md`

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 270: **0 percentage points**. Comparator foundation stays `24/25`; unique residual stays `0/20`. The iteration resolves the correct ordering of the next calculation but does not yet produce the final C5 comparator coordinate.

## Exact next gate — Iteration 272

Construct the closure-aware, **p-dependent** linked `T_cut` integrand for the already-certified null-soft `B3` sector:

1. explicit closing momentum/insertion `-K` (without final source tensor projection);
2. exact routed `B3(p)` or certified finite interpolation basis;
3. closed denominator census and direct verification of the Iteration-245/250 raised bubble/triangle bound;
4. certified numerator tensor degree/basis;
5. then scoped tensor/master-integral reduction and regular/log/nonanalytic hard-channel extraction.

Source/Ward/contact completion, Lorentzian hard-channel discontinuity, comparator quotient, Fisher/resources, and `ANSATZ-003` remain downstream.
