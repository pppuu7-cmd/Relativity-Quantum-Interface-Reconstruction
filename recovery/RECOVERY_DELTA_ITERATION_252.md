# Recovery delta — RQIR Iteration 252

**Date:** 2026-09-01  
**MODEL_READINESS:** 24%  
**Candidate Gravity authoritative front:** Iteration 252

## New frozen result

Primary-paper notation audit distinguishes the orbit metric from the minimal ghost matrix:

`N_orb_{alpha beta}=R^i_alpha G_ij R^j_beta`,

`Nhat^alpha_beta=Y^{alpha gamma} N_orb_{gamma beta}`.

Therefore

`U1 = Nhat^-1 Y^up [R.(D R).E] Nhat^-1`.

This validates the existence of the two Iteration-251 `delta(Nhat^-1)` placements and relocates the independent gauge-weight variation to the single explicit `Y^up` factor.

For frozen TT `h`,

`delta[sqrt(|g|) g^{mu nu}] = -epsilon^{mu nu}`

(up to the already fixed overall gauge-weight normalization). Finite-difference error at `1e-6`: `5.44e-11`.

Freeze:

`PASS_SCOPED_U1_ORBIT_GHOST_WEIGHT_FACTORIZATION_AND_TT_DELTA_WEIGHT`.

## Still blocked

The complete `E^(2)K^(1)` numerator is **not** closed. Missing:

`delta[R^i_gamma (D_i R^j_delta)] E^(2)_j`.

After this block is derived, combine it with the two resolvent placements and `delta Y^up`, then perform a condensed-index/Ward consistency test before tensor reduction.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`,

`BLOCKED_NOT_ZERO`.

No robust Candidate Gravity residual. `ANSATZ-003` not created. Heavy C5 run, Fisher and resource stages remain forbidden.

## Files

- `candidate_gravity/C5_VD_U1_WEIGHT_FACTORIZATION_ITERATION252.md`
- `candidate_gravity/code/iteration252_vd_u1_weight_factorization.py`
- `candidate_gravity/results/iteration252_vd_u1_weight_factorization.json`
- `research_log/2026-09-01_iteration_252_vd_u1_weight_factorization.md`
- `recovery/RECOVERY_DELTA_ITERATION_252.md`

## Next gate — Iteration 253

Derive `delta[R(DR)] E^(2)` in the same frozen convention and assemble the complete first-order `E^(2)K^(1)` `U1` numerator. Do not launch heavy integration before its Ward/condensed-index certificate passes.
