# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Latest raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index 2 / class 3 / `q^2=-1`; unresolved physical set `[2]`.
- BASE/HALF local support: complete through **Iteration 523**.
- BASE/HALF raw-valid MP80/MP120 pre-spectral assembly: **Iteration 527**, non-promoting.
- QUARTER support manifest/order: Iterations **529/532**.
- QUARTER ranks 1–12 raw authority: **Iterations 534, 538, 542, 545, 548, 550, 551, 556, 562, 565, 569, 571**, all raw-valid PASS and non-promoting.
- QUARTER new support closure: **12/12 = 100%**; full grid including four exact HALF-overlap corners: **16/16 = 100%**.
- Complete QUARTER pre-spectral sample-layer assembly: **Iteration 572**, PASS scoped/non-promoting.
- Frozen-clause authority mapping audit: **Iteration 573**, PASS scoped/non-promoting.
- Latest authoritative research iteration: **Iteration 573**.

## Critical Iteration572 scope
Iteration572 assembles the complete raw MP80/MP120 `(z,phi)` sample layer only. These rows are stripped-numerator angular/radial samples, not yet the final degree-4/affine-log spectrum-integrated `F(u,v)` and not physical scalar `D_s`.

Observed sample-layer checks retained:
- all 80 assembled outputs finite;
- QUARTER MP80↔MP120 scaled max `1.2787277797888786e-68`;
- HALF↔QUARTER sample-layer scaled max `2.8064444557403413e-6`;
- direct/u→v/v→u/orbit assembly routes agree at about `1e-114`;
- raw-grid bilinear diagnostic max `4.588236089297399e-15`.

None of those sample-layer values is silently promoted into a frozen physical Iteration424 clause.

## Iteration573 frozen-clause mapping
The direct-original-integrand criterion is inherited as **PASS** from raw-valid Iteration421: maximum scaled error `2.0658997659274425e-9 <= 2e-6`. Iteration424 prospectively freezes the same parent dynamics, routing, numerator, sign and normalization, so this is an exact parent-representation identity inheritance only; Iteration421 convergence/fit status is not inherited.

The tensor-degree-(1,1) clause is **OPERATIONAL_BLOCKED_NO_FROZEN_MAPPING**. Iteration421 defines `fit_residuals_scaled.tensor11` on symmetric-cross

`C(r,s)=[F(r,s)-F(r,-s)-F(-r,s)+F(-r,-s)]/(4rs)`

using squared-radius multipliers `[1,0.75,0.5,0.25]^2`. Iteration572 instead has a bilinear fit on raw pre-spectral 4x4 `F(u,v)` nodes. Different observable + different design matrix means no exact identity; substituting the tiny Iteration572 raw-grid residual would redefine/weaken a frozen gate post hoc.

This is an **operational BLOCKED**, not a consistency FAIL, comparator identity, model-level non-identifiability, near-degeneracy, or novelty certificate.

## Frozen Iteration424 physical acceptance — current status
All five must pass simultaneously before physical index2 promotion:
1. physical mass-step discrepancy `<=2e-5` — **BLOCKED pending full spectrum-integrated BASE/HALF/QUARTER physical D_s**;
2. direct original-integrand crosscheck `<=2e-6` — **PASS inherited from raw-valid Iteration421**;
3. tensor-degree-(1,1) fit residual `<=2e-5` — **OPERATIONAL BLOCKED: no prospectively frozen mapping from current raw-grid diagnostic**;
4. fixed-node MP80/MP120 agreement `<=2e-6` — **BLOCKED pending full spectrum-integrated physical D_s**;
5. finite outputs — **BLOCKED at physical spectrum-integrated level**.

Only simultaneous full PASS promotes physical index2 and authorizes frozen exact15 continuation. A computed failing clause is a scoped scientific FAIL; an uncomputed/undefined clause remains BLOCKED.

## Exact next gate
Using only already raw-valid support, reconstruct full spectrum-integrated `F(u,v)` at MP80/MP120 with the frozen Iteration407 pipeline:
1. phi-average at the five frozen `TRAIN_Z` nodes;
2. degree-4 interpolation;
3. frozen affine coefficients;
4. analytic affine-log recurrence;
5. central4 assemble BASE/HALF/QUARTER physical `D_s`;
6. evaluate physical mass-step, MP80/MP120 and finiteness clauses.

In parallel, search existing **pre-result** contracts/commits for an already-frozen high-precision tensor11 definition. If none exists, keep the tensor11 criterion operationally BLOCKED; do not invent a post-result mapping.

No new heavy mass-node computation is presently required solely for support. Do not duplicate closed ranks.

## Comparator blocker retained
Concrete upstream algebraic `Source/Ward/contact+K2` target and robust comparator-subtracted residual remain absent. Fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient therefore remains **operational BLOCKED**. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration573 closes an authority/provenance ambiguity and one inherited frozen clause, but no additional stable model-level rubric sector.

## Downstream chain
BASE/HALF support **CLOSED 523** → BASE/HALF pre-spectral assembly **527** → QUARTER support **12/12 CLOSED 571** → complete QUARTER pre-spectral assembly **572** → authority mapping **573** → full frozen spectral reconstruction of BASE/HALF/QUARTER physical `D_s` → resolve or preserve tensor11 BLOCKED → only then unchanged Iteration424 five-clause decision → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc gate redefinition. No raw-F bilinear substitution for tensor11. No u↔v support substitution. No smaller h, altered mass nodes/precision, threshold weakening or angular-grid escalation. Same parent dynamics/routing/numerator/sign/normalization are mandatory. Source/Born subtraction only after pole/cut-origin classification in the matched observable. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
