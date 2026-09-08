# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **587**.
- Frozen Iter424 is **5/5 PASS**; post-Iter580 unresolved physical set is `[]`.
- Iter581 frozen Iter412 exact15 `Tr U1^2` is raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}` frozen-weight assembly is PASS, non-residual.
- Iter583 fixes the quadratic MSSC-001 source/contact K2 prerequisite from the same covariant scalar parent action.
- Iter584 polarizes this into the mixed bilinear source contact `K2(h1,h2)` and is raw-valid PASS, non-residual.
- Iter586 is raw-valid PASS for the signature/invariant audit: the physical Iter582 timelike buckets require an off-shell MSSC source completion. Iter585 Breit elastic algebra is retained internally but is not a matched bridge to Iter582.
- Iter587 prospectively freezes and raw-validates the symmetric off-shell K1 routing and exact Ward longitudinal term from the same Iter218 MSSC-001 parent dynamics.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`, q2 buckets kept distinct:
- Candidate `q^2=-1.0`: `+0.0003272233895861266 i`;
- Candidate `q^2=-0.34`: `-0.00371666346186323 i`;
- Candidate `q^2=-0.14`: `-0.0007997265433511544 i`.

No Source/Born subtraction has been performed.

## Source convention bridge authority
Candidate discontinuity calculations use `eta=(-+++)` and timelike `s=-q^2`. MSSC-001 uses `eta=(+---)`. The same physical buckets therefore map to source `q^2=s={1,0.34,0.14}`.

For MSSC scalar mass `m=0.7`, all three source timelike values are below the two-scalar threshold `4m^2=1.96` and cannot be realized as an on-shell equal-mass elastic momentum difference. Classification: `PASS_SIGNATURE_INVARIANT_AUDIT__OFFSHELL_SOURCE_REQUIRED__NON_RESIDUAL`.

Canonical Iter586 provenance:
- run `34203781256`;
- head `70b7961ad5d7bcb3a94ed63eaf2e310921a10678`;
- artifact `10046877433`, digest `sha256:73ff7295e9396953f290edc32d6d38c310f75e0c060c90e93a40ce38a2a7da6a`;
- raw `result.json` SHA256 `8e83fec148e8d0acac3578a77023890db35c070ccff38af0f44591a10cd3c8d1`;
- audit `PASS_RAW_AUTHORITY_AUDIT_ITER586_SOURCE_SIGNATURE`, `failures=[]`.

## Iter587 frozen off-shell K1 routing
Parent authority is the Iter218 MSSC-001 action and exact Ward identity
`k_mu V^{mu nu}=(p'^2-m^2)p^nu-(p^2-m^2)p'^nu`.

For each `s={1,0.34,0.14}` freeze before the full K1+K2 tree result:
`q=(sqrt(s),0,0,0), p=-q/2, p'=+q/2, k=q` under MSSC `(+---)`.
Then
`p^2=p'^2=s/4` and exactly
`q_mu V^{mu nu}=(m^2-s/4) q^nu`.

Exact longitudinal coefficients:
- `s=1`: `6/25 = 0.24`;
- `s=0.34`: `81/200 = 0.405`;
- `s=0.14`: `91/200 = 0.455`.

Canonical Iter587 provenance:
- run `34203928999`;
- head `7b80d16d2ca2d1fa7333825da6e06ab223fe7c34`;
- artifact `10046935799`, digest `sha256:8e410a0481474b2e71571a76674209d3e84e16a13aa228f17b2931b2ce622b04`;
- raw `result.json` SHA256 `1fb42e1ab8e3de2ae31426297c40f9c845ddd38e08d3f3f63cd6d4381252bcfd`;
- audit `PASS_RAW_AUTHORITY_AUDIT_ITER587_OFFSHELL_ROUTING`, `failures=[]`;
- maximum direct Ward verification error `5.551115123125783e-17`.

Classification: `PASS_PROSPECTIVE_MSSC001_SYMMETRIC_OFFSHELL_K1_ROUTING_AND_WARD_CONTRACT__NON_RESIDUAL`.
This is not a comparator residual or Candidate-Gravity model PASS.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. The convention/kinematic ambiguity and a real off-shell K1 routing/Ward subgate are closed, but the complete same-dynamics source Ward object and comparator-subtracted residual remain open.

## Exact next gate
Construct the complete two-graviton MSSC-001 source Ward object on the frozen Iter587 routing from K1 exchange plus the raw-valid Iter584 K2 contact. Verify cancellation/matching of the scalar inverse-propagator longitudinal terms before any mapping to Iter582. Only after this same-dynamics Ward object is closed may the unchanged fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient be applied.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc estimator, altered normalization, changed q2 grouping, premature Source/Born subtraction, threshold weakening, or ansatz tuning. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
