# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **583**.
- Frozen Iter424 is **5/5 PASS**; post-Iter580 unresolved physical set is `[]`.
- Iter581 frozen Iter412 exact15 `Tr U1^2` is raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}` frozen-weight assembly is PASS, non-residual.
- Iter583 closes the quadratic MSSC-001 source/contact K2 prerequisite from the same covariant scalar parent action.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`, q2 buckets kept distinct:
- `q^2=-1.0`: `+0.0003272233895861266 i`;
- `q^2=-0.34`: `-0.00371666346186323 i`;
- `q^2=-0.14`: `-0.0007997265433511544 i`.

No Source/Born subtraction has been performed.

## Iter583 frozen MSSC-001 source K2 authority
Parent source action from Iter218:
`S_phi=-1/2 int sqrt(-g)[g^{mu nu} partial_mu phi partial_nu phi + m^2 phi^2]`, `g=eta+kappa h`, eta signature `(+---)`.

Canonical workflow provenance:
- run `34202716523`, job `101984987191`;
- head `82b2bf6b19d2afba7d42beae9617e51e2e940d71`;
- artifact `10046459699`, digest `sha256:1500ee5d9798966074312915c467438bfba0037e179a58b2a376f009cf4187a0`;
- independently consumed `result.json` SHA256 `824c9d06a6b8dc13f4ebd8ac8300bcb243621cba72a8f0641159dad96e3df10f`;
- audit `PASS_RAW_AUTHORITY_AUDIT_ITER583_SOURCE_K2`, `failures=[]`.

Frozen quadratic coefficients:
- `sqrt(-g)|kappa2 = h^2/8 - Tr(H^2)/4`;
- `[sqrt(-g)g^-1]|kappa2 = eta^-1 h eta^-1 h eta^-1 -(h/2)eta^-1 h eta^-1 +(h^2/8-Tr(H^2)/4)eta^-1`.

Classification: `PASS_SOURCE_K2_QUADRATIC_CONTACT_FROM_FROZEN_MSSC001__NON_RESIDUAL`.
This is a source/contact prerequisite only, not a comparator residual or Candidate-Gravity model PASS.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. The K2 contact prerequisite is real progress but no full model-level rubric sector closed.

## Exact next gate
Polarize the frozen quadratic K2 coefficient into the explicit mixed bilinear two-graviton source contact `K2(h1,h2)` and validate it against the mixed second derivative of the exact MSSC-001 covariant source density. If raw-valid, use K1 exchange plus this K2 contact to construct the matched conserved-source tree/Ward object, classify pole/cut origin, and only then map to the Iter582 q2-resolved operator coordinate before applying the unchanged comparator quotient.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc estimator, altered normalization, changed q2 grouping, premature Source/Born subtraction, threshold weakening, or ansatz tuning. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
