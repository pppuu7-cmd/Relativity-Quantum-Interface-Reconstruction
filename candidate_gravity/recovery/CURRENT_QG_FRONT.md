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
- BASE/HALF support: **CLOSED 523**; raw-valid pre-spectral assembly: **527**.
- QUARTER support: ranks 1–12 raw-valid; **12/12 new coordinates**, **16/16 full grid** including exact HALF-overlap corners; closed through **571**.
- Complete QUARTER pre-spectral assembly: **572**, PASS scoped/non-promoting.
- Frozen-clause authority mapping: **573**, PASS scoped/non-promoting.
- Full frozen Iteration-407 spectrum reconstruction raw-consumed: **574**, PASS for the three pending spectral numerical clauses, non-promoting because tensor11 remains BLOCKED.
- Latest authoritative research iteration: **574**.

## Iteration574 raw spectral authority
Canonical source:
- run `34179921282`
- job `101916751917`
- head `967525f318fac374124ca2a5127b82e0c771c7a2`
- artifact `10038557027`, `rqir-post573-iter424-full-spectrum-from-raw`
- artifact digest `sha256:330fc416a24935bbd1faf5f852420d179c0cd17a8bb2ba52dbae296bc00953e2`
- scientific result SHA-256 `d899623f64d98f12d19f32545e44fbcebe92ccc645f25a05b37f67a8b150a773`
- classification `PASS_ITER424_FULL_SPECTRUM_NUMERICAL_CLAUSES__TENSOR11_STILL_BLOCKED__NON_PROMOTING`.

Independent fail-closed raw consumption:
- run `34180176453`
- job `101917503739`
- head `cbcfa03af40ad0d01f44883187698dd7bb9361b3`
- exact artifact downloaded with `actions/download-artifact@v5`;
- embedded authority audit required exact Iter424 full-spectrum scope, `raw_result_integrity_valid=true`, and exact SHA binding before committing raw JSON into `candidate_gravity/results/`.

A green source workflow by itself is not authority; the raw result/audit binding above is the authority basis.

## Frozen Iteration424 five-clause decision — current status
All five remain prospectively frozen; no threshold or observable has been changed after seeing results.

1. physical mass-step discrepancy `<=2e-5` — **PASS** from Iteration574 full spectrum-integrated BASE/HALF/QUARTER `D_s`.
2. direct original-integrand crosscheck `<=2e-6` — **PASS**, inherited only through Iteration573 exact parent-representation identity from raw-valid Iteration421; observed inherited maximum `2.0658997659274425e-9`.
3. tensor-degree-(1,1) fit residual `<=2e-5` — **OPERATIONAL_BLOCKED_NO_FROZEN_MAPPING**.
4. identical fixed-node MP80/MP120 agreement `<=2e-6` — **PASS** from Iteration574.
5. finite outputs — **PASS** at the physical spectrum-integrated level from Iteration574.

Thus **4/5 frozen clauses are PASS, 1/5 is operationally BLOCKED**. This is not a full Iteration424 PASS. Physical index2 is not promoted; exact15 is not authorized yet.

## Tensor11 blocker
Iteration421 defines `fit_residuals_scaled.tensor11` on the symmetric-cross observable

`C(r,s)=[F(r,s)-F(r,-s)-F(-r,s)+F(-r,-s)]/(4rs)`

using squared-radius multipliers `[1,0.75,0.5,0.25]^2`.

The later raw 4x4 bilinear fit is a different observable/design matrix and must not substitute for tensor11. No post-result tensor11 mapping may be invented.

## Exact active/next gate
Nearest scientifically permitted gate: exhaustive **pre-result tensor11 provenance inventory** over repository snapshot/history through the prospective Iteration424 contract commit.

Active canonical audit at this front write:
- run `34180260935`
- workflow `RQIR post573 tensor11 precontract audit`
- head `cd109414b5b442460d79c8255f06e96083e12d28`
- launch status: `queued`.

If an already-frozen pre-result high-precision tensor11 definition/mapping is found, only that exact definition may be evaluated. If none exists, clause 3 remains operationally BLOCKED and the physical fallback cannot be promoted by inventing a replacement observable.

## Comparator blocker retained
Concrete upstream algebraic `Source/Ward/contact+K2` target and robust comparator-subtracted residual remain absent. Comparator quotient therefore remains **operational BLOCKED**. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**.

## Downstream chain
Support **CLOSED** → full raw support/pre-spectral assembly **CLOSED** → frozen full spectral numerical clauses **4/5 PASS overall with tensor11 BLOCKED** → pre-result tensor11 provenance audit → only simultaneous 5/5 PASS may promote index2 → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc gate redefinition. No raw-F bilinear substitution for tensor11. No u↔v support substitution. No smaller h, altered mass nodes/precision, threshold weakening or blind full-C5. Same parent dynamics/routing/numerator/sign/normalization remain mandatory. Source/Born subtraction only after pole/cut-origin classification in the matched observable. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
