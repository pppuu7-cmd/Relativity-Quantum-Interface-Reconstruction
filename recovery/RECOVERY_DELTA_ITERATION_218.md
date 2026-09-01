# Recovery Delta — RQIR Iteration 218

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Previous front

Iteration 217 proved that exact on-shell graviton cuts do not uniquely determine the off-shell/source-completed linked cut because inverse-kernel/EOM-proportional nonanalytic terms vanish on shell but can change off-shell discontinuities.

## New source authority

Freeze `MSSC-001`, one minimally coupled massive scalar:

`S_phi=-1/2 int sqrt(-g)[g^{mu nu} partial_mu phi partial_nu phi + m^2 phi^2]`.

The linear scalar source vertex satisfies exactly

`k_mu V^{mu nu}=(p'^2-m^2)p^nu-(p^2-m^2)p'^nu`.

Numerical certificate:

- max off-shell Ward identity error `4.44e-16`;
- on-shell source transversality error `1.14e-16`.

All nonlinear `h^n phi^2` contacts are fixed by expansion of the **same** covariant scalar action. Independent contact tuning is forbidden.

## Important nonlinear guardrail

Do not validate the `hh phi phi` seagull in isolation. The physical two-graviton scalar amplitude at `O(kappa^2)` is the coherent gauge-invariant sum encoded by the same gravity+matter dynamics, including exchange/contact structures. Gauge invariance belongs to the complete amplitude.

A published amplitude-level implementation route exists: covariant two-massive-scalar/multi-graviton tree amplitudes and their KLT construction (Bjerrum-Bohr et al., arXiv:1908.09755).

## Retained results

- `SRC-NG-001 — MINIMALLY_COUPLED_SCALAR_ACTION_FIXES_SOURCE_WARD_IDENTITY_AND_ALL_NONLINEAR_SOURCE_CONTACTS_FROM_ONE_DYNAMICS`;
- `SRC-NG-002 — DYNAMICAL_SOURCE_COMPLETION_IS_REQUIRED_BEFORE_AN_OFFSHELL_CONNECTED_CUT_CAN_BE_CALLED_GAUGE_SAFE`;
- `NG-FUNNEL-075 — USE_CONNECTED_DYNAMICAL_SOURCE_OBSERVABLES_TO_AVOID_GAUGE_DEPENDENT_OFFSHELL_VERTEX_PROMOTION`.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

## Exact restart instruction

Resume at **Iteration 219**. Instantiate the full `2 massive scalar + 2 graviton` tree amplitude from the published scalar-gluon + KLT construction. Verify:

1. exact external kinematics/mass shells;
2. both independent gravitational Ward tests (replace either copy of either graviton polarization by its momentum);
3. exchange symmetry of the two graviton legs;
4. no use of an isolated source contact as a physical column.

If successful, freeze this as the first nonlinear dynamical-source amplitude building block for a physical conserved-source unitarity cut.
