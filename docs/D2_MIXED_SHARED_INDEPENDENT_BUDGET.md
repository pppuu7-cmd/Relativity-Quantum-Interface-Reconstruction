# RQIR Iteration 045 — Mixed Shared-Science / Independent Mean-Calibration Budget

**Date:** 2026-08-29  
**Scope:** D2 best-four covariance/science trajectories plus independent mean-calibration copies.  
**Status:** optimistic lower-bound resource schedule after RQIR-NG-021; no apparatus forecast and no new-physics claim.

## 1. Motivation

Iteration 044 showed that a reciprocal quantum-limited linear probe cannot give arbitrary same-copy mean information while preserving the Toy009 ordered-response signal.

If we demand at least 90% of the unperturbed **raw detector signal Fisher**, then at ideal shared-copy efficiency

`xi_shared <= 0.7239817`,

so

`I_shared <= 0.5241495`

per normalized mean row per accepted science copy in the present dephasing proxy.

Iteration 040 requires at least

`N_best4 = 1.180254e6`

accepted best-four covariance/science trajectories.

Iteration 045 asks how much of the centered mean target those trajectories can safely carry, and how much calibration must remain on independent/sacrificial preparations.

## 2. Maximum optimistic shared mean credit

Current centered D2 mean target per row:

`gamma_mean = 1.830265e6`.

Maximum 90%-raw-Fisher-compatible shared credit is

`N_best4 I_shared ~= 6.18630e5`.

Therefore the shareable fraction is only

`boxed: ~0.3380`.

The residual independent mean Fisher per row is

`boxed: ~1.21164e6`,

or approximately

`boxed: 66.2%`

of the current centered target.

### RQIR-RESOURCE-019 — response-preserving shared-credit cap

> In the reciprocal linear quantum-limited reference class, a science trajectory may be credited with mean Fisher only up to the amount consistent with the allowed ordered-response disturbance. At the current Toy009 90%-raw-detector-Fisher criterion, the best-four science/covariance trajectories can cover at most about one third of the centered D2 mean target even under optimistic assumptions; most mean calibration must remain on independent preparations.

This is an optimistic upper bound because it credits the same per-row mean information to the multitime trajectory without adding further cross-time backaction.

## 3. Mixed campaign law

Let independent/sacrificial time-layer calibration achieve standardized row sensitivity

`xi_ind`.

Using the Iteration-042 seven-layer same-time dual-probe schedule, the residual mean campaign is

`T_mean,res = gamma_res/(xi_ind^2 p) * sum_j(t_j+d)`.

The total mixed campaign lower bound is

`T_mix = T_best4_cov/science + T_mean,res`.

Strong independent calibration copies may be disturbed because they are sacrificial; their backaction does not directly attenuate the separate science copies.

## 4. Transparent 100-Hz benchmark

Retain the existing transparent resource assumptions:

- `f_gap=100 Hz`;
- acceptance `p=0.5`;
- detector dead/readout time `d=1 ms`;
- same-time two-probe means acquired in parallel;
- source-preparation/reset time beyond these terms still omitted.

Best-four covariance/science floor:

`T_cov ~= 5.86402 h`.

The optimistic mixed campaign is then:

| independent `xi_ind` | residual mean time | mixed total | fully independent mean + cov | optimistic saving |
|---:|---:|---:|---:|---:|
| 1 | 29.85 h | 35.71 h | 50.95 h | 15.24 h |
| 2 | 7.46 h | 13.33 h | 17.14 h | 3.81 h |
| 3 | 3.32 h | 9.18 h | 10.87 h | 1.69 h |
| 5 | 1.19 h | 7.06 h | 7.67 h | 0.61 h |
| 10 | 0.298 h | 6.16 h | 6.31 h | 0.152 h |

Thus response-preserving weak shared monitoring can reduce wall time, but it does **not** eliminate the independent mean-calibration layer.

At practical `xi_ind` large enough that independent calibration is already fast, the absolute benefit of sharing becomes small.

## 5. Efficiency penalty

For a fixed 90%-raw-detector-Fisher disturbance criterion, the present quantum-limited proxy gives

`xi_shared,max^2 proportional eta_shared`.

Therefore the maximum fraction of the mean target that can be safely credited to science copies also scales linearly with shared-monitor efficiency:

- `eta=1`: ~33.8%;
- `eta=0.8`: ~27.0%;
- `eta=0.5`: ~16.9%;
- `eta=0.2`: ~6.76%.

Lower efficiency therefore simultaneously lengthens the resource burden and reduces the safe amount of same-copy Fisher.

## 6. Interpretation

The current D2 resource architecture is becoming hierarchical:

1. **science/best4 covariance copies** — keep monitoring weak enough to preserve the ordered-response signal;
2. **independent strong mean-calibration copies** — sacrificial preparations allow large `xi_ind` without damaging science coherence;
3. **source-state metrology** — retains the tiny residual `C_alpha` needed by best4 at the centered target;
4. **timing/additive references** — remain independent control resources under RQIR-CAL-007.

This is less elegant than an all-in-one trajectory, but it is physically safer and still allows partial sharing where it is actually beneficial.

## 7. Important optimism of this bound

The shared fraction `~33.8%` should not be interpreted as guaranteed achievable.

It assumes:

- reciprocal detector at the quantum limit;
- ideal efficiency for the headline number;
- the two-observable Toy009 dephasing proxy;
- no extra disturbance from the multitime nature of the full trajectory;
- no deterioration of nuisance/profile geometry;
- raw detector signal Fisher as the 90% criterion rather than final `F_beta|theta`.

The full profiled Fisher will generally make the safe shared credit smaller.

## 8. Reproducibility

Code:

`analysis/d2_mixed_shared_independent_budget_iteration045.py`

The script combines the Iteration-040 covariance trajectory floor, Iteration-042 time-layer scheduler and Iteration-044 response-preserving information cap.

## 9. Next gate

Propagate the backaction/dephasing map through the **complete hard-constrained D2 detector Jacobian** and recompute `F_beta|theta` for the centered best4 branch. The key output is the true maximum `xi_shared` compatible with final profiled `F_beta|theta>=0.90`, not only raw signal Fisher retention.