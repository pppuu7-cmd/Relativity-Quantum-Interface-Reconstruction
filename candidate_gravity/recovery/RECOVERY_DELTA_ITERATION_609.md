# RECOVERY DELTA — Iteration 609

Date: 2026-09-08

Iteration 609 closes the requested kinematic-pullback audit with an authoritative operational BLOCKED result, not a model FAIL.

For the full routed Iter594/605 same-action source object, internal scalar lines obey `r=p0+Q_A`, so `r^2=p0^2+Q_A^2+2 p0.Q_A` in MSSC `(+---)` convention. K1/K2 placements have `Q_A=+/-q_i`; K1^3 permutations have internal lines `p0+q_i` and `p0-q_k`; local K3 has no internal scalar propagator. Thus the scalar-pole support depends on `p0^2` and `p0.q_i`, not on an external Iter582 q2 bucket alone.

Iter588's symmetric isolated K1/K2 endpoint routing `p=-q_i/2`, `p'=+q_i/2` is retained in its frozen scope, but using `q_i^2/4` to replace the p0-dependent full-object propagators would be an unauthorized change of observable.

Classification: `BLOCKED_ITER609_INTERNAL_SCALAR_POLE_PULLBACK_NOT_DETERMINED_BY_Q2_ALONE__NON_RESIDUAL`.

Iter608 remains authoritative: `Disc[1/(m^2-r^2+i0)] = -2*pi*i*delta(m^2-r^2)`. Missing exactly: an explicit native `T_cut` cut/integration variable and same-parent relation to MSSC `p0` sufficient to determine the roots/Jacobian of `m^2-r_j^2` family by family. Native normalization/sign remains blocked as well. No zero-fill and no Source/Born subtraction.

MODEL_READINESS: 24%

Readiness change: 0 percentage points from Iter608. The obstruction is now mathematically localized, but robust unique residual remains 0/20 and no new complete rubric sector closes.

Exact next gate: recover or derive prospectively the frozen native cut variable `z` and the map `p0 -> z` (or direct formulas for `m^2-r_j^2(z,q_i)`), then validate the simple-root support/Jacobian before any matched projection. If repository authority cannot determine that bridge, preserve BLOCKED; do not invent an estimator, normalization, sign, or internal repartition.
