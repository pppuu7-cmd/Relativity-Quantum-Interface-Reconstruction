# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 291**

## Current scientific state

Iterations 278–289 established a strong computational description of the translation-closed weighted Vilkovisky kernel

`B := U1 W = Q A Q`,

including nonzero timelike support, canonical raised bubble/triangle families, complete actual-oracle numerator bases and DR tensor/Laurent diagnostics. Iteration 290 separated the off-shell weighted-kernel pole problem from the already frozen physical MSSC-001 Born-factorizing source IR completion.

Iteration 291 identifies and closes an upstream trace-orientation gap before those proxy scalar coefficients can be promoted to the one-loop effective action.

## Iteration 291 — actual Tr U1 versus weighted-kernel trace

The exact Iteration-252/256 orientation gives

`U1 W = B = Q A Q`,

hence

`U1 = B W^{-1} = B Y_down`,

where

`Y_down = sqrt(|g|) g`.

Therefore the cubic background coefficient of the effective-action insertion `Tr U1` is not `tr(B3)`.

For distinguishable translation-closed legs `(s,a,b)`, the complete mixed cubic coefficient is

`[Tr U1]_{sab} =`

`tr(B3[sab](p) Y0)`

`+ tr(B2[sa](p+k_b) Y1[b])`

`+ tr(B2[sb](p+k_a) Y1[a])`

`+ tr(B2[ab](p+k_s) Y1[s])`

`+ tr(B1[s](p+k_a+k_b) Y2[ab])`

`+ tr(B1[a](p+k_s+k_b) Y2[sb])`

`+ tr(B1[b](p+k_s+k_a) Y2[sa])`.

The local rightmost `Y_down` insertion changes the numerator contraction and the input momentum of the lower-background-order `B` block but adds no loop propagator.

### Frozen translation-closed checkpoint

At exactly the Iteration-273 checkpoint:

- old proxy `tr(B3) = 0.9605914180462887`;
- flat-weight term `tr(B3 Y0) = 0.1071384536577547`;
- total `B2Y1+B1Y2` dressing `= 0.6977901599155829`;
- complete cubic coefficient
  `[Tr U1]_{sab}(p0) = 0.8049286135733377`.

The trace completion is therefore order one.

Controls:

- `Y0 = diag(-1,1,1,1)`;
- `max|Y1[x]-epsilon_x| = 7.23e-11` for the frozen TT legs;
- null-soft `||B1[s]||_F = 4.15e-9`.

Freeze:

`PASS_EXACT_U1_TRACE_WEIGHT_COMPLETION_FORMULA_AND_B3_EOM_DEGREE_PROVENANCE`.

## Scope correction to Iterations 278–289

The previous results remain valid calculations of the weighted symmetric kernel `B=U1W`. Their B3 nonzero certificates, routing closure, denominator canonicalization, numerator basis audits and DR reduction diagnostics are retained.

However, the scalar `np.trace(B)` used for the downstream family reductions is not the one-loop effective-action trace `Tr U1`.

Therefore:

- Iteration-287 bubble coefficients are weighted-kernel proxy coefficients, not yet `Tr U1` coefficients;
- the Iteration-289 pole `-0.061289813814603585/epsilon` is a weighted-kernel proxy pole, not yet the pole authority of the `-(i/2)Tr U1` sector;
- its Iteration-290 Ward/EOM versus physical-Born-IR classification is deferred until the corrected trace is reduced.

Do not call the old calculations wrong; their interpretation is narrowed.

## EOM-degree provenance

`B3=[U1W]_{h^3}` means background perturbation degree three. Since `A=R(DR)E` contains one explicit EOM insertion, this is the

`e=1,c=2`

connection sector in the finite-`R^3` bookkeeping.

It is distinct from the separate EOM-degree-three sector frozen in Iteration 244:

`Gamma_conn^(e=3) = +(i/2)Tr(U1U2) - (i/6)Tr(U1^3)`.

A complete finite-`R^3` Vilkovisky result still requires separately:

- determinant `e=0,c=3`;
- linear-EOM `e=1,c=2` — current trace-completion route;
- quadratic-EOM `e=2,c=1` — dressed `Tr U2` and `Tr U1^2`;
- cubic-EOM `e=3,c=0` — `Tr(U1U2)` and `Tr(U1^3)`.

## Current C5 blocker

`BLOCKED_P_DEPENDENT_COMPLETE_TR_U1_E1C2_NUMERATOR_AND_REDUCTION_AFTER_WEIGHT_COMPLETION`.

The frozen linked physical target remains

`T_cut = D Gamma3_ret,soft - W[D K2]`,

but source/Ward/Born-IR classification is downstream of first reconstructing the actual `Tr U1` sector.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 290: **0 percentage points**. A significant authority error in trace interpretation is corrected, but no complete physical comparator coordinate or unique residual has closed a rubric point.

## Retained guardrails

- Repository recovery files, validated Actions artifacts and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not use Iteration-288 ordinary polynomial epsilon extrapolations as finite triangle coefficients.
- Do not promote the Iteration-289 weighted-kernel pole to `Tr U1` authority.
- Do not subtract `-8 M_Born` from a 1PI/weighted-kernel residue without an explicit matched observable map.
- Do not confuse background degree 3 with EOM degree 3.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Iteration 291 authority files

- `candidate_gravity/code/iteration291_u1_trace_weight_completion.py`
- `candidate_gravity/results/iteration291_u1_trace_weight_completion.json`
- `candidate_gravity/C5_U1_TRACE_WEIGHT_COMPLETION_ITERATION291.md`
- `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_291.md`
- `research_log/2026-09-03_iteration_291_u1_trace_weight_completion.md`

## Exact next gate — Iteration 292

1. Build the p-dependent complete `[Tr U1]_{sab}` oracle with all `B3Y0`, routed `B2Y1` and routed `B1Y2` partitions.
2. Recanonicalize the scalar denominator families; local `Y_down` adds no propagator but lower-order B blocks can change family multiplicities.
3. Determine complete numerator degree ceilings and held-out reconstruction bases for every non-scaleless family.
4. Tensor-reduce the corrected e=1,c=2 sector and repeat the Laurent IR-pole audit.
5. Only then resume the linked/source/Ward/Born-IR A/B classification.
6. e=2,c=1, e=3,c=0 and determinant e=0,c=3 sectors remain separately open.
7. `ANSATZ-003`, Fisher/resources and blind heavy full-C5 remain forbidden.
