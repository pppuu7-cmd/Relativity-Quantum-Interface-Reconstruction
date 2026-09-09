# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **638**.

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

Earlier run `34293593003` is non-authoritative implementation noise: the evaluator passed but the audit used exact floating equality for `u0`. Canonical V2 changed only the audit comparison to absolute tolerance `2e-15`; no scientific contract or kinematics changed.

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

Readiness change through Iter638: **0 percentage points**. Exact-fixture provenance is closed, but no robust comparator-subtracted residual or complete new rubric sector has closed.

## Exact next gate

**Iteration639:** evaluate the already prospectively frozen Iter636 scalar-denominator geometry with `t0=0.14`, `u0=0.34`, `m_phi=0.7`: K1/K2 equal-mass bubble threshold in the `s` channel and K1^3 equal-mass triangle leading Landau determinant plus positive-Feynman-parameter support. Preserve subthreshold/mixed-sign/no-support results exactly. This gate does not authorize native `Y/T_cut` projection or Source/Born subtraction by itself.
