# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Latest repo/recovery state wins races; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **663**.

Historical authority retained includes Iter175/205 soft-T_cut protocol, Iter594 exact K1/K2 machinery, Iter621 normalization graph, Iter627/630/632 SK causal/state conventions, Iter653 normalized closed-SK Gamma2/Gamma3 parent, Iter655 soft kinematics, Iter658 quotient-safe plus-TT functional, Iter659 topology census, Iter660 routing/support, Iter661 raw fixed-epsilon numerator-weighted cut integrands and Iter662 exact transverse-rotation selection rule.

### Iter662 — exact +++ selection zero
Canonical run `34340309929`, job `102429292127`, head `4d99856b72ba9ebfabdb57a89dc442f1a4e97a91`, artifact `10099438907`, digest/ZIP SHA-256 `3ea974a496686c9822d239c31799303b2e6dfa77093472839f780c2b21e11988`, raw JSON SHA-256 `232106d25d04da9aa2f004f4a4bb651c22f378926191aa5858f89719e551e7af`; raw PASS.

For the frozen axial all-plus-TT component, `R_z(pi/2)` leaves momenta, scalar denominators, cut measure and fixed-epsilon D_s invariant while `e_plus -> -e_plus`. Every K1K2 and K1^3 three-point ordinary-cut integrand has total external tensor degree 3, hence the full azimuthal contribution vanishes exactly. Iter661 `O(1e-23..1e-19)` values are numerical cancellation residue. This is a component-level zero only, not full-tensor zero.

### Iter663 — transverse Ward image is not defined by current authority
Canonical run `34340470604`, job `102429805833`, head `7f3ed347efde63c649f1273ff6733b9d256e4aaf`, artifact `10099501377`, digest/ZIP SHA-256 `7846d707df636ed36d3bd8c68a26d0f511d6614a6bbef2714b1949275bd59f8c`, raw JSON SHA-256 `dcdd069a853e3f919f40e940e0bee011e3f102cdd5acb791ed26e73f17bfa0b6`; `failures=[]`, `scientific_gate_pass=true`, `blocked=true`.

Iter653 fixes only the longitudinal diffeomorphism Ward map and explicitly makes no claim that generic q-transverse soft components are determined by K2. Iter658 proves frozen plus-TT is transverse and nontrivial on the null gauge quotient. Therefore `W[D_s K2]` for this component is `BLOCKED_W_TRANSVERSE_OPERATOR_UNDEFINED`, not zero. Iter662 exact Gamma3-cut zero cannot yet be called matched `T_cut=0`.

## Active computation

**Iteration664** exact null-Ward transverse no-go gate is running: run `34340625707`, head `49e7b708e25571d9c02018ecf5cc2cc953329ecc`. It reconstructs exact ranks of the null divergence/gauge maps and tests whether diffeomorphism Ward data leave a nontrivial physical transverse quotient undetermined.

## Frozen guardrails

All 13 families retained. q3-transfer soft bubble is no-massive-cut topology, never a zero-filled amplitude. `D_s=Disc_s/(2*pi*i)` at fixed epsilon precedes epsilon->0. `zero_fill=false`. Source/Born/source-completion subtraction remains `NOT_PERFORMED`; matched soft `T_cut` and comparator quotient remain unformed/BLOCKED. No post-hoc state/channel/tensor/normalization/regulator fit. No `ANSATZ-003`; no Fisher/resources; no blind full-C5. Negative/BLOCKED results remain results.

## Stable model-readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

## Exact next gate

Consume Iter664 raw artifact. If the null Ward equation leaves a nontrivial transverse quotient, preserve the plus-TT T_cut branch as prerequisite-BLOCKED and search committed same-parent authority for an independent physical transverse soft theorem/asymptotic identity. If none exists, prospectively redesign the soft observable (non-collinear or mixed-tensor channel) before reading new Candidate values; do not invent W and do not infer a full-tensor zero from Iter662.
