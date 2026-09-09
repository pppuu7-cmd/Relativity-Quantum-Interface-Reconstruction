# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **643**.

Historical authority retained: Iter581 exact15 PASS; Iter582 q2-resolved Candidate-side connection coordinate; Iter594 complete 13-family MSSC source object; Iter605 source nonlinear Ward PASS; Iter627 combined matter+gravity SK measurement contract; Iter632 Minkowski-vacuum scalar state; Iter636 frozen closed-Gamma3 invariant family; Iter638 exact fixture anchor; Iter639 threshold/Landau geometry.

### Iter640 — retarded support and native D_s projector

Canonical run `34297861017`, job `102298271491`, artifact `10083803236`, digest `sha256:4cb96e533c1c04bde656e5f0c811d3790645af246a214078b4d85f989c769c3d`, raw `failures=[]`. K3 has no ordinary finite hard-channel two-particle cut; K1/K2 and K1^3 ordinary support begins at `s>=1.96`; no positive-alpha leading anomalous K1^3 support exists on frozen `t0=0.14,u0=0.34`; native `D_s=Disc_s/(2*pi*i)` is inherited unchanged. Classification: `PASS_ITER640_RETARDED_CLOSED_LOOP_S_SUPPORT_AND_NATIVE_DS_PROJECTOR_CONTRACT__NON_RESIDUAL`.

### Iter641 — denominator spectral kernel

Canonical run `34298002367`, artifact `10083854574`, digest `sha256:43a11a1146406a71150140fe8377405e36f8bef615a63439a97c6da534a6bedd`, raw result SHA-256 `3927ed46fdde69b2f71e218742fc6fcec2aeb8ada9cc49bd08ec357ef7cd3b5a`, `failures=[]`. Frozen denominator-level ordinary-cut kernel is `Theta(s-1.96)` with analytic `beta(s)=sqrt(1-1.96/s)`; numerator/tensor contractions remain `BLOCKED_NOT_ZERO_FILLED`. Classification: `PASS_ITER641_PROSPECTIVE_CLOSED_LOOP_DENOMINATOR_SPECTRAL_KERNEL_CONTRACT__NUMERATOR_EXPLICITLY_BLOCKED__NON_RESIDUAL`.

### Iter642 — same-parent vertex authority recovered

Canonical run `34298137965`, job `102299130876`, head `0765961e3fd62af4e404244004a0be9e3662de82`, artifact `10083900312`, digest `sha256:76f329b38a557092a34e5d0a75d33760c769b5b5e11f30e7fc28e98d7e1d8735`; fail-closed raw audit `PASS_RAW_AUTHORITY_AUDIT_ITER642_VERTEX_AUTHORITY`, result SHA-256 `f67a8d48e277cd0a062718866165ffe5c56b1bf0e3134fe3ed89f58b51234fc7`, `failures=[]`.

Exact reusable same-parent MSSC001 vertex machinery is machine-recoverable from committed Iter594 parent dynamics, including `K1`, `K2`, `K3_mixed`, first/mixed metric coefficients, scalar propagator and routed assembly. Classification: `PASS_ITER642_SAME_PARENT_VERTEX_AUTHORITY_MACHINE_RECOVERABLE__NON_RESIDUAL`. Status: `READY_FOR_EXPLICIT_CUT_NUMERATOR_IMPLEMENTATION`, subject to external-tensor trajectory authority.

### Iter643 — external tensor trajectory BLOCKED

Canonical run `34298225934`, job `102299391524`, head `45f5b875276740814a9e9ab51a38dad9b27fc0c6`, conclusion `success`; artifact `10083932235`, digest `sha256:7de15e2c8ffb572dc17e3cb82f8d6c804cdf138ba39125b3251656d4e5c3186c`. Fail-closed raw audit classification `BLOCKED_RAW_AUTHORITY_AUDIT_ITER643_EXTERNAL_TENSOR_TRAJECTORY`, result SHA-256 `6b3e3aad4745bc8ecae052b66405620e0680f0b959ee49d2839c3e0858f822e6`, evaluator `failures=[]`.

The Iter636 scalar invariant trajectory is frozen and the exact Iter368/588 fixture supplies external metric tensors/polarizations at `s0=1`, but no existing authority defines a Lorentz-covariant continuation `h_s(s), h_a(s), h_b(s)` away from `s0`. Because the recovered K1/K2/K3 numerators depend explicitly on these tensors, evaluating them on ordinary-cut support `s>=1.96` without a prospective continuation would add post-hoc observable data. Reusing the anchor tensors for all `s`, or choosing a continuation after viewing cut values, is forbidden.

Classification: `BLOCKED_ITER643_CLOSED_GAMMA3_EXTERNAL_TENSOR_TRAJECTORY_NOT_FROZEN__S0_FIXTURE_CANNOT_BE_EXTENDED_POST_HOC__NON_RESIDUAL`.

This is operational/provenance BLOCKED, not Candidate-Gravity consistency FAIL/PASS, exact comparator identity, regime-specific non-identifiability, near-degeneracy, novelty statement or zero residual.

## Frozen guardrails

All K3/K1K2/K1^3 families retained; K3 remains analytic/contact; ordinary K1/K2 and K1^3 support remains `s>=1.96`; `zero_fill=false`; Candidate values unused. Source/Born subtraction `NOT_PERFORMED`; native Y/T_cut projection `NOT_PERFORMED`; comparator quotient `NOT_PERFORMED`. No post-hoc state/channel/tensor/normalization fit. No `ANSATZ-003`; no Fisher/resources; no blind full-C5. Negative/BLOCKED results remain results.

## Stable model-readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter643: **0 percentage points**. Exact vertex machinery is recovered, but numerator-weighted closed-loop density remains blocked by the missing external-tensor continuation; robust unique residual remains `0/20` and no complete rubric sector closed.

## Exact next gate

**Iteration644:** prospectively derive and freeze the minimal Lorentz-covariant external tensor/polarization continuation from same-parent covariance and the exact `s0=1` Iter368/588 fixture, before viewing any numerator-weighted cut output. The contract must reduce exactly to anchor tensors, preserve `q_s+q_a+q_b=0`, fixed `t0=0.14,u0=0.34`, and explicitly state gauge/transversality/normalization conditions. If covariance plus the anchor does not determine a unique continuation, classify the residual freedom and freeze a versioned observable definition prospectively rather than fitting cut outputs. Only after this gate may explicit K1/K2 and ordinary K1^3 retarded cut numerators be evaluated. Native Y/T_cut projection, Source/Born subtraction, fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient, `ANSATZ-003`, Fisher/resources remain downstream/forbidden.
