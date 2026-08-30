# RQIR Iteration 117 — Reference-Span Rank and Distinct-Setting Lower Bound

**Date:** 2026-08-31  
**Status:** Paper-III structural identifiability/resource gate. No apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 116 showed how to credit one physical reference record only once while preserving its full joint Fisher matrix. The next question is whether one four-real same-state dual-tone setting can even span the nuisance subspace required by common transfer gain plus the seven calibration layers.

This iteration answers that question at the level of Fisher rank and score span.

## 2. One-setting Fisher-rank ceiling

For one accepted dual-tone block, let the real observation vector have dimension

`d_obs=4`

and let its local Jacobian with respect to the retained reference nuisance coordinates be

`J_b`.

With positive-definite observation precision `W_b`, the per-block Fisher is

`K_b=J_b^T W_b J_b`.

Therefore

`rank(K_b)<=rank(J_b)<=4`.

### RQIR-NG-074 — repetition does not create missing Fisher directions

Repeating the **same operating setting with the same local Jacobian** gives

`K_N=N K_b`.

Hence

`rank(K_N)=rank(K_b)`

for every positive finite `N`.

No increase of injection SNR, block count or exposure time can identify a required nuisance direction that lies outside the score span of that setting.

This is a structural no-go, not a sensitivity shortage.

## 3. Exact support-feasibility condition

Let `H_*>=0` be the required information matrix from Iteration 116.

For a total reference Fisher matrix `K_tot`, a finite matrix quota

`T K_tot >= H_*`

can exist only if

`range(H_*) subseteq range(K_tot)`.

For positive-semidefinite matrices this is equivalent to

`boxed{null(K_tot) subseteq null(H_*)}`.

If there exists a vector `v` with

`K_tot v=0`

but

`v^T H_* v>0`,

then the required reference quota is infeasible at every finite exposure.

Do not hide this case with a numerical pseudoinverse cutoff.

### RQIR-RESOURCE-085 — reference-support certificate

> A proposed set of calibration/reference settings is admissible only if its total Fisher support contains the full required-information support.

Once this support condition passes, RESOURCE-082/083 determines the time cost.

## 4. Several distinct reference settings

Suppose `m` distinct settings are used, each giving a four-real observation Jacobian `J_b` and Fisher `K_b`.

Then

`K_tot=sum_b t_b K_b`

and

`rank(K_tot)<=sum_b rank(K_b)<=4m`.

Let

`r_req=rank(H_*)`.

A necessary dimensional lower bound is therefore

`boxed{m >= ceil(r_req/4)}`.

### RQIR-RESOURCE-086 — distinct-setting lower bound

This is necessary but not sufficient: two or more settings can still probe the same four-dimensional nuisance subspace and fail to increase total rank.

Examples:

- if the effective requirement consists of **one common-gain direction plus seven independent scalar layer directions**, then `r_req=8` and at least `2` distinct four-real settings are necessary;
- if the seven layers each require two independent directions in addition to one common-gain direction, then `r_req=15` and at least `4` distinct settings are necessary.

These are dimensional examples, not claims that the actual RQIR layer requirement has rank exactly 8 or 15. Physical overlaps and exact constraints must be computed first.

## 5. Stacked-Jacobian design certificate

Whiten each observation block and stack the distinct settings,

`J_stack = [W_1^(1/2) J_1; ... ; W_m^(1/2) J_m]`.

Let `U_req` be a basis for the required nuisance subspace `range(H_*)`.

A practical support test is

`rank(J_stack U_req)=r_req`.

Equivalently the smallest singular value on the required subspace must satisfy

`boxed{sigma_min(J_stack U_req)>0}`.

### RQIR-DESIGN-018 — optimize reference settings for span before SNR

> When adding a new reference setting, first maximize the missing required score span / smallest singular value on the required subspace. Increasing SNR in an already covered direction cannot repair a null direction.

This gives a concrete design rule for choosing different source preparations, injection phases, amplitudes, geometry points or detector operating settings.

## 6. Deterministic regression

The stored regression constructs an 8-dimensional required space.

- Setting 1 measures only coordinates 1–4.
- Setting 2 measures only coordinates 5–8.

Together they give rank 8 and pass the support gate.

Replacing setting 2 by a duplicate of setting 1 leaves rank 4 and remains infeasible regardless of repetition count.

Thus satisfying the counting lower bound `m>=2` is not sufficient; **orientation/complementarity** of the settings matters.

## 7. Consequence for common gain plus seven-layer calibration

Iteration 116 allowed a potentially large wall-clock saving if transfer and calibration information are obtained simultaneously. Iteration 117 supplies the missing caveat:

- simultaneity is valuable only for nuisance directions actually present in the same score span;
- one four-real dual-tone setting cannot generically carry an arbitrarily high-rank seven-layer calibration requirement;
- repeated identical blocks improve eigenvalues inside the existing span but do not enlarge that span;
- additional distinct physical settings are mandatory whenever `r_req>4` or the first setting misses part of `range(H_*)`.

Therefore the next robust scheduler must distinguish **same-block simultaneous information** from **distinct-setting span completion**.

## 8. Readiness snapshot after Iteration 117

These are project-management estimates, not statistical quantities.

- **Repository readiness for writing Paper III — scientific content:** **90%**.
- **Paper III submission-ready state:** **71%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **84%**.
- **Concrete Candidate-Gravity model itself:** **~10%**; no dynamics has yet passed QG-001…QG-010.

Paper III increased because the simultaneous-reference ambiguity is now separated cleanly into a support/rank gate followed by an exact time-allocation gate. Candidate-Gravity readiness is unchanged: this iteration strengthens the downstream experimental test machinery but does not close gauge/conservation/causality/EFT/renormalization gates or construct candidate dynamics.

## 9. Next admissible gate

Build the **minimal reference-setting cover** for the current Toy009/Toy014 nuisance basis:

1. reconstruct the actual required subspace after hard constraints and spectral-tilt quotient;
2. compute the rank contributed by each already-defined seven-layer calibration setting and the same-state dual-tone transfer setting;
3. identify redundant settings and missing directions;
4. derive the minimum subset that satisfies RESOURCE-085;
5. feed that subset into RESOURCE-083 to obtain a non-double-counted symbolic detector-side wall-clock certificate.

No new apparatus numbers should be invented.

## 10. Reproducibility

Run

`python analysis/reference_span_rank_iteration117.py`.

The script verifies the four-real rank ceiling, rank invariance under identical repetition, exact support infeasibility, the `ceil(r_req/4)` lower bound, complementary-vs-redundant two-setting examples and the stacked singular-value design criterion.
