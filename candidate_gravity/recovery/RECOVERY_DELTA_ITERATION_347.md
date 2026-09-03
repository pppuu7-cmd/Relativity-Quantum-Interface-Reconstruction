# Recovery Delta — Candidate Gravity Iteration 347

Date: 2026-09-03

## Scope

Fail-closed matched-timelike rebase contract joining the frozen U2 authorities from Iterations 339/341/342/345/346 to the exact Iteration-332 closed timelike triad. This gate does not create a physical `Tr U2` numerator and does not authorize cut integration by itself.

## Raw Actions authority

- run: `33776852072`
- artifact: `9901922754` (`iteration347-result`)
- artifact digest: `sha256:c3aaa23fe14bdcb6d7a01186d5f640955a503f3739ae706b7b4300da361a0f82`
- scientific JSON SHA-256: `f8d246b316d744f16c649cce7e7bd840d37696297891fbc8b6d64320c5cf30b5`
- workflow head: `c7f787acfa7336463f9e73b4e39afd5e24f08689`

The raw artifact and authority-audit JSON were downloaded and inspected. Workflow green status alone was not treated as scientific authority.

## Result

The exact Iteration-332 triad is recovered with closure error `0.0` and invariants `(-1.0, -0.14, -0.34)` to maximum error `5.551115123125783e-17`; all three legs are timelike in signature `(-,+,+,+)`.

All binding source conventions were present in the current repository versions of the frozen providers:

- Iteration 339: shifted graviton Green routing `G1=-G0(p+q) K1 G0(p)`;
- Iteration 341: physical Eq.(54)-(55) `A1/A2`, `A: field x ghost`, left `A.T`, right `A`;
- Iteration 342: `N/Y` inverse-routing bridge and flat `Y=-g` signs;
- Iteration 346/345: exact 12-route placement and functional transpose `A_T(Q;k)=A_R(Q;-k-Q)^T`.

Historical random-fixture component matrices are explicitly forbidden from being copied into the timelike calculation. The frozen formulas must be re-specialized on the exact common timelike background and evaluated at each route's cumulative incoming momentum.

Authority:

`PASS_U2_MATCHED_TIMELIKE_PHYSICAL_COMPONENT_REBASE_CONTRACT__12_ROUTE_SUBSTITUTION_AUTHORIZED_NEXT`.

## Operational determinant note

Iteration 335 replacement run `33759144658` ended in operational timeout/failure during the scientific product-quadrature step before sentinel/schema audit and artifact upload. It therefore has no new scientific PASS/FAIL authority. A third blind copy is not authorized; the determinant branch must move to symbolic/analytic angular reduction or another demonstrably non-blind method.

## Next active gate

Iteration 348 run `33777026420` was launched immediately after validating Iteration 347. It re-specializes the physical Iteration-341 `A1/A2` provider onto the exact timelike triad and the same seed-319/common-background metric tensors used by the determinant parent, retaining the frozen exact-geometry oracle and thresholds.

Still forbidden: `Tr U2` cut integration before full physical family reduction, Source/Born subtraction, `ANSATZ-003`, Fisher/resources, blind full-C5.

MODEL_READINESS: 24%

Change from Iteration 346: `0 pp`; the matched-fixture contract is now frozen, but no readiness bucket and no robust comparator-subtracted residual closed.
