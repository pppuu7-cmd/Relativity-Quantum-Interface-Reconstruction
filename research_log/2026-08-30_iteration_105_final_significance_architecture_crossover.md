# RQIR Research Log — Iteration 105

**Date:** 2026-08-30

## Goal

Continue from Iteration 104 and derive a final-significance Toy009/Toy014 architecture crossover after optimally combining detector-side and source-amplitude Fisher rates, including multiplicative duty.

## Compressed final-rate law

If architecture `i` has effective detector/transfer/seven-calibration rate `R_D,i` and independent source-amplitude rate `R_A,i`, then the separable multiplicative-amplitude model gives

`R_final,i = 1/[1/sqrt(R_D,i)+1/sqrt(R_A,i)]^2`.

With duty `d_i`, the wall-clock effective rate is

`Q_i=(1-d_i)R_final,i`.

Define

`u=R_D,14/R_D,09`,

`v=R_A,14/R_A,09`,

`z=R_A,09/R_D,09`,

`delta=(1-d_14)/(1-d_09)`.

Then **RQIR-RESOURCE-061** is

`Q_14/Q_09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

Architecture ranking is independent of final target `Z` in the local-linear regime because both times scale as `Z^2`.

## Crossover

With `w=1/sqrt(z)`, `A=1/sqrt(u)`, `B=1/sqrt(v)`, equality is

`sqrt(delta)(1+w)=A+B w`.

When positive finite,

`w_cross=(A-sqrt(delta))/(sqrt(delta)-B)`,

`z_cross=1/w_cross^2`.

## Design result

**RQIR-DESIGN-012:** source domination favors Toy014 exactly when `v>u`; favors Toy009 when `v<u`; and is neutral when `v=u` (apart from duty). This follows from the constant sign of the derivative with respect to `w=1/sqrt(z)`.

**RQIR-NG-060:** the Ramsey/source ratio alone cannot establish a source-rescue region. A valid final-significance claim requires common-normalization `u,v,z,delta` or the underlying full robust Fisher matrices.

## Regression slice

Using only the retained shared-kernel **science-only** ratio

`u_reg=0.2830146574583767`

and zero-reset Ramsey ratio

`v_reg=1.4913343179877905`,

equal duty gives

`z_cross=0.042393961570158255`.

Thus this limited regression says Toy014 wins only for a strongly source-dominated Toy009 baseline. This is not a physical detector+7cal decision because `u_reg` is science-only.

With illustrative `d09=.02`, `d14=.08`, the crossing shifts to

`z_cross=0.027135455186203732`.

## Files

- `analysis/final_significance_architecture_crossover_iteration105.py`
- `docs/PAPER_III_FINAL_SIGNIFICANCE_ARCHITECTURE_CROSSOVER_ITERATION105.md`
- `recovery/RECOVERY_DELTA_ITERATION_105.md`

## Next gate

The highest-value missing number is the robust common-apparatus `u=R_D,14/R_D,09` after complex transfer, temporal covariance uncertainty, seven physical calibration layers and detector/control scheduling. Derive a threshold envelope if apparatus data remain incomplete. Do not open Toy015 until the residual dominant marginal cost is source-dependent.
