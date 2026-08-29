# RQIR Iteration 030 — D2 Finite-Reference Potential Transduction

**Date:** 2026-08-29  
**Status:** physical transduction/resource audit for the current Toy009/Toy010 D2 calibration baseline; not an apparatus forecast and not a new-physics claim.

## 1. Question

Iteration 029 reduced D2 branch selection to native Fisher rates `(q_pot,q_force,q_cov,R_P)` but deliberately left `q_pot` open. The key unresolved point is physical: a force detector does not directly measure the absolute Newtonian potential row `B(y)` used in the NP3 calibration model.

A force-integral protocol measures a relational potential difference

`Delta B(y;y_ref)=B(y)-B(y_ref)`.

Therefore the finite reference position `y_ref` is simultaneously:

1. a calibration-geometry parameter that changes the exact nullspace;
2. a transduction-resource parameter that changes the force-integration noise.

This iteration quantifies that tradeoff for the current balanced Toy009/Toy010 calibration.

## 2. Relational potential from force

For the embedded Newtonian probe operator

`B(y)=sum_i |i><i| / |r_i-y|`

in the current domain where all denominators remain positive,

`G(y)=dB/dy`.

Hence

`B(y)-B(y_ref)=int_{y_ref}^y G(s) ds`.

This identity is exact in the toy model. It also exposes the missing physical assumption in any claim that the D2 force readout directly supplies the original potential rows: an absolute zero of potential is not measured by local force. A reference arm or another potential-sensitive observable must be declared.

### RQIR-CAL-010 — relational-potential requirement

A detector-native force channel can implement only a potential **difference** unless an independent reference fixes the integration constant. The reference geometry is part of the calibration model and must be included in nullspace/Fisher calculations.

## 3. White-force transduction model

Use a one-sided flat equivalent-force PSD `S_F`. For an ideal time average over duration `T`,

`Var(Fbar)=S_F/(2T)`.

Discretize a spatial force integral over path length `L=|y-y_ref|` into `N` equal segments, each observed for `T/N`. The integrated estimator has

`Var[int F dy]=L^2 S_F/(2T)`.

The `N` dependence cancels in this ideal white-noise limit. Therefore the native Fisher rate for a normalized source coordinate aligned with the raw differential-potential row is

`q_pot = 2 ||Delta B||^2/(L^2 S_F)`.

For a direct endpoint force row,

`q_force = 2 ||G(y)||^2/S_F`.

Thus

`q_pot/q_force = ||B(y)-B(y_ref)||^2 / [L^2 ||G(y)||^2]`.

This ratio is independent of the absolute PSD normalization under the shared-white-noise assumption.

## 4. Exact nullspace audit

The full 24-row normalized NP3 calibration was rebuilt using differential-potential means and covariance rows consistently. Trace and energy rows are unchanged.

The original absolute-potential baseline has

`rank=24/25`,

`s_min=0.001999540405542146`.

For every tested finite reference `y_ref in {-5,-10,-20,-50,-100,-1000}`, the differential calibration also remains exactly

`rank=24/25`.

So a finite reference does **not** automatically destroy the one-dimensional exact null. Instead it rotates it continuously.

Representative values:

| `y_ref` | `s_min` | `|<n_ref,n_abs>|` |
|---:|---:|---:|
| -5 | 2.7299e-3 | 0.9968101 |
| -10 | 2.5149e-3 | 0.9992856 |
| -20 | 2.3298e-3 | 0.9998904 |
| -50 | 2.1605e-3 | 0.9999943 |
| -100 | 2.0866e-3 | 0.99999953 |
| -1000 | 2.0090e-3 | 0.99999999994 |

The original Toy010/Iteration-011 nullspace is therefore recovered smoothly as the reference is moved far away.

## 5. Resource penalty of a distant reference

The same far-reference limit that reproduces the old potential geometry makes the force-integral Fisher rate collapse because the path length grows.

For the two current probe locations `y=0` and `y=Y1=-3.7766873837`, the ratios `q_pot/q_force` are:

| `y_ref` | probe 0 | probe 1 |
|---:|---:|---:|
| -5 | 3.6396e-2 | 6.6155e-1 |
| -10 | 1.1360e-2 | 2.1491e-1 |
| -20 | 3.2170e-3 | 6.2618e-2 |
| -50 | 5.5796e-4 | 1.1102e-2 |
| -100 | 1.4346e-4 | 2.8791e-3 |
| -1000 | 1.4722e-6 | 2.9792e-5 |

With seven mean time-settings per probe and the same corrected mean target weight for each row, the heterogeneous bundle cost ratio

`x_ref = K_force/K_pot`

becomes approximately

| `y_ref` | `x_ref` |
|---:|---:|
| -5 | 0.62086 |
| -10 | 0.20116 |
| -20 | 0.05850 |
| -50 | 0.01036 |
| -100 | 0.002684 |
| -1000 | 2.776e-5 |

Therefore the original absolute-potential branch is recovered only in a limit where its implementation by force integration becomes increasingly expensive relative to direct force calibration.

## 6. New obstruction/resource principle

### RQIR-RESOURCE-010 — reference-distance tradeoff

For a D2 force-integral implementation of potential calibration, calibration geometry and wall-clock cost cannot be optimized independently:

- moving `y_ref` outward makes `Delta B` approach the declared absolute-potential row and restores the old nullspace;
- but the integrated-force noise grows with path length, causing `q_pot` to fall approximately as `1/L^2` once the signal has saturated.

Thus there is no free limit in which a local force detector becomes an ideal absolute-potential calibrator.

### RQIR-NG-011 — force-to-potential integration-constant obstruction

Without an independently fixed potential reference, force data determine potential only up to an additive constant/reference value. Any D2 calibration analysis that uses absolute potential rows while assigning them the same native readout as force rows is physically under-specified.

This is an observability/gauge-relational issue, not new gravity physics.

## 7. Consequence for Iterations 028–029

Iteration 029 used a family-averaged `q_pot`. Iteration 030 shows that a physical force-integral implementation is naturally heterogeneous across probe locations:

`K_pot = gamma_mean * sum_i 1/q_pot,i`.

Therefore the exact phase-coordinate closure should use bundle costs rather than a single common row rate whenever path lengths or transduction gains differ strongly.

The branch-choice coordinate remains

`x=K_force/K_pot`,

but for a shared force PSD it can now be computed directly from the finite-reference geometry without inventing an absolute sensitivity.

## 8. What is and is not established

Established in the current Toy009/Toy010 model:

- finite-reference potential-difference calibration preserves rank `24/25` over the tested range;
- its null direction converges rapidly to the old absolute-potential null as `|y_ref|` grows;
- the same limit strongly suppresses force-integral `q_pot` relative to direct `q_force`;
- the finite reference is therefore a genuine joint geometry/resource design variable.

Not established:

- a laboratory mechanism for moving or realizing the reference arm;
- colored spatial noise, correlated drift or scan overhead;
- relativistic/gauge completion of the Newtonian potential observable;
- SI-hour superiority of any D2 branch.

## 9. Reproducibility

Code:

`analysis/d2_finite_reference_potential_iteration030.py`

The script reconstructs the deterministic Toy009 source, balanced calibration, finite-reference rows, exact ranks/null overlaps and white-force native-rate ratios, with regression assertions.

## 10. Next gate

Promote `y_ref` into the D2 resource phase diagram itself. For each finite reference:

1. rebuild the corrected hard-constrained `F_{beta|theta}` rather than relying only on exact null overlap;
2. use heterogeneous `q_pot,i(y_ref)` and direct `q_force,i`;
3. include source-preparation QFI rate and covariance rate;
4. include timing/reference recertification duty;
5. optimize jointly over branch, calibration exposure and `y_ref`.

That will determine whether a finite relational-potential arm is ever preferable to direct force calibration plus source metrology under a common apparatus model.
