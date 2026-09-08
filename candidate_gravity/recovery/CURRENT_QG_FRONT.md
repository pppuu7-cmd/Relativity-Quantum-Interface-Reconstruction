# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **589**.
- Frozen Iter424 is **5/5 PASS**; post-Iter580 unresolved physical set is `[]`.
- Iter581 frozen Iter412 exact15 `Tr U1^2` is raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}` frozen-weight assembly is PASS, non-residual.
- Iter583 fixes the quadratic MSSC-001 source/contact K2 prerequisite from the same covariant scalar parent action.
- Iter584 polarizes this into the mixed bilinear source contact `K2(h1,h2)` and is raw-valid PASS, non-residual.
- Iter586 is raw-valid PASS for the signature/invariant audit: the physical Iter582 timelike buckets require an off-shell MSSC source completion. Iter585 Breit elastic algebra is retained internally but is not a matched bridge to Iter582.
- Iter587 prospectively freezes and raw-validates the symmetric off-shell K1 routing and exact Ward longitudinal term from the same Iter218 MSSC-001 parent dynamics.
- Iter588 is raw-valid fixture-binding authority: on the exact Iter368/Iter582 three-mode fixture, each singleton `s/a/b` is paired with the complementary mixed K2 pair and both `K1->K2` / `K2->K1` block orientations are retained. No new split parameter is introduced.
- Iter589 prospectively freezes and raw-validates the same-action relative K1/K2 normalization before any cancellation test.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`, q2 buckets kept distinct:
- Candidate `q^2=-1.0`: `+0.0003272233895861266 i`;
- Candidate `q^2=-0.34`: `-0.00371666346186323 i`;
- Candidate `q^2=-0.14`: `-0.0007997265433511544 i`.

No Source/Born subtraction has been performed.

## Source convention bridge authority
Candidate discontinuity calculations use `eta=(-+++)` and timelike `s=-q^2`. MSSC-001 uses `eta=(+---)`. The same physical buckets therefore map to source `q^2=s={1,0.34,0.14}`.

For MSSC scalar mass `m=0.7`, all three source timelike values are below the two-scalar threshold `4m^2=1.96` and cannot be realized as an on-shell equal-mass elastic momentum difference. The matched source observable is therefore off-shell/source-completed.

## Iter587 frozen off-shell K1 routing
Parent authority is the Iter218 MSSC-001 action and exact Ward identity
`k_mu V^{mu nu}=(p'^2-m^2)p^nu-(p^2-m^2)p'^nu`.

For each `s={1,0.34,0.14}`:
`q=(sqrt(s),0,0,0), p=-q/2, p'=+q/2, k=q` under MSSC `(+---)`.
Then
`q_mu V^{mu nu}=(m^2-s/4) q^nu`.

Exact longitudinal coefficients:
- `s=1`: `6/25 = 0.24`;
- `s=0.34`: `81/200 = 0.405`;
- `s=0.14`: `91/200 = 0.455`.

## Iter588 fixture-bound source routing
The exact Iter368 parent fixture has three modes `s,a,b` with total momentum closure. For each singleton, the complementary two modes are the K2 input pair. In MSSC source convention the scalar routing is `p=-q/2 -> p'=+q/2` under K1(singleton), then the complementary K2 pair carries total momentum `-q` and returns the same scalar line to `p`. Both block orientations remain mandatory. Classification: `PASS_ITER582_FIXTURE_BOUND_MSSC_K1_K2_ROUTING_CONTRACT__NON_RESIDUAL`.

## Iter589 same-action K1/K2 normalization
Use one scalar inverse kernel

`K[g]=-p'_cov (sqrt(-g) g^-1) p_cov + m^2 sqrt(-g)`

from the frozen MSSC-001 parent action, `eta=(+---)`, `m=0.7`.

Its first variation is

`K1(h;p',p)=-p'_cov a1(h) p_cov + m^2 b1(h)=(1/2) h_{mu nu} V^{mu nu}(p',p)`.

Its mixed second variation is

`K2(h1,h2;p',p)=-p'_cov bt(h1,h2) p_cov + m^2 bs(h1,h2)`,

with the exact Iter584 mixed geometric coefficients. Therefore no independent relative sign or factor between K1 and K2 is permitted.

Canonical Iter589 provenance:
- prospective script commit `c9f4b337a298b656bf0c3181a55b80b2dc52c6c5`;
- workflow commit `50146e43c520a29812eec430cd1143f150b3c652`;
- run `34209731847`;
- artifact `10049270625`;
- raw `result.json` SHA256 `90cd8591f34deb9a7c0d49a21d554bc8f776c5c2fdbef30cbcd88455b2a0dfad`;
- audit `PASS_RAW_AUTHORITY_AUDIT_ITER589_K1_K2_NORMALIZATION`, failures `[]`;
- max `|K1-(1/2)h.V| = 1.1102230246251565e-16`;
- max pure-gauge Ward mismatch `3.552713678800501e-15`;
- frozen tolerance `2e-12`.

Classification: `PASS_MSSC001_K1_K2_SAME_ACTION_NORMALIZATION_CONTRACT__NON_RESIDUAL`.

This is not the full nonlinear Ward cancellation, not a source-tree value, not a comparator identity/residual, not a Candidate-Gravity consistency PASS/FAIL, and not a novelty certificate.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iter588 removes the remaining source-routing split ambiguity and Iter589 closes the relative-normalization hard constraint, but the complete same-fixture Ward object and comparator-subtracted residual remain open; no full rubric sector closes.

## Exact next gate
Using exactly the Iter589 normalization, Iter588 singleton/pair routing, both frozen block orientations, and Iter584 mixed contact, assemble the complete same-fixture `K1-G-K2 + K2-G-K1` source response. Test the correct off-shell Ward identity including the Iter587 inverse-propagator RHS before any mapping to Iter582. Only after this same-dynamics Ward object is closed may the unchanged fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient be applied.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc estimator, altered normalization, changed q2 grouping, premature Source/Born subtraction, threshold weakening, or ansatz tuning. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
