# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **590**.
- Frozen Iter424 is **5/5 PASS**; post-Iter580 unresolved physical set is `[]`.
- Iter581 exact15 `Tr U1^2` is raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}` assembly is PASS, non-residual.
- Iter583–584 close the same-parent MSSC-001 quadratic K2 contact and its mixed bilinear `K2(h1,h2)`.
- Iter586 proves the Iter582 timelike buckets require off-shell MSSC source completion; Iter585 remains an internal elastic diagnostic only.
- Iter587 raw-validates the symmetric off-shell K1 routing and inverse-propagator Ward term.
- Iter588 binds source routing to the exact Iter368/Iter582 three-mode singleton/pair fixture with both block orientations.
- Iter589 raw-validates the relative K1/K2 normalization from one scalar inverse kernel.
- **Iter590 raw-validates the cubic source-response completeness identity and proves that the six K1/K2 placements are a scoped subset, not automatically the full third mixed response: local K3 and K1^3 both have nonzero same-action support on the exact fixture.**

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`, q2 buckets kept distinct:
- Candidate `q^2=-1.0`: `+0.0003272233895861266 i`;
- Candidate `q^2=-0.34`: `-0.00371666346186323 i`;
- Candidate `q^2=-0.14`: `-0.0007997265433511544 i`.

No Source/Born subtraction has been performed.

## Source convention / routing authority
Candidate uses `eta=(-+++)` and timelike `s=-q^2`; MSSC-001 uses `eta=(+---)`. The same physical source buckets are `q^2=s={1,0.34,0.14}`. With `m=0.7`, all lie below `4m^2=1.96`, so the matched source must be off-shell/source-completed.

Iter587 freezes `q=(sqrt(s),0,0,0)`, `p=-q/2`, `p'=+q/2`, with
`q_mu V^{mu nu}=(m^2-s/4)q^nu` and exact coefficients `0.24, 0.405, 0.455` for `s=1,0.34,0.14`.

Iter588 binds this to the exact Iter368 fixture modes `s,a,b`: each singleton is paired with the complementary two modes as K2 input, and both K1->K2 and K2->K1 orientations are mandatory.

## Iter589 same-action normalization
Use the single MSSC inverse kernel
`K[g]=-p'_cov (sqrt(-g) g^-1) p_cov + m^2 sqrt(-g)`.
Then
`K1=(1/2)h_{mu nu}V^{mu nu}`
and mixed `K2` uses the raw-valid Iter584 geometric coefficients. No independent relative sign/factor is permitted.

Canonical Iter589 raw authority: run `34209731847`, artifact `10049270625`, result SHA256 `90cd8591f34deb9a7c0d49a21d554bc8f776c5c2fdbef30cbcd88455b2a0dfad`, audit PASS, failures `[]`. A later formatting-only repo byte drift was detected by Iter590 and repaired in commit `7217a6d0bb7fc6349497fd4dcf7af3fdcccff772`; no scientific content changed.

## Iter590 cubic completeness authority
For `G=K^-1`,

`d_abc G = -G Kabc G + sum_6(G Ki G Kjk G) - sum_6(G Ki G Kj G Kk G)`.

Thus the full third mixed inverse-kernel response has three origin families:
1. local mixed third contact `K3`;
2. six K1/K2 placements;
3. six ordered K1^3 chains.

Canonical successful Iter590 provenance:
- run `34210666988`;
- head `ffa700d898545048e1df7a81d0f5297e6ea0c818`;
- artifact `10049640731`, digest `sha256:804cbbaf1008a579c368001f4081d85b09c42f2504bdb19c0e6a959016a1e840`;
- result SHA256 `5ba0e9fc88b68b13d08d406829ebf4cc30e8ae85d8d92816f282d105a89d4d63`;
- authority audit SHA256 `6fa94126f8ed2a3680352a4c477afbfbe871bbc21a379631db350b102b2cbce0`;
- audit `PASS_RAW_AUTHORITY_AUDIT_ITER590_CUBIC_COMPLETENESS`, failures `[]`.

Universal regression norms:
- full response `0.004272419337809515`;
- six-K1/K2 subset `0.0009623302303630119`;
- omitted full-minus-subset `0.0035873975061226225`;
- K3 piece `0.0036081509810433035`;
- K1^3 piece `3.259073668020947e-05`.

Exact fixture support is nonzero for both omitted families for every singleton. Therefore:
- `K3_under_hard_channel_D_s = OPEN__LOCAL_ANALYTIC_PROJECTION_TO_BE_PROVED`;
- `K1cubed_under_frozen_linked_T_cut = OPEN__PROTOCOL_ORIGIN_CLASSIFICATION_REQUIRED`;
- `K1K2_only_as_complete_source_response = NOT_AUTHORIZED_YET`.

Machine consumption authority: `candidate_gravity/results/iteration590_source_cubic_completeness_raw_consumption.json`.

The first Iter590 run failed operationally only because the persisted Iter589 bytes had drifted from the raw SHA; diagnostic recovery localized this and the unchanged scientific gate subsequently passed. Operational failure is not scientific FAIL.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iter590 prevents an incomplete Ward closure but does not yet create a comparator-subtracted residual or close a full rubric sector.

## Exact next gate
First prove/freeze the hard-channel origin of the local MSSC K3 contact. A nonzero local contact is not automatically a nonzero discontinuity: if K3 is polynomial/local analytic in the channel momenta with no internal propagator or nonanalytic form factor, establish `D_s K3=0` in the frozen `D_s=Disc_s/(2 pi i)` convention.

Then separately classify K1^3 under the already-frozen split-invariant `Y=(K2,S_soft2_full)` / linked `T_cut` protocol. Do not drop K1^3 merely by calling it reducible or non-1PI, and do not import Born subtraction from unrelated on-shell cut observables.

Only after both origin-accounting questions close may the six K1/K2 terms be promoted to the complete discontinuity-bearing source block and used for the nonlinear Ward cancellation before mapping to Iter582/comparator quotient.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc estimator, altered normalization, changed q2 grouping, premature Source/Born subtraction, threshold weakening, ansatz tuning, or unproved internal repartition. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
