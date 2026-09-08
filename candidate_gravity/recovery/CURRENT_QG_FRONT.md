# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **592**.
- Frozen Iter424 is **5/5 PASS**; post-Iter580 unresolved physical set is `[]`.
- Iter581 exact15 `Tr U1^2` is raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}` assembly is PASS, non-residual.
- Iter583–584 close the same-parent MSSC-001 quadratic K2 contact and mixed bilinear `K2(h1,h2)`.
- Iter586 proves the Iter582 timelike buckets require off-shell MSSC source completion.
- Iter587 raw-validates symmetric off-shell K1 routing and the inverse-propagator Ward term.
- Iter588 binds source routing to the exact Iter368/Iter582 three-mode singleton/pair fixture with both block orientations.
- Iter589 raw-validates relative K1/K2 normalization from one scalar inverse kernel.
- Iter590 proves cubic source-response completeness requires K3 + six K1/K2 + six K1^3 families.
- Iter591 raw-validates that local MSSC K3 is nonzero but ordinary finite hard-channel `D_s K3=0`; K3 must still be retained in the full same-action source Ward tree until gauge closure is tested.
- **Iter592 raw-validates that K1^3 is a nonzero meromorphic scalar-source tree family: it has scalar poles but no ordinary finite branch cut away from poles. Its assignment to the frozen native linked `T_cut` is BLOCKED pending an explicit source-to-observable distributional map.**

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`, q2 buckets kept distinct:
- Candidate `q^2=-1.0`: `+0.0003272233895861266 i`;
- Candidate `q^2=-0.34`: `-0.00371666346186323 i`;
- Candidate `q^2=-0.14`: `-0.0007997265433511544 i`.

No Source/Born subtraction has been performed.

## Source convention / routing authority
Candidate uses `eta=(-+++)` and timelike `s=-q^2`; MSSC-001 uses `eta=(+---)`. Same physical source buckets are `q^2=s={1,0.34,0.14}`. With `m=0.7`, all lie below `4m^2=1.96`, so the matched source must be off-shell/source-completed.

Iter587 freezes `q=(sqrt(s),0,0,0)`, `p=-q/2`, `p'=+q/2`, with `q_mu V^{mu nu}=(m^2-s/4)q^nu`. Iter588 binds this to the exact Iter368 fixture modes `s,a,b`. Iter589 fixes the single MSSC inverse kernel `K[g]=-p'_cov (sqrt(-g) g^-1) p_cov + m^2 sqrt(-g)`; no independent K1/K2 sign/factor is permitted.

## Cubic source-response authority
For `G=K^-1`,

`d_abc G = -G Kabc G + sum_6(G Ki G Kjk G) - sum_6(G Ki G Kj G Kk G)`.

Thus a complete same-action cubic source tree contains:
1. local K3 contact;
2. six K1/K2 placements;
3. six ordered K1^3 chains.

Iter591 closes only the direct ordinary branch-cut origin of K3: `D_s K3=0` for the local analytic contact. It does not authorize removing K3 from the source Ward tree.

Iter592 closes only the ordinary finite branch-cut origin of K1^3 away from scalar poles. K1 is polynomial, while internal `G=1/(m^2-p^2)` factors are meromorphic. Exact frozen fixture K1^3 sums remain nonzero:
- `s`: `-0.000386885483743436`, minimum internal `|K0|=0.24`;
- `a`: `-0.0005328911177533087`, minimum internal `|K0|=0.145`;
- `b`: `+0.00012109066165593845`, minimum internal `|K0|=0.005`.

Canonical Iter592 raw authority:
- run `34214083326`;
- job `102021606620`;
- head `57b3a430abe387376376bd559c7f66cd7fa230f4`;
- artifact `10051001153`, digest `sha256:d3d0e4e4e57bbe047dc8019bd159d3434118542b4c28696a88692e97ac9f7c21`;
- result SHA256 `f2765720fddaf578df48bfaf40820c66412282f81968d4ad77a04a940aac94a6`;
- authority audit SHA256 `34eeaed0819efe1bd8942052acd3b67d119f9b795899cf5b04991c6b303c20eb`;
- audit `PASS_RAW_AUTHORITY_AUDIT_ITER592_K1CUBED_ORIGIN`, failures `[]`.

Binding status:
- `ordinary_finite_branch_cut_D_s_K1cubed = ZERO_AWAY_FROM_POLES`;
- `K1cubed_under_frozen_linked_T_cut = BLOCKED__NEEDS_EXPLICIT_SOURCE_TO_T_CUT_DISTRIBUTIONAL_MAP`;
- `K1K2_only_as_complete_discontinuity_source_block = NOT_AUTHORIZED`;
- Source/Born subtraction = `NOT_PERFORMED`.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iter591–592 close origin-classification subquestions but do not create a matched comparator-subtracted residual or close a full rubric sector.

## Exact next gate / blocker
Construct and prospectively freeze the matched source-to-native-linked-observable distributional map that states how MSSC scalar propagator pole terms project, or provably do not project, into the existing split-invariant `Y=(K2,S_soft2_full)` / linked `T_cut` protocol. Do not equate an off-shell scalar-source pole discontinuity with the native pure-gravity linked cut by label alone.

Until that map exists:
- retain K1^3 and K3 in the full same-action source Ward tree;
- do not call the six K1/K2 placements the complete discontinuity-bearing source block;
- do not perform Source/Born subtraction;
- do not map an incomplete source response into Iter582/comparator quotient.

No independent heavy Candidate-Gravity gate is presently authorized by repo authority without this prerequisite. Blind full-C5, ANSATZ-003, Fisher/resources, or residual promotion would violate frozen guardrails.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc estimator, altered normalization, changed q2 grouping, premature Source/Born subtraction, threshold weakening, ansatz tuning, or unproved internal repartition. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
