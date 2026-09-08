# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **596**.
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
- **Iter596 prospectively freezes and raw-validates that missing full nonlinear Ward contract and its one-leg reduction. This is a contract/reduction PASS only, not a nonlinear Ward PASS/FAIL.**

## Iter596 raw authority
Contract: `candidate_gravity/contracts/ITERATION596_NONLINEAR_WARD_CONTRACT.md`.

Classification:
`PASS_PROSPECTIVE_FULL_NONLINEAR_WARD_CONTRACT_FREEZE_AND_ONE_LEG_REDUCTION__NON_RESIDUAL`.

Canonical provenance:
- contract commit `ff3777613e85a23fc2f13c474cffc21bf155cae2`;
- audit-code commit `741d67d3992689e9e63c83c43936ebc084711d7f`;
- run/head commit `ad06a639b7d8e31fee1111e1c84c8b2018b416d0`;
- run `34230071486`, job `102073684316`;
- artifact `10057381903`, digest `sha256:cb066bda0040be91eb63ffe41e5e53ed336231d97a2ef3f69eb28847d8806ecd`;
- raw result SHA-256 `314d23356df4d1ce1213b6783d2e5420ef496ea41932bb9462f005b972907868`;
- raw authority-audit SHA-256 `829ac0d5e07bbc8da613877b329a81b0a3fae166b7c44d915c7d40916051f674`.

Raw audit has `failures=[]`. Exact Iter368/588 fixture momentum closure is `0.0`; max candidate-q2 drift is `5.551115123125783e-17`. Spectator-free reduction reproduces the Iter587 coefficients for `s={1,0.34,0.14}` within `1.1102230246251565e-16`.

## Frozen nonlinear Ward convention
Use `f(x)=int exp(-ik.x) f(k)` and stripped generator `Delta_xi=i delta_xi`.

For the later full cubic source Ward gate, all five classes are mandatory:
1. gauge-leg linear contraction;
2. spectator-u Lie derivative;
3. spectator-v Lie derivative;
4. left scalar/source endpoint transformation;
5. right scalar/source endpoint transformation.

The exact Iter588 three-mode fixture is inherited rather than retyped. No new momentum split, gauge normalization, result-dependent polarization or family deletion is permitted. The spectator-free limit must reproduce Iter587 exactly.

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

Readiness change from Iter595: **0 percentage points**. Iter596 closes a protocol prerequisite but does not yet establish full nonlinear Ward consistency or a robust comparator-subtracted residual.

## Exact next gate
Evaluate the complete same-parent Iter594 cubic Green-function response for all three cyclic gauge-leg choices under the frozen Iter596 recursion. The numerical object must retain K3 + all six K1/K2 placements + all six ordered K1^3 chains and must include both spectator Lie-derivative terms and both scalar/source endpoint terms.

A valid implementation should cross-check that its cubic Green-function coefficient reproduces the already-authoritative Iter594 assembly on the inherited probes before any Ward classification. The Ward result must then be raw-consumed fail-closed. Negative results are retained.

Only after full source-level Ward closure may source-to-Iter582/native-linked mapping be attempted, followed by the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.

Until that gate closes:
- do not perform Source/Born subtraction;
- do not map an incomplete or un-Ward-closed source response into Iter582/comparator quotient;
- do not create `ANSATZ-003`;
- do not run Fisher/resources.

The fixed comparator quotient remains **operational BLOCKED**.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc estimator, altered normalization, changed q2 grouping, premature Source/Born subtraction, threshold weakening, ansatz tuning, or unproved internal repartition. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
