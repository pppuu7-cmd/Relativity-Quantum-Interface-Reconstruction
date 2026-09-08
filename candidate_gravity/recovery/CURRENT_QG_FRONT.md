# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **634**.

Historical authority retained: Iter581 exact15 PASS; Iter582 q2-resolved Candidate-side connection coordinate; Iter594 complete 13-family MSSC source object; Iter605 source nonlinear Ward PASS; Iter613 open-source hard-channel trajectory; Iter614/615 historical source roots/coefficients; Iter616 exact q2/end-point identity; Iter627 combined matter+gravity SK measurement contract; Iter628 open retarded scalar-response coefficients.

### Iter629 — universal open→closed normalization rejected

Raw-valid run `34285497992`, artifact `10079284705`. Open source family totals `(-1,+6,-6)` are not proportional to closed `ThirdDerivative Tr log K` totals `(+1,-3,+2)`; ratios are `(-1,-2,-3)`. No single or fitted `N_native` is authority.

### Iter630 — closed retarded scalar loop requires `G_K`

Raw-valid run `34289414837`, artifact `10080743600`, digest `sha256:ee5a9b16d0e0a79d2346115090cf8a76f9767902add8c54ecba27c05d2ec616e`, `failures=[]`.

In the Iter627 r/a convention `G=[[G_K,G_R],[G_A,0]]`:
- K3 one-a closed contact: `G_K`;
- K1/K2: `G_K G_A + G_K G_R`;
- K1^3: `G_K G_A^2 + G_K G_R G_A + G_K G_R^2`.

Thus Iter628 all-`G_R` open response is preserved but is not direct gravitational-1PI authority.

### Iter631 — state prerequisite isolated

Raw-valid run `34289607051`, artifact `10080814393`, digest `sha256:6c8fb7fd6802bf4a996d3336c5e2dc76eb07cd0b83bd00b96eb368713145697c`, `failures=[]`.

Classification: `BLOCKED_ITER631_ITER627_CTP_CAUSAL_CONTRACT_DOES_NOT_FIX_SCALAR_KELDYSH_STATE__GK_REQUIRES_PROSPECTIVE_STATE_BOUNDARY_CONDITION__NON_RESIDUAL`. Iter627 fixes causal slots but not the scalar density matrix/occupation/Hadamard state.

### Iter632 — prospective scalar-state contract

Prospectively frozen before any closed-loop/native result: `MSSC001-SCALAR-STATE-MINKOWSKI-VACUUM-V1`, zero-temperature Poincare-invariant positive-energy Hadamard Minkowski state with `G_K(k)=sgn(k0)[G_R(k)-G_A(k)]` in the Iter627 convention. Raw validation passed; no Candidate values or normalization fit selected the state.

### Iter633 — closed-loop singularity origin

Raw-valid run `34289894774`, head `24c02d5dd6492c20af4fb4d0b3ec977e6ce5e2f9`, artifact `10080918118`, digest `sha256:003bae112510d0bce4947972e45f34b13f771624035ab2768045c952d8dd83be`; runtime SHA-256 `efe1fd7cc74952213debd985c6be041269de32d5dbce60e11272c4f77d528ba9`, audit SHA-256 `5f5ebf19221bd7ddf01fa1136b21c3af06057da29dd919547ef76106dc5ef218`, `failures=[]`.

- K3: retained one-propagator tadpole; no ordinary finite hard-channel branch cut. This is not amplitude zero.
- K1/K2: two-propagator bubble; ordinary two-scalar hard-channel cut.
- K1^3: triangle; normal pairwise cuts plus explicit anomalous/Landau check required.

### Iter634 — open-source `p0(s)` is not a closed-loop channel

Raw-valid run `34290043168`, head `8b47bbf47f8fdff5c9368e563a4891e3a379453c`, artifact `10080975783`, digest `sha256:9cd033ea997f55f623e32ab281a5794df58829482e597fef04824c52ea1a9cc5`; runtime SHA-256 `a4180e6b1bf1b8e6a692157ea2282b3cebfbfab0a61bc9d6072c60a6d11d0230`, audit SHA-256 `10ac167f7fc59464f2d82dcdee3974bcf7c56f9f82103a246b47ec9b45a179b0`, `failures=[]`.

Classification: `BLOCKED_ITER634_ITER613_OPEN_SOURCE_P0_TRAJECTORY_IS_NOT_CLOSED_LOOP_HARD_CHANNEL__EXTERNAL_INVARIANT_BINDING_REQUIRED_BEFORE_CUTKOSKY_LANDAU_EVALUATION__NON_RESIDUAL`.

Iter613 `p0(s)=sqrt(s)e0` is an open scalar-source endpoint trajectory. In the closed gravitational scalar loop that momentum is integrated and cannot be used as the external `D_s` variable. Iter633 topology remains valid; Iter613 mass/external-q parent data remain retained.

Iter610 remains controlling native authority: positive-timelike `s`, `D_s=Disc_s/(2*pi*i)` and `T_cut` are frozen, but no identity binds that `s` to a specific later closed-loop external invariant.

## Active run / ANTI-IDLE

**Iteration635 is in progress:** run `34290169228`, head `f1630eb924b500b38ea12dd268c33d0813dc64ca`.

It fail-closed audits whether existing authority fixes both (a) a specific external hard channel of closed retarded `Gamma3` and (b) a one-parameter external kinematic family on which `D_s` acts. The exact three-mode fixture is a fixed point and is not silently treated as a discontinuity trajectory.

If Iter635 confirms the missing family, the next allowed step is a prospective pre-result kinematic-family contract anchored to the exact fixture, with closure and polarization transport frozen before any bubble/triangle support is inspected.

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

Readiness change through Iter634: **0 percentage points**. The bridge is better specified, but no robust comparator-subtracted residual or complete new rubric sector has closed.

## Exact next gate

Terminal Iter635 -> independent raw artifact consumption. If the external channel/family is absent, freeze Iter636 prospectively: one closed-`Gamma3` positive-timelike external channel and one-parameter `q_s(s),q_a(s),q_b(s)` family preserving momentum closure, soft-leg role, parent polarization convention and native `D_s` orientation, while loop momentum remains independent. Only then perform Cutkosky/Landau evaluation.
