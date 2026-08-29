# RQIR Recovery Delta — Iteration 028

**Date:** 2026-08-29

This delta extends `docs/RECOVERY_GUIDE.md` from the confirmed Iteration-027 frontier.

## New confirmed result

The three D2 calibration architectures are now compared through a dimensionless physical wall-clock phase diagram rather than by Fisher rank or `lambda` alone.

Define

- `x=K_force/K_pot`,
- `y=K_cov/K_pot`,
- `z=R_P K_pot`.

At target `F_{beta|theta}=0.90`, minimize along each Iteration-027 Pareto frontier:

- `tau_null=lambda(1+y)+C_a^*(lambda)/z`;
- `tau_force=lambda(x+y)+C_a^*(lambda)/z`;
- `tau_aug=lambda(1+x+y)+C_a^*(lambda)/z`.

All three branches are optimal somewhere in `(x,y,z)` space.

Representative regimes:

- slow source metrology / cheap complementary gravity rows -> augmented;
- fast source metrology + cheap force rows -> native-force replacement;
- expensive force calibration -> original NP3-null + independent source metrology.

Representative transition slices:

- `y=0.1,z=1`: augmented -> native near `x~1.98`; native -> null near `x~3.74`;
- `y=1,z=1`: augmented -> native near `x~1.08`; native -> augmented near `x~3.22`; augmented -> null near `x~6.29`;
- `y=0.1,z=10`: native -> augmented near `x~2.07`; augmented -> null near `x~4.07`.

These are Toy009/Toy010 local numerical phase boundaries, not universal constants.

## New rule

**RQIR-RESOURCE-008 — branch choice is a resource phase diagram.**

Neither exact-rank completion, smallest required calibration multiplier, nor smallest `C_a` alone determines the least-cost D2 protocol. The correct comparison minimizes total wall-clock cost along each branch-specific `C_a^*(lambda)` frontier.

## Negative result retained

No SI-time winner may be claimed until `K_pot`, `K_force`, `K_cov`, and `R_P` are obtained from one internally consistent D2 apparatus/noise/transduction model. Do not silently set these rates equal.

## Mandatory consistency carry-forward

Retain without modification:

- RQIR-NUM-001 hard elimination of exact trace+energy constraints;
- RQIR-NG-005 for the declared NP3 exact-null branch;
- RQIR-NG-010 nullspace rotation under force-observable replacement;
- RQIR-CAL-009 complementary-observable completion for augmented potential+force calibration;
- D2 detector Fisher must remain force-PSD/live-time based;
- timing/reference duty must eventually include Iteration-023 colored-drift recertification;
- no new-physics claim before consistency/degeneracy/experimental gates.

## Reproducibility

- `analysis/d2_resource_phase_diagram_iteration028.py`
- `docs/D2_RESOURCE_PHASE_DIAGRAM.md`
- `research_log/2026-08-29_iteration_028_d2_resource_phase_diagram.md`

## Next exact continuation point

Construct one D2 apparatus-level rate model that maps equivalent-force PSD/transduction and calibration bandwidth/duty into `K_force/K_pot` and `K_cov/K_pot`, maps source-preparation cycle/acceptance/QFI efficiency into `R_P K_pot`, adds reference recertification duty, and propagates uncertainty in these ratios across the Iteration-028 phase boundaries.
