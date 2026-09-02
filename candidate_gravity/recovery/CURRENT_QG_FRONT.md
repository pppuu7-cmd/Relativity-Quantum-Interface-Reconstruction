# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 292**

## Current scientific state

Iterations 278–289 established a strong computational description of the translation-closed weighted Vilkovisky kernel

`B := U1 W = Q A Q`,

including nonzero support, raised bubble/triangle families, complete weighted-kernel numerator reconstructions and DR/Laurent diagnostics. Iteration 290 separated the weighted-kernel pole issue from the already frozen physical MSSC-001 Born-factorizing source IR completion.

Iteration 291 then closed an upstream trace-orientation gap:

`U1 = B W^-1 = B Y_down`,

so the actual effective-action trace is not `tr(B3)`.

At the frozen translation-closed checkpoint:

- old proxy `tr(B3)=0.9605914180462887`;
- `tr(B3Y0)=0.1071384536577547`;
- `B2Y1+B1Y2=0.6977901599155829`;
- complete `[Tr U1]_{sab}=0.8049286135733377`.

Freeze Iteration 291:

`PASS_EXACT_U1_TRACE_WEIGHT_COMPLETION_FORMULA_AND_B3_EOM_DEGREE_PROVENANCE`.

The previous Iteration-287/289 scalar coefficients remain valid weighted-kernel diagnostics but are not `Tr U1` coefficient authority.

## Iteration 292 — exact complete Tr U1 denominator census

The local `Y_down` insertion carries external momentum but no loop propagator. Exact primitive enumeration of the complete mixed cubic trace gives:

- total primitive branches: `36`;
- `B3Y0`: `23`;
- `B2Y1`: `11`;
- nonzero `B1Y2`: `2` after null-soft elimination;
- non-scaleless primitive branches: `32`.

Direct complete trace at the frozen checkpoint:

`0.8049286124063145`.

Primitive denominator reconstruction:

`0.8049286124067728`.

Absolute residual:

`4.583000645652646e-13`.

Freeze:

`PASS_EXACT_WEIGHT_COMPLETED_TRU1_DENOMINATOR_CENSUS_AND_PRIMITIVE_RECONSTRUCTION`.

### Complete family counts

Retained raised families:

- raised bubbles: `10` = hard-a `4`, hard-b `4`, null/scaleless `2`;
- raised triangles: `12` = four in each repeated-vertex sector `(0,0.21)`, `(0,0.41)`, `(0.21,0.41)`;
- one single scaleless branch.

New weight-completion families:

- ordinary bubbles: `5` = hard-a `2`, hard-b `2`, null/scaleless `1`;
- ordinary one-null two-mass triangles: `8`, invariant set `(0,0.21,0.41)`.

Thus the old raised-only denominator/master census is incomplete for the actual `Tr U1` insertion.

### Analytic loop-momentum degree ceilings

From the exact primitive definitions:

- `N1,N2`: degree `<=2` in loop momentum;
- every `A_n`: degree `<=2`;
- `Y_n`: local, degree `0`.

Therefore the complete conservative numerator ceilings are:

- ordinary bubble: `<=2`;
- ordinary triangle: `<=4`;
- raised bubble: retained `<=4`;
- raised triangle: retained `<=6`.

Iteration 293 must still provide independent held-out family-summed reconstruction certificates at these ceilings.

## Null-soft EOM-sector inventory

Do not reopen the generic EOM-degree-three sector as an active blocker on this observable.

Iteration 246 already proves on the frozen null-TT soft branch:

`Gamma_conn,e=3,c=0^(3)[soft,a,b] = 0`,

because every trilinear `e=3` placement contains the exact factor `E^(1)[h_soft]=0`.

Hence active C5 sectors on this branch are:

- determinant `e=0,c<=3`;
- connection `e=1,c<=2` — current `Tr U1` route;
- connection `e=2,c<=1`.

The generic exact `e=3` Vilkovisky formula remains authority but is null-soft blind in the frozen branch.

## Current C5 blocker

`BLOCKED_COMPLETE_TRU1_FAMILY_NUMERATOR_RECONSTRUCTION_AFTER_WEIGHT_COMPLETION`.

The frozen linked physical target remains

`T_cut = D Gamma3_ret,soft - W[D K2]`.

Source/Ward/Born-IR classification is downstream of completing the actual `e=1,c=2` `Tr U1` reduction and then the remaining active `e=0,e=2` pieces.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 291: **0 percentage points**. The actual `Tr U1` topology is now exact, but no complete physical comparator coordinate or unique residual has closed a rubric point.

## Retained guardrails

- Repository recovery files, validated Actions artifacts and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not promote the Iteration-289 weighted-kernel pole to `Tr U1` authority.
- Do not subtract `-8 M_Born` from a 1PI/weighted-kernel residue without an explicit matched observable map.
- Do not confuse background degree three with EOM degree three.
- Do not treat the generic `e=3` sector as active on the frozen null-TT soft branch; Iteration 246 already kills it there.
- Local `Y_down` adds no propagator but its momentum routing and index contraction are mandatory.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Iteration 292 authority files

- `candidate_gravity/code/iteration292_complete_tru1_denominator_census.py`
- `candidate_gravity/results/iteration292_complete_tru1_denominator_census.json`
- `candidate_gravity/C5_TRU1_DENOMINATOR_CENSUS_ITERATION292.md`
- `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_292.md`
- `research_log/2026-09-03_iteration_292_tru1_denominator_census.md`

## Exact next gate — Iteration 293

1. Canonicalize loop routing for all eight non-scaleless `Tr U1` sectors.
2. Fit full-coordinate polynomial numerator bases at the proven ceilings: ordinary bubbles degree `<=2`, ordinary triangles `<=4`, raised bubbles `<=4`, raised triangles `<=6`.
3. Require full rank and independent held-out residuals for every family.
4. Export coefficients for corrected DR tensor reduction.
5. Repeat the Laurent IR-pole audit only after the complete numerator oracle is certified.
6. Then continue with the active `e=2,c<=1` and determinant `e=0,c<=3` sectors before source-completed linked `T_cut` projection.
7. `ANSATZ-003`, Fisher/resources and blind heavy full-C5 remain forbidden.
