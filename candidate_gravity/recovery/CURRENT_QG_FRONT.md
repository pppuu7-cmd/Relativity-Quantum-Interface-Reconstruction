# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **640**.

Historical authority retained: Iter581 exact15 PASS; Iter582 q2-resolved Candidate-side connection coordinate; Iter594 complete 13-family MSSC source object; Iter605 source nonlinear Ward PASS; Iter613 open-source hard-channel trajectory; Iter614/615 historical source roots/coefficients; Iter616 exact q2/end-point identity; Iter627 combined matter+gravity SK measurement contract; Iter628 open retarded scalar-response coefficients.

### Iter629–632 — open/closed bridge and scalar state

Iter629 raw-validly rejects a universal open→closed `N_native`; Iter630 shows every closed retarded scalar-loop family carries exactly one `G_K`; Iter631 shows Iter627 does not uniquely fix `G_K`; Iter632 prospectively freezes the zero-temperature Poincare-invariant positive-energy Hadamard Minkowski state `MSSC001-SCALAR-STATE-MINKOWSKI-VACUUM-V1` with `G_K(k)=sgn(k0)[G_R(k)-G_A(k)]`, before closed-loop/native results.

### Iter633–635 — singularity origin and closed-channel blocker

Iter633 raw-validly classifies K3 as a retained tadpole with no ordinary finite hard-channel cut, K1/K2 as a bubble with ordinary two-scalar cut, and K1^3 as a triangle with normal cuts plus an explicit anomalous/Landau check. Iter634 proves the Iter613 open-source `p0(s)` trajectory is not the closed-loop hard channel. Iter635 preserves native positive-timelike `s` and `D_s=Disc_s/(2*pi*i)` but finds that the closed-Gamma3 external channel family had not yet been frozen.

### Iter636 — prospective closed-Gamma3 invariant family

Raw-valid run `34290339702`, head `3975d5cca742dc41e27491881caed05e9a48827a`, artifact `10081080144`, digest `sha256:cc8475ed718e6cfc09dd380ab67e2757fb9d758b1372a305199eabf40ba748e7`, `failures=[]`.

Prospectively frozen before threshold/Landau inspection: `MSSC001-CLOSED-GAMMA3-INV-FAMILY-V1`.
- `s := q_s^2 > 0` is the external channel;
- `t := q_a^2=t0` and `u := q_b^2=u0` are fixed at the exact-fixture anchor;
- `q_s+q_a+q_b=0`;
- `q_s·q_a=(u-s-t)/2`, `q_s·q_b=(t-s-u)/2`, `q_a·q_b=(s-t-u)/2`;
- loop momentum `ell` is independent and integrated;
- `m_phi=0.7` retained;
- scope is scalar-denominator Cutkosky/Landau support geometry only.

### Iter637 — JSON-only exact-fixture discovery BLOCKED

Run `34290476762`, job `102275666433`, head `ff0625e44ca4647ba41b0f63a3d8f2e952b4d842`, artifact `10081130325`, digest `sha256:403257bb69cc81bb46d8a14bc3f28b98da45fcdd70e39b4af91922a4bb4690fd`, raw `failures=[]`.

Committed-JSON exact-key discovery found no explicit `q_s,q_a,q_b` triplet and therefore correctly returned `BLOCKED_ITER637_EXACT_FIXTURE_INVARIANT_ANCHOR_NOT_UNIQUE_OR_NOT_MACHINE_RECOVERABLE__NO_T0_U0_INVENTED__NON_RESIDUAL`. This result remains valid in its JSON-only scope.

### Iter638 — exact same-parent code provenance recovered

Canonical raw-valid run `34293646233`, job `102285415240`, head `1bdc8fb40a4f369c006c7f42f4d368a71cb0166f`, artifact `10082281625`, digest `sha256:95ed469a705250ea341873d493dec4eb04c199c674c091cefdf07b11072c297e`. Independent raw artifact consumption gives result SHA-256 `cbf27355a5d3a6bc83163cebf889188b526cb1699ef6e299190bf296de72e0ec`, audit SHA-256 `ee011c75cf6c8390ddd682607ebc626744975e01a84ad171a653ee8078e29dc6`, `failures=[]`.

Committed same-parent code closes the provenance blocker:
- Iter368 explicitly fixes `LEGS=('s','a','b')`;
- `q_s=(1,0,0,0)`, `q_a=(-0.4,0.1,0.1,0)`, `q_b=(-0.6,-0.1,-0.1,0)`;
- Iter588 explicitly re-executes the Iter368 setup prefix and inherits `M=ns['M']`, binding this fixture through `Iter368 -> Iter370/372 -> Iter582` rather than retyping it;
- in physical `+---` signature, exact closure holds and the unique anchor is `(s0,t0,u0)=(1,0.14,0.34)`.

Classification: `PASS_ITER638_UNIQUE_SAME_PARENT_EXACT_FIXTURE_ANCHOR_RECOVERED_FROM_COMMITTED_CODE__NON_RESIDUAL`.

### Iter639 — frozen closed scalar singularity geometry

Canonical independent raw-valid Action run `34293815174`, head `7c58ca664a18a52cf42d3e38ca19d24fc3cc00c4`, conclusion `success`; artifact `10082346913`, digest `sha256:75d55a449941181f5cf7d852cc97eed3b0de88771334849508e7458258a9a5e9`.

Using only the frozen Iter636 family with `t0=0.14`, `u0=0.34`, `m_phi=0.7`:
- K1/K2 equal-mass bubble normal threshold in the `s` channel is `s_thr=4 m_phi^2=1.96`;
- exact fixture anchor `s0=1` is below threshold; fixed crossed invariants `t0=0.14`, `u0=0.34` are also below `1.96`;
- K1^3 equal-mass triangle Cayley/Landau determinant is proportional to `175 s^2-151 s+7`;
- the two real determinant roots are `s≈0.04915823221180988` and `s≈0.813698910645333`;
- normalized Feynman parameters are mixed-sign at both roots, hence `positive_alpha_leading_roots=[]`.

Therefore there is no positive-alpha physical leading/anomalous triangle Landau root on this frozen real-`s` family. Boundary singularities reduce to ordinary bubble subchannels and remain retained. Canonical classification: `PASS_ITER639_CLOSED_GAMMA3_SCALAR_GEOMETRY__BUBBLE_THRESHOLD_1P96__NO_POSITIVE_ALPHA_LEADING_TRIANGLE_LANDAU_ROOT__NON_RESIDUAL`.

### Iter640 — retarded closed-loop support and native D_s projector

Canonical Action run `34297861017`, job `102298271491`, head `0b468549f4232a814cd5a91b9ae44c886e95e3bf`, conclusion `success`; artifact `10083803236`, digest `sha256:4cb96e533c1c04bde656e5f0c811d3790645af246a214078b4d85f989c769c3d`. Fail-closed raw audit result SHA-256 is `12e7a1116ea4c77b88619c878b325e9b41778deb1fa5f553647912d6cb7f93c1`, with `failures=[]`.

Under frozen Iter627+632+636+639 authority:
- K3 is retained as tadpole/analytic-contact origin and has no ordinary finite hard-channel two-particle `s` cut;
- K1/K2 ordinary `s` support is only `s>=1.96`;
- K1^3 ordinary `s` support is only `s>=1.96`, with no extra positive-alpha leading anomalous term on the frozen `t0/u0` family;
- the exact fixture anchor `s0=1` is below ordinary-cut support;
- the native operator is inherited exactly as `D_s[F]=Disc_s[F]/(2*pi*i)` with frozen Iter205 orientation, not refitted.

Canonical classification: `PASS_ITER640_RETARDED_CLOSED_LOOP_S_SUPPORT_AND_NATIVE_DS_PROJECTOR_CONTRACT__NON_RESIDUAL`.

This is a support/projector PASS, not a Candidate residual or model-level consistency PASS/FAIL. The actual closed-loop discontinuity density/numerator has not yet been derived.

## Frozen guardrails

All K3/K1K2/K1^3 families remain retained; `zero_fill=false`. Source/Born subtraction `NOT_PERFORMED`. Native projection `NOT_PERFORMED`. No comparator quotient. No post-hoc state/channel/trajectory/normalization fit. No open-source root weights may stand in for closed-loop cut density. No `ANSATZ-003`; no Fisher/resources; no blind full-C5. Negative/BLOCKED results remain results.

## Stable model-readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter640: **0 percentage points**. The retarded support/projector subgate closed, but no robust comparator-subtracted residual or complete new rubric sector has closed.

## Exact next gate

**Iteration641:** derive the actual same-parent retarded closed-loop discontinuity density/numerator for K1/K2 and K1^3 ordinary `s` cuts from the frozen Iter594 parent dynamics, Iter627 combined SK measurement map, Iter632 scalar state and Iter636 invariant family. Preserve K3 as a retained analytic/contact contribution. Unsupported numerator/tensor pieces are `BLOCKED`, never zero-filled. Only after a raw-valid same-parent density exists may matched native `Y/T_cut` projection be tested; Source/Born subtraction and fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain downstream, and `ANSATZ-003`, Fisher/resources remain forbidden.
