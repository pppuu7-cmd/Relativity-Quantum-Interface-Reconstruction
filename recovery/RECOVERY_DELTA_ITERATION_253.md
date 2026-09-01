# Recovery delta — RQIR Iteration 253

**Date:** 2026-09-02  
**MODEL_READINESS:** 24%  
**Candidate Gravity authoritative front:** Iteration 253

## New frozen result

Exact same-parent gauge invariance gives

`E_j R^j_delta = 0`,

hence, using the Vilkovisky field-space covariant derivative,

`R^i_gamma (D_i R^j_delta) E_j = -R^i_gamma R^j_delta (D_i E_j)`.

The full object is symmetric in `gamma,delta` because `D_i E_j=D_iD_jS` is a symmetric covariant Hessian.

At total cubic background order,

`K=R.(D R)=K0+tK1+t^2K2+...`,

`E=tE1+t^2E2+t^3E3+...`,

so

`[K E]_(t^3) = K0 E3 + K1 E2 + K2 E1`.

Therefore the exact cubic Ward/symmetry condition applies to the complete sum, not automatically to the isolated `K1 E2` partition.

Freeze:

`PASS_SCOPED_CUBIC_WARD_PARTITION_AUDIT`,

`NO_STANDALONE_CUBIC_WARD_FAIL_FROM_E2K1_PARTITION`.

## Scientific meaning

This is an upstream algebraic correction. It prevents a false scientific FAIL if the isolated `E^(2)K^(1)` block is not separately symmetric. It does not prove a comparator identity or a residual.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`,

`BLOCKED_NOT_ZERO`.

No robust Candidate Gravity residual. `ANSATZ-003` not created. Heavy C5 integration, Fisher and resource stages remain forbidden.

## Files

- `candidate_gravity/C5_VD_U1_WARD_PARTITION_AUDIT_ITERATION253.md`
- `candidate_gravity/code/iteration253_vd_u1_ward_partition_audit.py`
- `candidate_gravity/results/iteration253_vd_u1_ward_partition_audit.json`
- `research_log/2026-09-02_iteration_253_vd_u1_ward_partition_audit.md`
- `recovery/RECOVERY_DELTA_ITERATION_253.md`

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 252: **0 percentage points**. The correct cubic Ward target is now frozen, but no readiness-rubric block closes.

## Next gate — Iteration 254

Derive the explicit `delta[R(DR)] E^(2)` contribution in the frozen `D=4`, `Lambda=0`, `a=-1/2` convention and combine it with the two frozen `delta(Nhat^-1)` placements plus `delta Y^up`. Perform only internal algebraic/index/TT checks on that partition. Prepare `K0E3` and `K2E1` so the eventual Ward/symmetry certificate is applied to the complete cubic same-parent sum. Do not launch heavy integration, Fisher/resources, or create `ANSATZ-003`.
