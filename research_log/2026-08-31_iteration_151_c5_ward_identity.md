# RQIR Candidate Gravity Research Log — Iteration 151

Date: 2026-08-31

Started from authoritative Iteration 150 after checking `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_150.md`, the latest research log, and recent commits.

## Work performed

Derived the off-shell EH Ward identity directly from diffeomorphism invariance of the same unreduced action used in Iteration 150. Instead of imposing the invalid isolated condition `k.Gamma3=0`, the implemented identity is

`B3[L_xi,e2,e3] + B2[Lie_xi e2,e3] + B2[e2,Lie_xi e3] = 0`.

Implemented `analysis/c5_ward_identity_iteration151.py` and evaluated this completed action-level identity on the same six frozen spacelike probes.

## Numerical result

Across step pairs `(d3,d2)=(2e-3,2e-4),(1e-3,1e-4),(5e-4,5e-5)`, the worst absolute residual decreases

`2.5767566e-5 -> 6.4418544e-6 -> 1.6104613e-6`, with reduction factors ~4 at each halving.

Finest-step worst relative residual: `2.7240026e-6`.

This is the expected second-order convergence of the centered finite-difference extraction and certifies cancellation of the isolated longitudinal cubic variation by the nonlinear Lie/source-contact variation of the quadratic EH action.

## Status

PASS_SCOPED:
- EH source-completed off-shell Ward identity on the six frozen probes;
- interpretation of `NG-FUNNEL-010` confirmed: isolated longitudinal null is an invalid gate, while the correct completed identity passes.

BLOCKED:
- equivalent source-completed Ward validation for the two curvature-cubic EFT directions;
- higher-dimension local C5 columns;
- loop/nonanalytic C5 columns;
- N2/C3sym;
- full fixed comparator quotient.

No Fisher/resources. No `ANSATZ-003`.

## Next

Iteration 152: validate the two existing covariant curvature-cubic columns under the same action-level diffeomorphism identity, then decide whether to expand the finite local C5 basis or instantiate the first fixed C3 tangent.
