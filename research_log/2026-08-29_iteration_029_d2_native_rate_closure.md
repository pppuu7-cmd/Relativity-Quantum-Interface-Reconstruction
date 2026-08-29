# RQIR Research Log — Iteration 029

**Date:** 2026-08-29  
**Target:** replace the free Iteration-028 D2 phase-diagram coordinates by exact functions of native apparatus Fisher-rate ratios without inventing SI sensitivities.

## Starting point

Iteration 028 established a three-coordinate resource phase diagram

`x=K_force/K_pot`, `y=K_cov/K_pot`, `z=R_P K_pot`

for the NP3-null, native-force replacement, and augmented D2 calibration branches. A branch winner could not be declared until those costs were tied to one common apparatus.

## Method

Using the corrected D2 row weights from Iteration 015,

- 14 mean rows at `GM=2.414e6`;
- 8 covariance rows at `GC=0.929e6`;

introduced native normalized Fisher rates per second `q_pot`, `q_force`, `q_cov` plus independent preparation rate `R_P`.

Bundle times are

`K_pot=14 GM/q_pot`,

`K_force=14 GM/q_force`,

`K_cov=8 GC/q_cov`.

Substitution gives the exact closure

`x=q_pot/q_force`,

`y=0.219907681382 q_pot/q_cov`,

`z=3.3796e7 R_P/q_pot`.

## Results

1. `z=1` corresponds to `R_P/q_pot ~= 2.95893e-8`. Therefore independent source metrology can be many orders of magnitude slower in Fisher/s than a single potential row and still be resource-competitive because the full corrected potential bundle requires `14 GM ~= 3.3796e7` accumulated Fisher units.

2. `y=1` corresponds to `q_cov/q_pot ~=0.2199077`. If stationary covariance/log-PSD Fisher accumulates at the same normalized rate as a mean row, covariance bundle cost is only `y~=0.2199`; broadband covariance can be cheaper still. Colored drift/correlation gates remain mandatory.

3. Since both mean bundles contain 14 rows with the same corrected `GM`, `x` is simply the inverse relative native force-calibration speed: `x=q_pot/q_force`.

## New rule

**RQIR-RESOURCE-009 — native-rate closure:** for the current corrected D2 calibration structure, branch selection can be mapped directly from `(q_pot,q_force,q_cov,R_P)` to the Iteration-028 phase diagram. Arbitrary wall-clock normalization is no longer needed at this layer.

## Negative result

No SI-time branch winner is yet scientifically justified because `q_pot`, `q_force`, and `q_cov` still need a common physical transduction model. Potential and force calibration cannot be identified by assumption; Iterations 025–026 showed that they are distinct observables with different nullspace consequences.

## Files

- `analysis/d2_native_rate_closure_iteration029.py`
- `docs/D2_NATIVE_RATE_CLOSURE.md`
- `recovery/RECOVERY_DELTA_ITERATION_029.md`

## Next gate

Build one physical D2 transduction model in which a single equivalent-force PSD/source-drive model yields `q_force`, a declared potential-sensitive or force-integral protocol yields `q_pot`, the same bandwidth/duty yields `q_cov`, and preparation acceptance/QFI efficiency yields `R_P`. Then include Iteration-023 recertification duty and propagate rate uncertainty through the phase boundaries.
