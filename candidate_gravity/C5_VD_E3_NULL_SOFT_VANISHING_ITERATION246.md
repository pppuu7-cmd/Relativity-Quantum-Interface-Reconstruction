# RQIR Candidate Gravity — Scoped Vilkovisky `e=3` Null-Soft Vanishing

**Iteration:** 246  
**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Question

Iterations 243–245 reduced the previously indefinite finite Vilkovisky problem to a finite set of sectors. Iteration 244 fixed the cubic connection piece

`Gamma_conn^(3) = +(i/2) Tr(U1 U2) - (i/6) Tr(U1^3)`.

Iteration 243 showed that on the Minkowski, `Lambda=0`, curvature-cubic target this is the `e=3,c=0` sector: three explicit EOM insertions and otherwise flat kernels.

Does that sector contribute to the **physical null-TT soft branch** frozen by the RQIR soft protocol?

## Frozen soft leg

Retain the Iteration-175 null soft momentum and plus TT polarization:

`k=(1,0,0,1)`, signature `(-,+,+,+)`,

`eps_xx=1/sqrt(2)`, `eps_yy=-1/sqrt(2)`.

The reproducible validator gives exactly

- `k^2 = 0`;
- `Tr eps = 0`;
- `k^mu eps_mu nu = 0`;
- `R_mu nu^(1)[eps,k] = 0`;
- `G_mu nu^(1)[eps,k] = 0`.

At the same time the soft field is not trivial/pure gauge:

- `max |Riemann^(1)| = 0.35355339059327373`;
- `||Riemann^(1)||_F = 1.9999999999999998`.

Thus the soft graviton carries physical linearized curvature while satisfying the linearized Einstein equations.

## EOM-degree argument

In the exact Vilkovisky reduction:

- `U1` is linear in the Einstein EOM insertion;
- `U2` is quadratic in EOM insertions.

Therefore

- `Tr(U1^3)` has three explicit EOM factors;
- `Tr(U1 U2)` also has three explicit EOM factors.

In the `e=3,c=0` sector all propagators, gauge generators, `Y` factors and other kernels are frozen at their flat values. Consequently the cubic functional dependence on the three external metric perturbations arises by taking the **linear** part of each of the three EOM factors.

For three external legs `(soft,a,b)`, every term in the trilinear symmetrization contains one factor

`E^(1)[h_soft] = 0`.

Hence

`delta^3 Tr(U1^3)[soft,a,b] = 0`,

and

`delta^3 Tr(U1 U2)[soft,a,b] = 0`

on the frozen physical null-TT soft branch.

Therefore

`Gamma_conn,e=3,c=0^(3)[soft_TT_null,a,b] = 0`.

## Scope guard

This result is deliberately narrow.

It does **not** imply:

- that the full one-loop C5 cubic response vanishes;
- that the Vilkovisky connection sector is zero for generic off-shell three-point kinematics;
- that `T_cut` is zero;
- that C5 can be zero-filled in the final comparator quotient.

The following sectors remain capable of contributing because the soft leg may enter through curvature/operator/propagator dressing rather than through an explicit linear EOM factor:

1. determinant sector `e=0,c<=3`;
2. connection sector `e=1,c<=2`;
3. connection sector `e=2,c<=1`.

These sectors remain part of the required gauge-safe C5 comparator.

## Relation to loop soft protocol

Iteration 209 requires holding the physical soft momentum finite and nonzero before taking the hard-channel discontinuity. The present result is compatible with that order: scaling the null soft vector by a finite nonzero soft parameter preserves `k_soft^2=0`, TT transversality and the linearized Einstein-EOM zero exactly.

The result should therefore be used only as an algebraic simplification of the `e=3,c=0` contribution before the hard-channel cut/source projection, not as a replacement for the finite-soft loop calculation of the surviving sectors.

## New scoped results

- `C5-CUT-031 — VD_E3_FLAT_CONNECTION_SECTOR_VANISHES_WITH_ONE_PHYSICAL_NULL_TT_SOFT_LEG`.
- `C5-NG-023 — CUBIC_VD_EOM_TRACE_IS_NONZERO_GENERICALLY_BUT_NULL_SOFT_BLIND_IN_THE_FROZEN_BRANCH`.
- `REL-NG-021 — PHYSICAL_NULL_TT_SOFT_GRAVITON_HAS_ZERO_LINEAR_EINSTEIN_EOM_BUT_NONZERO_LINEARIZED_RIEMANN`.
- `NG-FUNNEL-100 — C5_T_CUT_AUTHORITY_REDUCES_TO_E0_E1_E2_SECTORS_AFTER_SCOPED_E3_NULL_SOFT_ELIMINATION`.

## Classification

`PASS_SCOPED_VD_E3_NULL_SOFT_TT_VANISHING`.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

This removes one difficult connection sub-block but does not yet close the physical C5 comparator coordinate.

## Next gate — Iteration 247

Re-triage the surviving C5 sectors under the same null-soft projection:

1. determinant `e=0` sector: identify the minimum CPT3 form-factor combinations that can survive one null-TT soft leg after Ward/source subtraction;
2. `e=1,c=2` sector: enumerate where the soft leg can enter without being the explicit EOM factor;
3. `e=2,c=1` sector: do the same and test whether placements with a soft EOM factor vanish, leaving only curvature-dressing placements;
4. construct a minimal surviving-sector graph/table before any heavy tensor computation;
5. preserve hard-channel discontinuity and finite-soft ordering from Iterations 205/209.
