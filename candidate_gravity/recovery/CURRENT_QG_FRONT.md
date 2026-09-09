# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **661**.

Historical authority retained includes Iter175/205 soft-T_cut protocol, Iter594 exact K1/K2 source machinery, Iter621 normalization graph, Iter627/630/632 SK causal/state conventions, Iter653 normalized closed-SK Gamma2/Gamma3 parent, Iter655 soft kinematic contract, Iter658 quotient-safe plus-TT measurement, Iter659 six-term topology census and Iter660 fixed-epsilon routing/threshold/Landau support.

### Iter661 — raw-valid fixed-epsilon numerator-weighted D_s integrands

Canonical raw authority: run `34340069225`, job `102428518922`, head `c8efdc4da0dbf434689aa1d14b2722c90bd25df7`, artifact `10099348470`, artifact/downloaded-ZIP SHA-256 `89c8eddf4e2c757c507dc29da0fce30a9a1452cb7fe26cab21d7684e2c4cafe3`, raw JSON SHA-256 `1817b437a4dd86743d6cef8bbbc55dd84c9f44e90d108e2a7222ab673c2cf758`.

Raw `failures=[]`, `blocked=[]`, `scientific_gate_pass=true`. The prospective grid has six `(s,epsilon)` points. q1/q2 hard-transfer K1K2 bubbles and both K1^3 triangle orientations were evaluated using exact Iter594 K1/K2 vertices and the Iter658 quotient-safe frozen plus-TT functional. No sampled uncut triangle pole occurs (`min |D_uncut|=0.011201904523433559`); cut-shell error is below `7.8e-16`. q3 transfer remains a no-massive-cut topology and is not zero-filled.

The reported +TT densities are only `5.67e-23` to `4.60e-19` with zero reported imaginary parts. They are **not** promoted as nonzero physics: before epsilon-leading extraction the exact transverse quarter-turn selection rule must be audited, because the frozen all-plus tensor sector is trilinear in `e_plus` while the axial t-z kinematics and scalar cut measure are invariant under `R_z(pi/2)`.

## Active computation

**Iteration662** exact plus-TT quarter-turn selection-rule gate is queued/running: run `34340309929`, head `4d99856b72ba9ebfabdb57a89dc442f1a4e97a91`. It tests exactly whether `R_z(pi/2) e_plus R_z(pi/2)^T=-e_plus`, all frozen q-vectors are invariant, and therefore every retained +++ K1K2/K1^3 `D_s` integrand is odd under a measure-preserving azimuthal rotation.

Earlier Iter661 runs `34339504343` and `34339595133` are non-authoritative dependency/diagnostic runs. Their failures were traced to canonical Iter655/659 raw-valid JSON being artifact-only rather than persisted in `main`; those canonical authorities have now been materialized with artifact provenance. No scientific gate was weakened.

## Frozen guardrails

All 13 families retained. K3 analytic/contact. q3-transfer soft bubble is analytically no-cut, not a zero-filled amplitude. Native `D_s=Disc_s/(2*pi*i)` and Iter655 cut-before-soft-limit ordering remain frozen. `zero_fill=false`. Iter653 normalized same-parent closed-SK parent remains authority. Source/Born/source-completion subtraction remains `NOT_PERFORMED`; native matched soft `T_cut` and comparator quotient remain `NOT_PERFORMED`. Tiny floating-point residues are not treated as algebraic nonzero signal. No post-hoc state/channel/tensor/normalization/regulator fit. No `ANSATZ-003`; no Fisher/resources; no blind full-C5. Negative/BLOCKED results remain results.

## Stable model-readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter661: **0 percentage points**.

## Exact next gate

Consume Iter662 raw artifact. If the exact quarter-turn antisymmetry passes, classify Iter661 tiny +++ densities as numerical cancellation residue and carry an exact zero **only for this frozen plus-plus-plus measurement**, never for the full tensor amplitude. Then audit the matched same-parent Ward image `W[D_s K2]` in the same rotational representation before forming `T_cut` or performing any Source/Born subtraction. If the selection rule fails, retain Iter661 values only after a precision/convergence gate establishes a genuine nonzero algebraic coefficient.
