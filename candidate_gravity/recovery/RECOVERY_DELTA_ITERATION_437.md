# RECOVERY DELTA — ITERATION 437

**Status:** raw-consumed PASS; parent-precision closure, non-promoting.  
**Classification:** `PASS_ITER270_Q1_80_120_DIGIT_CLOSURE__LEGACY_REPRODUCED__NON_PROMOTING`  
**Prerequisite:** Iteration 436 N1 raw-valid PASS.  
**MODEL_READINESS:** 24% (unchanged).

## Raw provenance

Run `33901017066`, job `101114844067`, artifact `9947628767`, artifact digest `sha256:3797aef5b6e7883a9329b3bbbc1c23779f069fe6a7a197b75217bdf489def270`; raw scientific JSON SHA-256 `541652223024ae98a5f12c7cfc073f1d91c0ebd346a3f6ce47cb3c805f7719d8`.

## Frozen object and result

The gate evaluated

`Q1(M,x,P0,h) = -Q0(P0+k_x) @ N1(M,x,P0,h) @ Q0(P0)`

for `M=POS`, legs `s/a/b`, exact Iteration-270 `P0`/shifted momenta and unchanged `h=3e-5`.

Observed maxima:

- `Q0_80` vs `Q0_120`: `5.4158045595683956e-81` scaled;
- binary64 vs 120-digit `Q0`: `2.805309734513274e-16` scaled;
- `Q1_80` vs `Q1_120`: `9.991307363105424e-77` scaled;
- binary64 vs 120-digit `Q1`: `7.380458997002565e-12` scaled;
- all values finite.

The legacy Q1 discrepancy is again far inside the unchanged `2e-5` physical reference tolerance. Together with Iteration 436 this rules out a material arithmetic-precision error in the frozen representative `N1/Q1` parent layer at the tested kinematics.

## Exact next gate

Close the `A_finite` arithmetic core before applying the finite-difference `Acoef/Asub` stencil. The next gate must preserve exact Iteration-270 amplitudes, modes, momenta, total shifts and formulas for `geometry`, `gamma_tensor`, `action_covector`, `R_and_dR`, `lie_on_tensor`, and the final contractions.

## Guardrails

No physical `D_s` promotion, no threshold weakening, no step change, no parent-dynamics change, no zero fill, no `ANSATZ003`, no Fisher/resource claims.
