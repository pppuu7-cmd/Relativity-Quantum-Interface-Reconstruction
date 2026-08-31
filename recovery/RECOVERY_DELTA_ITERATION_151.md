# Recovery Delta — RQIR Iteration 151

**Date:** 2026-08-31  
**Authoritative change:** the exact Einstein-Hilbert off-shell source-completed Ward identity is now implemented and numerically passed on the frozen six-probe protocol.

## Previous front

Iteration 150 produced the first explicit local tree C5 nonlinear-response tangent but left `BLOCKED_WARD_TAKAHASHI_COMPLETION` because an isolated longitudinal replacement of the off-shell EH three-vertex is nonzero.

## New result

The correct action-level cubic-order diffeomorphism identity in the frozen `g=eta+kappa h` convention is

`B3[L_xi,e2,e3] + B2[Lie_xi e2,e3] + B2[e2,Lie_xi e3] = 0`.

The two `B2` terms are the nonlinear Lie/inverse-propagator/source-contact completion missing from the naive `k.Gamma3=0` test.

On all six frozen probes, halving the finite-difference steps gives maximum residuals

`2.5767566e-5 -> 6.4418544e-6 -> 1.6104613e-6`,

with ~4x reduction each time, and finest-step worst relative residual `2.7240026e-6`.

Therefore the EH source-completed Ward identity is **PASS_SCOPED**.

Authorities:
- `analysis/c5_ward_identity_iteration151.py`;
- `results/c5_ward_identity_iteration151.json`;
- `candidate_gravity/C5_WARD_IDENTITY_ITERATION151.md`;
- `research_log/2026-08-31_iteration_151_c5_ward_identity.md`.

## Retained methodological result

`NG-FUNNEL-010` remains retained: an isolated off-shell longitudinal-null test is invalid. Iteration 151 does not remove that negative result; it replaces the invalid gate with the correct completed identity and shows that EH passes it.

## Exact restart instruction

Resume at **Iteration 152**:
1. test the two existing covariant curvature-cubic directions under the same action-level diffeomorphism identity;
2. keep any column that fails due implementation/convention error separate from a genuine consistency FAIL;
3. if both pass, expand the finite local C5 tangent or instantiate the first fixed C3 comparator tangent;
4. keep higher-dimension unsupported and loop/nonanalytic columns explicitly BLOCKED;
5. no Fisher/resources and no `ANSATZ-003` before a nonzero algebraic residual survives the concrete fixed comparator quotient.
