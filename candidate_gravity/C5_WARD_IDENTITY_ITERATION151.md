# C5 Source-Completed Off-Shell Ward Identity — Iteration 151

## Scope

This iteration closes the immediate `BLOCKED_WARD_TAKAHASHI_COMPLETION` blocker for the exact Einstein-Hilbert cubic sub-block used in Iteration 150. It does **not** certify the full C5 EFT tangent, loop/nonanalytic sector, or any new ansatz.

The frozen convention remains `g_{mu nu}=eta_{mu nu}+kappa h_{mu nu}`, with the same six spacelike triplets and unreduced `sqrt(-g) g Gamma Gamma` Einstein-Hilbert action implementation.

## Identity actually tested

For one infinitesimal diffeomorphism mode `xi(k1)` and two metric modes `h2(k2), h3(k3)` with `k1+k2+k3=0`, diffeomorphism invariance of the action gives, at cubic order,

`B3[L_xi, h2, h3] + B2[Lie_xi h2, h3] + B2[h2, Lie_xi h3] = 0`.

Here `L_xi` is the linear metric gauge variation and `Lie_xi h` is the nonlinear Lie-derivative part. The two quadratic terms are exactly the inverse-propagator/source-contact completion that is absent from the naive isolated test `k.Gamma3=0`.

This action-level form is preferable for the present repository because it follows directly from the same declared EH dynamics and field convention, without importing an incompatible amputated-vertex normalization.

## Numerical certificate

The identity was evaluated on all six frozen off-shell probes with three nested finite-difference scales. The maximum absolute residual behaves as

- `2.5767566291e-5` at `(d3,d2)=(2e-3,2e-4)`;
- `6.4418544161e-6` at `(1e-3,1e-4)`;
- `1.6104612568e-6` at `(5e-4,5e-5)`.

The reduction factors are approximately `4.00002` and `4.00001`, matching the expected second-order central-difference convergence. At the finest tested step the worst relative residual is

`2.7240025570e-6`.

Therefore the previously nonzero longitudinal cubic response is quantitatively cancelled by the nonlinear Lie/source-contact contribution, to a residual that converges to zero with the discretization error.

## Scientific status

**EH off-shell source-completed Ward identity: PASS_SCOPED.**

This resolves `NG-FUNNEL-010` in the intended sense: the negative result remains valid as a methodological warning (`isolated longitudinal null is the wrong gate`), while the correct completed identity passes for the EH block.

This is **not** a certificate for the two curvature-cubic EFT columns. Their own source-completed Ward covariance must either be checked directly from their covariant actions or kept scoped to TT response only.

## Literature consistency

The result is consistent with the standard gravitational Ward/Slavnov-Taylor structure: off-shell gauge identities relate higher vertices to lower inverse-propagator/contact structures rather than requiring an isolated three-vertex contraction to vanish. DeWitt's covariant perturbative gravity framework and later BRST/Slavnov-Taylor treatments make this distinction explicit.

## Consequence for the funnel

The immediate EH Ward blocker is closed. The full C5 comparator remains incomplete because higher local columns, loop/nonanalytic directions, `N2`, and `C3sym` are still not instantiated. Fisher/resources and `ANSATZ-003` remain forbidden.

The next scientifically useful gate is to validate the two existing covariant curvature-cubic columns under the same action-level diffeomorphism identity; if they pass, extend the finite local C5 tangent before moving to a fixed C3 comparator.
