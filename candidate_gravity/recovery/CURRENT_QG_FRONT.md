# Candidate Gravity Current Front

**Updated:** 2026-09-07  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Latest raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index 2 / class 3 / `q^2=-1`; exact unresolved physical set `[2]`.
- BASE/HALF local mass support: **Iteration 523**, `32/32 = 100% = 2560/2560` across 28 distinct coordinates.
- Independent BASE/HALF MP80/MP120 assembly: **Iteration 527**, raw-valid PASS, non-promoting.
- QUARTER exact support manifest: **Iteration 529** — 16-grid, 4 exact HALF-overlap corners, 12 new coordinates required.
- Full 12-rank QUARTER successor order prospectively frozen: **Iteration 532**.
- Three-level exact diagnostics retained: **Iterations 530–533, 536–537, 540–541**; diagnostic-only, non-promoting.
- QUARTER rank1 raw authority: **Iteration 534**, raw-valid PASS.
- QUARTER rank2 raw authority: **Iteration 538**, `PASS_RAW_CONSUMED_ITER424_QUARTER_SUPPORT_RANK2_MP80_MP120__NON_PROMOTING`.
- Latest authoritative research iteration: **Iteration 541**.

## Iteration 538 — rank2 raw-valid PASS
Canonical run `34102627559`, job `101680313500`, artifact `10014273722`, artifact digest `sha256:02ca8895b69ed4aeb9404882bae369101d2160a3915687c11ab1b66a3fbca231`, head `1046545619a9ae564eb7e611708e4e3db7b5eb42`.

Frozen rank2 coordinate `(-2.5e-6,+1.25e-6)` passed `80/80` finite samples, max scaled MP80↔MP120 discrepancy `2.69972435730420647190377912951e-80 <= 1e-30`, and max radial Richardson scaled error `2.56823894036034380187639556588e-15 <= 5e-4`.

New QUARTER support closure is **2/12**. Including four exact HALF-overlap corners, authoritative full QUARTER-grid coordinate coverage is **6/16 = 37.5%**. This does not promote physical index 2.

## Iteration 540 — exact three-level step-ratio diagnostic
For the common smooth hierarchy `X_h=D+A+B+C+O(h^10)` with `A=a h^4`, `B=b h^6`, `C=c h^8`, and `d1=BASE-HALF`, `d2=HALF-QUARTER`:

- `d1=(15/16)A+(63/64)B+(255/256)C`,
- `d2=(15/256)A+(63/4096)B+(255/65536)C`.

Pure h^4, h^6 and h^8 contributions therefore have exact `d1/d2` ratios **16, 64, 256** respectively. For h^4+h^6 only,

`B/A = (80/21)(r-16)/(64-r)`, where `r=d1/d2`,

with exact cancellation points `d1=0` at `B/A=-20/21` and `d2=0` at `B/A=-80/21`.

Same-sign A,B imply `16<=r<=64`; same-sign A,B,C imply `16<=r<=256`. Violation diagnoses opposite-sign cancellation and/or higher-order contamination under the stated expansion; it is **not** by itself a Candidate-Gravity consistency FAIL.

Classification: `PASS_ITER424_THREE_LEVEL_STEP_RATIO_SIGN_STRUCTURE_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Machine authority: `candidate_gravity/results/iteration540_iter424_three_level_step_ratio_sign_contract.json`.

## Iteration 541 — exact three-level extrapolator noise contract
Retain the frozen diagnostic estimator

`R3=(BASE-80 HALF+1024 QUARTER)/945`.

Its exact weight norms are

- `||w||_1=221/189 ~= 1.1693121693121693`,
- `||w||_2^2=50237/42525`, hence `||w||_2 ~= 1.0869002464792206`,
- `||w||_inf=1024/945`.

Therefore, if all three assembled inputs satisfy the same absolute error envelope `|e_i|<=eps`, then the sharp worst-case propagation bound is

`|e_R3| <= (221/189) eps`.

Under independent equal-variance input noise, the output standard-deviation factor is `sqrt(50237/42525) ~= 1.0869002464792206`.

For `X_h=D+a h^4+b h^6+c h^8+e h^10+...`, exact leakage coefficients under these same frozen weights are h4=`0`, h6=`0`, h8=`1/1344`, h10=`1/1024`, so

`R3=D+c h^8/1344+e h^10/1024+...`.

This is a numerical/truncation diagnostic only and does not replace any frozen Iteration-424 physical clause.

Classification: `PASS_ITER424_THREE_LEVEL_EXTRAPOLATOR_NOISE_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Machine authority: `candidate_gravity/results/iteration541_iter424_three_level_extrapolator_noise_contract.json`.

## Active heavy computation — rank3
Exactly one successor remains authorized and running:
- rank: **3/12**;
- coordinate: `u=-1.25e-6`, `v=-2.5e-6`;
- run: `34115105768`;
- job: `101719973617`;
- head/trigger commit: `ec77639ef423249426ee9b5b560b0662521f56a9`;
- live state at Iteration-541 inspection: `in_progress`; raw audit and upload pending.

No duplicate rank3 heavy run is authorized. Workflow green alone must not be accepted; raw artifact consumption is mandatory before rank3 authority.

## Frozen Iteration-532 QUARTER order
1. `(-2.5e-6,-1.25e-6)` — raw PASS at Iteration 534
2. `(-2.5e-6,+1.25e-6)` — raw PASS at Iteration 538
3. `(-1.25e-6,-2.5e-6)` — running
4. `(-1.25e-6,-1.25e-6)`
5. `(-1.25e-6,+1.25e-6)`
6. `(-1.25e-6,+2.5e-6)`
7. `(+1.25e-6,-2.5e-6)`
8. `(+1.25e-6,-1.25e-6)`
9. `(+1.25e-6,+1.25e-6)`
10. `(+1.25e-6,+2.5e-6)`
11. `(+2.5e-6,-1.25e-6)`
12. `(+2.5e-6,+1.25e-6)`.

PASS advances only to the next listed rank. Scientific FAIL/BLOCKED stops advancement and localizes the concrete failure under unchanged science. Operational failure permits only minimal technical repair and rerun of the same rank. Result-dependent reordering/skipping, unsupported u↔v substitution, zero-fill, threshold weakening, mass-node changes and precision changes are forbidden.

## Frozen Iteration-424 physical acceptance
After all 12 new QUARTER coordinates and QUARTER assembly are raw-closed, physical index 2 requires all simultaneously:
1. physical mass-step discrepancy `<=2e-5`;
2. direct original-integrand cross-check `<=2e-6`;
3. tensor-degree-(1,1) fit residual `<=2e-5`;
4. fixed-node MP80/MP120 agreement `|D_s(80)-D_s(120)|<=2e-6`;
5. finite outputs.

Only full PASS promotes index 2 and authorizes frozen exact15 continuation. A computed failing clause is a scoped scientific FAIL for this fallback route; an uncomputed clause is BLOCKED.

## Comparator blocker retained
The concrete upstream algebraic `Source/Ward/contact+K2` target and robust comparator-subtracted residual are absent. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 541 closes an exact diagnostic subgate only; no stable rubric sector closes.

## Exact next gate
After rank3 terminal completion: fail-closed raw-consume run `34115105768`. Only raw-valid PASS authorizes frozen rank4 `(-1.25e-6,-1.25e-6)`. Scientific FAIL/BLOCKED stops advancement; operational failure permits only minimal rank3 repair.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No unsupported `u<->v` substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
