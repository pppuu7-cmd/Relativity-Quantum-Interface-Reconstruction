# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **636**.

Historical authority retained: Iter581 exact15 PASS; Iter582 q2-resolved Candidate-side connection coordinate; Iter594 complete 13-family MSSC source object; Iter605 source nonlinear Ward PASS; Iter613 open-source hard-channel trajectory; Iter614/615 historical source roots/coefficients; Iter616 exact q2/end-point identity; Iter627 combined matter+gravity SK measurement contract; Iter628 open retarded scalar-response coefficients.

### Iter629–632 — open/closed bridge and scalar state

Iter629 raw-validly rejects a universal open→closed `N_native`; Iter630 shows every closed retarded scalar-loop family carries exactly one `G_K`; Iter631 shows Iter627 does not uniquely fix `G_K`; Iter632 prospectively freezes the zero-temperature Poincare-invariant positive-energy Hadamard Minkowski state `MSSC001-SCALAR-STATE-MINKOWSKI-VACUUM-V1` with `G_K(k)=sgn(k0)[G_R(k)-G_A(k)]`, before closed-loop/native results.

### Iter633 — singularity origin

Raw-valid run `34289894774`, artifact `10080918118`, digest `sha256:003bae112510d0bce4947972e45f34b13f771624035ab2768045c952d8dd83be`; runtime SHA-256 `efe1fd7cc74952213debd985c6be041269de32d5dbce60e11272c4f77d528ba9`, audit SHA-256 `5f5ebf19221bd7ddf01fa1136b21c3af06057da29dd919547ef76106dc5ef218`, `failures=[]`.

K3 is a retained tadpole with no ordinary finite hard-channel cut; K1/K2 is a bubble with ordinary two-scalar cut; K1^3 is a triangle with normal cuts plus explicit anomalous/Landau check required.

### Iter634 — source `p0(s)` is not the closed-loop channel

Raw-valid run `34290043168`, artifact `10080975783`, digest `sha256:9cd033ea997f55f623e32ab281a5794df58829482e597fef04824c52ea1a9cc5`; runtime SHA-256 `a4180e6b1bf1b8e6a692157ea2282b3cebfbfab0a61bc9d6072c60a6d11d0230`, audit SHA-256 `10ac167f7fc59464f2d82dcdee3974bcf7c56f9f82103a246b47ec9b45a179b0`, `failures=[]`.

Classification: `BLOCKED_ITER634_ITER613_OPEN_SOURCE_P0_TRAJECTORY_IS_NOT_CLOSED_LOOP_HARD_CHANNEL__EXTERNAL_INVARIANT_BINDING_REQUIRED_BEFORE_CUTKOSKY_LANDAU_EVALUATION__NON_RESIDUAL`. Iter613 `p0(s)` is an open scalar-source endpoint trajectory; in a closed scalar loop the corresponding momentum is integrated and cannot be the external `D_s` variable.

### Iter635 — external channel/family missing from prior authority

Raw-valid run `34290169228`, artifact `10081018207`, digest `sha256:5ed0d00b6c45ef83eb1cdeed902b2ea290fdd0edfaf941ae5655f85afca7fdd2`; runtime SHA-256 `0f7765941fcae7b0e7f9114850a9df15b761579104b44c2abbec136104b2ed6e`, audit SHA-256 `6815fc02758fb0f6f7b584da2b229f6ce8ba29a258b8ad8e50f0d7271fd934a1`, `failures=[]`.

Classification: `BLOCKED_ITER635_NATIVE_DS_VARIABLE_EXISTS_BUT_CLOSED_GAMMA3_EXTERNAL_CHANNEL_AND_ONE_PARAMETER_KINEMATIC_FAMILY_ARE_NOT_FROZEN__NON_RESIDUAL`. Iter610 preserves positive-timelike native `s` and `D_s=Disc_s/(2*pi*i)`, but the exact three-mode fixture was only one fixed point and not a discontinuity family.

### Iter636 — prospective closed-Gamma3 invariant family

Raw-valid run `34290339702`, head `3975d5cca742dc41e27491881caed05e9a48827a`, artifact `10081080144`, digest `sha256:cc8475ed718e6cfc09dd380ab67e2757fb9d758b1372a305199eabf40ba748e7`; runtime SHA-256 `d296abe64cd8a891ee68548eb034f15539b1dc7117b1bf40e09beda116aef06b`, audit SHA-256 `a1d9ac5d9e1b8836b77eb2699c9110aedbffecfad0802d1fb804b16efd0a3339`, `failures=[]`.

Prospectively frozen before threshold/Landau inspection: `MSSC001-CLOSED-GAMMA3-INV-FAMILY-V1`.
- `s := q_s^2 > 0` is the external channel;
- `t := q_a^2=t0` and `u := q_b^2=u0` fixed at the exact-fixture anchor;
- `q_s+q_a+q_b=0`;
- `q_s·q_a=(u-s-t)/2`, `q_s·q_b=(t-s-u)/2`, `q_a·q_b=(s-t-u)/2`;
- loop momentum `ell` is independent and integrated;
- `m_phi=0.7` retained;
- scope is scalar-denominator Cutkosky/Landau support geometry only.

No Candidate values, bubble/triangle support, or normalization fit were used to select the contract.

## Active run / ANTI-IDLE

**Iteration637 is queued:** run `34290476762`, head `ff0625e44ca4647ba41b0f63a3d8f2e952b4d842`.

It performs repository-wide fail-closed exact-fixture anchor discovery: parses committed JSON, accepts only explicit `q_s,q_a,q_b` four-vector triplets with exact momentum closure, computes `+---` invariant triples `(s0,t0,u0)`, preserves all candidates, and promotes an anchor only if the invariant triple is unique. No `t0/u0` is invented and Iter582 Candidate values are not used.

## Frozen guardrails

All K3/K1K2/K1^3 families remain retained; `zero_fill=false`. Source/Born subtraction `NOT_PERFORMED`. Native projection `NOT_PERFORMED`. No comparator quotient. No post-hoc state/channel/trajectory/normalization fit. No `ANSATZ-003`; no Fisher/resources; no blind full-C5. Negative/BLOCKED results remain results.

## Stable model-readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter636: **0 percentage points**. No robust comparator-subtracted residual or complete new rubric sector has closed.

## Exact next gate

Terminal Iter637 -> independent raw artifact consumption. If exactly one authoritative `(s0,t0,u0)` anchor is recovered, evaluate the frozen Iter636 K1/K2 bubble threshold and K1^3 equal-mass triangle Landau determinant/positive-Feynman-parameter support. If anchor provenance is absent or non-unique, record `BLOCKED` and audit original fixture authority instead of inventing invariants. Native `Y/T_cut` projection and Source/Born subtraction remain downstream.
