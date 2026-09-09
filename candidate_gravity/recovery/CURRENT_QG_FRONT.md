# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **660**.

Historical authority retained: Iter175 null soft direction / plus-TT historical soft structure; Iter205 linked `D_s=Disc_s/(2*pi*i)` and cut-before-soft-limit protocol; Iter581 exact15 PASS; Iter582 q2-resolved Candidate-side connection coordinate; Iter594 complete 13-family MSSC source object; Iter605 source nonlinear Ward PASS; Iter621 normalization-authority graph; Iter627 combined matter+gravity SK measurement contract; Iter629 open-vs-closed one-factor proxy rejection; Iter630 closed retarded one-GK causal structure; Iter632 Minkowski-vacuum scalar state; Iter636 frozen finite closed-Gamma3 invariant family; Iter638 exact fixture anchor; Iter639 threshold/Landau geometry; Iter640 native D_s projector/support; Iter641 denominator spectral kernel; Iter642 same-parent vertex authority; Iter644 Tensor-Transport-V1; Iter645 reduced finite-family numerator-weighted ordinary-cut densities; Iter646/647 normalization audits; Iter648 projective finite-family observable; Iter652 exact source-completion semantics; Iter653 normalized closed-SK Gamma2/Gamma3 parent and Ward map; Iter654 finite-family versus historical-soft mismatch; Iter655 prospective soft-T_cut kinematic completion; Iter656 exact-null domain blocker; Iter657 exact three-dimensional null gauge overlap; Iter658 quotient-safe plus-TT measurement; Iter659 normalized soft-Gamma3 topology census.

### Iter660 — fixed-epsilon soft-family routing / thresholds / Landau support

Frozen Iter655 kinematics give `q3^2=0`, `q1^2=s`, and `q2^2=s-2 eps sqrt(s)` before the soft limit. With `m^2=49/100`, the massive two-particle threshold is `4m^2=49/25`.

The q3-transfer K1K2 bubble has no massive ordinary two-particle cut. The q1-transfer bubble has support for `s>=49/25`. The q2-transfer bubble has support for `s-2 eps sqrt(s)>=49/25`, equivalently `sqrt(s)>=eps+sqrt(eps^2+4m^2)`.

Both K1^3 triangle orientations retain the same invariant set `{0,s,s-2 eps sqrt(s)}`. At fixed `eps>0`, the equal-mass interior Landau stationarity condition requires `alpha2(s-u)=2 alpha2 eps sqrt(s)=0`, impossible for positive `alpha2`; therefore no positive-alpha leading triangle Landau point exists at fixed epsilon. The coincident `eps->0` boundary is not promoted because `D_s` is taken before the soft limit.

Classification: `PASS_ITER660_SOFT_ROUTING__Q3_BUBBLE_NO_MASSIVE_CUT__Q1_Q2_THRESHOLDS_EXPLICIT__NO_FIXED_EPS_POSITIVE_ALPHA_LEADING_TRIANGLE_LANDAU__NON_RESIDUAL`.

Canonical raw authority: run `34334410816`, job `102410321810`, head `6c74089df150fa4eb465e636e29d81d36f2e7f84`, artifact `10097091086`, digest / downloaded ZIP SHA-256 `e98203376c103d6119efb10d2fdab66b8e378d26a3e9ac29639c727170735232`, raw JSON SHA-256 `777003d4f8d31bf9222ebb7b392002647699924324487d234e9e72a5dafed75a`; `failures=[]`, `scientific_gate_pass=true`. Earlier race-persisted digest metadata was corrected after direct artifact download verification; scientific payload is unchanged.

## Active computation

Iteration661 quotient-safe plus-TT numerator-weighted fixed-epsilon `D_s` integrand gate is active. First run `34339504343` failed before artifact upload and is non-authoritative. Diagnostic-preserving canonical retry run `34339595133`, head `f048cb6badbf9056fab7a11fee5b52e918fd5ad4`, is queued/running. The gate uses exact Iter594 K1/K2 vertices, Iter655 kinematics, Iter658 quotient-safe plus-TT measurement and Iter653 parent normalization; it does not use Candidate values or perform Source/Born subtraction.

## Frozen guardrails

All 13 families retained. K3 analytic/contact. The q3-transfer soft bubble is analytically no-cut, not a zero-filled amplitude. Native `D_s=Disc_s/(2*pi*i)` and Iter655 cut-before-soft-limit ordering remain frozen. `zero_fill=false`. Iter653 same-parent normalized closed-SK Gamma2/Gamma3 parent remains authority. Source/Born/source-completion subtraction remains `NOT_PERFORMED`; native numerical soft `T_cut` and fixed comparator quotient remain `NOT_PERFORMED`. No post-hoc state/channel/tensor/normalization/regulator fit. No `ANSATZ-003`; no Fisher/resources; no blind full-C5. Negative/BLOCKED results remain results.

## Stable model-readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter660: **0 percentage points**. The soft routing/support gate is closed, but no stable rubric point is added and no robust unique residual exists.

## Exact next gate

**Iteration661:** consume the queued/running quotient-safe plus-TT numerator-weighted fixed-epsilon `D_s` computation. If the two-line triangle cut encounters an uncut propagator pole, bind its retarded/CTP prescription from same-parent Iter630/653 authority before numerical promotion; otherwise extract the prescribed epsilon-leading coefficient only on compact domains away from threshold. In either case, keep Source/Born subtraction `NOT_PERFORMED` until matched `W[D_s K2]` is independently classified.
