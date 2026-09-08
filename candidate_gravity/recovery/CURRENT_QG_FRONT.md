# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **598**.
- Frozen Iter424 is **5/5 PASS**; post-Iter580 unresolved physical set is `[]`.
- Iter581 exact15 `Tr U1^2` is raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}` assembly is PASS, non-residual.
- Iter583–584 close the same-parent MSSC-001 quadratic K2 contact and mixed bilinear `K2(h1,h2)`.
- Iter586 proves the Iter582 timelike buckets require off-shell MSSC source completion.
- Iter587 raw-validates symmetric off-shell K1 routing and the inverse-propagator Ward term.
- Iter588 binds source routing to the exact Iter368/Iter582 three-mode singleton/pair fixture with both block orientations.
- Iter589 fixes relative K1/K2 normalization from one scalar inverse kernel.
- Iter590 proves cubic source-response completeness requires K3 + six K1/K2 + six K1^3 families.
- Iter591 raw-validates local MSSC K3 as nonzero but ordinary finite hard-channel `D_s K3=0`; K3 remains in the complete source Ward tree.
- Iter592 raw-validates K1^3 as nonzero meromorphic scalar-source tree family with scalar poles but no ordinary finite branch cut away from poles.
- Iter593 closes family-by-family source-to-`T_cut` projection negatively: individual K1^3 pole assignments are not themselves frozen observables under the Iter183 split-invariant protocol.
- Iter594 explicitly assembles the complete routed same-action cubic source object containing K3 + all six K1/K2 placements + all six ordered K1^3 chains; it is finite/nonzero/permutation-symmetric on inherited probes but explicitly NON_WARD.
- Iter595 finds the full cubic nonlinear diffeomorphism Ward target underdetermined until spectator-graviton and scalar/source endpoint transformations are prospectively frozen.
- Iter596 prospectively freezes and raw-validates the full nonlinear Ward contract and one-leg reduction.
- Iter597 produced converged negative numbers, but independent review found that its implemented anchor and full Ward rows used arbitrary `PROBES`, not the exact per-gauge symmetric scalar route frozen in Iter596; therefore those numbers are preserved as diagnostics but are **not** frozen-contract Ward authority.
- **Iter598 raw-validates that contract mismatch fail-closed.**

## Iter598 raw authority
Classification:
`BLOCKED_ITER597_IMPLEMENTATION_DOES_NOT_INSTANTIATE_FROZEN_ITER596_ROUTE__NEGATIVE_NUMBERS_PRESERVED_NONAUTHORITATIVE`.

Canonical provenance:
- audit code commit `5cd2e62fd68dca1d5b8910adf7beae6e601c60ea`;
- workflow/trigger head `f65c23ab46f5b4571a6fc9ce5cb39d958fd0109a`;
- run `34236177851`, job `102094351910`;
- artifact `10059929340`, digest `sha256:abf81c0cc102980501618516d0dfe4e7117958af6063c53af9acffc67107fade`;
- raw result SHA-256 `0ba9032dc076fb7b5b420e99cdc293df839365eb97610e395c7c7cc7d7a0a291`;
- raw authority-audit SHA-256 `e868c8fb917c2be3b37faced7c005569d9cad2c7c733221703fec835ce2b62f7`.

The mismatch is specific and does not weaken Iter596: the mandatory reduction and Ward evaluation must use `p=-q_g/2`, `p'=+q_g/2` for each gauge singleton. Unsupported/off-contract output is BLOCKED, never promoted by zero-fill or by workflow colour.

## Frozen nonlinear Ward convention
Use `f(x)=int exp(-ik.x) f(k)` and stripped generator `Delta_xi=i delta_xi`.

For the full cubic source Ward gate, all five classes are mandatory:
1. gauge-leg linear contraction;
2. spectator-u Lie derivative;
3. spectator-v Lie derivative;
4. left scalar/source endpoint transformation;
5. right scalar/source endpoint transformation.

The exact Iter588 three-mode fixture is inherited rather than retyped. No new momentum split, gauge normalization, result-dependent polarization or family deletion is permitted. The spectator-free limit must reproduce Iter587 exactly. The scalar route attached to gauge leg `g` is exactly `p=-q_g/2`, `p'=+q_g/2`.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`, q2 buckets kept distinct:
- Candidate `q^2=-1.0`: `+0.0003272233895861266 i`;
- Candidate `q^2=-0.34`: `-0.00371666346186323 i`;
- Candidate `q^2=-0.14`: `-0.0007997265433511544 i`.

No Source/Born subtraction has been performed.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change from Iter596: **0 percentage points**. Iter598 closes an implementation/authority ambiguity but does not establish nonlinear Ward consistency or a comparator-subtracted residual.

## Exact next gate
Prospectively repair the Iter597 evaluator and rerun the full same-parent nonlinear Ward gate using the exact per-gauge symmetric scalar route `p=-q_g/2`, `p'=+q_g/2` for both the mandatory anchor and full Ward rows. Retain K3 + all six K1/K2 placements + all six ordered K1^3 chains, both spectator Lie terms, both endpoint terms, and the pre-existing frozen numerical thresholds. The Iter594 cubic family cross-check may remain on its inherited probes only as an implementation cross-check; it must not replace the frozen Ward route.

The corrected run must be raw-consumed fail-closed. Negative corrected results are retained as scientific results.

Only after full source-level Ward closure may source-to-Iter582/native-linked mapping be attempted, followed by the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.

Until that gate closes:
- do not perform Source/Born subtraction;
- do not map an incomplete or off-contract source response into Iter582/comparator quotient;
- do not create `ANSATZ-003`;
- do not run Fisher/resources.

The fixed comparator quotient remains **operational BLOCKED**.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc estimator, altered normalization, changed q2 grouping, premature Source/Born subtraction, threshold weakening, ansatz tuning, or unproved internal repartition. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
