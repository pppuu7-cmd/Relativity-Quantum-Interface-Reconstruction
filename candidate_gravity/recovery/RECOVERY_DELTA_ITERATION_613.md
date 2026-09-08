# Recovery Delta — Iteration 613

**Date:** 2026-09-08  
**MODEL_READINESS:** 24%  
**Authority:** `PASS_ITER613_PROSPECTIVE_MSSC001_NATIVE_TIMELIKE_REST_FRAME_KINEMATIC_COMPLETION_CONTRACT__NON_RESIDUAL`

## New frozen authority

After Iter612 proved that no prior same-parent authority supplied the two auxiliary invariants required by Iter611, Iter613 prospectively freezes kinematic completion `MSSC001-NATIVE-S-KIN-V1` before any pole-support evaluation.

In the MSSC-001 / Iter594 `(+---)` convention:

- `s>0`;
- `omega=+sqrt(s)`;
- `p0(s)=sqrt(s) e0`, `e0=(1,0,0,0)`;
- exact Iter368/588 `q_i`, `h_i`, mass `m=0.7`, routing/sign/normalization/i0 remain fixed.

Therefore

- `u(s)=s`;
- `a_i(s)=sqrt(s) q_i^0`;
- `a_s+a_a+a_b=0`;
- `D_i^+(s)=m^2-s-q_i^2-2sqrt(s)q_i^0`;
- `D_i^-(s)=m^2-s-q_i^2+2sqrt(s)q_i^0`;
- `partial_s D_i^+=-1-q_i^0/sqrt(s)`;
- `partial_s D_i^-=-1+q_i^0/sqrt(s)`.

Iteration167 is design precedent only (`k=(omega,0,0,0)`, `s=omega^2`) and is not equated to the nonlinear source observable. Iter613 is explicitly a newly versioned prospective bridge convention.

## Anti-bias lock

No pole roots/residues were inspected before this freeze. No target-dependent trajectory choice, family deletion, zero fill or q2 regrouping is allowed afterward.

## Still blocked

- actual positive-`s` scalar-pole support and root multiplicities;
- `|partial_s D_A|` Jacobians at supported roots;
- native `Y/T_cut` sign/normalization binding to Iter582;
- Source/Born subtraction;
- fixed comparator quotient;
- robust residual;
- `ANSATZ-003`, Fisher/resources.

## Exact next gate

Derive all retained pole roots/Jacobians from the frozen trajectory only. If support is absent for a family, record `NO_POSITIVE_ROOT` rather than zero-filling an amplitude; if a repeated/non-simple root occurs, stop and treat it distributionally rather than applying the ordinary simple-root formula.
