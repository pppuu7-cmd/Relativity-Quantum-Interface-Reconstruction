# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 295**

## Current scientific state

Repository commits, validated Actions artifacts and recovery material are source of truth. Iterations 291–295 supersede the older weighted-kernel proxy interpretation for the actual `Tr U1` insertion.

### Iteration 291 — exact trace-weight completion

`B=U1 W=Q A Q`, hence `U1=B Y_down`. Therefore the old scalar proxy `tr(B3)` is not the cubic effective-action coefficient `Tr U1` when `Y_down` carries background dependence.

Freeze: `PASS_EXACT_U1_TRACE_WEIGHT_COMPLETION_FORMULA_AND_B3_EOM_DEGREE_PROVENANCE`.

### Iteration 292 — complete denominator census

Exact weight-completed cubic `Tr U1` has 36 primitive branches, 32 non-scaleless primitive branches, and eight non-scaleless denominator/numerator families after scaleless/null sectors are removed.

Freeze: `PASS_EXACT_WEIGHT_COMPLETED_TRU1_DENOMINATOR_CENSUS_AND_PRIMITIVE_RECONSTRUCTION`.

### Iteration 293 — full family structural reconstruction

All eight non-scaleless families admit full-coordinate polynomial reconstruction at the frozen numerator degree ceilings. This is structural basis authority, not timelike coefficient authority.

Freeze: `PASS_COMPLETE_WEIGHT_COMPLETED_TRU1_NUMERATOR_RECONSTRUCTION_ALL_EIGHT_NONSCALAR_SECTORS`.

### Iteration 294 — timelike nonzero trace certificate

On the frozen Lorentzian slice `k_s^2=0`, `k_s.k_a=-0.1`, `k_a^2=-s`, `k_b^2=-(s+0.2)`, the actual weight-completed `[Tr U1]_{sab}` is positive/nonzero for every tested `s=0.004,...,0.032`. At `s=0.016`, `[Tr U1]_{sab}=1.0786279385468147`.

Freeze: `PASS_SCOPED_TIMELIKE_TRANSLATION_CLOSED_WEIGHT_COMPLETED_TRU1_NONZERO_ALL_ROWS`.

### Iteration 295 — direct timelike all-family numerator reconstruction

At the frozen timelike point `s=0.016`, with

- `k_s^2=0`;
- `k_a^2=-0.016`;
- `k_b^2=-0.216`;
- `k_s.k_a=-0.1`,

all eight non-scaleless families were reconstructed directly from the timelike parent/oracle rather than by rotating denominators while retaining checkpoint/spacelike numerator coefficients.

Validated Actions provenance:

- run `33688456731`;
- job `100441403084`;
- artifact `9869280530` (`iteration295-result`);
- artifact digest `sha256:2c702d3aef66d052b63553590114900b2754b98e6871762ca3bda9ed8ec9ee77`.

Audited certificate:

- primitive branches: `36`;
- non-scaleless families: `8`;
- primitive/direct residual: `6.485922909860165e-13`;
- maximum held-out reconstruction error: `4.842076903979733e-09`;
- maximum oracle imaginary contamination: `0.0`.

Freeze:

`PASS_DIRECT_TIMELIKE_S0016_WEIGHT_COMPLETED_TRU1_ALL_FAMILY_NUMERATOR_RECONSTRUCTION`.

This is numerator-family authority only. It is not yet an integrated discontinuity, full C5 comparator coordinate, or Candidate Gravity residual.

## Null-soft EOM-sector inventory

Iteration 246 already proves on the frozen null-TT soft branch that the generic connection `e=3,c=0` trilinear sector vanishes because every placement contains exact `E^(1)[h_soft]=0`. Do not reopen it as an active blocker.

Active C5 sectors remain:

- determinant `e=0,c<=3`;
- connection `e=1,c<=2` — current `Tr U1` route;
- connection `e=2,c<=1`.

## Current blocker

`BLOCKED_DIRECT_TIMELIKE_COMPLETE_TRU1_DR_LAURENT_PLUS_MINUS_I0_REDUCTION`.

The linked physical target remains

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`.

Source/Ward/Born-IR classification remains downstream of the actual timelike `e=1,c=2` `Tr U1` reduction and the remaining active `e=0,e=2` pieces.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 294: **0 percentage points**. Iteration 295 closes a direct-timelike numerator prerequisite but not an integrated comparator coordinate or robust unique residual.

## Retained guardrails

- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not promote weighted-kernel `tr(B3)` coefficients or the Iteration-289 proxy pole to `Tr U1` authority.
- Do not subtract `-8 M_Born` from the present 1PI/comparator intermediate without an explicit matched source-observable map.
- Do not confuse background perturbation degree three with EOM degree three.
- Reconstruct timelike numerator coefficients directly from the same parent dynamics; do not rotate denominators only.
- Blind heavy full-C5 remains unauthorized.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Iteration 295 authority files

- `candidate_gravity/results/iteration295_timelike_tru1_family_reconstruction_s0016.json`
- `candidate_gravity/C5_TIMELIKE_TRU1_FAMILY_RECONSTRUCTION_ITERATION295.md`
- `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_295.md`
- `research_log/2026-09-03_iteration_295_timelike_tru1_family_reconstruction.md`

## Exact next gate — Iteration 296

1. Consume/reconstruct the eight direct-timelike Iteration-295 family coefficients.
2. Reduce ordinary and raised bubbles/triangles in one common `i*pi^(D/2)` DR normalization.
3. Evaluate explicit `+i0` and `-i0` branches.
4. Record raw epsilon scans before any fit.
5. Fit Laurent structure; do not use naive finite-epsilon extrapolation.
6. Extract the actual `e=1,c=2` `Tr U1` pole and discontinuity.
7. Do not source/Born subtract until pole origin is classified in a matched observable.
8. Then continue active `e=2,c<=1` and determinant `e=0,c<=3` sectors before source-completed linked `T_cut` projection.
