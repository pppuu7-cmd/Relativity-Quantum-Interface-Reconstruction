# Candidate Gravity Current Front

**Updated:** 2026-09-07  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Latest validated structural authority: **Iteration 410**.
- Latest raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index 2 / class 3 / `q^2=-1`.
- Exact unresolved physical set: **`[2]`**.
- Latest completed local mass-support authority: **Iteration 523**, final rank27 raw-consumed PASS.
- Certified local precision support: **`32/32 = 100% = 2560/2560`** across 28 distinct coordinates.
- Latest assembled numerical authority: **Iteration 527**.
- Latest authoritative research iteration: **Iteration 527**.
- Current post-support classification: **`PASS_RAW_CONSUMED_INDEPENDENT_BASE_HALF_MP80_MP120_ASSEMBLY__NON_PROMOTING`**.

## Iterations 525–527 — provenance closure and assembled PASS
Iteration 525 recursive exact provenance preflight narrowed the historical schema problem. Iteration 526 closed the remaining historical authority with an exact multipart bridge: 28 frozen coordinates are backed by 29 exact artifact parts because rank 10 `(+5e-6,+5e-6)` is explicitly a two-artifact z-partition rather than a synthetic single artifact. The workflow verifies every scientific JSON SHA-256, each expected z partition, rejects duplicate `(z,phi)` samples and requires exactly 80 merged samples per coordinate.

One frozen independent BASE/HALF assembly was then run from head `8ff6ef9d3b1a946ca3215c5905e1432adbb18fe8`: run `34089957999`, job `101641252363`, artifact `10006477417`, artifact digest `sha256:44b34e3174ce6e23659733c76004f269f8eac07b01d67211a6a1b859b2d35b48`.

Iteration 527 downloaded and raw-consumed the artifact rather than trusting workflow colour. Scientific `result.json` SHA-256 is `8ac2949e795b201efbaa70b63fb3aeef9805eecc2e6c13362b9db38f52a9e451`; `authority_audit.json` SHA-256 is `f2b762b4224d15e1baa32787cb35071e1a750c769c2e8ee61567e88fa83560d8`, and the audit embeds the same scientific SHA with `scientific_authority_pass=true`.

Frozen assembly results:
- all 80 common samples finite: PASS;
- BASE MP80↔MP120 scaled max `0.0 <= 2e-6`: PASS;
- HALF MP80↔MP120 scaled max `0.0 <= 2e-6`: PASS;
- BASE↔HALF mass-step scaled max `8.60575121785458117805036434436e-7 <= 2e-5`: PASS;
- BASE/HALF row rank remains exactly 2, Gram determinant `5948843/559872 > 0`;
- `ds=-d_base`; no Richardson promotion; no threshold weakening.

Machine-readable authority: `candidate_gravity/results/post526_independent_base_half_assembly_raw_consumption.json`. Recovery authority: `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_527.md`.

This is a genuine assembled numerical PASS and removes the Iteration-524 legacy-provenance operational blocker. It **does not by itself promote physical index 2** and therefore does not overwrite Iteration 421.

## Exact next gate — frozen Iteration-424 reevaluation
The prospectively frozen Iteration-424 fixed-node high-precision fallback may now be reevaluated on the identical parent dynamics and fixed mass nodes. No clause may be weakened or silently replaced by a differently normalized assembled metric.

Full acceptance still requires all of:
1. physical mass-step discrepancy `<=2e-5`;
2. direct original-integrand cross-check `<=2e-6`;
3. tensor-degree-(1,1) fit residual `<=2e-5`;
4. identical fixed-node 80/120-digit agreement `|D_s(80)-D_s(120)|<=2e-6`;
5. finite outputs.

Only full PASS promotes index 2 and authorizes frozen exact15 continuation. A computed failing clause is a scoped scientific FAIL for this fallback route. A missing/uncomputed clause is operational BLOCKED, never zero-filled.

## Retained exact assembly authorities
Iterations 510–522 remain exact numerical/provenance authorities: BASE/HALF row rank is 2; `W_DELTA=W_BASE-W_HALF` is derived; exact Gram matrix is `[[4225/5184,4/81],[4/81,4225/324]]` with determinant `5948843/559872`; exact norms are `||W_BASE||_1=9/4`, `||W_HALF||_1=9`, `||W_BASE-W_HALF||_1=397/36`. Local scaled MP PASS does not imply assembled PASS; Iteration 527 independently closed that assembly gate.

## Retained comparator and physical blockers
Iteration 504 remains `BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING`: the concrete upstream algebraic `Source/Ward/contact+K2` target is absent, so fixed C3/C4/C5/nonlocal/asymptotic-safety comparator identity/rank loss/near-degeneracy/novelty remain unevaluable. BLOCKED is not scientific FAIL.

Iteration 421 remains raw-valid `BLOCKED_CONVERGENCE` for physical index 2 pending the frozen Iteration-424 reevaluation. Diagnostic values are not authority and no zero-fill is allowed. Frozen thresholds are not weakened.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 527 closes a real frozen assembled numerical prerequisite, but no additional model-level rubric sector is complete.

## Exact downstream chain
Full local support **CLOSED at Iteration 523** → exact multipart provenance **CLOSED at Iteration 526** → independent BASE/HALF assembly **CLOSED at Iteration 527** → frozen Iteration-424 reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No `u<->v` support substitution without exact frozen identity. Exact BASE/HALF coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
