# RQIR Research Log — Iteration 028

**Date:** 2026-08-29
**Target:** convert the three D2 calibration/preparation Pareto frontiers into a physical resource phase diagram.

## Starting point

Iteration 027 produced `C_a^*(lambda)` at 90% retained detector Fisher for NP3-null, native-force replacement, and augmented potential+force calibration. It deliberately did not select a wall-clock winner because the physical costs of the row families differ.

## Method

Defined the dimensionless physical ratios

- `x=K_force/K_pot`,
- `y=K_cov/K_pot`,
- `z=R_P K_pot`.

For each branch minimized

- `tau_null=lambda(1+y)+C_a/z`,
- `tau_force=lambda(x+y)+C_a/z`,
- `tau_aug=lambda(1+x+y)+C_a/z`,

subject to the exact Iteration-027 frontier `C_a=C_a^*(lambda)` and target `F_{beta|theta}=0.90`.

## Results

All three branches have nonempty optimal regions.

Representative winners:

- `(x,y,z)=(0.1,0.1,0.1)`: augmented;
- `(0.1,0.1,1)`: augmented;
- `(0.1,0.1,10)`: native-force replacement;
- `(1,1,1)`: augmented;
- `(1,1,10)`: native-force replacement;
- `(10,0.1,1)`: NP3-null;
- `(10,1,10)`: NP3-null.

Representative transition slices:

- `y=0.1,z=1`: augmented -> native-force near `x~1.98`, then native-force -> NP3-null near `x~3.74`;
- `y=1,z=1`: augmented -> native-force near `x~1.08`, native-force -> augmented near `x~3.22`, augmented -> NP3-null near `x~6.29`;
- `y=0.1,z=10`: native-force -> augmented near `x~2.07`, augmented -> NP3-null near `x~4.07`.

The nonmonotone sequence in some slices is real in the current numerical phase diagram: each branch re-optimizes `lambda` and therefore moves to a different point on its calibration/preparation Pareto curve as resource ratios change.

## New rule

**RQIR-RESOURCE-008:** branch selection is a resource phase-diagram problem. Rank completion, calibration threshold, or preparation burden alone cannot determine the cheapest protocol; one must minimize the branch-specific Pareto frontier against physical rate ratios.

## Negative result

No global SI-time winner is yet justified. The quantities `K_pot`, `K_force`, `K_cov`, and `R_P` must be estimated for one internally consistent D2 apparatus model before selecting a physical branch.

## Consistency checks

The result preserves RQIR-NG-005, RQIR-NG-010, RQIR-CAL-009, the Iteration-015 hard-constrained Fisher correction, and D2 force-domain detector Fisher. No new-physics claim is made.

## Files

- `analysis/d2_resource_phase_diagram_iteration028.py`
- `docs/D2_RESOURCE_PHASE_DIAGRAM.md`
- `recovery/RECOVERY_DELTA_ITERATION_028.md`

## Next gate

Build one internally consistent D2 apparatus-level rate model to estimate `(x,y,z)` from equivalent-force PSD/transduction, covariance bandwidth/duty, and source-preparation acceptance/QFI efficiency; include timing/reference recertification duty and propagate rate uncertainty across the phase boundaries.
