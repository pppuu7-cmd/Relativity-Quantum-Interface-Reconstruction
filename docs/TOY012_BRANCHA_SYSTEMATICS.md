# RQIR Iteration 059 — Toy012 Branch-A Systematics Revalidation

**Date:** 2026-08-30  
**Scope:** balanced Toy012, complementary relational/direct-force D2 branch.  
**Status:** normalized control/Fisher result; not a hardware forecast and not a new-physics claim.

## 1. Why this gate was mandatory

Toy009 control priors cannot be transferred unchanged to Toy012. Iteration 057 already showed that covariance complementarity is source-specific. The same discipline must be applied to timing, geometry and additive controls before constructing a total wall-clock budget.

The tested local branch contains

- 14 finite-reference relational-potential means;
- 14 direct-force means;
- a selected subset of centered relational covariance rows;
- independent source-amplitude metrology `C_alpha`.

Exact trace+energy elimination and the corrected fractional `alpha` coordinate are retained.

## 2. Control nuisance model

Six independent low-rank calibration nuisances are included:

1. second-probe position drift `delta y1`;
2. finite-reference position drift `delta y_ref`;
3. common source-drive/detector-reference phase shift `delta tau`;
4. additive offset for relational mean rows;
5. additive offset for direct-force mean rows;
6. additive offset for centered covariance rows.

The geometry/time score vectors are numerical derivatives of the **normalized Toy012 calibration rows**, not transplanted Toy009 derivatives.

A conservative control allocation requires the largest whitened perturbation from each nuisance to be no more than 10% of one row standard deviation.

## 3. Toy012 control targets

For the resource-relevant k4, k5 and k8 relational-covariance branches the active maxima are the same, giving

`boxed: sigma(delta y1) ~= 0.585485`

`boxed: sigma(delta y_ref) ~= 1.184282`

`boxed: sigma(delta tau) ~= 0.00260497`.

At a 100-Hz gap the phase/timing target becomes

`boxed: sigma_t ~= 4.14594 us`.

The normalized additive targets are

- relational mean: `~9.09585e-5`;
- direct-force mean: `~9.09585e-5`;
- centered covariance: `~7.25572e-5`.

If the dimensionless spatial unit is identified with the historical `L0=10 um` benchmark, the geometry numbers correspond only illustratively to

- `sigma(y1) ~5.85 um`;
- `sigma(y_ref) ~11.84 um`.

These are not SI hardware requirements until the source/radius scale is physically fixed.

## 4. Timing is tighter than on Toy009

The mature centered Toy009 D2 timing target was about `9.19 us` at 100 Hz. Toy012 branch A requires about

`4.15 us`.

Thus localization/resource-aware source redesign improved nuisance calibration cost but rotated the timing score geometry in a less favorable direction.

This is another example of why detector/control modules cannot be transferred between source designs without re-profiling.

## 5. Independent controls remain mandatory

For the k4 branch, keeping the source prior but giving the six control nuisances no independent priors yields approximately

| calibration exposure scale | `F_beta|theta` |
|---:|---:|
| 1 | `~0.556` |
| 2 | `~0.659` |
| 10 | `~0.772` |
| 100 | `~0.804` |

So simply accumulating more gravitational calibration data does not recover the 90% target.

### RQIR-NG-027 — Toy012 control-floor obstruction

> Full hard rank and independent source-amplitude metrology do not remove low-rank timing/geometry/additive degeneracies. In the current Toy012 branch, calibration exposure alone asymptotes below the target unless independent control/reference information is supplied.

This is the Toy012 continuation of NG-006, now on the actual complementary local branch.

## 6. Cost of a properly controlled branch is small if references exist

With the 10%-per-row prior allocation, the k4 branch at its nominal source prior gives

`F_beta|theta ~= 0.899802`

at scale one. Scaling the main calibration, source prior and reference campaigns together by only

`boxed: lambda ~= 1.00237`

restores the exact 90% target.

For k5 the corresponding value is

`lambda ~= 1.00259`.

Therefore **the existence of independent controls is critical, but once available at the stated precision their extra Fisher burden is only a few parts in 10^3 in the normalized model.**

### RQIR-CAL-017 — control existence dominates control overexposure

The current Toy012 problem is not a need for enormous extra control Fisher. It is the need for physically independent references whose scores are not detector-degenerate. Once those references reach the stated priors, further overexposure gives little benefit.

## 7. Physical timing-reference example

Using the same transparent reference convention as earlier iterations — 10-us single-event timing uncertainty, 100-Hz gap, 1-ms dead/readout time, acceptance `p=0.5`, and measuring the timing reference to one third of the allowed target — the required timing-reference block is of order one second (`~0.98 s`).

This number is illustrative only. Low-frequency drift/recertification remains governed by the Allan/TDEV/PSD gate of NG-007 and can dominate over the one-time white-noise reference block.

## 8. Reproducibility

Code:

`analysis/toy012_branchA_systematics_iteration059.py`

Regression values include the six control targets, the `4.14594 us` timing target, the k4/k5 scale corrections and the no-control-prior exposure scan.

## 9. Next gate

The next total-wall-clock step must not automatically retain all eight **base relational covariance rows**. Iteration 057 varied only the additional force-covariance subset, while all eight relational covariance rows were treated as common overhead. For total time this is no longer harmless.

The next calculation should enumerate subsets of the eight relational covariance rows and trade their phase-referenced trajectory cost against independent source-metrology Fisher. This is required before a physically meaningful `T_wall` can be minimized.
