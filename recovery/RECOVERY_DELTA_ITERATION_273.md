# Recovery delta — RQIR Iteration 273

**Date:** 2026-09-02  
**MODEL_READINESS:** 24%

## Authoritative correction carried forward

Iteration 272 imposed the exact translation-closure condition `k_s+k_a+k_b=0` for the physical closed three-point trace. Therefore the Iteration-270 `K!=0` nonzero B3 value is retained only as `VALID_OFF_CONSERVATION_SURFACE_PARENT_KERNEL_NONIDENTICAL_ZERO_CERTIFICATE`, not as the final physical three-point nonzero certificate.

## New exact result

The 15 frozen null-soft `B3=[Q A Q]_3` partitions were expanded through the exact routed Q1/Q2 recursion. The primitive branch count remains 23.

After imposing `k_b=-(k_s+k_a)`, the joint Q0-factor / distinct-denominator census is exactly:

- `2 Q0 / 1 distinct`: 1 branch;
- `3 Q0 / 2 distinct`: 10 branches;
- `4 Q0 / 3 distinct`: 12 branches.

Thus the maximum number of distinct denominators in any translation-closed primitive branch is 3, and there are zero four-distinct-denominator closed branches.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_B3_DENOMINATOR_TOPOLOGY_REDUCTION`.

This reconciles Iteration 271 with the frozen Iterations 245/250 closed-topology theorem: the translation-closed object lies within raised bubble/triangle families. The four-Q0 sectors become raised triangles with a repeated denominator rather than boxes.

## Remaining blocker

`BLOCKED_TRANSLATION_CLOSED_PHYSICAL_B3_NONZERO_AND_P_DEPENDENT_NUMERATOR_AUTHORITY`.

The topology problem is no longer the blocker. The immediate missing evidence is the numerical K=0 physical B3 result from `candidate_gravity/code/iteration273_closed_kinematics_physical_b3.py`, followed by p-dependent numerator reconstruction if nonzero.

This is operational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or absence/presence of a novelty certificate.

## Guardrails

- Do not reintroduce box masters from the unclosed K!=0 branch census.
- Do not claim the K=0 physical B3 is nonzero until the closed rerun is numerically certified.
- Do not master-reduce a one-point numerator value.
- No `ANSATZ-003`; Fisher/resources and blind heavy full-C5 remain forbidden.

MODEL_READINESS: 24%

Change from Iteration 272: 0 percentage points. Comparator foundation remains 24/25; unique residual remains 0/20. Exact closed topology is now certified, but no rubric block closes until the physical closed numerator and comparator coordinate are established.

## Exact next gate

Execute/refine the K=0 physical B3 rerun, commit its numerical certificate, then reconstruct B3(p) and reduce only inside the certified raised bubble/triangle families.
