# RQIR Research Log — Iteration 088

**Date:** 2026-08-30

## Goal

Propagate the uncertainty-safe rate logic of Iteration 087 through the seven same-time dual-probe D2 calibration layers, without inserting an arbitrary apparatus ASD.

## Result

For each integrated two-row Fisher-rate block

`F_j=[[a_j,c_j],[c_j,b_j]]`,

the isotropic calibration throughput is the smallest eigenvalue.

For a PSD-safe independent entry box, `lambda_min(F)` is concave, so its exact lower envelope is attained at one of the eight matrix-entry corners. This gives a deterministic layer rate lower bound `R_cal,j^-`.

New **RQIR-RESOURCE-041**:

`H_cal^- = 7 / sum_j 1/R_cal,j^-`

and

`T_cal^upper = gamma sum_j 1/R_cal,j^- = 7 gamma/H_cal^-`.

The same certificate maps per-accepted-cycle information to physical resources:

`N_acc,j >= gamma/i_j^-`,

with worst-acceptance expected trial budget

`N_try,j,required <= gamma/(p_j^- i_j^-)`

as an upper bound on the required expectation when the true acceptance obeys `p_j>=p_j^-`, and

`R_cal,j^- = p_j^- i_j^- / t_cyc,j^+`.

This connects the abstract `gamma` to accepted repetitions, shot/acceptance loss, cycle/read-reset overhead and coherence-constrained evolution time.

New **RQIR-NG-038**: a central positive Fisher matrix with independent entry error bars that cross the PSD boundary does not provide a positive robust layer-rate certificate. Use a PSD-preserving uncertainty model or report the robust rate unresolved.

## Regression

Seven synthetic PSD-safe blocks give

`R_j^- = (301.6610, 378.6667, 358.8235, 290.5922, 324.3845, 346.5774, 349.6453) s^-1`

and

`H_cal^- = 333.1410685791254 s^-1`.

The code verifies `gamma sum 1/R_j^- == 7 gamma/H_cal^-` to floating precision and checks 200 random PSD-safe entry boxes against 2000 random interior samples each.

The numerical blocks are regression-only and are not detector measurements.

## Reproduce

`python analysis/seven_layer_robust_calibration_iteration088.py`

## Document

`docs/PAPER_III_SEVEN_LAYER_ROBUST_CALIBRATION_ITERATION088.md`

## Next gate

Construct a reusable joint robust total-time certificate combining:

- Iteration-087 `R_beta^-`;
- Iteration-088 seven-layer `R_cal,j^-` / `H_cal^-`;
- bounded independent `R_src`;
- bounded control/reference duty;

then evaluate NG-030 interval nonoverlap before any apparatus-specific Toy009/Toy014 branch claim.
