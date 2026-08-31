# RQIR Research Log — Iteration 183

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

Iteration 182 showed that an off-shell split `Gamma_soft=W[K2]+Rlin:B` is not unique for nonzero `K2`. Iteration 183 removes that convention from the physical novelty test.

Freeze directly observable/source-completed rows

`Y=(K2_rows,S_soft2_full_rows)`.

For parameter tangents `A=dK/dtheta`, `B=dS/dtheta`, impose exact quadratic calibration first:

`A delta_theta=0`.

If `N_A` spans `ker(A)`, the allowed conditional cubic comparator tangent is

`B_cond=B N_A`.

This construction uses the full cubic response and is invariant under any internal Ward/transverse repartition. Six-row numerical split test: maximum change `4.44e-16`.

Quadratic audit on the frozen `q^2` rows:

- local C5 inverse-kernel basis `[x,x^2,x^3,x^4,x^5,x^6]`: rank `6/6`;
- condition number `2.3982e7`;
- nonlocal lambda tangent `x^2 exp(x)` appended: row rank remains `6`;
- one exact parameter-space null direction exists;
- normalized nonlocal coefficient `+1` is compensated by local coefficients approximately `[3.72e-5,-1.00059,-0.99613,-0.51334,-0.14137,-0.06615]`;
- quadratic null residual `1.65e-16`.

Therefore the physical nonlocal discriminator is the **conditional full soft2 cubic prediction** of this K2-preserving parameter combination. The required local quadratic EFT soft2 cubic columns have not yet been instantiated in the null-soft protocol.

Retain:

- `REL-NG-001 — JOINT_K2_SOFT2_HARD_CONDITIONING_IS_INVARIANT_UNDER_INTERNAL_WARD_TRANSVERSE_REPARTITION`;
- `C5-NG-010 — LOCAL_QUADRATIC_EFT_SOFT2_COMPLETIONS_ARE_REQUIRED_WHEN_THEIR_K2_DIRECTIONS_COMPENSATE_NONLOCAL_CALIBRATION`;
- `NL-NG-006 — SIX_ROW_NONLOCAL_K2_TANGENT_HAS_AN_EXACT_LOCAL_POLYNOMIAL_COMPENSATION_DIRECTION_AT_FROZEN_DIMENSION12_RESOLUTION`;
- `NG-FUNNEL-041 — CONDITION_FULL_SOURCE_COMPLETED_SOFT2_ON_CALIBRATED_K2_INSTEAD_OF_PROMOTING_AN_OFFSHELL_W_B_SPLIT`.

`MODEL_READINESS: 24%` — unchanged because no full comparator quotient or residual is yet available.

Next: Iteration 184, compute source-completed null-soft `S_soft2` cubic columns for local quadratic C5 EFT directions through the frozen dimension-12 order, then form the calibrated nonlocal combination.
