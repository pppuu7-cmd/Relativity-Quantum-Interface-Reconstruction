# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **646**.

Historical authority retained: Iter581 exact15 PASS; Iter582 q2-resolved Candidate-side connection coordinate; Iter594 complete 13-family MSSC source object; Iter605 source nonlinear Ward PASS; Iter627 combined matter+gravity SK measurement contract; Iter630 closed retarded one-GK causal structure; Iter632 Minkowski-vacuum scalar state; Iter636 frozen closed-Gamma3 invariant family; Iter638 exact fixture anchor; Iter639 threshold/Landau geometry; Iter640 native D_s projector/support; Iter641 denominator spectral kernel; Iter642 same-parent vertex authority; Iter644 Tensor-Transport-V1.

### Iter645 — reduced numerator-weighted ordinary-cut densities

The committed evaluator `candidate_gravity/code/iteration645_closed_gamma3_reduced_cut_density.py` evaluates reduced numerator-weighted ordinary s-channel cut densities on the frozen closed-Gamma3 family at `s=(1.96,2.0,2.25,2.5,3.0,4.0)`. It uses only Iter594 K1/K2 machinery, Iter627/630/632 SK/state authority, Iter640/641 support/projector authority, and `MSSC001-CLOSED-GAMMA3-TENSOR-TRANSPORT-V1`.

K3 remains analytic/contact; the K1/K2 closed cyclic representative and both K1^3 closed orientations are retained while all 13 source families remain provenance-retained. `zero_fill=false`. Threshold beta vanishes at `s=1.96`; above threshold the reduced angular integrals are finite under the committed quadrature and no unexpected sampled uncut triangle pole appears.

Canonical Action `34305969612` completed `success`; artifact `10086648514`, digest `sha256:1f865d8da0413d50ef6c36056385258de6a175301d19a3856a3a440c85b6a75d`.

Classification: `BLOCKED_ITER645_ABSOLUTE_CLOSED_CTP_CUT_NORMALIZATION_NOT_YET_BOUND__REDUCED_NUMERATOR_DENSITIES_COMPUTED__NON_RESIDUAL`.

The remaining ambiguity is one overall closed-CTP effective-action phase/loop-measure normalization. No root-, family-, or q2-dependent fit is licensed, and the missing factor may not be chosen from Iter645 outputs after the fact.

### Iter646 — same-parent normalization authority audit

A fail-closed audit compared the committed Iter627 SK generating-functional contract, Iter630 one-G_K closed-loop structure, Iter632 `G_K=2*pi*i*delta(D)` vacuum normalization, Iter311 relative cubic Tr-log topology, and Iter645 reduced kernel.

Existing authority explicitly fixes causal slots, state/spectral normalization, relative determinant topology, and the reduced `beta/(16*pi^2)` cut kernel. It does **not** explicitly bind the complete `W=-i ln Z` / Legendre-to-native-Gamma3 normalization carrying the real-scalar Gaussian one-loop global phase/prefactor into the exact native Gamma3 convention. Iter311 contains the relative Tr-log cubic coefficients but intentionally no explicit real-scalar `i/2` global prefactor.

Therefore exactly one common nonzero global scalar factor remains unbound. Standard literature conventions can motivate the familiar Gaussian determinant factor, but literature cannot retroactively replace missing same-parent pre-result authority after Iter645 reduced values have already been evaluated.

Canonical Action `34306240992` completed `success`; artifact `10086735213`, digest `sha256:c4348360d606f4707dff5d8f792aadbef74b62d8d5c08ae116b4a47b05392973`.

Classification: `BLOCKED_ITER646_ABSOLUTE_CLOSED_CTP_TO_NATIVE_GAMMA3_NORMALIZATION_NOT_EXPLICITLY_BOUND__ONE_GLOBAL_FACTOR_REMAINS__NON_RESIDUAL`.

This is operational/provenance BLOCKED. It is not Candidate-Gravity consistency FAIL/PASS, exact comparator identity, regime-specific non-identifiability, near-degeneracy, novelty certificate, or Candidate residual.

## Frozen guardrails

All 13 families retained; K3 analytic/contact; ordinary K1/K2 and K1^3 support `s>=1.96`; native `D_s=Disc_s/(2*pi*i)` frozen; Tensor-Transport-V1 frozen; `zero_fill=false`; Candidate values unused. Source/Born subtraction `NOT_PERFORMED`; native Y/T_cut projection `NOT_PERFORMED`; fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient `NOT_PERFORMED`. No post-hoc state/channel/tensor/normalization fit. No `ANSATZ-003`; no Fisher/resources; no blind full-C5. Negative/BLOCKED results remain results.

## Stable model-readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter646: **0 percentage points**. Numerator-weighted cut information exists and the remaining normalization freedom is narrowed to one global factor, but robust unique residual remains `0/20`; no complete readiness-rubric sector closes.

## Exact next gate

**Iteration647:** search only **pre-Iter645** repository history/authority for an explicit same-parent CTP `W=-i ln Z`, Legendre transform, real-scalar Gaussian determinant prefactor and Fourier/loop-measure convention that uniquely binds the one remaining global factor. If no such earlier authority exists, record a permanent normalization-provenance BLOCKED for this observable branch rather than choosing `i/2`, `+/-i` or a fitted constant post hoc. Only after that classification may a new prospectively versioned projective/ratio observable that cancels the common factor be considered, and its definition must not use Iter645 values. Native projection, Source/Born subtraction, comparator quotient, ANSATZ-003, Fisher/resources remain forbidden until the relevant gate is lawfully closed.
