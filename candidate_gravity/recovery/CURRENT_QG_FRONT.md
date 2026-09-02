# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 294**

## Current scientific state

Repository commits and recovery material are source of truth. Iterations 291–294 supersede the older weighted-kernel proxy interpretation.

### Iteration 291 — trace-weight completion

The actual effective-action insertion is obtained from

`U1 = B W^-1 = B Y_down`,

so `tr(B3)` is not the `Tr U1` coefficient authority. At the frozen translation-closed checkpoint:

- old proxy `tr(B3)=0.9605914180462887`;
- `tr(B3Y0)=0.1071384536577547`;
- `B2Y1+B1Y2=0.6977901599155829`;
- complete `[Tr U1]_{sab}=0.8049286135733377`.

Freeze:

`PASS_EXACT_U1_TRACE_WEIGHT_COMPLETION_FORMULA_AND_B3_EOM_DEGREE_PROVENANCE`.

### Iteration 292 — exact complete Tr U1 denominator census

The local `Y_down` insertion carries external momentum but no loop propagator. Exact primitive enumeration gives:

- total primitive branches: `36`;
- `B3Y0`: `23`;
- `B2Y1`: `11`;
- nonzero `B1Y2`: `2` after null-soft elimination;
- non-scaleless primitive branches: `32`.

Complete trace at the frozen checkpoint: `0.8049286124063145`.
Primitive denominator reconstruction: `0.8049286124067728`.
Absolute residual: `4.583000645652646e-13`.

Freeze:

`PASS_EXACT_WEIGHT_COMPLETED_TRU1_DENOMINATOR_CENSUS_AND_PRIMITIVE_RECONSTRUCTION`.

Retained raised families:
- raised bubbles: `10` = hard-a `4`, hard-b `4`, null/scaleless `2`;
- raised triangles: `12` = four in each repeated-vertex sector `(0,0.21)`, `(0,0.41)`, `(0.21,0.41)`;
- one single scaleless branch.

Weight-completion families:
- ordinary bubbles: `5` = hard-a `2`, hard-b `2`, null/scaleless `1`;
- ordinary one-null two-mass triangles: `8`.

Conservative loop-momentum numerator ceilings:
- ordinary bubble `<=2`;
- ordinary triangle `<=4`;
- raised bubble `<=4`;
- raised triangle `<=6`.

### Iteration 293 — structural full-family reconstruction authority

All eight non-scaleless weight-completed `Tr U1` sectors were set up for canonical loop routing using translations plus optional global reflection, with full-coordinate polynomial bases at the exact degree ceilings. This iteration is structural reconstruction authority for the spacelike/checkpoint geometry, not authority for timelike numerator coefficients.

Guardrail: do not analytically continue spacelike/checkpoint numerator coefficients onto the timelike cut by rotating denominators alone.

### Iteration 294 — direct timelike weight-completed Tr U1 nonzero certificate

On the frozen Iteration-278 translation-closed Lorentzian slice

- `k_s^2=0`;
- `k_s.k_a=-0.1`;
- `k_a^2=-s`;
- `k_b=-(k_s+k_a)`, hence `k_b^2=-(s+0.2)`;
- `s=0.004,...,0.032`;

the actual weight-completed mixed-cubic trace `[Tr U1]_{sab}` is positive and nonzero on every tested row:

`0.88125485, 0.93713710, 1.00201640, 1.07862794, 1.17089411, 1.28465260, 1.42899352, 1.61889698`.

Maximum step-scan relative spread: `2.92e-6`.

At `s=0.016`:

- old proxy `tr(B3)=-20.458473546663335`;
- flat-weight `tr(B3Y0)=+1.2194066904823941`;
- weight dressing `=-0.14077875193557943`;
- actual `[Tr U1]_{sab}=+1.0786279385468147`.

Freeze:

`PASS_SCOPED_TIMELIKE_TRANSLATION_CLOSED_WEIGHT_COMPLETED_TRU1_NONZERO_ALL_ROWS`.

This is a fixed-loop-momentum numerator certificate, not an integrated discontinuity and not a Candidate Gravity residual.

## Active computation — Iteration 295

GitHub Actions run `33688456731` is already in progress for direct timelike `s=0.016` reconstruction of all eight non-scaleless weight-completed `Tr U1` family numerators. Do not launch a duplicate run. The script reconstructs coefficients directly from the timelike parent dynamics and does not reuse spacelike numerator coefficients.

Iteration 295 is not authoritative until its run completes and its artifact/result is audited and committed.

## Null-soft EOM-sector inventory

Do not reopen generic EOM-degree-three as an active blocker on this observable. Iteration 246 already proves on the frozen null-TT soft branch

`Gamma_conn,e=3,c=0^(3)[soft,a,b] = 0`,

because every trilinear `e=3` placement contains `E^(1)[h_soft]=0`.

Active C5 sectors remain:
- determinant `e=0,c<=3`;
- connection `e=1,c<=2` — current `Tr U1` route;
- connection `e=2,c<=1`.

## Current blocker

`BLOCKED_DIRECT_TIMELIKE_COMPLETE_TRU1_FAMILY_NUMERATOR_RECONSTRUCTION_AND_DR_REDUCTION`.

The frozen linked physical target remains

`T_cut = D Gamma3_ret,soft - W[D K2]`.

Source/Ward/Born-IR classification is downstream of completing the actual timelike `e=1,c=2` `Tr U1` reduction and then the remaining active `e=0,e=2` pieces.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 293: **0 percentage points**. Iteration 294 closes a timelike nonzero numerator certificate for the correctly weight-completed trace, but no integrated comparator coordinate or unique residual has closed a readiness-rubric point.

## Retained guardrails

- Repository recovery files, validated Actions artifacts and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not promote weighted-kernel `tr(B3)` coefficients/poles to `Tr U1` authority.
- Do not subtract `-8 M_Born` from a 1PI/weighted-kernel residue without an explicit matched observable map.
- Do not confuse background degree three with EOM degree three.
- Local `Y_down` adds no propagator but its momentum routing and index contraction are mandatory.
- Do not analytically continue numerator coefficients from the checkpoint/spacelike reconstruction to timelike cut rows by changing denominator signs alone; reconstruct directly from the same parent dynamics at the timelike row.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Iteration 294 authority files

- `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_294.md`
- `research_log/2026-09-03_iteration_294_timelike_weight_completed_tru1.md`
- Iteration-294 timelike scan code/results committed immediately before those authority files.

## Exact next gate

1. Let the already-running Iteration-295 direct timelike `s=0.016` family reconstruction finish; do not duplicate it.
2. Audit all eight families for full rank, held-out residuals, imaginary numerical contamination, direct-vs-primitive trace reconstruction and canonical-routing validity.
3. Commit the validated Iteration-295 result and update recovery/log/front.
4. Perform corrected DR tensor reduction on the directly reconstructed timelike ordinary/raised bubble and triangle sectors with explicit `+/- i0` conventions.
5. Repeat the Laurent IR-pole audit only for the actual weight-completed `Tr U1` insertion.
6. Continue active `e=2,c<=1` and determinant `e=0,c<=3` sectors before source-completed linked `T_cut` projection.
7. `ANSATZ-003`, Fisher/resources and blind heavy full-C5 remain forbidden.
