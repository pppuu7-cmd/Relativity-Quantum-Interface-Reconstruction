# Candidate Gravity Current Front

**Updated:** 2026-09-05  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated physical/operator authority:** **Iteration 411**  
**Latest validated structural authority:** **Iteration 410**  
**Latest raw-valid physical blocker:** **Iteration 421 — `BLOCKED_CONVERGENCE`, double-double index 2 / class 3 / q^2=-1**  
**Latest parent precision/representation authority:** **Iteration 442 consuming Iteration 441 PASS**  
**Latest raw Y-site authority:** **Iteration 445 PASS, non-promoting**  
**Latest post-parent contraction authority:** **Iteration 446 PASS, non-promoting**  
**Latest source/provenance boundary authority:** **Iteration 447 PASS, non-promoting and not a numerical closure**  
**Active gate:** repaired Iteration-407 spectral-algebra 80/120-digit stage, run `33924198609`, head `4e4b168a47afe5e294b4551785d8b76d09630b3e`, currently `in_progress` at last check.

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Workflow colour alone is never scientific authority. Authoritative iteration IDs are never reused; race-created newer registry/recovery state wins.

## Retained physical operator coordinates

Timelike `Tr U2` from Iteration 406 before `+i/2` weight:
- `q^2=-1 -> +0.0005345424186332474`;
- `q^2=-0.34 -> -0.000734101259784574`;
- `q^2=-0.14 -> -0.001572666890130343`.

Timelike `Tr U1^2` frozen census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / q^2=-0.14 = `+0.000119747535002548`, Iteration 409 index 4 / q^2=-1 = `+0.003562716046166582`, and Iteration 411 index 11 / q^2=-0.34 = `+0.013050543643260309`.

**Exact unresolved double-double physical set: `[2]`.**

Iteration 421 remains the latest physical attempt: run `33871920373`, job `101019660127`, artifact `9942128452`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic `D_s Tr(U1^2)[2] ~= +0.0035843041850530683` is not authority. Frozen failures were `max_stability_scaled = 2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`. No zero fill is allowed.

## Precision-chain authority

Iterations 419/422 exclude simple summation and affine-moment instability as dominant explanations. Iteration 425 requires differentiating the full fixed-mass `F(u,v)`. Iteration 427 is retained as exact non-measure-chain oracle. Iteration 428 exposes severe whole-path symmetric-cross conditioning. Iteration 431 localizes the true inner precision boundary to Iteration-270 primitives. Iterations 436/437 close N1/Q1 at 80/120 digits. Iteration 438 closes exact `A_finite` arithmetic over 26 frozen nodes. Iteration 439 diagnoses severe binary64 Acoef cancellation. Iteration 440 closes Acoef/Asub 80/120 arithmetic. Iteration 441, raw-consumed as Iteration 442, closes the fixed-h fourth-order Acoef/Asub representation oracle with unchanged `h1=1e-4`, `h2=5e-4`, `h3=1e-3`.

Iteration 445 raw-consumed the frozen Y-site `y1` gate at unchanged `h=4e-5`: max `|y1_80-y1_120| = 4.09656958147226919955796882988e-77 <= 1e-30`; max central-vs-same-h-fourth-order scaled discrepancy `3.74207475261066955599469102919e-11 <= 2e-5`; 3/3 frozen pairs finite.

Iteration 446 raw-consumed the frozen continuous post-parent contraction gate: 126/126 representative contractions finite, exact 21 routed classes x 2 probes x A/B/A_SHIFT coverage, all seven matrix multiplications plus final trace carried continuously at 80/120 digits; max scaled discrepancy `5.88078000546852010816680540366e-80 <= 1e-30`. Binary64-vs-120 max `2.88197990019611433767821721255e-15` is diagnostic only.

## Iteration 447 source/provenance authority

The post-446 source audit was raw-consumed from run `33921051425`, job `101179211149`, artifact `9955020563`, artifact digest `sha256:844f689499bb3984130735423b29b6e089f21dc737f4ea7febc410888cd4ea34`, raw scientific JSON SHA-256 `16aadcbe0725fc903a594c7c7587ee35239f0a842defbb6fa1eeaef4f1ee129e`.

Classification: `PASS_SOURCE_BOUNDARY_LOCATED__NON_PROMOTING_NOT_NUMERICAL_CLOSURE`.

The audit located 18 active downstream code records and confirms that the retained Iteration-407 active path still contains uncertified binary64/NumPy arithmetic materially including:
- kinematic/basis arrays and scalar reductions;
- complex phi-mean sample arrays;
- degree-4 polynomial fit/evaluation;
- affine logarithmic moment recurrence;
- mass-node central4 mixed-derivative assembly.

Therefore upstream precision closure through the Iteration-368/370 parent/Y-site/post-parent chain does **not** imply full Iteration-407/full-`F(u,v)` precision closure.

## Active spectral-algebra gate

A separate stage already exists and must not be duplicated: `RQIR Iteration407 spectral-algebra precision stage`, run `33924198609`, repaired head `4e4b168a47afe5e294b4551785d8b76d09630b3e`. The repair is operational only: source loading now splits at the final Iteration-407 execution marker using `rsplit`; physics/routing/numerator/nodes/thresholds are unchanged.

This stage evaluates degree-4 interpolation, affine-denominator log recurrence and terminal spectral assembly at 80/120 decimal digits over frozen parent samples. Even a raw-valid PASS is scoped: it does **not** certify phi-mean/sample-generation precision and cannot promote physical index 2.

## Downstream exact gates

1. Raw-consume the repaired Iteration-407 spectral-algebra stage fail-closed. If PASS, close only that scoped spectral arithmetic layer.
2. Then carry continuous 80/120-digit provenance through the active phi-mean/sample-generation layer; no complex128 recasting of numerator samples is allowed unless quantitatively bounded below every downstream frozen gate.
3. Only after full `F(u,v)` provenance closure evaluate the frozen Iteration-424 physical mass nodes independently at 80 and 120 digits and compare with Iteration 427. Physical acceptance remains: mass-step discrepancy `<=2e-5`, direct original-integrand cross-check `<=2e-6`, tensor-degree-(1,1) fit residual `<=2e-5`, `|D_s(80)-D_s(120)|<=2e-6`, all finite; no smaller physical mass step, angular-grid escalation, threshold weakening or zero fill.
4. Promote index 2 only if every frozen condition passes.
5. Only then execute Iteration 412 exact15, requiring all 15 unique double-double indices and five valid records per q^2, then assemble complete `Tr U1^2` and `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2.
6. Comparator quotient / Source-Ward-contact+K2 / C3-C5 / nonlocal / asymptotic-safety closure remains downstream. Source/Born subtraction only in the matched observable after pole/cut-origin classification. No candidate residual before comparator closure.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iteration 447: **0 percentage points**. Numerical/provenance sublayers were closed or localized, but no additional readiness-rubric component and no new physical coordinate closed.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Authoritative IDs are never reused. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
