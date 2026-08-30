# RQIR Recovery Delta — Iteration 088

**Date:** 2026-08-30

## New retained result

Iteration 088 propagates the interval-robust apparatus logic from the two-band science rate into the seven same-time dual-probe calibration layers.

For an integrated two-row Fisher-rate block

`F_j=[[a_j,c_j],[c_j,b_j]]`,

use

`R_cal,j=lambda_min(F_j)`

as the scalar isotropic layer throughput.

### RQIR-RESOURCE-041

For a PSD-safe independent entry box, `lambda_min` is concave, so its exact lower envelope is found at the eight box vertices.

With certified layer lower rates `R_cal,j^-`,

`H_cal^- = 7/sum_j(1/R_cal,j^-)`

and

`T_cal^upper = gamma sum_j(1/R_cal,j^-) = 7 gamma/H_cal^-`.

For per-accepted-cycle block `I_j`, lower minimum-eigenvalue information `i_j^-`, acceptance floor `p_j^-` and cycle upper bound `t_cyc,j^+`:

`N_acc,j >= gamma/i_j^-`,

`N_try,j,required = gamma/(p_j^- i_j^-)` at the expectation/Asimov scheduling level,

`R_cal,j^- = p_j^- i_j^- / t_cyc,j^+`.

This is the explicit bridge from abstract `gamma` to repetitions, acceptance/shot loss, read/reset overhead and coherence-constrained cycle time.

### RQIR-NG-038

A nominal positive Fisher matrix with independent entry uncertainties that cross the PSD boundary does not certify a positive robust layer rate. Use a PSD-preserving uncertainty region/parameterization or report the layer robust rate unresolved.

## Reproducibility

- `analysis/seven_layer_robust_calibration_iteration088.py`
- `docs/PAPER_III_SEVEN_LAYER_ROBUST_CALIBRATION_ITERATION088.md`
- `research_log/2026-08-30_iteration_088_seven_layer_robust_calibration.md`

## Next gate

Combine Iteration-087 science bounds and Iteration-088 calibration bounds with bounded independent source-metrology rate and control/reference duty into a reusable total-time interval certificate. Use it to implement NG-030 robust nonoverlap for Toy009/Toy014 before inserting apparatus-specific numbers.
