# RQIR Research Log — Iteration 012

**Date:** 2026-08-29  
**Topic:** physical Fisher resource budget after RQIR-NG-005  
**Labels:** `DRV`, `NUM`, `NEG`, `OPEN`

## Target

Convert the abstract noisy-identifiability resources `C_a` and `gamma` into physical repetition/time/coherence budgets without misrepresenting row-normalized Fisher strength as an experimental shot count.

## Repository state used

Current operational source/calibration baseline: Iteration 011 balanced Toy009 geometry, not the older Toy010 noisy-Fisher geometry.

Current normalized smallest singular value:

`1.9995404e-3`.

Calibration-row decomposition:

- trace: 1;
- source mean energy: 1;
- gravitational potential means: 14;
- symmetrized covariance/noise rows: 8.

## Step A — current scalar-gamma Fisher reconstruction

The D1 four-quadrature local nuisance Fisher model was rebuilt on the Iteration-011 baseline.

With effectively perfect independent source-amplitude characterization, required scalar-gamma strengths are approximately:

- 50% detector-information retention: `2.83e4`;
- 80%: `6.85e5`;
- 90%: `1.58e6`;
- 95%: `3.38e6`.

This confirms that `1/s_min^2` is only a proxy. The exact finite-noise requirement depends on detector-tangent alignment with the weak calibration singular vectors.

New retained rule: `RQIR-CAL-004` — conditioning alone is not a sufficient physical-resource proxy.

## Step B — preparation-amplitude budget

For detector-only information `S_D=rho_D^2`, the null-amplitude calibration law becomes

`C_a = [r/(1-r)] S_D`.

At illustrative detector SNR `rho_D=5`, hence `S_D=25`:

- 80% retention: `C_a=100`;
- 90%: `C_a=225`;
- 95%: `C_a=475`.

For single-shot standardized preparation sensitivity `xi_prep`, `N_prep=C_a/xi_prep^2`.

At 90% retention:

- `xi_prep=0.1` -> 22500 preparations;
- `xi_prep=1` -> 225;
- `xi_prep=10` -> order-unity preparations in the local idealized model.

Thus nongravitational source verification need not dominate if its per-shot information is strong.

## Step C — calibration shot-equivalent diagnostic

At 90% retention and detector SNR 5,

`gamma_90 S_D ~= 3.95e7`

normalized Fisher units per abstract row.

For orientation only, assigning all 22 gravitational mean/covariance rows the same standardized single-shot sensitivity `xi` gives:

- `xi=1`: total `~8.70e8` shots; ~10.1 days at 1 ms/shot;
- `xi=10`: total `~8.70e6` shots; ~2.42 h at 1 ms/shot;
- `xi=100`: total `~8.70e4` shots; ~87 s at 1 ms/shot.

These values are intentionally labelled diagnostics, not forecasts.

## Step D — key negative correction

A single physical shot count cannot be inferred from scalar `gamma`.

Reason: the abstract matrix weights trace, energy, potential means and covariance rows identically after row normalization, but their physical single-shot Fisher laws differ. In particular:

- Gaussian mean channel: `I_1=(dmu/dtheta)^2/sigma^2`;
- Gaussian variance channel: `I_1=0.5 (d ln V/dtheta)^2`.

Trace normalization and energy metrology are also logically separate from gravitational readout noise.

Therefore the physical calibration matrix must become

`F_C = A^T Sigma_C^{-1} A`

or an equivalent repeated-setting sum with row-specific `N_i I_i^(1)`.

## Step E — coherence budget

For dimensionless phase `tau=Omega t`, with `f_gap=Omega/(2 pi)`, the largest accepted Iteration-011 phase `4.99085` requires per-shot coherent evolution

`T_coh >= 0.7943/f_gap`.

Examples:

- 1 Hz -> 0.794 s;
- 100 Hz -> 7.94 ms;
- 1 kHz -> 0.794 ms.

New retained rule: `RQIR-RESOURCE-001` — coherence time and total repetition/integration time are different resources. With independent repeated preparations, coherence is required per shot; long total integration primarily becomes a preparation-reproducibility and drift-control problem.

## Files

- `docs/PHYSICAL_FISHER_RESOURCE_BUDGET.md`
- `analysis/physical_resource_budget_iteration012.py`
- `docs/RECOVERY_DELTA_ITERATION_012.md`

## Next gate

Replace scalar gamma with heterogeneous physical covariance and optimize wall-clock cost at fixed profiled `F_beta|theta` retention. Minimum row classes: source normalization, energy metrology, potential means, symmetrized covariance estimates, source-preparation amplitude, and drift/common-mode covariance. D1 and D2 must receive separate detector noise laws.
