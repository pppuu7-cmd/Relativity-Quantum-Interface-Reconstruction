# RQIR Iteration 028 — D2 Calibration/Preparation Resource Phase Diagram

**Date:** 2026-08-29  
**Status:** hard-constrained Toy009/Toy010 local resource analysis; not an experimental forecast.

## 1. Question

Iteration 027 derived the three branch-specific 90%-retention Pareto frontiers `C_a^*(lambda)` for D2. The next question is which branch minimizes actual wall-clock resource once the physical relative costs of potential calibration, force calibration, covariance calibration, and independent source metrology are allowed to differ.

No equal-rate assumption is introduced.

## 2. Dimensionless physical coordinates

Let

- `K_pot` = wall-clock time required for the `lambda=1` potential-mean calibration bundle;
- `K_force` = corresponding time for the force-gradient mean bundle;
- `K_cov` = corresponding time for the covariance/noise bundle;
- `R_P` = independent source-preparation Fisher rate.

Define

`x = K_force/K_pot`,

`y = K_cov/K_pot`,

`z = R_P K_pot`.

Dividing total time by `K_pot`, each branch has

`tau_null  = lambda(1+y)   + C_a/z`,

`tau_force = lambda(x+y)   + C_a/z`,

`tau_aug   = lambda(1+x+y) + C_a/z`.

For each branch, `C_a` is restricted to the exact Iteration-027 frontier `C_a^*(lambda)` at `F_{beta|theta}=0.90`, and `tau` is minimized over `lambda`.

## 3. Main result: there is no universal cheapest D2 branch

All three branches occupy nonempty regions of the physical resource space.

Representative points:

| `(x,y,z)` | cheapest branch | interpretation |
|---|---|---|
| `(0.1,0.1,0.1)` | augmented | preparation metrology is slow; paying for complementary gravitational observables is cheaper |
| `(0.1,0.1,1)` | augmented | same regime persists at moderate preparation rate |
| `(0.1,0.1,10)` | native-force replacement | source metrology is fast and force calibration is cheap |
| `(1,1,1)` | augmented | comparable calibration costs still favor complementarity at moderate preparation rate |
| `(1,1,10)` | native-force replacement | fast preparation makes the rotated-null branch viable |
| `(10,0.1,1)` | NP3-null | force calibration is sufficiently expensive that the original potential branch plus source metrology wins |
| `(10,1,10)` | NP3-null | same high-force-cost regime even with faster preparation |

Thus Iteration 026's structural Fisher conclusions and Iteration 027's Pareto curves do not select a globally preferred experimental architecture by themselves.

## 4. Transition structure

A scan over `x` shows branch changes rather than a monotone single threshold in every slice.

For `y=0.1, z=1`, the approximate transition sequence is

`augmented -> native-force -> NP3-null`

at

`x ~ 1.98` and `x ~ 3.74`.

For `y=1, z=1`, a richer sequence appears:

`augmented -> native-force -> augmented -> NP3-null`,

with transition brackets near

`x ~ 1.08`, `x ~ 3.22`, and `x ~ 6.29`.

For `y=0.1, z=10`, the low-`x` region is native-force, then augmented, then NP3-null, with approximate boundaries near

`x ~ 2.07` and `x ~ 4.07`.

For large covariance cost (`y=10`) in the tested slices, the augmented branch dominates a broad low/intermediate-force-cost region and crosses directly to NP3-null only at very large `x` (roughly tens). The covariance term is shared by all branches, so its main effect is to alter the optimal `lambda` and the value of preparation relative to mean-calibration cost rather than simply adding a constant after optimization.

These transition values are numerical Toy009/Toy010 phase-diagram coordinates, not universal constants.

## 5. Why the augmented branch can win despite using more calibration rows

The augmented branch pays the extra factor `1+x+y`, but it is the only branch that can eliminate the exact source null using gravitational calibration alone. Along its Pareto frontier it can drive `C_a` all the way to zero at finite `lambda ~4.89`.

When source-preparation metrology is slow (`z << 1`), the term `C_a/z` is expensive. In that regime it can be cheaper to spend more gravitational calibration time to remove the nuisance geometrically.

This is a genuine resource tradeoff, not a Fisher-rank paradox.

## 6. Why native-force replacement can win even though its exact null survives

The replacement branch retains a rotated one-dimensional exact null, so `C_a=0` is impossible at 90% retention. However, its strong-preparation calibration threshold is much lower than the NP3-null branch (`lambda_min ~0.353` versus `~1.00024`).

If force rows are physically cheap (`x << 1`) and source metrology is fast enough (`z >= O(1)` in the current normalized coordinates), a modest independent `C_a` can be cheaper than augmented complementary calibration.

Therefore `exact null remains` does not imply `experimentally dominated` once independent metrology is admitted.

## 7. Why NP3-null returns at large force cost

When `x` is large, both force-based branches inherit a large wall-clock penalty. The NP3-null branch then becomes cheaper despite its preparation burden because it never pays `K_force`.

This is the resource-side counterpart of RQIR-NG-005: the original null obstruction is not fatal if the independent preparation channel is sufficiently efficient.

## 8. New rule

### RQIR-RESOURCE-008 — branch choice is a resource phase diagram

For a fixed detector-level retention target, calibration architecture must be selected only after minimizing the branch-specific Pareto frontier against physical rate ratios.

A rank advantage, a smaller calibration threshold, or a smaller source-preparation requirement in isolation is insufficient to identify the cheapest protocol.

Formally, the correct comparison is

`min_lambda tau_branch(lambda; x,y,z)`

with `C_a=C_a^*(lambda)` for each branch.

## 9. Negative result

There is still no honest SI-time winner without experimentally justified values of `K_pot`, `K_force`, `K_cov`, and `R_P` for the same D2 apparatus. Any claim that one branch is globally cheaper before those inputs are supplied would reintroduce the hidden equal-rate assumption forbidden by RQIR-RESOURCE-005.

## 10. Consistency with previous gates

This iteration leaves the following intact:

- RQIR-NG-005 for the declared NP3 exact-null gravitational calibration;
- RQIR-NG-010 for force-observable replacement and nullspace rotation;
- RQIR-CAL-009 for complementary-observable completion;
- the Iteration-015 hard-constraint numerical correction;
- the D2 detector-native force-PSD formulation.

No new-physics claim is made.

## 11. Reproducibility

Code: `analysis/d2_resource_phase_diagram_iteration028.py`.

The script reconstructs the exact Iteration-027 frontiers, minimizes the dimensionless wall time in `(x,y,z)`, prints representative optima and scans transition brackets. Regression guards require all three qualitatively distinct regimes to remain present.

## 12. Next gate

The most useful next step is to replace the free phase-diagram coordinates by apparatus-level estimates from one internally consistent D2 model:

1. derive `K_force/K_pot` from one equivalent-force PSD and transduction model rather than mixing incompatible sensitivities;
2. derive `K_cov/K_pot` from the same bandwidth/duty assumptions;
3. derive `R_P K_pot` from the concrete source-preparation cycle, acceptance, and achievable fraction of the Toy009 QFI;
4. include timing/reference recertification duty from Iteration 023;
5. propagate uncertainty in these rate ratios to branch-selection robustness.

Only after that substitution is an SI wall-clock comparison scientifically admissible.
