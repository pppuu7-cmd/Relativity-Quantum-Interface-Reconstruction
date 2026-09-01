# RQIR Candidate Gravity — Iteration 231 C5 VD/nonlocal cubic re-audit

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Question

Does current 2025–2026 literature now provide a directly executable, gauge/parametrization-safe, pure-Einstein graviton+ghost curvature-cubic nonlocal one-loop object that can be continued into the Lorentzian/source-completed RQIR linked-cut convention?

## Starting authority

Iteration 207 already established three separate facts which must not be conflated:

1. Barvinsky–Gusev–Zhytnikov–Vilkovisky covariant perturbation theory supplies generic third-order nonlocal form factors and spectral representations for Laplace-type operators (`arXiv:0911.1168`).
2. The Vilkovisky unique effective-action calculation for quantum Einstein gravity supplies gauge/parametrization-independent one-loop divergent authority (`arXiv:2006.04217`).
3. Pure-gravity one-loop integrand technology can include graviton/ghost combinatorics, but an ordinary gauge-fixed off-shell vertex is not itself a physical RQIR comparator column.

Iteration 231 therefore does **not** repeat the generic-CPT3 audit. It checks whether newer work closes the missing *intersection* of these ingredients.

## Fresh 2025–2026 authority check

### 1. 2025 Vilkovisky-DeWitt black-hole application

Calmet, Giusti and Sebastianutti, `arXiv:2506.09489` / EPL 150 (2025) 69001, explicitly state that they work **to second order in curvature**. Their nonlocal unique action contains the familiar curvature-bilinear structures

`R log(Box/mu^2) R`, `R_mn log(Box/mu^2) R^mn`, `R_mnrs log(Box/mu^2) R^mnrs`,

with quoted graviton coefficients, but it does not provide the finite curvature-cubic form-factor set needed for the RQIR nonlinear linked cut.

### 2. 2026 Vilkovisky-DeWitt phenomenology remains curvature-bilinear

The 2026 unique-effective-action applications found in the fresh audit likewise formulate the calculable universal nonlocal sector at second order in curvature. This strengthens physical use of the VD framework, but does not supply a pure-gravity finite `R^3` nonlocal specialization.

### 3. 2025–2026 effective-action measure/gauge literature

Recent work on diffeomorphism invariance of the gravitational path-integral measure and on gauge/parametrization dependence sharpens the warning that a formally covariant gauge-fixed determinant is not automatically interchangeable with the unique off-shell effective action. These papers do not provide the missing finite nonlocal curvature-cubic graviton+ghost unique-action coefficients.

### 4. Generic third-order covariant perturbation theory remains necessary but insufficient

`arXiv:0911.1168` still supplies the general third-order basis and form factors for generic differential operators. However, using it for the RQIR off-shell comparator requires a **fully specified VD covariant Hessian**, including the field-space connection contribution, together with the gravity ghost sector and a consistent reduction to the four-dimensional cubic-curvature basis. No fresh publication located in this audit performs this complete pure-Einstein finite nonlocal specialization in a form directly usable for the RQIR source convention.

## Minimal missing object

The blocker can now be stated more narrowly than in Iteration 207.

What is missing is an executable coefficient map

`{Gamma_A(Box1,Box2,Box3)}_VD,pure-Einstein`

for the finite one-loop curvature-cubic nonlocal action

`Delta Gamma^(1)_VD |_(R^3, finite) = sum_A integral sqrt(-g) I_A Gamma_A(Box1,Box2,Box3)`,

where all of the following are fixed **from one declared quantum operator convention**:

1. the Vilkovisky covariant Hessian `S_;ij = S_,ij - Gamma^k_ij S_,k` for Einstein gravity;
2. gauge fixing and Faddeev–Popov ghost operators compatible with that unique-action construction;
3. the complete finite CPT3 reduction into an independent 4D curvature-cubic basis;
4. the same renormalization/normalization convention used to identify `K2` and the nonlinear response;
5. a controlled continuation of the resulting form factors to the retarded/source-completed hard-channel discontinuity entering `T_cut = D Gamma3_ret,soft - W[D K2]`.

The first three items are the **minimal Euclidean specialization blocker**. The fifth is a subsequent Lorentzian/source-completion blocker and should not be used to obscure the more immediate missing calculation.

## Scientific classification

`BLOCKED_C5_VD_NONLOCAL_CUBIC_SPECIALIZATION`

with sharper current-funnel substatus

`BLOCKED_MINIMAL_VD_COVARIANT_HESSIAN_TO_FINITE_CPT3_COEFFICIENT_MAP`.

This is:

- not a consistency FAIL of quantum Einstein gravity;
- not an exact comparator identity;
- not regime-specific near-degeneracy;
- not evidence that the C5 nonanalytic column is zero;
- not a Candidate Gravity novelty certificate.

## Heavy-computation decision

A heavy symbolic CPT3 run is **not yet authorized**. Generic gauge-fixed graviton+ghost Hessian substitution would only reproduce an off-shell gauge-dependent object and would violate the frozen RQIR rule. The next useful calculation must first freeze the explicit VD covariant Hessian/operator convention and verify that the connection terms can be represented in the CPT3 machinery without an untracked model/gauge choice.

## Retained results

- `C5-CUT-014 — 2025_2026_VD_APPLICATIONS_STILL_SUPPLY_CURVATURE_BILINEAR_NONLOCAL_GRAVITY_AUTHORITY_NOT_THE_REQUIRED_FINITE_R3_SPECIALIZATION`.
- `C5-CUT-015 — THE_MINIMAL_C5_OFFSHELL_BLOCKER_IS_THE_PURE_EINSTEIN_VD_COVARIANT_HESSIAN_TO_FINITE_CPT3_COEFFICIENT_MAP`.
- `REL-NG-011 — GENERIC_CPT3_FORM_FACTORS_MUST_NOT_BE_COMBINED_WITH_A_SEPARATE_GAUGE_FIXED_GRAVITY_HESSIAN_AND_CALLED_A_UNIQUE_RQIR_COMPARATOR`.
- `NG-FUNNEL-087 — NO_ANSATZ_PROMOTION_IS_ALLOWED_WHILE_THE_C5_UNIQUE_ACTION_CUBIC_COEFFICIENT_MAP_REMAINS_UNAVAILABLE`.

## Candidate state

Robust Candidate Gravity residual: `NONE`.  
`ANSATZ-003`: `NOT_CREATED`.  
Fisher/resources: `FORBIDDEN`.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 230. The C5 blocker is materially narrower, but no additional comparator coordinate has become physically executable, so comparator foundation remains `24/25` and robust unique residual remains `0/20`.

## Exact next gate

Iteration 232: freeze the **explicit pure-Einstein Vilkovisky covariant Hessian operator convention** suitable for expansion around the RQIR background, including field-space metric/connection, gauge condition and ghost operator, and determine whether the connection-dependent terms can be reduced to a minimal Laplace-type (or controlled nonminimal) operator set accepted by CPT3. If yes, implement only that operator-level reduction and unit-test the known divergent `R^2` coefficients before any finite `R^3` computation. If no unique executable operator convention can be frozen from published authority, retain C5 as `BLOCKED` and return to the AS linked-relation boundary rather than fitting or inventing a representative.
